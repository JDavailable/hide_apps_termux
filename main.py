# v2.5

import asyncio
import argparse
import os
import subprocess
import re

from os import path, remove
from colorama import Fore, Style

from config import DEBUG_IS, id_other_user, path_to_screen_folder, app_list, app_list_other_user, del_screen_app_list, path_to_tg_downloads, path_to_screenrecords_folder, launcher, home_path, path_to_conf, path_to_termux_prop, str_for_termux_prop, true_termux_home, default_str_for_termux_prop, true_launcher


async def hide_app(key):
    if DEBUG_IS:
        print(f"{Fore.BLUE}Вход в hide_app{Style.RESET_ALL}\n")
    user_id_ident = False
    userid_pattern = r"UserInfo\{(\d+):"
    result = subprocess.run("su -c pm list users", shell=True, text=True, capture_output=True)
    matches = re.findall(userid_pattern, result.stdout)
    
    if str(id_other_user) in matches:
        user_id_ident = True

    try:
        if key:
            for i in app_list:
                try:
                    result = subprocess.run(["su", "-c", "pm", "enable", i], check=True, stdout=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    bad_apps_list.append(i)
                    if DEBUG_IS:
                        print(f"Error enabling package {Fore.RED}{i}{Style.RESET_ALL}: {e}")
            if DEBUG_IS:
                if not bad_apps_list:
                    print(f"\n{Fore.RED}Проблемные sприложения:{Style.RESET_ALL}\n{bad_apps_list}\n")

            if user_id_ident:
            
                for p in app_list_other_user:
                    try:
                        subprocess.run(["su", "-c", "pm", "enable", "--user", id_other_user, p], check=True, stdout=subprocess.PIPE)
                    except subprocess.CalledProcessError as e:
                        print(f"Error enabling package {p} for user 10: {e}")
            
        else:
            for i in app_list:
                try:
                    result = subprocess.run(["su", "-c", "pm", "disable", i], check=True, stdout=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    bad_apps_list.append(i)
                    if DEBUG_IS:
                        print(f"Error disabling package {Fore.RED}{i}{Style.RESET_ALL}: {e}")
            if DEBUG_IS:
                print(f"\n{Fore.RED}Проблемные приложения:{Style.RESET_ALL}\n{bad_apps_list}\n")

            if user_id_ident:
                for p in app_list_other_user:
                    try:
                        subprocess.run(["su", "-c", "pm", "disable", "--user", "10", p], check=True, stdout=subprocess.PIPE)
                    except subprocess.CalledProcessError as e:
                        print(f"Error disabling package {p} for user 10: {e}")
            
    except Exception as e:
        print(f"Error executing commands: {e}")


async def hide_termux_home(key):
    if DEBUG_IS:
        print(f"{Fore.BLUE}Вход в hide_home{Style.RESET_ALL}\n")
    try:

        if not key:
            with open(path_to_conf, 'r') as config_file:
                data = config_file.readlines()
                if home_path not in data:
                    data.append(home_path + '\n')
                    try:
                        with open(path_to_conf, "w") as rewrite_conf:
                            rewrite_conf.writelines(data)
                    except Exception as e:
                        if DEBUG_IS:
                            print(f"Error: {path_to_conf} not available for write: {e}")
                with open(path_to_termux_prop, "r") as term_prop_file:
                    termux_prop = term_prop_file.readlines()
                    if str_for_termux_prop not in termux_prop:
                        termux_prop.append(str_for_termux_prop)
                        try:
                            with open(path_to_termux_prop, "w") as rewrite_prop:
                                rewrite_prop.writelines(termux_prop)
                        except Exception as e:
                            if DEBUG_IS:
                                print(f"Error: {path_to_termux_prop} not available for write: {e}")
        else:
            with open(path_to_conf, "r") as config_file:
                data = config_file.readlines()
                if true_termux_home not in data:
                    data.append(true_termux_home + '\n')
                    try:
                        with open(path_to_conf, "w") as rewrite_conf:
                            rewrite_conf.writelines(data)
                    except Exception as e:
                        if DEBUG_IS:
                            print(f"Error: {path_to_conf} not available for write: {e}")
                with open(path_to_termux_prop, "r") as term_prop_file:
                    termux_prop = term_prop_file.readlines()
                    if default_str_for_termux_prop not in termux_prop:
                        termux_prop.append(default_str_for_termux_prop)
                        try:
                            with open(path_to_termux_prop, "w") as rewrite_prop:
                                rewrite_prop.writelines(termux_prop)
                        except Exception as e:
                            if DEBUG_IS:
                                print(f"Error: {path_to_termux_prop} not available for write: {e}")
        print(done)
    except Exception as e:
        print("Err",e)

async def set_default_launcher(key):
    if DEBUG_IS: print(f"{Fore.BLUE}Вход в set_launcher{Style.RESET_ALL}\n")
    try:
        if not key:
            try:
                subprocess.run(["su", "-c", "cmd package set-home-activity", launcher], shell=False, stdout=subprocess.PIPE)
                subprocess.run(f"su -c kill $(su -c pidof -s {true_launcher})", shell=True, stdout=subprocess.DEVNULL)
            except Exception as e:
                if DEBUG_IS:
                    print(f"{Fore.RED}Error:{Style.RESET_ALL} Failed to set default launcher: {e}")
        else:
            try:
                subprocess.run(["su", "-c", "cmd package set-home-activity", true_launcher], shell=False, stdout=subprocess.PIPE)
                subprocess.run(f"su -c kill $(su -c pidof -s {launcher})", shell=True, stdout=subprocess.DEVNULL)
            except Exception as e:
                if DEBUG_IS:
                    print(f"Error: Failed to set true launcher: {e}")
        print(done)
    except Exception as e:
        print("Err", e)

async def del_tg_downloads():
    if DEBUG_IS:
        print(f"{Fore.BLUE}Вход в del_tg_downloads{Style.RESET_ALL}\n")
    try:
        for root, dirs, files in os.walk(path_to_tg_downloads):
            for file in files:
                if "Telegram" in file:
                    os.remove(os.path.join(root, file))
        if DEBUG_IS:
            print(done)
    except Exception as e:
        if DEBUG_IS:
            print(f"Error: Failed to delete Telegram downloads: {e}")

async def del_folders():
    if DEBUG_IS: print(f"{Fore.BLUE}Вход в del_folders{Style.RESET_ALL}\n")

    try:
        subprocess.run(["su", "-c", "rm", "-rf", "/sdcard/fooViewSave"], shell=False)
        subprocess.run(["su", "-c", "rm", "-rf", "/sdcard/Pictures/exteraGram"], shell=False)
        if DEBUG_IS: print(done)
    except Exception as e:
        if DEBUG_IS:
            print(f"{Fore.RED}Err del folder:{Style.RESET_ALL} ", e)


async def del_screenshots():
    if DEBUG_IS:
        print(f"{Fore.BLUE}Вход в del_sreenshots{Style.RESET_ALL}\n")
    try:
        for root, dirs, files in os.walk(path_to_screen_folder):
            for file in files:
                for app in del_screen_app_list:
                    if app in file:
                        os.remove(os.path.join(root, file))
        if DEBUG_IS:
            print(done)
    except Exception as e:
        if DEBUG_IS:
            print(f"Error: Failed to delete screenshots: {e}")


async def del_screenrecords():
    if DEBUG_IS:
        print(f"{Fore.BLUE}Вход в del_sreenrecors{Style.RESET_ALL}\n")
    try:
        subprocess.run(f"su -c rm -rf {path_to_screenrecords_folder}", shell=True)
        if DEBUG_IS:
            print(done)
    except Exception as e:
        if DEBUG_IS:
            print(f"{Fore.RED}Error: Failed to delete screen recordings:{Style.RESET_ALL}\n {e}")


async def disable_fingerprint_unlock_app():
    if DEBUG_IS: print(f"{Fore.BLUE}Вход в disable_figerprint{Style.RESET_ALL}")
    if not key:
        try: 
            subprocess.run("su -c dpm remove-active-admin mstoic.apps.disablefingerprintunlocktemporarily/.MyAdmin", shell=True, stdout=subprocess.PIPE)
            subprocess.run(["su","-c","pm disable mstoic.apps.disablefingerprintunlocktemporarily"], shell=False, stdout=subprocess.PIPE)            
            if DEBUG_IS:print(done)
        except Exception as e:
            if DEBUG_IS:
                print(f"{Fore.RED}Error:{Style.RESET_ALL}{e}")
    else:
        try:
            subprocess.run(["su","-c","pm enable mstoic.apps.disablefingerprintunlocktemporarily"], shell=False, stdout=subprocess.PIPE)            
            subprocess.run("su -c dpm set-active-admin mstoic.apps.disablefingerprintunlocktemporarily/.MyAdmin", shell=True, stdout=subprocess.PIPE)
            if DEBUG_IS:print(done)

        except Exception as e:
            if DEBUG_IS:
                print(f"{Fore.RED}Error:{Style.RESET_ALL}{e}")

# async def hide_folders:
    # if DEBUG_IS: print(f"{Fore.BLUE}Вход в hide_folders{Style.RESET_ALL}")
# 
    # if key:
        # try:
            # for folder_name in folders_list:
                # 
                # subprocess.run(["su", "-c", "mv", folder_name, )

async def main(key):
    if key:
        tasks = [
            asyncio.create_task(hide_app(key)),
            asyncio.create_task(hide_termux_home(key)),
            asyncio.create_task(set_default_launcher(key)),
            asyncio.create_task(disable_fingerprint_unlock_app()),
        ]
        await asyncio.gather(*tasks)
    else:
        tasks = [
            asyncio.create_task(set_default_launcher(key)),
            asyncio.create_task(hide_termux_home(key)),
            asyncio.create_task(del_tg_downloads()),
            asyncio.create_task(del_screenshots()),
            asyncio.create_task(del_screenrecords()),
            asyncio.create_task(hide_app(key)),
            asyncio.create_task(disable_fingerprint_unlock_app()),
            asyncio.create_task(del_folders())
        ]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--unhide', help='', action='store_true')
    args = parser.parse_args()
    key = bool(args.unhide)
    bad_apps_list = []
    user_id_ident = False
    done = f"{Fore.GREEN}Done\n{Style.RESET_ALL}"
    asyncio.run(main(key))
