# coding:gbk
import os
a = os.system("git add .")
b = os.system("git commit -m \"abcd\"")
c = os.system("git push -u origin main")
print("上传成功！")