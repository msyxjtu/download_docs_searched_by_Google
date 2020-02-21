# -*- coding:utf-8 -*-
# Author: Adam Mei
# Date: 2019/7/20
# Time: 10:18
# Name: main
# ---------------------------------------------

import os
import pickle
import time

import requests
from googlesearch import search

from general_function import rename_filename_remove_forbidden_char
from key_word import to_download_keyword
from pdf_rename import rename_file_to_pdf_title


def download_files_from_google(key_word,
                               url_list_total,
                               filetype='pdf',
                               output_count=10,
                               output_folder=os.getcwd()):

    key_word_for_search = key_word + ' filetype:' + filetype
    print(key_word_for_search)
    url_list = search(key_word_for_search, stop=output_count)
    print(url_list)
    # try:
    for url in url_list:
        if url in url_list_total:
            continue
        else:
            print(url)
            url_list_total.append(url)
            filename = url.split('/')[-1]
            if filename[-3:] != filetype:
                continue
                # filename = filename + '.' + filetype
            # print(filename)

            else:
                try:
                    page_content = requests.get(url, allow_redirects=True)
                except:
                    pass
        filename = rename_filename_remove_forbidden_char(filename)

        try:
            output_filename = os.path.join(output_folder, filename)
            with open(output_filename, 'wb') as target_file:
                target_file.write(page_content.content)
            rename_file_to_pdf_title(output_folder, os.path.join(output_folder, filename))
        except:
            if os.path.exists(output_filename):
                os.remove(output_filename)  # 如果有错，就直接把文件删掉，避免出现无用文件。

    return url_list_total


if __name__ == '__main__':
    print('使用这个脚本的时候，需要把VPN模式改为全局模式，否则会报错。')
    if os.path.exists(os.path.join(os.getcwd(), 'search_log')):
        search_log_list = pickle.load(open('search_log', 'rb'))
    else:
        search_log_list = []

    root_download_dir = os.path.join(os.getcwd(), 'download_file_folder')
    if not os.path.exists(root_download_dir):
        os.makedirs(root_download_dir)

    for _ in to_download_keyword:
        target_folder = os.path.join(root_download_dir, _)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        search_log_list = download_files_from_google(_, search_log_list, output_count=3, output_folder=target_folder)

    pickle.dump(search_log_list, open('search_log', 'wb'))
