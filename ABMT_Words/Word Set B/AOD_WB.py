from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from time import sleep
from time import time
from PIL import Image,ImageTk
from screeninfo import get_monitors
import os.path
import random
import readkeys


root = Tk()
root.title("AOD Words (Set B)")
root.iconbitmap("Pointers/psy.ico")
root.configure(bg="black")
root.resizable(False,False)

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

for m in get_monitors():
    mn=(str(m))

mn=mn.split()

wd=list()
ht=list()

for i in mn:
    if "width" in i:
        i=i.replace("="," ")
        i=i.replace(",","")
        i=i.split()
        wd.append([i[0],i[1]])
    else:
        continue

for i in mn:
    if "height" in i:
        i=i.replace("="," ")
        i=i.replace(",","")
        i=i.split()
        ht.append([i[0],i[1]])
    else:
        continue

mmh=float(ht[1][1])/float(ht[0][1])#each pixle=mm in width
mmw=float(wd[1][1])/float(wd[0][1])#each pixle=mm in height

imgwidth=(37.5/mmw)
imgheight=(50/mmh)
imgspace=(15/mmh)
imgwidth=int(imgwidth)
imgheight=int(imgheight)
imgspace=int(imgspace)


welcome_frame=LabelFrame(root,bd=10,padx=50,pady=10,relief=FLAT,bg="#CACAFF")
welcome_frame.grid(row=0,column=0,padx=30,pady=20,columnspan="2")

img=Image.open("Pointers/intro.PNG")
img_intro=img.resize((int(ws/2.5),int(hs/2.5)))
img_intro=ImageTk.PhotoImage(img_intro)

Label(welcome_frame,image=img_intro,borderwidth=0).pack()




img=Image.open("Pointers/Plus.PNG")
img_plus=img.resize((int(imgwidth/2),int(imgheight/2)))
img_plus=ImageTk.PhotoImage(img_plus)

img=Image.open("Pointers/Right.PNG")
img_right=img.resize((int(imgwidth/2),int(imgheight/2)))
img_right=ImageTk.PhotoImage(img_right)

img=Image.open("Pointers/Left.PNG")
img_left=img.resize((int(imgwidth/2),int(imgheight/2)))
img_left=ImageTk.PhotoImage(img_left)

img=Image.open("Pointers/Black.PNG")
img_black=img.resize((int(ws/2),int(hs/2.0)))
img_black=ImageTk.PhotoImage(img_black)

img=Image.open("Pointers/Num1.PNG")
img_num1=img.resize((int(ws/4),int(hs/2)))
img_num1=ImageTk.PhotoImage(img_num1)

img=Image.open("Pointers/Num2.PNG")
img_num2=img.resize((int(ws/4),int(hs/2)))
img_num2=ImageTk.PhotoImage(img_num2)

img=Image.open("Pointers/Num3.PNG")
img_num3=img.resize((int(ws/4),int(hs/2)))
img_num3=ImageTk.PhotoImage(img_num3)

img=Image.open("Pointers/Num4.PNG")
img_num4=img.resize((int(ws/4),int(hs/2)))
img_num4=ImageTk.PhotoImage(img_num4)

img=Image.open("Pointers/Num5.PNG")
img_num5=img.resize((int(ws/4),int(hs/2)))
img_num5=ImageTk.PhotoImage(img_num5)

img=Image.open("Training/1.PNG")
img_tr1=img.resize((int(3*imgwidth/2),imgheight))
img_tr1=ImageTk.PhotoImage(img_tr1)

img=Image.open("Training/2.PNG")
img_tr2=img.resize((int(3*imgwidth/2),imgheight))
img_tr2=ImageTk.PhotoImage(img_tr2)

img=Image.open("Training/3.PNG")
img_tr3=img.resize((int(3*imgwidth/2),imgheight))
img_tr3=ImageTk.PhotoImage(img_tr3)

img=Image.open("Training/4.PNG")
img_tr4=img.resize((int(3*imgwidth/2),imgheight))
img_tr4=ImageTk.PhotoImage(img_tr4)

img=Image.open("Training/5.PNG")
img_tr5=img.resize((int(3*imgwidth/2),imgheight))
img_tr5=ImageTk.PhotoImage(img_tr5)

img=Image.open("Training/6.PNG")
img_tr6=img.resize((int(3*imgwidth/2),imgheight))
img_tr6=ImageTk.PhotoImage(img_tr6)

img=Image.open("Training/7.PNG")
img_tr7=img.resize((int(3*imgwidth/2),imgheight))
img_tr7=ImageTk.PhotoImage(img_tr7)

img=Image.open("Training/8.PNG")
img_tr8=img.resize((int(3*imgwidth/2),imgheight))
img_tr8=ImageTk.PhotoImage(img_tr8)

img=Image.open("Training/9.PNG")
img_tr9=img.resize((int(3*imgwidth/2),imgheight))
img_tr9=ImageTk.PhotoImage(img_tr9)

img=Image.open("Training/10.PNG")
img_tr10=img.resize((int(3*imgwidth/2),imgheight))
img_tr10=ImageTk.PhotoImage(img_tr10)

img=Image.open("Training/11.PNG")
img_tr11=img.resize((int(3*imgwidth/2),imgheight))
img_tr11=ImageTk.PhotoImage(img_tr11)

img=Image.open("Training/12.PNG")
img_tr12=img.resize((int(3*imgwidth/2),imgheight))
img_tr12=ImageTk.PhotoImage(img_tr12)

img=Image.open("Training/13.PNG")
img_tr13=img.resize((int(3*imgwidth/2),imgheight))
img_tr13=ImageTk.PhotoImage(img_tr13)

img=Image.open("Training/14.PNG")
img_tr14=img.resize((int(3*imgwidth/2),imgheight))
img_tr14=ImageTk.PhotoImage(img_tr14)

img=Image.open("Training/15.PNG")
img_tr15=img.resize((int(3*imgwidth/2),imgheight))
img_tr15=ImageTk.PhotoImage(img_tr15)

img=Image.open("Training/16.PNG")
img_tr16=img.resize((int(3*imgwidth/2),imgheight))
img_tr16=ImageTk.PhotoImage(img_tr16)

img=Image.open("Words/1.PNG")
imgt1=img.resize((int(3*imgwidth/2),imgheight))
imgt1=ImageTk.PhotoImage(imgt1)

img=Image.open("Words/2.PNG")
imgt2=img.resize((int(3*imgwidth/2),imgheight))
imgt2=ImageTk.PhotoImage(imgt2)

img=Image.open("Words/3.PNG")
imgt3=img.resize((int(3*imgwidth/2),imgheight))
imgt3=ImageTk.PhotoImage(imgt3)

img=Image.open("Words/4.PNG")
imgt4=img.resize((int(3*imgwidth/2),imgheight))
imgt4=ImageTk.PhotoImage(imgt4)

img=Image.open("Words/5.PNG")
imgt5=img.resize((int(3*imgwidth/2),imgheight))
imgt5=ImageTk.PhotoImage(imgt5)

img=Image.open("Words/6.PNG")
imgt6=img.resize((int(3*imgwidth/2),imgheight))
imgt6=ImageTk.PhotoImage(imgt6)

img=Image.open("Words/7.PNG")
imgt7=img.resize((int(3*imgwidth/2),imgheight))
imgt7=ImageTk.PhotoImage(imgt7)

img=Image.open("Words/8.PNG")
imgt8=img.resize((int(3*imgwidth/2),imgheight))
imgt8=ImageTk.PhotoImage(imgt8)

img=Image.open("Words/9.PNG")
imgt9=img.resize((int(3*imgwidth/2),imgheight))
imgt9=ImageTk.PhotoImage(imgt9)

img=Image.open("Words/10.PNG")
imgt10=img.resize((int(3*imgwidth/2),imgheight))
imgt10=ImageTk.PhotoImage(imgt10)

img=Image.open("Words/11.PNG")
imgt11=img.resize((int(3*imgwidth/2),imgheight))
imgt11=ImageTk.PhotoImage(imgt11)

img=Image.open("Words/12.PNG")
imgt12=img.resize((int(3*imgwidth/2),imgheight))
imgt12=ImageTk.PhotoImage(imgt12)

img=Image.open("Words/13.PNG")
imgt13=img.resize((int(3*imgwidth/2),imgheight))
imgt13=ImageTk.PhotoImage(imgt13)

img=Image.open("Words/14.PNG")
imgt14=img.resize((int(3*imgwidth/2),imgheight))
imgt14=ImageTk.PhotoImage(imgt14)

img=Image.open("Words/15.PNG")
imgt15=img.resize((int(3*imgwidth/2),imgheight))
imgt15=ImageTk.PhotoImage(imgt15)

img=Image.open("Words/16.PNG")
imgt16=img.resize((int(3*imgwidth/2),imgheight))
imgt16=ImageTk.PhotoImage(imgt16)

img=Image.open("Words/17.PNG")
imgt17=img.resize((int(3*imgwidth/2),imgheight))
imgt17=ImageTk.PhotoImage(imgt17)

img=Image.open("Words/18.PNG")
imgt18=img.resize((int(3*imgwidth/2),imgheight))
imgt18=ImageTk.PhotoImage(imgt18)

img=Image.open("Words/19.PNG")
imgt19=img.resize((int(3*imgwidth/2),imgheight))
imgt19=ImageTk.PhotoImage(imgt19)

img=Image.open("Words/20.PNG")
imgt20=img.resize((int(3*imgwidth/2),imgheight))
imgt20=ImageTk.PhotoImage(imgt20)

img=Image.open("Words/21.PNG")
imgt21=img.resize((int(3*imgwidth/2),imgheight))
imgt21=ImageTk.PhotoImage(imgt21)

img=Image.open("Words/22.PNG")
imgt22=img.resize((int(3*imgwidth/2),imgheight))
imgt22=ImageTk.PhotoImage(imgt22)

img=Image.open("Words/23.PNG")
imgt23=img.resize((int(3*imgwidth/2),imgheight))
imgt23=ImageTk.PhotoImage(imgt23)

img=Image.open("Words/24.PNG")
imgt24=img.resize((int(3*imgwidth/2),imgheight))
imgt24=ImageTk.PhotoImage(imgt24)

img=Image.open("Words/25.PNG")
imgt25=img.resize((int(3*imgwidth/2),imgheight))
imgt25=ImageTk.PhotoImage(imgt25)

img=Image.open("Words/26.PNG")
imgt26=img.resize((int(3*imgwidth/2),imgheight))
imgt26=ImageTk.PhotoImage(imgt26)

img=Image.open("Words/27.PNG")
imgt27=img.resize((int(3*imgwidth/2),imgheight))
imgt27=ImageTk.PhotoImage(imgt27)

img=Image.open("Words/28.PNG")
imgt28=img.resize((int(3*imgwidth/2),imgheight))
imgt28=ImageTk.PhotoImage(imgt28)

img=Image.open("Words/29.PNG")
imgt29=img.resize((int(3*imgwidth/2),imgheight))
imgt29=ImageTk.PhotoImage(imgt29)

img=Image.open("Words/30.PNG")
imgt30=img.resize((int(3*imgwidth/2),imgheight))
imgt30=ImageTk.PhotoImage(imgt30)

img=Image.open("Words/31.PNG")
imgt31=img.resize((int(3*imgwidth/2),imgheight))
imgt31=ImageTk.PhotoImage(imgt31)

img=Image.open("Words/32.PNG")
imgt32=img.resize((int(3*imgwidth/2),imgheight))
imgt32=ImageTk.PhotoImage(imgt32)

img=Image.open("Words/33.PNG")
imgt33=img.resize((int(3*imgwidth/2),imgheight))
imgt33=ImageTk.PhotoImage(imgt33)

img=Image.open("Words/34.PNG")
imgt34=img.resize((int(3*imgwidth/2),imgheight))
imgt34=ImageTk.PhotoImage(imgt34)

img=Image.open("Words/35.PNG")
imgt35=img.resize((int(3*imgwidth/2),imgheight))
imgt35=ImageTk.PhotoImage(imgt35)

img=Image.open("Words/36.PNG")
imgt36=img.resize((int(3*imgwidth/2),imgheight))
imgt36=ImageTk.PhotoImage(imgt36)




#-----------------------------------------------------------------------------


#160 trial(128(neg-neut)/32(neut-neut))

tr1=[img_tr1,img_tr3,img_tr5,img_tr7,img_tr9,img_tr11,img_tr13,img_tr15]
tr2=[img_tr2,img_tr4,img_tr6,img_tr8,img_tr10,img_tr12,img_tr14,img_tr16]
neut=[imgt2,imgt4,imgt6,imgt8,imgt10,imgt12,imgt14,imgt16,imgt18,imgt20,imgt22,imgt24,imgt25,imgt27,imgt29,imgt31,imgt33,imgt35,imgt26,imgt28,imgt30,imgt32,imgt34,imgt36]#neutral - Incongruent
neg=[imgt1,imgt3,imgt5,imgt7,imgt9,imgt11,imgt13,imgt15,imgt17,imgt19,imgt21,imgt23]#negative - congruent
poi=["Top","Bot"]#pointer
poi_2=["->","<-"]#pointer direction

rand_lst1=list()
rand_lsttr=list()

for i in range(len(tr1)):
    rand_lsttr.append([tr1[i],tr2[i]])

for i in rand_lsttr:
    random.shuffle(i)

random.shuffle(rand_lsttr)

for i in range(len(neg)):
    for j in range(len(poi)):
        for k in range(len(poi_2)):
            rand_lst1.append([neut[i],neg[i],poi[j],poi_2[k]])
            rand_lst1.append([neg[i],neut[i],poi[j],poi_2[k]])

#rand_lst1=rand_lst1+rand_lst1

#neutral and negative list
#for i in range(len(rand_lst1)):
    #print(rand_lst1[i])
#print(len(rand_lst1))
#neutral and negative list end

rand_lst2=list()
for i in range(12,18):
    for j in range(len(poi)):
        for k in range(len(poi_2)):
            rand_lst2.append([neut[i],neut[i+6],poi[j],poi_2[k]])


#neutral and neutral list
#for i in range(len(rand_lst2)):
    #print(rand_lst2[i])

#print(len(rand_lst2))
#neutral and neutral list end

rand_lst=rand_lst1+rand_lst2
random.shuffle(rand_lst)

#random list for trial
#for i in range(len(rand_lst)):
    #print(rand_lst[i])

#print(len(rand_lst))
#random list for trial end
global tri0,tri,aod

tri0=dict()
tri=dict()

tri0["Frequency Of False Responses"]=0#3#ok
tri0["Percentage Of False Responses"]=0#15.0#ok
tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]=0#1#ok
tri0["Percentage Of Oultiers Responses (<0.15 or >1.5)"]=0#5#ok
tri0["Frequency of Very too Slow Or Rapid Responses (</2 or >*2)"]=0#1#ok
tri0["Percentage of Very too Slow Or Rapid Responses (</2 or >*2)"]=0#5#ok

tri["Frequency Of True Responses"]=0#15#ok
tri["Percentage Of True Responses"]=0#75#ok
tri["Total Mean True Reaction Time(Con,Incon,Nuet)"]=0#0.3842979499271938#ok


tri["Mean True Congruent Reaction Time"]=0#0.4640751566205706#ok
tri["Frequency Of True Congruent Responses"]=0#7#ok
tri["Percentage Of True Congruent Responses"]=0#87.5#ok

tri["Mean True Incongruent Reaction Time"]=0#0.4047678470611572#ok
tri["Frequency Of True Incongruent Responses"]=0#5#ok
tri["Percentage Of True Incongruent Responses"]=0#62.5#ok

tri["Mean True Neutral Reaction Time"]=0#0.43059396743774414#ok
tri["Frequency Of True Neutral Responses"]=0#3#ok
tri["Percentage Of True Neutral Responses"]=0#75.0#ok

aod=dict()
aod["Traditional Attention Bias"]=0#-0.05930730955941338
aod["Traditional Orientation"]=0#-0.03348118918282644
aod["Traditional Disengagement"]=0#-0.025826120376586936

global res_total_con,res_total_incon,res_total_nuet,tot_con,tot_incon,tot_nuet,res_true
res_total_con=0     #total response time Congruent
res_total_incon=0   #total response time Incongruent
res_total_nuet=0    #total response time neutral
tot_con=0
tot_incon=0
tot_nuet=0
res_true=list()      #total response time Frequency Of True Responses


 #-----------------------------------------------------------------------------


global count1_tr,count2_tr,count1,count2
count1_tr=0
count2_tr=0
count1=0
count2=0

img_lst=[img_num5,img_num4,img_num3,img_num2,img_num1]


def resize():
    w = root.winfo_reqwidth() # width for the Tk root
    h = root.winfo_reqheight() # height for the Tk root
    xw = (ws/2) - (w/2)
    yw = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, xw, yw))


def training():
    def fquit():
        global count1_tr
        global count2_tr
        count1_tr=0
        count2_tr=0
        top.destroy()
    top = Toplevel(bg="black")
    top.title("Training")
    top.iconbitmap("Pointers/psy.ico")
    top.focus_force()
    top.attributes("-fullscreen",True)

    img=Label(top,image=img_lst[0],borderwidth=0)
    img2=Label(top,image=None,borderwidth=0)
    exit_bot=Button(top,text="EXIT",width=10,height=2,command=fquit,borderwidth=5,bg="#CACAFF")
    exit_bot.place(x=ws-int(ws/18),y=hs-int(hs/16))
    def change():
        global count1_tr
        if count1_tr==5:
            count1_tr=0
            TrainingTrial()
        else:
            img.config(image=img_lst[count1_tr])
            img.place(x=int(ws*3/8),y=int(hs/4))
            count1_tr+=1
            top.after(1000,change)
    change()


    def TrainingTrial():

        def plusshow():
            trnum=Label(top,text=str(count2_tr+1)+" Of 8",bg="black",fg="white")
            trnum.place(x=ws-int(ws/25),y=int(hs/40))
            img.config(image=img_plus)
            img.place(x=(ws/2)-(imgwidth/4),y=(hs/2)-(imgheight/4))
            img2.config(image=None)
            img2.place(x=0,y=hs)
            top.after(500,imgshow)

        def imgshow():
            img.config(image=rand_lsttr[count2_tr][0])
            img.place(x=int((ws/2)-(int(3*imgwidth/2)/2)),y=int((hs/2)-imgheight-(imgspace/2)))
            img2.config(image=rand_lsttr[count2_tr][1])
            img2.place(x=int((ws/2)-(int(3*imgwidth/2)/2)),y=int((hs/2)+(imgspace/2)))
            top.after(500,prob)


        def prob():
            poi_pos=random.choice(poi)
            poi_dir=random.choice(poi_2)
            if poi_pos=="Top" and poi_dir=="<-":
                img.config(image=img_left)
                img2.config(image=img_black)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            elif poi_pos=="Top" and poi_dir=="->":
                img.config(image=img_right)
                img2.config(image=img_black)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            elif poi_pos=="Bot" and poi_dir=="<-":
                img.config(image=img_black)
                img2.config(image=img_left)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            elif poi_pos=="Bot" and poi_dir=="->":
                img.config(image=img_black)
                img2.config(image=img_right)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            ansget()

        def ansget():
            def press(event):
                ans = event.char
                ans=ans.lower()
                if ans!="m" and ans!="n" :
                    top.bind("<Key>",press)
                else:
                    blankshow()

            top.bind("<Key>",press)


        def blankshow():
            top.unbind("<Key>")
            global count2_tr
            count2_tr+=1

            if count2_tr!=8:
                img.config(image=img_black)
                img.place(x=int(ws/4),y=0)
                img2.config(image=img_black)
                img2.place(x=int(ws/4),y=int(hs/2))
                top.after(500,plusshow)

            else:
                img.config(image=img_black)
                img.place(x=int(ws/4),y=0)
                img2.config(image=img_black)
                img2.place(x=int(ws/4),y=int(hs/2))
                count2_tr=0
                top.after(500,top.destroy)

        plusshow()


def start():

    def fquit():
        global count1
        global count2
        count1=0
        count2=0

        tri0["Frequency Of False Responses"]=0#3#ok
        tri0["Percentage Of False Responses"]=0#15.0#ok
        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]=0#1#ok
        tri0["Percentage Of Oultiers Responses (<0.15 or >1.5)"]=0#5#ok
        tri0["Frequency of Very too Slow Or Rapid Responses (</2 or >*2)"]=0#1#ok
        tri0["Percentage of Very too Slow Or Rapid Responses (</2 or >*2)"]=0#5#ok

        tri["Frequency Of True Responses"]=0#15#ok
        tri["Percentage Of True Responses"]=0#75#ok
        tri["Total Mean True Reaction Time(Con,Incon,Nuet)"]=0#0.3842979499271938#ok


        tri["Mean True Congruent Reaction Time"]=0#0.4640751566205706#ok
        tri["Frequency Of True Congruent Responses"]=0#7#ok
        tri["Percentage Of True Congruent Responses"]=0#87.5#ok

        tri["Mean True Incongruent Reaction Time"]=0#0.4047678470611572#ok
        tri["Frequency Of True Incongruent Responses"]=0#5#ok
        tri["Percentage Of True Incongruent Responses"]=0#62.5#ok

        tri["Mean True Neutral Reaction Time"]=0#0.43059396743774414#ok
        tri["Frequency Of True Neutral Responses"]=0#3#ok
        tri["Percentage Of True Neutral Responses"]=0#75.0#ok
        aod["Traditional Attention Bias"]=0#-0.05930730955941338
        aod["Traditional Orientation"]=0#-0.03348118918282644
        aod["Traditional Disengagement"]=0#-0.025826120376586936

        top.destroy()

    top = Toplevel(bg="black")
    top.title("Trial")
    top.iconbitmap("Pointers/psy.ico")
    top.focus_force()
    top.attributes("-fullscreen",True)

    img=Label(top,image=img_lst[0],borderwidth=0)
    img2=Label(top,image=None,borderwidth=0)
    exit_bot=Button(top,text="EXIT",width=10,height=2,command=fquit,borderwidth=5,bg="#CACAFF")
    exit_bot.place(x=ws-int(ws/18),y=hs-int(hs/16))

    def change():
        global count1
        if count1==5:
            count1=0
            Trial()
        else:
            img.config(image=img_lst[count1])
            img.place(x=int(ws*3/8),y=int(hs/4))
            count1+=1
            top.after(1000,change)
    change()

    def Trial():
        def plusshow():
            trnum=Label(top,text=str(count2+1)+" Of " + str(len(rand_lst)),bg="black",fg="white")
            trnum.place(x=ws-int(ws/25),y=int(hs/40))
            img.config(image=img_plus)
            img.place(x=(ws/2)-(imgwidth/4),y=(hs/2)-(imgheight/4))
            img2.config(image=None)
            img2.place(x=0,y=hs)
            top.after(500,imgshow)

        def imgshow():
            global count2,object_1,object_2
            object_1=rand_lst[count2][0]
            object_2=rand_lst[count2][1]
            img.config(image=rand_lst[count2][0])
            img2.config(image=rand_lst[count2][1])
            img.place(x=int((ws/2)-(int(3*imgwidth/2)/2)),y=int((hs/2)-imgheight-(imgspace/2)))
            img2.place(x=int((ws/2)-(int(3*imgwidth/2)/2)),y=int((hs/2)+(imgspace/2)))
            top.after(500,prob)


        def prob():
            global poi_pos,poi_dir
            poi_pos=rand_lst[count2][2]
            poi_dir=rand_lst[count2][3]
            if poi_pos=="Top" and poi_dir=="<-":
                img.config(image=img_left)
                img2.config(image=img_black)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            elif poi_pos=="Top" and poi_dir=="->":
                img.config(image=img_right)
                img2.config(image=img_black)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            elif poi_pos=="Bot" and poi_dir=="<-":
                img.config(image=img_black)
                img2.config(image=img_left)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            elif poi_pos=="Bot" and poi_dir=="->":
                img.config(image=img_black)
                img2.config(image=img_right)
                img.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)-(3*imgheight/4)-(imgspace/2)))
                img2.place(x=int((ws/2)-(imgwidth/4)),y=int((hs/2)+imgspace/2)+(imgheight/4))

            ansget()

        def ansget():
            def press(event):
                global res_t,ans
                ans = event.char
                ans=ans.lower()
                if ans!="m" and ans!="n" :
                    top.bind("<Key>",press)
                else:
                    end=time()
                    res_t=end-start
                    blankshow()

            start=time()
            top.bind("<Key>",press)


        def blankshow():
            top.unbind("<Key>")
            global count2
            count2+=1
            def calc():
                global object_1,object_2,poi_dir,poi_pos,res_t,tot_con,tot_incon,tot_nuet,res_true

                if object_1 in neg and poi_pos=="Top" and poi_dir=="->":
                    tot_con+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                    else :
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                        elif ans=="m":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Congruent",res_t])

                elif object_1 in neg and poi_pos=="Top" and poi_dir=="<-":
                    tot_con+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="m":
                            tri0["Frequency Of False Responses"]+=1
                    else :
                        if ans=="n":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Congruent",res_t])
                        elif ans=="m":
                            tri0["Frequency Of False Responses"]+=1

                elif object_1 in neg and poi_pos=="Bot" and poi_dir=="->":
                    tot_incon+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                    else :
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                        elif ans=="m":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Incongruent",res_t])

                elif object_1 in neg and poi_pos=="Bot" and poi_dir=="<-":
                    tot_incon+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="m":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Incongruent",res_t])
                        elif ans=="m":
                            tri0["Frequency Of False Responses"]+=1

                elif object_1 in neut and object_2 in neut and poi_pos=="Top" and poi_dir=="->":
                    tot_nuet+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                        elif ans=="m":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Nuetral",res_t])

                elif object_1 in neut and object_2 in neut and poi_pos=="Top" and poi_dir=="<-":
                    tot_nuet+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="m":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Nuetral",res_t])
                        elif ans=="m":
                            tri0["Frequency Of False Responses"]+=1

                elif object_1 in neut and object_2 in neut and poi_pos=="Bot" and poi_dir=="->":
                    tot_nuet+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                        elif ans=="m":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Nuetral",res_t])

                elif object_1 in neut and object_2 in neut and poi_pos=="Bot" and poi_dir=="<-":
                    tot_nuet+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="m":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Nuetral",res_t])
                        elif ans=="m":
                            tri0["Frequency Of False Responses"]+=1

                elif object_1 in neut and poi_pos=="Top" and poi_dir=="->":
                    tot_incon+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                        elif ans=="m":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Incongruent",res_t])

                elif object_1 in neut and poi_pos=="Top" and poi_dir=="<-":
                    tot_incon+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="m":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Incongruent",res_t])
                        elif ans=="m":
                            tri0["Frequency Of False Responses"]+=1

                elif object_1 in neut and poi_pos=="Bot" and poi_dir=="->":
                    tot_con+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri0["Frequency Of False Responses"]+=1
                        elif ans=="m":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Congruent",res_t])

                elif object_1 in neut and poi_pos=="Bot" and poi_dir=="<-":
                    tot_con+=1

                    if res_t<0.15 or res_t>1.5:
                        tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]+=1
                        if ans=="m":
                            tri0["Frequency Of False Responses"]+=1
                    else:
                        if ans=="n":
                            tri["Frequency Of True Responses"]+=1
                            res_true.append(["Congruent",res_t])
                        elif ans=="m":
                            tri0["Frequency Of False Responses"]+=1

            if count2==len(rand_lst):
                img.config(image=img_black)
                img.place(x=int(ws/4),y=0)
                img2.config(image=img_black)
                img2.place(x=int(ws/4),y=int(hs/2))
                count2_tr=0
                top.after(500,calc2)

            else:
                img.config(image=img_black)
                img.place(x=int(ws/4),y=0)
                img2.config(image=img_black)
                img2.place(x=int(ws/4),y=int(hs/2))
                top.after(500,plusshow)

            calc()

        def calc2():
            global res_true,tri,tri0,aod,res_total_con,res_total_incon,res_total_nuet

            res_total_true=0
            avg_total_true=0
            for i in range(len(res_true)):
                res_total_true=res_total_true+res_true[i][1]

            if len(res_true)==0:
                avg_total_true=0
            else:
                avg_total_true=res_total_true/len(res_true)

            pure_true=list()
            #check for x/2 or 2x timing
            for i in range(len(res_true)):
                if res_true[i][1]<(avg_total_true/2) or res_true[i][1]>(avg_total_true*2):
                    tri0["Frequency of Very too Slow Or Rapid Responses (</2 or >*2)"]+=1
                    tri["Frequency Of True Responses"]-=1
                else:
                    pure_true.append([res_true[i][0],res_true[i][1]])
                    if res_true[i][0]=="Congruent":
                        tri["Frequency Of True Congruent Responses"]+=1
                        res_total_con+=res_true[i][1]
                    elif res_true[i][0]=="Incongruent":
                        tri["Frequency Of True Incongruent Responses"]+=1
                        res_total_incon+=res_true[i][1]
                    elif res_true[i][0]=="Nuetral":
                        tri["Frequency Of True Neutral Responses"]+=1
                        res_total_nuet+=res_true[i][1]

            #check for x/2 or 2x timing end

            res_pure=0

            for i in range(len(pure_true)):
                res_pure+=pure_true[i][1]


            tri0["Percentage Of False Responses"]=((tri0["Frequency Of False Responses"]/len(rand_lst))*100)
            tri0["Percentage Of Oultiers Responses (<0.15 or >1.5)"]=((tri0["Frequency Of Oultiers Responses (<0.15 or >1.5)"]/len(rand_lst))*100)
            tri0["Percentage of Very too Slow Or Rapid Responses (</2 or >*2)"]=((tri0["Frequency of Very too Slow Or Rapid Responses (</2 or >*2)"]/len(rand_lst))*100)
            tri["Percentage Of True Responses"]=((tri["Frequency Of True Responses"]/len(rand_lst))*100)
            if len(pure_true)==0:
                tri["Total Mean True Reaction Time(Con,Incon,Nuet)"]=0
            else:
                tri["Total Mean True Reaction Time(Con,Incon,Nuet)"]=(res_pure/len(pure_true))

            if tri["Frequency Of True Congruent Responses"]==0:
                tri["Mean True Congruent Reaction Time"]=0
            else:
                tri["Mean True Congruent Reaction Time"]=(res_total_con/tri["Frequency Of True Congruent Responses"])

            if tri["Frequency Of True Incongruent Responses"]==0:
                tri["Mean True Incongruent Reaction Time"]=0
            else:
                tri["Mean True Incongruent Reaction Time"]=(res_total_incon/tri["Frequency Of True Incongruent Responses"])

            if tri["Frequency Of True Neutral Responses"]==0:
                tri["Mean True Neutral Reaction Time"]=0
            else:
                tri["Mean True Neutral Reaction Time"]=(res_total_nuet/tri["Frequency Of True Neutral Responses"])

            tri["Percentage Of True Congruent Responses"]=((tri["Frequency Of True Congruent Responses"]/tot_con)*100)
            tri["Percentage Of True Incongruent Responses"]=((tri["Frequency Of True Incongruent Responses"]/tot_incon)*100)
            tri["Percentage Of True Neutral Responses"]=((tri["Frequency Of True Neutral Responses"]/tot_nuet)*100)

            aod=dict()
            aod["Traditional Attention Bias"]=tri["Mean True Incongruent Reaction Time"]-tri["Mean True Congruent Reaction Time"]
            aod["Traditional Orientation"]=tri["Mean True Neutral Reaction Time"]-tri["Mean True Congruent Reaction Time"]
            aod["Traditional Disengagement"]=tri["Mean True Incongruent Reaction Time"]-tri["Mean True Neutral Reaction Time"]

            top.after(500,top.destroy)




        plusshow()


def scores():
    global tri,tri0,aod
    top = Toplevel(bg="black")
    top.title("Scores")
    top.iconbitmap("Pointers/psy.ico")
    top.focus_force()
    top.resizable(False,False)
    def resize():
        wt = top.winfo_reqwidth() # width for the Tk root
        ht = top.winfo_reqheight() # height for the Tk root
        ws = top.winfo_screenwidth() # width of the screen
        hs = top.winfo_screenheight() # height of the screen
        xt = (ws/2) - (wt/2)
        yt = (hs/2) - (ht/2)
        top.geometry('%dx%d+%d+%d' % (wt, ht, xt, yt))

    def save():
        def resize2():
            wt2 = top2.winfo_reqwidth() # width for the Tk root
            ht2 = top2.winfo_reqheight() # height for the Tk root
            ws2 = top2.winfo_screenwidth() # width of the screen
            hs2 = top2.winfo_screenheight() # height of the screen
            xt2 = (ws2/2) - (wt2/2)
            yt2 = (hs2/2) - (ht2/2)
            top2.geometry('%dx%d+%d+%d' % (wt2, ht2, xt2, yt2))

        top2=Toplevel(bg="black")
        top2.title("Save")
        top2.iconbitmap("Pointers/psy.ico")
        top2.focus_force()
        Label(top2,text="File Title",bg="black",fg="white").pack(pady=10)
        e=Entry(top2,width=30)
        e.pack(padx=30,pady=5)

        def save2():
            filename=e.get()
            filenametxt=str(filename)+".txt"
            if os.path.exists("Results/"+filenametxt):
                messagebox.showerror("Error", "File name <" + filename + "> exists.",parent=top2)
            else:
                a1=messagebox.askokcancel("Saving","Saving file as "+filename,parent=top2)

                if a1:
                    f = open("Results/"+filenametxt,"w")
                    for k,v in tri0.items():
                        if "Percentage" in k :
                            f.write(str(k) + " : " + str(v) + "%" + "\n")
                        else :
                            f.write(str(k) + " : " + str(v) + "\n")

                    for k,v in tri.items():
                        if "Percentage" in k:
                            f.write(str(k) + " : " + str(v) + "%" + "\n")
                        else :
                            f.write(str(k) + " : " + str(v) + "\n")

                    for k,v in aod.items():
                        f.write(str(k) + " : " + str(v) + "\n")

                    f.close()
                    top2.destroy()
                    top.destroy()

                else:
                    return

        save_but2=Button(top2,text="Save",command=save2,bg="#CACAFF").pack(pady=10)
        top2.after(1,resize2)



    f1=LabelFrame(top,bg="black",fg="white")#,padx=10,pady=10)
    f2=LabelFrame(top,bg="black",fg="white")#,padx=10,pady=10)
    f3=LabelFrame(top,bg="black",fg="white")#,padx=10,pady=10)
    f1.grid(row=0,column=0,columnspan=2,padx=15,pady=15,sticky=NW)
    f2.grid(row=0,column=3,rowspan=4,padx=15,pady=15,sticky=N)
    f3.grid(row=1,column=0,columnspan=2,padx=15,pady=15)

    for k,v in tri0.items():
        if "Percentage" in k :
            Label(f1,text=str(k) + " : " + str(v) + "%",bg="black",fg="white",pady=10,padx=10).pack()
            result1=str(k) + " : " + str(v)

        else :
            Label(f1,text=str(k) + " : " + str(v),bg="black",fg="white",pady=10,padx=10).pack()
            result1=str(k) + " : " + str(v)

    for k,v in tri.items():
        if "Percentage" in k:
            Label(f2,text=str(k) + " : " + str(v) + "%",bg="black",fg="white",pady=10,padx=10).pack()
            result2=str(k) + " : " + str(v)

        else :
            Label(f2,text=str(k) + " : " + str(v),bg="black",fg="white",pady=10,padx=10).pack()
            result2=str(k) + " : " + str(v)


    for k,v in aod.items():
        Label(f3,text=str(k) + " : " + str(v),bg="black",fg="white",pady=10,padx=10).pack()
        result3=str(k) + " : " + str(v)





    exit_but=Button(top,text="Return",width=15,height=2,command=top.destroy,borderwidth=5,bg="#CACAFF")
    save_but=Button(top,text="Save",width=15,height=2,command=save,borderwidth=5,bg="#CACAFF")
    exit_but.grid(row=2,column=0,padx=15,pady=15)
    save_but.grid(row=2,column=1,padx=15,pady=15)



    top.after(1,resize)


def close():
    response = messagebox.askyesno("EXIT","Are you sure that you want to exit the program ?")
    if response==True:
        root.quit()
    else:
        return


Training_bot=Button(root,text="Training",width=25,height=3,command=training, bg="#CACAFF", relief=RIDGE, font=("Arial",15,"bold"))
start_bot=Button(root,text="Start Trial",width=25,height=3,command=start, bg="#CACAFF",relief=RIDGE, font=("Arial",15,"bold"))
score_bot=Button(root,text="Show The Scores",width=25,height=3,command=scores, bg="#CACAFF",relief=RIDGE, font=("Arial",15,"bold"))
exit_bot=Button(root,text="EXIT Program",height=2,command=close, bg="#CACAFF",relief=RIDGE, font=("Arial",15,"bold"))



Training_bot.grid(row=1,column=1,padx=20,pady=10)
start_bot.grid(row=1,column=0,padx=20,pady=10)
score_bot.grid(row=3,column=0,padx=20,pady=10)
exit_bot.grid(row=3,column=1,padx=20,pady=10)


root.after(1,resize)
root.mainloop()
