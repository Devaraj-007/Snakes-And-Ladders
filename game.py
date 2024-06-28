import tkinter as tk
from PIL import ImageTk,Image
import random
from gtts import gTTS
# from playsound import playsound
import os


root = tk.Tk()
root.title("Snakes and Ladders ")
root.geometry('1200x800')

F1=tk.Frame(root,width=1200,height=800,relief='raised')
F1.place(x=0,y=0)

#Set Board
img1=ImageTk.PhotoImage(Image.open('snake-ladder.jpg'))
Lab=tk.Label(F1,image=img1)
Lab.place(x=0,y=0)

#player-1 coin
player_1=tk.Canvas(root,width=40,height=40)
player_1.create_oval(10,10,40,40,fill='blue')

#player-2 coin
player_2=tk.Canvas(root,width=40,height=40)
player_2.create_oval(10,10,40,40,fill='red')

#hows turn first...by default player-1
turn=1

# initial positions of players
pos1=None
pos2=None

#Ladder Bottom to Top
Ladder={4:25,13:46,33:49,42:63,50:69,62:81,74:92}

#snakes head to Tail
Snake={99:41,89:53,76:58,66:45,54:31,43:18,40:3,27:5}

def start_game():
    global im
    global b1,b2
    #Butons for Players
    #player -1
    b1.place(x=900,y=400)
    #player -2
    b2.place(x=900,y=550)

    #Dice Image to show
    im=Image.open("unnamed.png")
    im=im.resize((65,65))
    im=ImageTk.PhotoImage(im)
    b=tk.Button(root,image=im,height=80,width=80)
    b.place(x=980,y=200)

    #Exite Button
    b=tk.Button(root,text="Click Here to End Game",height=3,width=20,fg="red",bg="yellow",font=('Cursive',14,'bold'),activebackground='red',command=root.destroy)
    b.place(x=900,y=20)

def reset_coins():
    global player_1,player_2
    global pos1,pos2

    player_1.place(x=0,y=630)
    player_2.place(x=50,y=630)

    pos1=0
    pos2=0
# To store Dice Images
Dice=[]
def load_dice_images():
    global Dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for nam in names:
        im=Image.open(nam)
        im=im.resize((65,65))
        im=ImageTk.PhotoImage(im)
        Dice.append(im)

def roll_dice():
    global Dice
    global turn
    global pos1,pos2
    global b1,b2

    r=random.randint(1,6)
    b3=tk.Button(root,image=Dice[r-1],height=80,width=80)
    b3.place(x=980,y=200)
    Lad = 0 # No Ladder
    if turn==1:
        if (pos1+r)<=100:
            pos1 = pos1 + r
        Lad=check_ladder(turn)
        check_Snake(turn)
        move_coin(turn,pos1)
        if r!=6 and Lad!=1:
            turn=2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if (pos2+r)<=100:
            pos2 = pos2 + r
        Lad=check_ladder(turn)
        check_Snake(turn)
        move_coin(turn,pos2)
        if r!=6 and Lad!=1:
            turn=1
            b1.configure(state='normal')
            b2.configure(state='disabled')
    is_Winner()

def is_Winner():
    global pos1,pos2

    if pos1==100:
        msg= "Player - 1 is the Winner...!!"
        Lab= tk.Label(root,text=msg,height=2,width=20,bg='red',font=('cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
    elif pos2==100:
        msg= "Player - 2 is the Winner...!!"
        Lab= tk.Label(root,text=msg,height=2,width=20,bg='red',font=('cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
        

def check_ladder(Turn):
    global pos1,pos2
    global Ladder

    f=0 # No Ladder
    if Turn==1:
        if pos1 in Ladder:
            pos1 = Ladder[pos1]
            f=1
        else:
            if pos2 in Ladder:
                pos2 = Ladder[pos2]
                f=1
        return f

def check_Snake(Turn):
    global pos1,pos2

    if Turn==1:
        if pos1 in Snake:
            pos1=Snake[pos1]   # Chenging position to tail
    else:
        if pos2 in Snake:
            pos2=Snake[pos2]

def move_coin(Turn,r):
    global player_1,player_2
    global index
    if Turn==1:
        player_1.place(x=index[r][0],y=index[r][1])
    else:
        player_2.place(x=index[r][0],y=index[r][1])



def get_index():
    global player_1,player_2
    Num=[100,99,98,97,96,95,94,93,92,91,
         81,82,83,84,85,86,87,88,89,90,
         80,79,78,77,76,75,74,73,72,71,
         61,62,63,64,65,66,67,68,69,70,
         60,59,58,57,56,55,54,53,52,51,
         41,42,43,44,45,46,47,48,49,50,
         40,39,38,37,36,35,34,33,32,31,
         21,22,23,24,25,26,27,28,29,30,
         20,19,18,17,16,15,14,13,12,11,
         1,2,3,4,5,6,7,8,9,10]
    row=0
    i=0
    for x in range(1,11):
        col=0
        for y in range(1,11):
            index[Num[i]]=(col,row)
            col = col + 62.2
            i = i+1
        row = row + 62.2

#player -1 Button
b1=tk.Button(root,text="player - 1",height=3,width=20,fg="red",bg="cyan",font=('Cursive',14,'bold'),activebackground='blue',command=roll_dice)

#player -2 Button
b2=tk.Button(root,text="player - 2",height=3,width=20,fg="red",bg="orange",font=('Cursive',14,'bold'),activebackground='red',command=roll_dice)

#To store x & y Co-ordinates of given Num
index={}

#keep coins at initial positions
reset_coins()

#Get index of each number
get_index()
#Load Dice Images
load_dice_images()
#setting all the butons
start_game()
root.mainloop()

