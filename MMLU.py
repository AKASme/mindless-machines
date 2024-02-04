import pyautogui as p #movement of cursor and typing of text
from time import sleep#just for waiting; nothing else
import datasets as d #importing datasets from HuggingFace
from pyperclip import paste #just for pasting
p.FAILSAFE = False #pyautogui will automatically stop and trigger the failsafe if the mouse cursor is in a corner.
configs = d.get_dataset_config_names("Stevross/mmlu") #gets all topics (called configs in datasets library)
responsesFile = open("GPT (MMLU).txt", "a+")
p.moveTo(120, 1200)
sleep(1)
p.click() #opens chrome
p.moveTo(960, 600, duration=0.75) # so that taskbar dissapears 
p.click() #just in case
for c in configs:
    dataset = d.load_dataset("Stevross/mmlu", c, split="test")
    for i in range(2, 4):
        p.moveTo(640, 1110)
        p.click() #clicks on gpt input box
        p.typewrite(dataset[i]["question"])
        p.typewrite(" please respond with only one letter: the letter of the choice that corresponds to your answer.")
        p.hotkey("shift", "enter")
        p.typewrite("A. ")
        p.typewrite(dataset[i]["choices"][0])
        p.hotkey("shift", "enter")
        p.typewrite("B. ")
        p.typewrite(dataset[i]["choices"][1])
        p.hotkey("shift", "enter")
        p.typewrite("C. ")
        p.typewrite(dataset[i]["choices"][2])
        p.hotkey("shift", "enter")
        p.typewrite("D. ")
        p.typewrite(dataset[i]["choices"][3])
        p.press("enter") #no better way to do this; cant concatenate strings in typewrite()
        sleep(8)
        p.moveTo(1122, 1015)
        sleep(0.1)
        p.click() #instead of scrolling, gpt will automatically have a "go to bottom" button
        p.sleep(0.1)
        p.moveTo(670, 985)
        p.click() #copies response
        copied = paste()
        responsesFile.write(copied[:2])
        responsesFile.write(" ")
        responsesFile.write({0:"A.", 1:"B.", 2:"C.", 3:"D."}[dataset[i]["answer"]])
        responsesFile.write(" ")
        responsesFile.write(str(copied[:2] == {0:"A.", 1:"B.", 2:"C.", 3:"D."}[dataset[i]["answer"]]))
        responsesFile.write("\n") #sadly i dont think theres a better way to do this; if i try to put parentheses around the inputs so that it counts as one string it just thinks that it is a tuple
        #also will change to with open(blah blah blah) as responsesFile
