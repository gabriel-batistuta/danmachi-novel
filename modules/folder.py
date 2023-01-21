import os

def makeFolder():
    if os.path.isdir('./novels'):
        pass
    else:
        os.mkdir('./novels')

def makeNovelFolder(title):
    if os.path.isdir(f'./novels/{title}'):
        pass
    else:
        os.mkdir(f'./novels/{title}')