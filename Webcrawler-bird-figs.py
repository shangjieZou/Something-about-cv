import requests
import re

def get_url_txt(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Occured in get_url"

#url = "http://baike.niaolei.org.cn/index.php?category-view-13-12"
#print(get_url_txt(url))


def get_categories(html):
    category_pattern = r"<dd><a href=\"(.+)</a></dd>"
    all_categories = str(re.findall(category_pattern, html))
    print(all_categories)
    all_categories_list = all_categories.split(",")
    for i in range(len(all_categories_list)):
        all_categories_list[i] = "http://baike.niaolei.org.cn/" + all_categories_list[i]
    return all_categories_list


def fileoutput_categoryindex():
    html = get_url_txt("http://baike.niaolei.org.cn/index.php?category-view-13-12")
    f = open('Categories-index.txt', 'w')
    all_categories_list = get_categories(html)
    for i in range(len(all_categories_list)):
        f.write(all_categories_list[i]+"\n")
    f.close()
    print("finished")

fileoutput_categoryindex()