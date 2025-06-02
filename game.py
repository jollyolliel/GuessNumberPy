from tkinter import *
import random

colors = ["#00FF00", "#00FF00", "#00FF00", "#00FF00", "#66FF00", "#FFFF00", "#FF9900", "#FF3300", "#FF0000"]

BACKGROUND = "#F06543"
TEXT = "Black"
BUTTON = "#2D7DD2"
CLICK = "#89AAE6"

window = Tk()
window.title("Game")
window.geometry('650x500')
window.config(background=BACKGROUND)
randomtransition = 7
dot = 0
randomNumber = None
gameDone = True
tries = 0

def randomize():
    global randomtransition, dot, randomNumber, gameDone
    if gameDone:
        triesLbl.config(highlightbackground=colors[tries])
        imgLbl.config(image=diceImg)
        triesLbl.config(text="Tries: " + str(tries))
        if randomtransition > 0:
            randomtransition -= 1
            if dot == 3:
                dot = 0
            dot += 1
            if dot == 1:
                thinkingLbl.config(image=oneDot)
            elif dot == 2:
                thinkingLbl.config(image=twoDot)
            elif dot == 3:
                thinkingLbl.config(image=threeDot)

            thinkingLbl.after(400, randomize)
        if randomtransition == 0:
            thinkingLbl.config(image="")
            inputBox.config(state='normal')
            randomNumber = random.randint(0,100)
            triesLbl.config(highlightbackground=colors[tries])
            inputBox.focus_set()
            gameDone = False
def reset():
    global randomtransition, dot, randomNumber, tries, gameDone
    gameDone = True
    inputBox.config(state='disabled')
    randomtransition = 7
    dot = 0
    randomNumber = None
    tries = 0


def every(event):
    text = inputBox.get()
    if not text.isdigit():
        inputBox.delete(len(text)-1, END)

def feedback(event):
    global tries, gameDone
    playerInput = int(inputBox.get())
    if randomNumber and playerInput != "":
        if randomNumber > playerInput:
            imgLbl.config(image=upImg)
        elif randomNumber < playerInput:
            imgLbl.config(image=downImg)
        elif randomNumber == playerInput:
            imgLbl.config(image=correctImg)
            imgLbl.after(1000, reset)
        tries += 1
    triesLbl.config(text="Tries: " + str(tries))
    inputBox.delete(0,END)
    if tries >= 8:
        triesLbl.config(highlightbackground=colors[8])
    else:
        triesLbl.config(highlightbackground=colors[tries])

correctImg = PhotoImage(file="assets/correct.png")
diceImg = PhotoImage(file="assets/dice.png")
upImg = PhotoImage(file="assets/up.png")
downImg = PhotoImage(file="assets/down.png")
oneDot = PhotoImage(file="assets/dots1.png")
twoDot = PhotoImage(file="assets/dots2.png")
threeDot = PhotoImage(file="assets/dots3.png")
logoImg = PhotoImage(file="assets/logo.png")

gameIntoLbl = Label(window, image=logoImg, bg=BACKGROUND)
gameIntoLbl.grid(column=0, row=0,columnspan=3, pady=15)

gameInstuctionsLbl = Label(window, bg=BACKGROUND, fg=TEXT, font=("Arial", 13, 'bold'), text="   This is a number guessing game. You will choose a dificulty and the computer \nwill choose a number. You will guess a number and it will tell you to guess \nhigher or lower.")
gameInstuctionsLbl.grid(column=0, row=1,columnspan=3, pady=7)

imgLbl = Label(window, image=diceImg, bg=BACKGROUND)
imgLbl.grid(column=0, row=2, rowspan=2)

inputBox = Entry(window, bg="darkgrey", state='disabled')
inputBox.grid(column=1,row=2)

triesLbl = Label(window, text="Tries: 0", fg="#2D7DD2", bg=BACKGROUND, font=("Arial", 12, 'bold'),  height=2, width=10)
triesLbl.config(highlightbackground="red", highlightthickness=4)
triesLbl.grid(column=1, row=3)

exitBtn = Button(window, text="Exit", bg=BUTTON, fg="black", width=15, height=4, command=window.destroy, activebackground=CLICK)
exitBtn.grid(column=2,row=2)

randomBtn = Button(window, text="Randomize", bg=BUTTON, fg="black", width=15, height=4, command=randomize, activebackground=CLICK)
randomBtn.grid(column=2,row=3)

thinkingLbl = Label(window, bg=BACKGROUND)
thinkingLbl.grid(column=0,row=4, columnspan=3, padx=(0,10))

window.bind('<Return>', feedback)
window.bind('<Key>', every)

window.mainloop()