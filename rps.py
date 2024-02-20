from tkinter import *
from PIL import Image,ImageTk
from random import randint

window=Tk()
window.title("rock paper scizzor")
window.configure(background="black")

img_rock1=ImageTk.PhotoImage(Image.open("rock.jpeg").resize((200, 200)))
img_paper1=ImageTk.PhotoImage(Image.open("paper.jpeg").resize((200, 200)))
img_scizzor1=ImageTk.PhotoImage(Image.open("scizzor.jpeg").resize((200, 200)))
img_rock2=ImageTk.PhotoImage(Image.open("rock.jpeg").resize((200, 200)))
img_paper2=ImageTk.PhotoImage(Image.open("paper.jpeg").resize((200, 200)))
img_scizzor2=ImageTk.PhotoImage(Image.open("scizzor.jpeg").resize((200, 200)))


player=Label(window,image=img_scizzor1)
comp=Label(window,image=img_scizzor2)
comp.grid(row=1,column=0)
player.grid(row=1,column=4)

comp_scr=Label(window,text=0,font=("arial",50,"bold"), fg="red")
plyr_scr=Label(window,text=0,font=("arial",50,"bold"),fg="green")
comp_scr.grid(row=1,column=1)
plyr_scr.grid(row=1,column=3)


plyr_lb=Label(window,font=("arial",30,"bold"),text="Player", fg="green",bg="black")
comp_lb=Label(window,font=("arial",30,"bold"),text="Computer" ,fg="red",bg="black")
plyr_lb.grid(row=0,column=3)
comp_lb.grid(row=0,column=1)

btn_rock=Button(window,width=10,height=5,text="Rock",
             font=("arial",20,"bold"),bg="white",fg="black",command=lambda:choice_update("Rock"))
btn_rock.grid(row=2,column=1)

btn_paper=Button(window,width=10,height=5,text="Paper",
             font=("arial",20,"bold"),bg="white",fg="black",command=lambda:choice_update("Paper"))
btn_paper.grid(row=2,column=2)

btn_scizzor=Button(window,width=10,height=5,text="Scizzor",
             font=("arial",20,"bold"),bg="white",fg="black",command=lambda:choice_update("Scizzor"))
btn_scizzor.grid(row=2,column=3)

rounds_played = 0
max_rounds = 10

def update_message(a):
    res['text'] = a

def comp_update():
    final=int(comp_scr['text'])
    final+=1
    comp_scr['text']=str(final)

def player_update():
    final=int(plyr_scr['text'])
    final+=1
    plyr_scr['text']=str(final)

def win_check(p,c):
    global rounds_played
    if rounds_played >= max_rounds:
        disable_buttons()
        update_message("Game over!")
        return

    rounds_played += 1
    if p == c:
        update_message("It's a tie")
    elif p == "Rock":
        if c == "Paper":
            update_message("You lose!")
            comp_update()
        else:
            update_message("You win!")
            player_update()
    elif p == "Paper":
        if c == "Scizzor":
            update_message("You lose!")
            comp_update()
        else:
            update_message("You win!")
            player_update()
    elif p == "Scizzor":
        if c == "Rock":
            update_message("You lose!")
            comp_update()
        else:
            update_message("You win!")
            player_update()  

to_sel=["Rock","Paper","Scizzor"]

def choice_update(a):
    ch_comp=to_sel[randint(0,2)]
    if ch_comp=="Rock":
        comp.configure(image=img_rock2)
    elif ch_comp == "Paper":
        comp.configure(image=img_paper2)
    else:
        comp.configure(image=img_scizzor2)    

    if a=="Rock":
        player.configure(image=img_rock1)
    elif a == "Paper":
        player.configure(image=img_paper1)
    else:
        player.configure(image=img_scizzor1) 

    win_check(a,ch_comp)

def reset_game():
    global rounds_played
    rounds_played = 0
    enable_buttons()
    update_message("")
    plyr_scr['text'] = '0'
    comp_scr['text'] = '0'

def disable_buttons():
    btn_rock['state'] = 'disabled'
    btn_paper['state'] = 'disabled'
    btn_scizzor['state'] = 'disabled'

def enable_buttons():
    btn_rock['state'] = 'normal'
    btn_paper['state'] = 'normal'
    btn_scizzor['state'] = 'normal'

res=Label(window,width=20,height=10,font=("arial",20,"bold"),bg="black",fg="white")
res.grid(row=3,column=2)

reset_btn = Button(window, text="Reset Game", font=("arial", 20, "bold"), bg="white", fg="black", command=reset_game)
reset_btn.grid(row=3, column=3)

window.mainloop()