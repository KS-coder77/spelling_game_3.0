#!/usr/bin/env python
# coding: utf-8

# In[64]:


#spelling game 3.0 
#1. Import libraries 
#2. Create a class to generate the question
#3. Create a class to display the GUI and widgets 

#import libraries 
import os 
import time 
from gtts import gTTS
import playsound
import speech_recognition as sr
import random 
#import pyaudio
    
#class to generate the questions 
class Spelling_Question:
    
#initialize variables to generate question 
    def __init__(self):
        with open ("spelling.txt", "r") as f:
            self.data = f.read().split()   
        
        self.word = " "                                                                                                                                            
        self.question = " "
        self.num = int()
        self.filename = " "
        self.file = " "
        self.filename_with_ext = " "
      # print(self.data)   

#generate question
    def generate_question(self):
        #print(self.data)
        self.spelling_word = random.choice(self.data)
        self.question = "Please spell, " + self.spelling_word
        self.data.remove(self.spelling_word)
        print(self.question)          
        
#create audio
    def create_audio(self):
        #self.file = "Q_Output"
      #  self.ext = ".mp3"
       # self.num = 1
      #  self.filename = self.file + self.ext
        
       # if os.path.exists(self.file+self.ext):
       #     self.filename_with_ext = f"{self.file}{self.num}{self.ext}"
       #     self.num += 1 
        self.num = random.randint(1,100)  
        self.filename = "Q_Output"+str(self.num)+".mp3"                
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.language = "en"
        self.myText = self.question 
        self.output = gTTS(text = self.myText, lang = self.language, slow = False)
        self.output.save(self.filename) 
        self.sound = playsound.playsound(self.filename)
        #time.sleep(2)

        return self.sound

#repeat audio     
    def repeat_audio(self):
        self.sound = playsound.playsound(self.filename)
        print(self.filename)
        return self.sound 

#check answer 
    def solution(self):        
        return self.spelling_word
                      
spelling_game=Spelling_Question()
spelling_game.generate_question()
spelling_game.create_audio()


# In[65]:


spelling_game.repeat_audio()


# In[70]:


## class to create the gui !!!

#import libraries 
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import time

class GUI_Creator: 
    
    def __init__(self):
        
        # Create a GUI Window
        self.gui = Tk()
        
        # set the size of the GUI Window
        self.gui.geometry("800x450")

        # set the title of the Window
        self.gui.title("Let's practise our spelling!")
        
        self.title = Label(self.gui, text = "Welcome to the spelling game!", 
                      width = 50, bg="blue", fg="white", 
                      font=("ariel", 20, "bold"))
        #pos of title
        self.title.place(x=0, y=0) 
        
        #initialize variables 
        self.q_num = 0 
        self.score = 0 
        #self.turns = 0
        self.my_string_var = StringVar()
        self.finish_button_text = StringVar()
        self.inp = " "
        self.q = " "
        self.audio = " "
        self.a = " "  
        self.spelling_game = Spelling_Question()
             
        self.info = Label(self.gui, textvariable = self.my_string_var,
                        width = 60,
                        font=("ariel", 16, "bold"), anchor = "w")
        self.info.place(x=70, y=100)     
        
        self.user_entry_box = Entry(self.gui, width=15, 
                          font=("ariel", 16, "bold"))
        
        
        self.enter_button = Button(self.gui, text="Enter", command = self.check_answer,
                                  width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        
        self.start_button = Button(self.gui, text="Start", command = self.assign_question,
                                  width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        
        self.repeat_button = Button(self.gui, text="Repeat", command = self.spelling_game.repeat_audio,
                                  width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        
        self.msg = Label(self.gui, text = " ", width = 60, font=("ariel", 16, "bold"), anchor = "w")
        self.msg.place(x=60, y =260)
        
        #placing buttons on the screen
        self.start_button.place(x=310, y=210) 
             
        #bind the return key to the window
        self.gui.bind('<Return>', lambda event:self.check_answer())
              
    
        #start the GUI
        self.gui.mainloop()
        
    def welcome(self):
        self.my_string_var.set("Press Start to begin playing!")
        
        
    #method to assign question to my_string_var
    def assign_question(self):
        self.q_num += 1
        self.user_entry_box.place(x=70, y=150)
        self.enter_button.place(x=350, y=210) 
        self.repeat_button.place(x=480, y = 210)
        self.start_button.place_forget()
        self.info.place_forget() 
        self.q = self.spelling_game.generate_question()
        self.audio = self.spelling_game.create_audio()
        self.a = self.spelling_game.solution()
        #self.my_string_var.set(self.q)  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            
    #method to check the answer 
    def check_answer(self):             
        inp = str(self.user_entry_box.get())
        if inp.isalpha(): 

            if inp == self.a:
                self.score += 1
                self.msg.config(text = "Correct! Score: " + str(self.score) + " Q.number: " + str(self.q_num))
            else:
                self.msg.config(text = "Incorrect. The answer is " + str(self.a) + ".")
                
                
            if self.q_num <4: 
                self.assign_question()
            elif self.q_num == 4: 
                self.enter_button.place_forget()
                self.repeat_button.place_forget()
                self.user_entry_box.place_forget()
                self.my_string_var.set("Round completed!")
                self.finish_button = Button(self.gui, text="Finish", command = self.finish_game, 
                         width=8,bg="blue",fg="white",font=("ariel",12,"bold")) 
                self.finish_button.place(x=350,y=380)     

        else:     
            self.msg.config(text="Please enter a word.")
            
       
        self.user_entry_box.delete(0, END)  
    
    
    def finish_game(self):
        self.msg.config(text= "Well done! You have completed the game! You scored, "+ str(self.score) + " out of "+ str(self.q_num) + ".\n"
                       "Would you like to play again?")
        self.finish_button.place_forget()
        self.repeat_button.place_forget()
        self.info.place_forget()
        self.no_button = Button(self.gui, text="No", command = self.exit_game, 
                             width=8,bg="blue",fg="white",font=("ariel",12,"bold")) 
        self.yes_button = Button(self.gui, text="Yes", command = self.restart_game, 
                             width=8,bg="blue",fg="white",font=("ariel",12,"bold")) 
        self.yes_button.place(x=200,y=380)
        self.no_button.place(x=100,y=380)
        
    def restart_game(self):
        self.yes_button.place_forget()
        self.no_button.place_forget()
        self.score = 0 
        self.q_num = 0 
        self.assign_question()
        self.user_entry_box.place(x=70, y=150)
        self.enter_button.place(x=350, y=210)
        self.repeat_button.place(x=480, y = 210)
        self.msg.config(text = " ")
        
    def exit_game(self):
        self.gui.destroy()
        self.gui.quit()
        
window=GUI_Creator()
#spelling_game=Spelling_Question()


# In[ ]:





# In[ ]:




