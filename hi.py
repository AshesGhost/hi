import argparse
import subprocess
import shutil
from plyer import notification
from datetime import datetime


def line():
    terminal_width = shutil.get_terminal_size().columns
    print("\rhi!:"+"-" * (terminal_width-4))

def parse_commands():
    parser = argparse.ArgumentParser(description="hi!")

    parser.add_argument("--run", type=str, help="Command to run")

    return parser.parse_args()

args = parse_commands()

def main():
    try:
        if args.run:
            start = datetime.now()
            
            #proc = subprocess.Popen(shlex.split(args.run))

            proc = subprocess.Popen(args.run, shell=True)

            proc.wait()

            end = datetime.now()
            line()
            print("Start :", start.strftime("%H:%M:%S"))
            print("End   :", end.strftime("%H:%M:%S"))
            print("Diff  :", end - start)

            try:
                
                notification.notify(
                    title="Task Finished",
                    message=f"Finished in {end - start}",
                  #  app_icon=r"PATH ICON",

                    timeout=1)
            except Exception as e:
                print(e)
               
    except:
        pass
        
main()