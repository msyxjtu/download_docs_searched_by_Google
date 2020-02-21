# -*- coding:utf-8 -*-
# Author: Adam Mei
# Date: 2018-08-25
# Time: 09:14
# Name: pdf_rename.py
# ---------------------------------------------
import os

from pdfrw import PdfReader

from general_function import get_dir_from_console
from general_function import rename_filename_remove_forbidden_char


def get_all_files_name(path):
    """输出一个列表，包括一个文件夹当中所有的没有被隐藏的文件名称。（用.前缀来判断是否隐藏）"""
    all_file = os.listdir(path)
    for _ in all_file:
        if _[0] == '.':
            all_file.remove(_)

    for _ in all_file:
        yield _


def rename_file_to_pdf_title(path, filename):
    if path[-4:] == '.pdf':
        new_name = PdfReader(filename).Info.Title
        if new_name is not None:
            # Remove surrounding brackets that some pdf titles have
            new_name = new_name.strip('()') + '.pdf'
            new_name = rename_filename_remove_forbidden_char(new_name)
            new_full_name = os.path.join(path, new_name)
            print(new_full_name, filename)
            os.rename(filename, new_full_name)
        else:
            print(filename, 'no title found.')


if __name__ == '__main__':
    pdf_files_path = get_dir_from_console()
    for root, dirs, files in os.walk(pdf_files_path):
        for _ in files:
            if _[-3:] == 'pdf':
                rename_file_to_pdf_title(root, os.path.join(root, _))
