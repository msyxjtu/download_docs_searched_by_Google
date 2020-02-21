#!/usr/bin/env python
# encoding: utf-8
"""
@author: Adam Mei
@file: general_function.py
@time: 2019/7/13 20:45
@desc:
"""

import os


def get_dir_from_console():
    """复制文件夹地址然后粘贴到控制台，如果是windows，会自动处理为程序可以用的地址"""
    dir_temp = input('请输入文件路径:')
    if os.name == 'nt':
        directory = dir_temp.replace('\\', '/')
    elif os.name == 'posix':
        directory = dir_temp
    else:
        directory = 'unknown'

    return directory


def rename_filename_remove_forbidden_char(filename_str, replace_with='_'):
    un_acceptable_str = ['?', '&', '\\', '/', '*', '>', '<', ':', '|']

    for _ in un_acceptable_str:
        filename_str = filename_str.replace(_, replace_with)

    return filename_str


if __name__ == '__main__':
    print(rename_filename_remove_forbidden_char('?&<>||\\/\/\*:xyz.pdf'))
