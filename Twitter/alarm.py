#Alarm clock using Python Tkinter module by Rajkumar Selvaraj
from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox
import tweepy
import PIL
import tkinter as tk
from PIL import Image, ImageTk

# Authenticate to Twitter
auth = tweepy.OAuthHandler("MnVuMdiYoFDE1Si1MnsHSTPk9", "TZzhCYnzKXDJMxdvCWlgnciF066L7wn6Yo0dfS5Dqn4VhUBrZ8")
auth.set_access_token("1218637142168965120-StrPRBbGLD1pvaL031MBGMm6BK5n9x", "gIX62oJIW5Gt6MC1FeB1dT1XFp1pZgryDAu7JywzyvGbP")

api = tweepy.API(auth)

tweets = ["@snapback_andraka hit the snooze button like a lazy bum","Oh look at that, she did it again@snapback_andraka","Stop hitting the snooze button @snapback_andraka!","@snapback_andraka hit the snooze button for the 4th time","Help me publicly shame @snapback_andraka for refusing to get out of bed","@snapback_andraka what a lazy bum","@snapback_andraka This is jsut getting embarassing","@snapback_andraka I am embarrassed for you","@snapback_andraka for shame. How many times can you hit snooze before you just turn your alarm off?","This gal needs to get up @snapback_andraka", "Why ain't she getting up @Snapback_Andraka", "Girl, Don't you hit snooze again @Snapback_Andraka", "Girl, @snapback_andraka"]

#def main():
root = Tk()
root.title("The OG Snooze Shamer")
def snoozebutton(AlarmTime):
  print("Sleep")
  time.sleep(10)
  print("Snoozing.... \n ZzzzZzzzZ")
  #snooze = AlarmTime + time.strftime()
  CurrentTime = time.strftime("%H:%M")
  print("the alarm time is: {}".format(AlarmTime))
  #label2.config(text="")
  while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    CurrentTime = time.strftime("%H:%M")
    
  if AlarmTime == CurrentTime:
      #current = current +1
      #tweets.pop(1)
      current = 0
      api.update_status(tweets[current])
      tweets.pop(0)
      print("now Alarm Musing Playing")
      os.system("start alarmsound.wav")
      label2.config(text = "Alarm music playing.....")
      MsgBox = tk.messagebox.askquestion ('Exit Application','Do you want to Snooze?',icon = 'warning')
      if MsgBox == 'yes':
        snoozebutton(AlarmTime)
      else:
        print("Exiting alarm")
        
  #AlarmTime = AlarmTime +5

def SubmitButton():
  current = 0
  AlarmTime= entry1.get()
  Message1()
  #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
  CurrentTime = time.strftime("%H:%M")
  print("the alarm time is: {}".format(AlarmTime))
  #label2.config(text="")
  while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    CurrentTime = time.strftime("%H:%M")
    time.sleep(1)
  if AlarmTime == CurrentTime:
      #current = current +1
      #tweets.pop(1)
      api.update_status(tweets[current])
      tweets.pop(0)
      print("now Alarm Musing Playing")
      os.system("start alarmsound.wav")
      label2.config(text = "Alarm music playing.....")
      MsgBox = tk.messagebox.askquestion ('Exit Application','Do you want to Snooze?',icon = 'warning')
      if MsgBox == 'yes':
        #return(AlarmTime)
        snoozebutton(AlarmTime)
      else:
        tk.messagebox.showinfo('Return', 'Returning')
      
     
def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="the Alarm time is Counting...")
    #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))     
frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height = 100, width = 100)
frame2 = ttk.Frame(root)
frame2.pack()
frame2.config(height = 150, width = 150)

label1= ttk.Label(frame1,text = "Enter the Alarm time :")
label1.pack()


entry1 = ttk.Entry(frame1, width = 30)
entry1.pack()
entry1.insert(3,"example - 13:15")

labelAlarmMessage= ttk.Label(frame1, text="Alarm Message:")
labelAlarmMessage.pack()

entry2= ttk.Entry(frame1, width=30)
entry2.pack()

button1= ttk.Button(frame1, text= "submit", command=SubmitButton)
button1.pack()

#this Label2 will show the Last Alarm Time
label2= ttk.Label(frame1)
label2.pack()
load = Image.open("twittericon.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x=850, y=700)

load2 = Image.open("snoozer.png")
render2 = ImageTk.PhotoImage(load2)
img2 = Label(image=render2)
img2.image = render
img2.place(x=650, y=300)
    
#label2.config(text="hello")

root.mainloop()