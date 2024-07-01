import os
a = os.system("git add .")
print(a)
b = os.system("git commit -m \"abcd\"")
print(b)
c = os.system("git push -u origin main")
print(c)