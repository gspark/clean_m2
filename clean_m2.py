# -*-coding:utf8 -*-
import os

import shutil


def gci(file_path):
    files = os.listdir(file_path)
    if len(files) == 0 and os.path.isdir(file_path):
        print file_path
        os.removedirs(file_path)

    for fi in files:
        fi_d = os.path.join(file_path, fi)
        if os.path.exists(fi_d):
            if os.path.isdir(fi_d):
                gci(fi_d)
            else:
                remove(file_path)
                break


def remove(file_path):
    path = os.path.split(file_path)[0]
    files = sorted(os.listdir(path))
    count = len(files)
    for index, item in enumerate(files, start=1):
        if index < count:
            small_version = os.path.join(path, item)
            print small_version
            if os.path.isdir(small_version):
                shutil.rmtree(small_version)
        elif index == count:
            file_path = os.path.join(path, item)
            files = os.listdir(file_path)
            need_remove = True
            for fi in files:
                name, subfix = os.path.splitext(fi)
                if subfix == '.jar':
                    need_remove = False
                    break
            if need_remove:
                print file_path
                shutil.rmtree(file_path)


if __name__ == '__main__':
    gci("e:\\opt\\.m2\\repository")
