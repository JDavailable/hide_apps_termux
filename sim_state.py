from subprocess import run,PIPE
from time import sleep

def get_sim_state():
    raw_state = run('getprop gsm.sim.state | awk -F \',\' \'{print $2}\'', shell=True, stdout=PIPE)
    return raw_state.stdout.decode('utf-8')

def main():
    sleep(3)
    absent_var = 0
    while True:
        tmp = get_sim_state()
        
        if tmp == "ABSENT\n":
            absent_var += 1
            if absent_var >= 10:
                absent_var = 0
                sleep(15)
        if tmp == "PIN_REQUIRED\n":
            sleep(15)
            tmp = get_sim_state()

            if tmp != "READY\n" or tmp != "LOADED\n":
                run("termux-notification -t 'Reboot after 5 sec", shell=True)
                sleep(5)
                run("su -c reboot")
                with open(".tmp", "r") as f:
                    file = f.read()
                    
                    if int(file) < 3 or file == '':
                        file_len = int(file) + 1

                        with open(".tmp","w") as new_f:
                            new_f.write(str(file_len))

                    elif int(file) >= 3:
                        run("", shell=True)
                        with open(".tmp","w") as over_three:
                            over_three.write('0')                
        sleep(1)
        
    
if __name__ == "__main__":
    main()
