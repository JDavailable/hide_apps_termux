# version 1.2
import asyncio
import argparse
import os
from os import path, remove
from subprocess import run
from shutil import rmtree
from time import time

from config import DEBUG_IS
from config import path_to_screen_folder
from config import app_list
from config import app_list_user10
from config import del_screen_app_list
from config import path_to_tg_downloads
from config import path_to_screenrecords_folder
from config import launcher
from config import home_path
from config import path_to_conf
from config import path_to_termux_prop
from config import str_for_termux_prop
from config import true_termux_home
from config import default_str_for_termux_prop
# Проверка флага запуска скрипта
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--unhide', help='', action='store_true')
 # Необходимые переменные
args = parser.parse_args()
key = bool(args.unhide)

async def hide_app(): # Скрытие приложений посредством pm hide и перебора package name из config.py

    if DEBUG_IS:
        print("Вход в hide_app")
    
    if key:
        for i in app_list:
            run(f"su -c pm unhide {i}", shell=True,  check=False, capture_output=False)
        for p in app_list_user10:
            run(f"su -c pm unhide --user 10 {p}", shell=True, check=False, capture_output=False)
    if not key:
        for i in app_list:
            run(f"su -c pm hide {i}", shell=True, check=False, capture_output=False)
        for p in app_list_user10:
            run(f"su -c pm hide --user 10 {p}", shell=True, check=False, capture_output=False)

async def del_tg_downloads(): # Фунция удаляющая папку телеги в загрузках

    if DEBUG_IS:
        print("Вход в del_tg")

    if path.exists(path_to_tg_downloads):  # проверяем, существует ли папка
        rmtree(path_to_tg_downloads, ignore_errors=False, onerror=None)


# Фунцкия изменяющая домашнюю дирректорию термукса home на home2
async def hide_termux_home():

    if DEBUG_IS:
        print("Вход в hide_home")

    if not key:########################################
               ################## Работа с файлом .zshrc при флаге hide ######################

        with open(path_to_conf, 'r') as config_file:
        
            data = config_file.readlines()
            
            for index, item in enumerate(data):
                if home_path == item:
                    data[index] = home_path
                    try:
                        with open(path_to_conf, "w") as rewrite_conf:
                            rewrite_conf.writelines(data)
                            rewrite_conf.close()
                    except: 
                        if DEBUG_IS: 
                            print("Error:" + path_to_conf + " not avalible for write!")
                    break
            else:
                with open(path_to_conf, "a") as rewrite_conf:
                    rewrite_conf.write(home_path + '\n')
                    rewrite_conf.close()
               
        ######### """Работа с файлом termux.properties при флаге hide """########
       
        with open(path_to_termux_prop, "r") as term_prop_file:
            termux_prop = term_prop_file.readlines()
            for index, item in enumerate(termux_prop):
                if str_for_termux_prop == item or default_str_for_termux_prop == item:
                    data[index] = str_for_termux_prop
                    try:
                        with open(path_to_termux_prop, "w") as rewrite_prop:
                            rewrite_prop.writelines(termux_prop)
                            rewrite_prop.close()
                    except: 
                        if DEBUG_IS: 
                            print("Error:" + path_to_termux_prop + " not avalible for write!")



    if key:########################################
           ################## Работа с файлом .zshrc при флаге unhide ######################
        with open(path_to_conf, "r") as config_file:
            data = config_file.readlines()
            for index, item in enumerate(data):
                print(f"{index}: {item}")
                if home_path == item or true_termux_home == item:
                    data[index] = true_termux_home
                    try:
                        with open(path_to_conf, "w") as rewrite_conf:
                            rewrite_conf.writelines(data)
                            rewrite_conf.close()
                    except: 
                        if DEBUG_IS: print("Error:" + path_to_conf + " not avalible for write!")
                    break
            else:
                with open(path_to_conf, "a") as config_f:
                    config_f.write(true_termux_home)
                    config_f.close()
                if DEBUG_IS: print(f"String: {home_path} not find in {path_to_conf}\n {true_termux_home} will be addet")
                
           ############ Работа с файлом termux.properties при флаге unhide #############
        # if key ↓
        with open(path_to_termux_prop, "r") as term_prop_file:
            termux_prop = term_prop_file.readlines()
            for index, item in enumerate(termux_prop):
                if str_for_termux_prop == item:
                    data[index] = default_str_for_termux_prop
                    try:
                        with open(path_to_termux_prop, "w") as rewrite_prop:
                            rewrite_prop.writelines(termux_prop)
                            rewrite_prop.close()
                    except: 
                        if DEBUG_IS: 
                            print("Error:" + path_to_termux_prop + " not avalible for write!")
                    break
    run("termux-reload-settings", shell=True)
#run("source ", shell=True)
# Функция ставит сторонний лаунчера по дефолту
async def set_default_launcher():
    if DEBUG_IS:
        print("Вход в set_launcher")
    run(f"su -c cmd package set-home-activity {launcher}", shell=True)
    
# Фунция удаляющая скриншоты по тригер-слову, в данном варианте - "Telegram"
async def del_screenshots():
    if DEBUG_IS:
        print("Вход в del_sreenshots")
    for root, dirs, files in os.walk(path_to_screen_folder):
        for file in files:
            for app in del_screen_app_list:
                if app in file:
                    try:
                        remove(f"{root}/{file}")
                        if DEBUG_IS:
                            print("Скрины удалены")
                    except:
                        if DEBUG_IS:
                            print("Ошибка удаления скринов")


async def del_screenrecords():
    if DEBUG_IS:
        print("Вход в del_sreenrecors")
        try:
            run(f"su -c rm -f {path_to_screenrecords_folder}*", shell=True)
            if DEBUG_IS:
                print("Видео удалены")
        except:
            if DEBUG_IS:
                print("Ошибка удаления видео")

async def main():
    if key:
        tasks = [
            asyncio.create_task(hide_app()),
            asyncio.create_task(hide_termux_home()),
        ]
        await asyncio.gather(*tasks)

    if not key:
            tasks =[
                asyncio.create_task(del_tg_downloads()), 
                asyncio.create_task(del_screenshots()), 
                asyncio.create_task(set_default_launcher()),
                asyncio.create_task(del_screenrecords()),
            ]
            await asyncio.gather(*tasks)

if not key:
    timer = time() + 2
    temp = 0
    while True:
	    result = os.popen('su -c getevent /dev/input/event4 |  grep -m 1 "00000001" ').read()
	    if result:
	        temp += 1
	        if temp == 3:
	            asyncio.run(main())
	            break

	        if time() > timer:
	            temp = 0
	            timer = time() + 2
if key:
    asyncio.run(main())

