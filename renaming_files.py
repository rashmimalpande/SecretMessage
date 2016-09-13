import os
import re


def rename():
    # get the file names
    list = os.listdir(r"C:\Users\rashm\PycharmProjects\SecretMessage\prank")
    # print(list)
    current = os.getcwd()
    # print(current)
    os.chdir(r"C:\Users\rashm\PycharmProjects\SecretMessage\prank")
    for file_name in list:
        new_name = re.sub(r'[0-9]', "", file_name)
        os.rename(file_name, new_name)

    os.chdir(current)


rename()
