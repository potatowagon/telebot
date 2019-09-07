import subprocess
import os
import argparse

try:
    import pyautogui
except ModuleNotFoundError as e:
    cmd = ['pip', 'install', 'pyautogui']


def launch_tele():
    tele_path = os.path.join(os.environ['appdata'], 'Telegram Desktop', 'Telegram.exe')
    subprocess.call([tele_path]) 

def send_msg(msg):
    launch_tele()
    screenWidth, screenHeight = pyautogui.size()
    posX = screenWidth // 2
    posY = screenHeight // 1.11
    pyautogui.click(posX, posY)
    pyautogui.typewrite(msg)
    pyautogui.press('enter')

def main():
    parser = argparse.ArgumentParser(prog='telebot', description='Telegram spam bot.\n\nUsage: py hi-tele.py <number of times to send> <msg>\nExample usage: py hi-tele.py 100 "This is written by a bot :)"')
    parser.add_argument('times', type=int, help="number of times to send")
    parser.add_argument('msg', type=str, help="message")
    args = parser.parse_args()
    for i in range(args.times):
            send_msg(args.msg)

main()
