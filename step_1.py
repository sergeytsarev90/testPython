import  tkinter
import PIL
import os
import psutil
import sys
import shutil

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("File ", newfile, " make")
            return True
        else:
            print("Problem")
            return False

def del_dublicats(dirname):
    file_list = os.listdir(dirname)
    double_count = 0

    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                double_count += 1
                print("Файл",fullname," был удален")
    return double_count

print('hello world')
name = input('Your name:')

print(name," Hello")
answer = ''
while answer != 'q':
       answer = input("Lets work (y/n)")
       if answer == 'y':
            print("good")
            print("1- Files")
            print("2- System info")
            print("3- Process")
            print("4- Dublicate")
            print("5- Dublicate user file")
            print("6- Delete dublicate")
            do = int(input())
            if do == 1:
              print(os.listdir())
            elif do == 2:
              print(os.name)
            elif do == 3:
              print(psutil.pids())
            elif do == 4:
                file_list = os.listdir()
                i = 0
                while i < len(file_list):
                    duplicate_file(file_list[i])
                    i += 1
            elif do == 5:
                filename = input('Укажите имя файла')
                duplicate_file(filename)
            elif do == 6:
                dirname = input('Укажите имя директории')
                count = del_dublicats(dirname)
                print("Delete files ", count)


            else:
              pass
       elif answer=='n':
            pass
       else:
            print("bad")
