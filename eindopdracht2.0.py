from tkinter import*
from tkinter import messagebox
import random

# titel
root=Tk()
root.title("Hangman Version 1.0.0")
root.geometry("600x500+120+100")

# info scherm
frame1=Frame(root,width=600,height=50,bd=2,relief="raise")
frame1.pack(side=TOP,fill=BOTH)
frame2=Frame(root,width=600,height=200,relief="raise")
frame2.pack(side=TOP,fill=BOTH)
frame3=LabelFrame(root,text='keys',width=600,height=250,bd=2,relief="raise")
frame3.pack(side=TOP,fill=BOTH)

lchild_frame2=Frame(frame2,width=300,height=200,relief='raise')
lchild_frame2.pack(side=LEFT)
rchild_frame2=LabelFrame(frame2,text='Hangman',width=300,height=200,bd=2,relief='raise')
rchild_frame2.pack(side=RIGHT)

l1child_frame2=LabelFrame(lchild_frame2,text='status',width=300,height=60,relief='raise')
l1child_frame2.pack(side=TOP)
l2child_frame2=LabelFrame(lchild_frame2,text='word',width=300,height=60,relief='raise')
l2child_frame2.pack(side=TOP)
l3child_frame2=LabelFrame(lchild_frame2,text='enter key',width=300,height=60,relief='raise')
l3child_frame2.pack(side=TOP)
def select(value):
    if value =='Space':
        entry.insert(END,'')
    else:
        entry.insert(END,value)

entry=Text(l3child_frame2,width=36,height=2)
entry.grid(row=1,columnspan=40)

# welke leters er kunnen worden gebruikt
buttons=[
'!','q','w','e','r','t','y','u','i','o','p',
'a','s','d','f','g','h','j','k','k',
'z','x','c','v','b','n','m'
]
varRow=2
varcolumn=0
for button in buttons:
    command=lambda  x=button: select(x)
    if button!='Space':
        Button(frame3,text=button,width=5,font=("arial",10,"bold"),bg='powder blue',command=command,padx=3,pady=3,bd=5).grid(row=varRow,column=varcolumn)
    if button=='Space':
        Button(frame3,text=button,command=command).grid(row=5,column=varcolumn)
    varcolumn+=1
    if varcolumn>11 and varRow==2:
        varcolumn=0
        varRow+=1
    if varcolumn>11 and varRow==3:
        varcolumn=0
        varRow+=1


# opnieuw spelen
def play_again():
    answer=messagebox.askyesno("play again","Do you want to play again")
    if answer=='True'or'true':
        play_game()
    else:
        pass

# het woord krijgen
def get_word():
    words=['dog','cat','monkey','tiger','snake','rabbit','elephant']
    return random.choice(words)

# het spel spelen
def play_game():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    word=get_word()
    latter_guessed=[]
    tries=10
    guessed=False
    l1=Label(l2child_frame2,text='The word contain '+str(len(word))+' latters')
    l1.grid(row=0,column=0)
    l2=Label(l2child_frame2,text='The Word '+str(len(word)*'*'))
    l2.grid(row=1,column=0)
    #hoevaak het mis mag gaan
    while guessed==False and tries>0:
        tries_left=Label(l1child_frame2,text='Tries left: '+str(tries))
        tries_left.grid(row=0,column=0)
        global entry
        guess=input("Enter a latter").lower()
        if len(guess)==1:
            if guess not in alphabet:
                el=Label(l2child_frame2,text='you have not entred a latter')
                el.grid(row=2,column=0,sticky=W)
            elif guess in latter_guessed:
                el=Label(l2child_frame2,text='you have all guesse a latter')
                el.grid(row=2,column=0,sticky=W)
            elif guess not in word:
                el=Label(l2child_frame2,text='sorry latter not part of word')
                el.grid(row=2,column=0,sticky=W) 
                latter_guessed.append(guess)   
                tries-=1
            elif guess in word:
                el=Label(l2child_frame2,text='Welldone latter exist in word')
                el.grid(row=2,column=0,sticky=W)
            else:
                el=Label(l2child_frame2,text='No idea why this message apped')
                el.grid(row=2,column=0,sticky=W)
        elif len(guess)==len(word):
            if guess==word:
                el=Label(l2child_frame2,text='Wel done you have gessed words')
                el.grid(row=2,column=0,sticky=W)
                guessed=True
            else:
                el=Label(l2child_frame2,text='Sorry,that was not in word oop')
                el.grid(row=2,column=0,sticky=W)
                tries-=1
        else:
            el=Label(l2child_frame2,text='The length of guessed word is diff')
            el.grid(row=2,column=0,sticky=W)
    status=''
    if guessed==False:
        for latter in word:
            if latter in latter_guessed:
                status+=latter
            else:
                status+='*'
        sl=Label(l1child_frame2,text=status)
        sl.grid(row=2,column=0)
    #of je hebt gewonnen of hebt verloren
    if status==word:
        el=Label(l2child_frame2,text='Well done you guessed the word')
        el.grid(row=2,column=0,sticky=W)
        guessed=True
    elif tries==0:
        el=Label(l2child_frame2,text='You run out of life :(')
        el.grid(row=2,column=0,sticky=W)


Button(frame1,text='play game',command=play_game).pack()


root.mainloop()
