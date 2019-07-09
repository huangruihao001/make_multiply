# 参考网址：https://www.cnblogs.com/ssyfj/p/9051734.html
from PIL import Image
import PIL.ImageChops as IC
import os

def make_multiply(img1_name, img2__name, img3_name):
    """
    将图片进行正片叠底处理
    :param img1_name:
    :param img2__name:
    :param img3__name:
    :return:
    """
    img1 = Image.open(img1_name)
    img2 = Image.open(img2__name)
    IC.multiply(img1, img2).save(img3_name) #是以img1为源，所以以img1的尺寸为准


if __name__ == '__main__':
    print("请将黑白底版放在文件夹“黑白底片模板”中")
    print("请将材质图片放在文件夹“待处理材质”中")
    input("按回车键开始正片叠底处理……")
    negative_list = os.listdir("./黑白底片模板/")
    filename_list = os.listdir("./待处理材质/")
    # make_multiply("./黑白底片模板/平凹板.jpg", "./待处理材质/风信蓝.jpg", "1.jpg")
    # make_multiply("./待处理材质/风信蓝.jpg", "./黑白底片模板/平凹板.jpg", "2.jpg")
    for n in negative_list:
        negative = n.replace(".jpg", "")
        negative_path = "./黑白底片模板/" + n
        # 判断处理结果是否存在
        try:
            os.makedirs("./处理结果/" + negative)
        except:
            pass
        for f in filename_list:
            filename = f.replace(".jpg", "")
            filename_path = "./待处理材质/" + f
            dir_path = "./处理结果/" + negative + "/" + negative + filename + ".jpg"
            make_multiply(negative_path, filename_path, dir_path)
    input("正片叠底处理完成！请在文件夹“处理结果”中查看结果……")