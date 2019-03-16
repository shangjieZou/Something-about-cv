import requests
import re
from bs4 import BeautifulSoup
import urllib.request
import os


def get_url_txt(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Occured in get_url"

# url = "http://baike.niaolei.org.cn/index.php?category-view-13-12"
# print(get_url_txt(url))

# ________________________________________获取链接列表_____________________________________________
def get_categories(html):
    # 获取所有鸟类科的链接
    category_pattern = r"<dd><a href=\"(.+)</a></dd>"
    all_categories = str(re.findall(category_pattern, html))
    print(all_categories)
    all_categories_list = all_categories.split(",")
    for i in range(len(all_categories_list)):
        all_categories_list[i] = "http://baike.niaolei.org.cn/" + all_categories_list[i].strip("] '")
    return all_categories_list


def fileoutput_categoryindex():
    # 输出鸟类科链接文件
    html = get_url_txt("http://baike.niaolei.org.cn/index.php?category-view-13-12")
    f = open('Categories-index.txt', 'w')
    all_categories_list = get_categories(html)
    for i in range(len(all_categories_list)):
        f.write(all_categories_list[i]+"\n")
    f.close()
    print("finished")

# _________________________________________________________________________________________________________


# ________________________________________下载图片_______________________________________________________
def download_imgs_and_make_dirs():
    f = open("Categories-index.txt", "r")
    href_category = f.read()
    href_category_list = href_category.split("\n")
    url_href_list = []
    category_list = []
    for i in range(len(href_category_list)):
        href_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+") #http链接
        category_pattern = re.compile(r'[\u4e00-\u9fa5]+') #汉字
        url_href = re.findall(href_pattern, href_category_list[i])
        category = re.findall(category_pattern, href_category_list[i])
        url_href_list.append(url_href)
        category_list.append(category)
    for i in range(len(category_list)):
        path = "C:/Users/Administrator/PycharmProjects/Bird-cv/%s"%(category_list[i])
        is_exists = os.path.exists(path)
        if not is_exists:
            os.makedirs(path)
            print("%s创建成功"%(category_list[i]))
        print(url_href_list[i])
        print(path)
        get_all_img_source(url_href_list[i][0],path)


def get_all_img_source(url, path):
    # 获取某一科鸟类所有图片的链接
    depth = 10
    title_list = []
    src_href_list = []
    for i in range(1, depth+1):
        try:
            url_iter = url + "-" + str(i)
            print(url_iter)
            html = get_url_txt(url_iter)
            soup = BeautifulSoup(html, "html.parser")
            for item in soup.find_all("img"):
                try:
                    title_list.append(item.attrs['title'])
                    src_href_list.append(item.attrs['src'])
                except:
                    continue
        except:
            continue
    dict_img_href = dict(zip(title_list, src_href_list))
    print(dict_img_href)
    for key in dict_img_href.keys():
        urllib.request.urlretrieve(dict_img_href[key],path+"/%s.jpg" % (key))
# _________________________________________________________________________________________________________


if __name__ == '__main__':
    if(1):
        #获取页面进行初步浏览
        url = "http://baike.niaolei.org.cn/index.php?category-view-13-12"
        print(get_url_txt(url))
    if(1):
        #输出链接于文档txt
        fileoutput_categoryindex()
    if(0):
        #下载所有图片，需要时把if中的0改为1
        download_imgs_and_make_dirs()

