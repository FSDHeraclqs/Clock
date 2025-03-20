import time
import os

def countdown(minutes, message):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'\rTime left: {mins:02d}:{secs:02d}'
        print(timer, end='')
        time.sleep(1)
        seconds -= 1
    print(f'\n{message}')
    
    # 在 MacOS 和 Linux 上尝试通知
    if os.name == "posix":
        os.system(f'notify-send "{message}"')
    # 在 Windows 上尝试通知
    elif os.name == "nt":
        os.system(f'msg * "{message}"')

def focus_timer(focus_time=25, break_time=5):
    while True:
        countdown(focus_time, "Focus time is up! Take a break.")
        countdown(break_time, "Break is over! Time to focus.")

if __name__ == "__main__":
    focus_timer()
