import os


def file_count(folder):
    count = next(os.walk("C:/zeus/"+folder))[2]  # dir is your directory path as string
    return len(count)+1
