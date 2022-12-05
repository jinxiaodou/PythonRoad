import glob
import os
from PIL import Image

# 1、获取文件夹名称
path = r'/Users/lijinshuai/Documents/个人文档/python历史/python项目/坦克大战'
newpath=r'/Users/lijinshuai/Documents/个人文档/python历史/python项目/坦克大战/images1/'
dirnames = [f for f in os.listdir(path) if os.path.isdir(path + "/" + f)]
print(dirnames)


def convertSize(jpgfile, outdir, width=112, height=112):  # 将图片的大小的尺寸调整为112*112

    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height))

        # if new_img.mode == 'P':
        #     new_img = new_img.convert("RGB")
        # if new_img.mode == 'RGBA':
        #     new_img = new_img.convert("RGB")

        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


# 2、遍历文件夹
for dir_name in dirnames:
    dir_path = path + "/" + dir_name

    # 3、创建新文件夹
    target_path = newpath
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # 4、遍历文件夹中的图片, 修改尺寸
    for pic in os.listdir(dir_path):  # 修改该文件夹下的图片
        if pic[0]=='e':
            convertSize(dir_path + "/" + pic, target_path, 30, 30)  # 另存为的文件夹路径
    print(dir_path + "文件夹下的图片处理完毕.\n")

print("全部文件夹下的图片处理完毕.")

