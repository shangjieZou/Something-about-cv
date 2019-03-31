import os

def change_file_name(start_num, path):

    # 获取该目录下所有文件，存入列表中
    f = os.listdir(path)
    n = 0
    for i in f:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + i

        # 设置新文件名
        newname = path + str(start_num + n) + '.jpg'

        # 用os模块中的rename方法对文件改名
        os.rename(oldname, newname)
        print(oldname, '======>', newname)

        n += 1

if __name__ == '__main__':
    path = "C:/Users/Shangjie Zou/PycharmProjects/Bird-recognition/Something-about-cv/imgs/涉禽/['鹳科']/"
    start_num = 119
    change_file_name(start_num, path)