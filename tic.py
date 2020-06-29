from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap('img/toeico.ico')
root.geometry("570x710")
playerNum = 1
bList = []
myFont = font.Font(size=50)
#even turns are X, odd turns are O

def twoPlayer():
    global multPlayers
    global t
    global f
    t.destroy()
    f.destroy()
    multPlayers = True
    startGame()

def onePlayer():
    global multPlayers
    global t
    global f
    multPlayers = False
    t.destroy()
    f.destroy()
    startGame()

multPlayers = False
t = Button(root, text="One Player", command= onePlayer, font = myFont)
f = Button(root, text="Two Player", command= twoPlayer, font = myFont)
t.place(relx = .5, rely = .15, anchor=CENTER)
f.place(relx= .5, rely = .5, anchor=CENTER)

def checkDone():
    global myFont
    global playerNum
    global bList
    for x in range (3):
        one = bList[x]['text']
        colTwo = bList[x+3]['text']
        colThree = bList[x+6]['text']
        if one == colTwo and colTwo == colThree and one != "":
            for l in bList:
                l.destroy()
            l = Label(root, text= one + " wins!", font = myFont)
            l.place(relx=.5,rely=.5,anchor=CENTER)
            return True
    x = 0
    while x < 9:
        one = bList[x]['text']
        two = bList[x+1]['text']
        three = bList[x+2]['text']
        if one == two and two == three and one != "":
            for l in bList:
                l.destroy()
            l = Label(root, text=one + " wins", font=myFont)
            l.place(relx=.5,rely=.5,anchor=CENTER)
            return True
        x += 3
    tlc = bList[0]['text']
    middle = bList[4]['text']
    brc = bList[8]['text']
    if tlc == middle and middle == brc and tlc !="":
        for l in bList:
            l.destroy()
        l = Label(root, text= tlc + " wins!", font = myFont)
        l.place(relx=.5, rely=.5, anchor=CENTER)
        return True

    trc = bList[2]['text']
    blc = bList[6]['text']
    if trc == middle and middle == blc and trc != "":
        for l in bList:
            l.destroy()
        l = Label(root, text= trc + " wins!", font = myFont)
        l.place(relx=.5, rely=.5, anchor=CENTER)
        return True
    if playerNum == 10:
        for x in bList:
            x.destroy()
        l = Label(root, text="Tie Game!", font = myFont)
        l.place(relx=.5, rely=.5, anchor=CENTER)
        return True
        

def click(index):
    global bList
    global playerNum
    global multPlayers
    if bList[index]['text'] == "":
        playerNum += 1
        if playerNum % 2 == 0:
            bList[index]['text'] = 'X'
            bList[index]['padx'] = 32
        else:
            bList[index]['text'] = 'O'
            bList[index]['padx'] = 27
        isDone = checkDone()
        if isDone:
            return
    else:
        return
    if not multPlayers:
        index = random.randint(0,8)
        while bList[index]['text'] != "":
            index = random.randint(0,8)
        playerNum += 1
        if playerNum % 2 == 0:
            bList[index]['text'] = 'X'
            bList[index]['padx'] = 32
        else:
            bList[index]['text'] = 'O'
            bList[index]['padx'] = 27
        checkDone()
        


def startGame():
    global bList
    for x in range (9):
        num = x
        bList.append(Button(root, text="", padx=60, pady=40,command=lambda i=num: click(i),font=myFont))

    bList[0].grid(row=0,column=0)
    bList[1].grid(row=0,column=1)
    bList[2].grid(row=0,column=2)

    bList[3].grid(row=1,column=0)
    bList[4].grid(row=1,column=1)
    bList[5].grid(row=1,column=2)

    bList[6].grid(row=2,column=0)
    bList[7].grid(row=2,column=1)
    bList[8].grid(row=2,column=2)


root.mainloop()
