import os
import shutil

def clearDiretory():
    dirPath = './novels'
    if os.path.isdir(dirPath):
        if len(os.listdir(dirPath)) != 0:
            # print('tem arquivos no diretório')
            try:
                shutil.rmtree(dirPath)
            except OSError as e:
                print(f"Error:{ e.strerror}")
        else:
            # print('diretório vazio')
            os.rmdir('./novels')
    else:
        pass

clearDiretory()