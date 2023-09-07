from pynput.keyboard import Key, Controller
from time import sleep

Keyboard = Controller()

filein = input("Enter file name: ")
text = open(filein, 'r')
print("Preparing macro...")
sleep(3)
for line in text:
    Keyboard.type(line)
    Keyboard.press(Key.enter)
    Keyboard.press(Key.backspace)

print("Job done!")
