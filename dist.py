# -*- coding: utf-8 -*-
# Python 3


import time
import os
from glob import glob, iglob
from pathlib import Path


directory = r"<folder>"
RUNS = 20


def run_os_walk():
    a = time.time_ns()
    for i in range(RUNS):
        fu = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if
                  os.path.splitext(f)[1].lower() == '.jpg']
    print(f"os.walk\t\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found files: {len(fu)}")


def run_os_walk_glob():
    a = time.time_ns()
    for i in range(RUNS):
        fu = [y for x in os.walk(directory) for y in glob(os.path.join(x[0], '*.jpg'))]
    print(f"os.walk-glob\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found files: {len(fu)}")


def run_glob():
    a = time.time_ns()
    for i in range(RUNS):
        fu = glob(os.path.join(directory, '**', '*.jpg'), recursive=True)
    print(f"glob.glob\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found files: {len(fu)}")


def run_iglob():
    a = time.time_ns()
    for i in range(RUNS):
        fu = list(iglob(os.path.join(directory, '**', '*.jpg'), recursive=True))
    print(f"glob.iglob\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found files: {len(fu)}")


def run_pathlib_rglob():
    a = time.time_ns()
    for i in range(RUNS):
        fu = list(Path(directory).rglob("*.jpg"))
    print(f"pathlib.rglob\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found files: {len(fu)}")


def find_files(files, dirs=[], extensions=[]):
    # https://stackoverflow.com/a/45646357/2441026

    new_dirs = []
    for d in dirs:
        try:
            new_dirs += [ os.path.join(d, f) for f in os.listdir(d) ]
        except OSError:
            if os.path.splitext(d)[1].lower() in extensions:
                files.append(d)

    if new_dirs:
        find_files(files, new_dirs, extensions )
    else:
        return


def run_fast_scandir(dir, ext):    # dir: str, ext: list
    # https://stackoverflow.com/a/59803793/2441026

    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files



if __name__ == '__main__':
    run_os_walk()
    run_os_walk_glob()
    run_glob()
    run_iglob()
    run_pathlib_rglob()


    a = time.time_ns()
    for i in range(RUNS):
        files = []
        find_files(files, dirs=[directory], extensions=[".jpg"])
    print(f"find_files\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found files: {len(files)}")


    a = time.time_ns()
    for i in range(RUNS):
        subf, files = run_fast_scandir(directory, [".jpg"])
    print(f"fast_scandir\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found files: {len(files)}. Found subfolders: {len(subf)}")
