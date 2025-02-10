
import os

os.chdir('D:\\Music')

print(os.getcwd())

for f in os.listdir():
    print(f)