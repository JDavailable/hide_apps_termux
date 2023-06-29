from subprocess import run, PIPE, DEVNULL
from os import listdir, path

def scan_folder():
    try:
        list_dir = listdir(folder_path)
        global list_pdf
        tmp = 0
        
        for i in list_dir:
            if path.isfile(path.join(folder_path, i)) and i.endswith(".pdf"):
                list_pdf.append(i)
    except Exception as e:
        print("\n", e)

def move_pdf():
    path_bkp = "/data/data/com.termux/files/home/pdf" 
    try:
        if list_pdf:
            for i in list_pdf:
                path_to_pdf = "/sdcard/Download/" + i
                run(["mv",path_to_pdf ,path_bkp], shell=False, stdout=DEVNULL)
            gpg_list = listdir(path_bkp)
            
            for i in gpg_list:
                #run(["gpg", "-c", i])
                print(i)
    except Exception as e:
        print("\n",e)

def get_pdf_list():

    folder_path = "/sdcard/Download"
        
    folder = listdir(folder_path)
    pdf_list = [name for name in folder]
