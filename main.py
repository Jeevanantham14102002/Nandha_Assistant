import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webbrowser
import os
from tkinter import *
import welcome2
welcome2.s()
a=input("Enter your E-mail ID:" )
import smtplib
tx="www.google.com/maps/d/u/0/viewer?ll=11.285827595625872%2C77.62197704828743&z=19&mid=1A7JxqQG0Y8dd3lDwugSJ4RxHO5Q0ic8"
user_mail="arunachalamgurusamy2002@gmail.com"
user_pass="czyydiywbwrgxnjo"
con=smtplib.SMTP("smtp.gmail.com",587)
con.starttls()
con.login(user=user_mail,password=user_pass)
con.sendmail(from_addr=user_mail,to_addrs=a,msg=f"Click this link for map guidance {tx}")
con.close()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('rate',165)
engine.setProperty('voice', voices[1].id)



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 100
        audio = r.listen(source,None,6)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<15:
        speak("Good Afternoon!")  

    elif(hour>=15 and hour<19):
        speak("Good Evening!")
    else:
        speak("Good night")

    speak("Hello ,, Iam  Nandha  My  Assistant ,  How  may  I  help you")      
if __name__ == "__main__":
    wishMe()
    # Create an instance of the Chrome driver with the options
    driver = webdriver.Chrome()
    # Set the window size
    driver.set_window_size(800, 850)
    #set window position
    driver.set_window_position(750, 0)
    # Navigate to a website
    driver.get("https://www.google.com/maps/d/u/0/viewer?ll=11.285827595625872%2C77.62197704828743&z=19&mid=1A7JxqQG0Y8dd3lDwugSJ4RxHO5Q0ic8")
    while True:
        #query = takeCommand().lower()
        query = takeCommand().lower()
    
        if "way to block 3" in query:
            speak("from the entrance point a, go till you reach the point B, and proceed left, to reach the block 3 ")

        elif "way to block 1" in query:
            speak("from the entrance point A, proceed straight till you reach the point C, and at your right hand side, you will see the block 1")
            
        elif "way to admin block" in query:
            speak("from the  entrance point A, proceed till you reach the point D, now, proceed on the pathway on your right to reach the admin block")

        elif "way to block 2" in query:
            speak("from the entrance point A, proceed till you reach the point E, now, proceed on the pathway on your right to reach the block 2")

        elif  "way to central library" in query:
            speak("from the entrance point A, proceed till you reach the point G, then proceed on your left to reach the central library")

        elif "way to block 4" in query:
            speak("from the entrance point A,proceed till you reach the point G, now, proceed in the left path way to reach the block 4")

        elif "way to block 5" in  query:
            speak("from the entrance point A,proceed till you reach the point G, now, proceed in the left path way, and you will see the block 5 at your right")

        elif ("way to block 6") in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the straight until  you  see the block 6 at your right")
        elif "way to block pics" in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the straight until  you  see the block 6 at your right")
        elif query== "way to block":
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the straight until  you  see the block 6 at your right")

        elif "way to block 9" in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the road at your right until  you  see the block 9 at your left")
        

        elif "way to block 7" in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the road at your right until  you  see the junction of three roads, now proceed in the pathway at you left until you see the block 7 at your left")

        elif  "way to auditorium" in query:
            speak("from the entrance point A, proceed till you reach the point I, now at your left you will see the N E C auditorium")

        elif ("way to basketball court")in query:
           speak("from the entrance point A, proceed till you reach the point I, now proceed straight until you see the basket ball court at your right")

        elif ("way to volleyball court") in query:
           speak("from the entrance point A, proceed till you reach the point I, now proceed straight until you see the vollet ball court at your right")

        elif "way to hostel" in query:
            speak("from the entrance point A, now proceed till you reach the point J, where you will see the hostel")
        elif "way to bus stand" in query:
            speak("from the entrance point A, now proceed till you reach the point J, where you will see the n e c bus stand at your left")

        elif "where is block 3" in query:
            speak("from the entrance point a, go till you reach the point B, and proceed left, to reach the block 3 ")

        elif "where is block 1" in query:
            speak("from the entrance point A, proceed straight till you reach the point C, and at your right hand side, you will see the block 1")
            
        elif "where is admin block" in query:
            speak("from the  entrance point A, proceed till you reach the point D, now, proceed on the pathway on your right to reach the admin block")

        elif "where is block 2" in query:
            speak("from the entrance point A, proceed till you reach the point E, now, proceed on the pathway on your right to reach the block 2")

        elif "where is central library" in query:
            speak("from the entrance point A, proceed till you reach the point G, then proceed on your left to reach the central library")

        elif "where is block 4" in query:
            speak("from the entrance point A,proceed till you reach the point G, now, proceed in the left path way to reach the block 4")

        elif "where is block 5" in  query:
            speak("from the entrance point A,proceed till you reach the point G, now, proceed in the left path way, and you will see the block 5 at your right")

        elif "where is block 6" in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the straight until  you  see the block 6 at your right")
        elif "where is blocked pics" in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the straight until  you  see the block 6 at your right")
        elif(query=="where is block"):
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the straight until  you  see the block 6 at your right")
        
        elif "where is block pics" in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the straight until  you  see the block 6 at your right")

        elif "where is block 9" in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the road at your right until  you  see the block 9 at your left")

        elif "where is block 7"  in query:
            speak("from the entrance point A, proceed till you reach the point H, now proceed in the road at your right until  you  see the junction of three roads, now proceed in the pathway at you left until you see the block 7 at your left")

        elif "where is auditorium" in query:
            speak("from the entrance point A, proceed till you reach the point I, now at your left you will see the N E C auditorium")
        elif "where is the bus stand" in query:
            speak("From the entrance point A, go till you reach the point j, and at your left you will see the n e c bus stand")

        elif ("where is basketball court") in query:
           speak("from the entrance point A, proceed till you reach the point I, now proceed straight until you see the basket ball court at your right")
        elif ("where is basket ball court") in query:
           speak("from the entrance point A, proceed till you reach the point I, now proceed straight until you see the basket ball court at your right")

        elif "where is volley ball court" in query:
           speak("from the entrance point A, proceed till you reach the point I, now proceed straight until you see the volley ball court at your right")
        elif "where is volleyball court" in query:
           speak("from the entrance point A, proceed till you reach the point I, now proceed straight until you see the volley ball court at your right")

        elif "where is m b a laboratory" in query:
            speak("the MBA laboratory  present in the ground floor of block 5")
        elif "where is mba laboratory" in query:
            speak("the MBA laboratory  present in the ground floor of block 5")
        

        elif "where is civil cabd laboratory" in query:
            speak("the civil CABD laboratory  present in the ground floor of block 5")
        elif "where is civil ca bd laboratory" in query:
            speak("the civil CABD laboratory  present in the ground floor of block 5")
        elif "where is civil bd laboratory" in query:
            speak("the civil CABD laboratory  present in the ground floor of block 5")
        elif "where is civil ca bd laboratory" in query:
            speak("the civil CABD laboratory  present in the ground floor of block 5")

        elif "where is structural laboratory" in query:
            speak("the structural laboratory present in the ground floor of block 6")

        elif "where is strength of materials laboratory" in query:
            speak("the strength of materials laboratory  present in the ground floor of block 6")

        elif "where is concrete laboratory" in query:
            speak("the concrete laboratory  present in the ground floor of block 6")

        elif "where is surveying laboratory" in query:#at block 6
            speak("the surveying laboratory present in the ground floor of block 6")
        elif "where is serving laboratory" in query:#at block 6
            speak("the surveying laboratory present in the ground floor of block 6")

        elif "where is mechanical operational laboratory"in query:
            speak("the mechanical operational  laboratory present in the ground floor of block 9")
        elif "where is 1st drawing hall" in query:
            speak("The first drawing hall is present in the second floor of block 6")
        elif "where is first drawing hall" in query:
            speak("The first drawing hall is present in the second floor of block 6")
        elif "where is 2nd drawing hall" in query:
            speak("The second drawing hall is present in the third floor of block 6")
        elif "where is second drawing hall" in query:
            speak("The second drawing hall is present in the third floor of block 6")

        elif "where is fm laboratory" in query:
            speak("the FM laboratory present in the ground floor of block 9")

        elif "where is process dynamic control laboratory"in query:
            speak("the process dynamic control laboratory is present in the second floor of block 9")

        elif "where is heat transfer laboratory"in query:
            speak("the heat transfer laboratory  present in the second floor of block 9")

        elif "where is computer laboratory"in query:
            speak("the computer laboratory  present in the second floor and third floor of block 9")

        elif "where is mass transfer laboratory"in query:
            speak("the mass transfer laboratory present in the third floor of block 9")

        elif "where is soil mechanics laboratory"in query:
            speak("the soil mechanics laboratory present in the shed of block 9")

        elif "where is environmental laboratory"in query:
            speak("the environmental laboratory present in the shed of block 9")

        elif "where is chemical laboratory" in query:
            speak("the chemical laboratory  present in the shed of block 9")

        elif "where is surveying lab" in query:
            speak("the surveying laboratory present in the shed of block 9")
        elif "where is serving lab" in query:
            speak("the surveying laboratory present in the shed of block 9")

        elif "where is pg laboratory" in query:
            speak("the PG laboratory present in the block 9")
        elif "tg laboratory" in query:
            speak("the PG laboratory present in the block 9")
        elif "pg laboratory" in query:
            speak("the PG laboratory present in the block 9")

        elif "where is thermal and steam laboratory" in query:
            speak("the thermal and steam laboratory present in the shed near block 9")
        elif("where is thermal and team laboratory") in query:
            speak("the thermal and steam laboratory present in the shed near block 9")

        elif "where is engineering practices laboratory" in query:
            speak("the engineering practices laboratory present in the shed near block 9")
        elif "where is foundary smithy laboratory" in query:
            speak("the foundary  smithy laboratory present in the shed near block 9")
        elif "where is foundry laboratory" in query:
            speak("the foundary laboratory present in the shed near block 9")
        
        elif "where is mitti laboratory" in query:
            speak("the smithy laboratory present in the shed near block 9")
        elif "where is samiti laboratory" in query:
            speak("the smithy laboratory present in the shed near block 9")
        elif "where is niti laboratory" in query:
            speak("the smithy laboratory present in the shed near block 9")
        elif("where is foundries niti laboratory") in query:
            speak("the foundary  smithy laboratory present in the shed near block 9")
        elif "where is foundry samiti laboratory " in query:
            speak("the foundary  smithy laboratory present in the shed near block 9")
        elif "where is metrology laboratory" in query:
            speak("the metrology laboratory present in the shed near block 9")
        elif "where is manufacturing technology laboratory" in query:
            speak("the manufacturing technology laboratory present in the shed near block 9")
        elif "where is thermal laboratory" in query:
            speak("the thermal laboratory present in the shed near block 9")
        elif "where is lathe shop laboratory" in query:
            speak("the lathe shop laboratory present in the shed near block 9")
        elif("where is late shop laboratory" in query):
            speak("the lathe shop laboratory present in the shed near block 9")
        elif("where is bm laboratory") in query:
            speak("the bme laboratory  present in first floor of block 3")
        elif "where is fluid mechanics laboratory" in query:
            speak("the fluid mechanics and amchinery laboratory present in the block 9")
        elif "where is project laboratory" in query:
            speak("the project laboratory present in  second floor of  admin block")
        elif "project laboratory" in query:
            speak("the project laboratory present in  second floor of  admin block")
        elif "where is physics laboratory" in query:
            speak("the physics laboratory present in  second floor of  block 1")
        elif "where is chemistry laboratory" in query:
            speak("the chemistry laboratory present in  second floor of block 1")
        elif "where is digital laboratory" in query:
            speak("the digital laboratory present in second floor of block 2")
        elif "where is microprocessor laboratory" in query:
            speak("the microprocessor laboratory  present in second floor of block 2")
        elif "where is electronics system design laboratory" in query:
            speak("the electronics system design laboratory  present in third floor of block 2")
        elif("electronic system design laboratory") in query:
            speak("the electronics system design laboratory  present in third floor of block 2")
        elif("where is electronic system design laboratory") in query:
            speak("the electronics system design laboratory  present in third floor of block 2")
            
        elif "where is first pg lab" in query:#at block2
            speak("the pg laboratory  1 present in third floor of block 2")
        elif "first pg lab" in query:#at block2
            speak("the pg laboratory  1 present in third floor of block 2")
        elif "where is microwave and optical laboratory" in query:
            speak("the microwave and optical laboratory  present in third floor of block 2")
        elif "where is communication systems laboratory" in query:
            speak("the communication systems  laboratory  present in  third floor of  block 2")
        elif "where is fifth computing center" in query:
            speak("the fifth computing center is present in ground floor of block 3")
        elif "where is fifth computing centre" in query:
            speak("the fifth computing center is present in ground floor of block 3")
        elif "where is 5th computing centre" in query:
            speak("the fifth computing center is present in ground floor of block 3")
        elif("where is swift computing centre") in query:
            speak("the fifth computing center is present in ground floor of block 3")
        elif "where is placement auditorium" in query:
            speak ("the placement auditorium  present in ground floor of block 3")
        elif "when is tc to laboratory" in query:
            speak("the cc2 laboratory  present in ground floor of block 3")
        elif "where is Titu laboratory" in query:
            speak("the cc2 laboratory  present in ground floor of block 3")
        elif "tc2 laboratory" in query:
            speak("the cc2 laboratory  present in ground floor of block 3")
        elif "where is cc2 laboratory" in query:
            speak("the cc2 laboratory  present in ground floor of block 3")
        elif "where is operating systems laboratory" in query:
            speak("the cse cc or operating system laboratory  present in first floor of block 3")
        elif "where is operating system laboratory" in query:
            speak("the cse cc or operating system laboratory  present in first floor of block 3")
        elif "where is pg lab" in query:#at block 3
            speak("the pg lab is present in first floor of  block 3")
        elif "where is bme laboratory" in query:
            speak("the bme laboratory  present in first floor of block 3")
        elif "where is bm laboratory" in query:
            speak("the bme laboratory  present in first floor of block 3")
        elif "bm laboratory" in query:
            speak("the bme laboratory  present in first floor of block 3")
        elif "where is it laboratory" in query:
            speak("the IT laboratory  present in  second floor of  block 3")
        elif "it laboratory" in query:
            speak("the IT laboratory  present in  second floor of  block 3")
        elif "where is iit laboratory" in query:
            speak("the IT laboratory  present in  second floor of  block 3")
        elif "where is m c a laboratory" in query:
            speak("the mca laboratory  present in second floor of  block 3")
        elif "where is mca laboratory" in query:
            speak("the mca laboratory  present in second floor of  block 3")
        elif "where is mt a laboratory" in query:
            speak("the mca laboratory  present in second floor of  block 3")
        elif "where is m t a laboratory" in query:
            speak("the mca laboratory  present in second floor of  block 3")
        elif "where is technology theatre" in query:
            speak("technology theatre is at block 1")
        elif "technology theatre" in query:
            speak("technology theatre is at block 1")



        elif "tricky circuits" in query:
            speak("ECE department is conducting Tricky Circuits at Block 1")
        elif "tricky circuit" in query:
            speak("ECE department is conducting Tricky Circuits at Block 1")
        elif "baloon car " in query:
            speak("Mechanical department is conducting Baloon Car at Block 1 ")
        elif "diy water purifier and air conditionaer" in query:
            speak(" Both Civil and Chemical department is conducting diy water purifier and air conditionaer at Block 1")
        elif "incentive spirometer" in query:
            speak("B M E department is conducting Incentive Spirometer at Block 1")
        elif "simple drone" in query:
            speak("A I D S department is conducting Simple Drone at Block 1")
        elif "3 d show" in query:
            speak("3D Show is at Conference Hall in Block 1")
        elif "where is projects" in query:
            speak("All the unique projects are at C I P D in block 9")
        elif "unique project" in query:
            speak("All the unique projects are at C I P D in block 9")
        elif "unique projects" in query:
            speak("All the unique projects are at C I P D in block 9")

            
        elif("where is m p a laboratory") in query:
            speak("the mca laboratory  present in second floor of  block 3")
        elif "where is crop process laboratory" in query:
            speak("the crop process laboratory  present in ground floor of  block 4")
        elif "where is farm tractors laboratory" in query:
            speak("the farm tractors laboratory present in  ground floor of  block 4")
        elif "where is form tractors laboratory" in query:
            speak("the farm tractors laboratory present in  ground floor of  block 4")
        elif "farm tractors laboratory" in query:
            speak("the farm tractors laboratory present in  ground floor of  block 4")
        elif "where is unit operations laboratory" in query:
            speak("the unit operations laboratory  present in  ground floor of  block 4")
        elif "where is unit operation laboratory" in query:
            speak("the unit operations laboratory  present in  ground floor of  block 4")
        elif "unit operation laboratory" in query:
            speak("the unit operations laboratory  present in  ground floor of  block 4")
        elif "where is food process laboratory" in query:
            speak("the food process laboratory present in  ground floor of  block 4")
        elif "where is computer lab 1" in query:
            speak("the computer laboratory  1 is present in first floor of  block 4")
        elif "where is  project lab" in query:
            speak("the project laboratory  present in first floor of block 4")
        elif "project lab" in query:
            speak("the project laboratory  present in first floor of block 4")
        elif  "where is digital and analog integrated circuits laboratory" in query:
            speak("the digital and analog integrated circuits laboratory is present in the  fourth floor of  block 4")
        elif  "where is digital and analogue integrated circuits laboratory" in query:
            speak("the digital and analog integrated circuits laboratory is present in the  fourth floor of  block 4")
        elif "m and i laboratory" in query:
            speak("the m and i laboratory is present in  fourth floor of  block 4")
        
        elif "where is power electronics and microprocessor laboratory" in query:
            speak("the power electronics and micro processor laboratory  present in  fourth floor of  block 4")
        elif "schedule " in query:
            import officeadmin
            officeadmin.initi()
        elif "block 1" in query:
            speak("in block one , you can find ,ECE and BME departments")
        elif "who are you" in query:
            speak("i am nandha the assistant for this college and you")
        elif "block 3" in query:
            speak("in block three , you can find ,information technology,computer science engineering,and MCA depertments ")
        elif "block 2" in query:
            speak("in block 2 , you can find ,E C E department and c o e cell")
        elif "block 4" in query:
            speak("in block four , you can find , triple e, A I D S departments")
        elif "block 5" in query:
            speak("in block 5 , you can find , Civil , M B A , and  Agri departments")
        elif "block 6" in query:
            speak("in block 6 , you can find , First year M.E departments")
        elif "block 7" in query:
            speak("in block 7 , you can  find , MECHANICAL and M.E departments ")
        elif "block 9" in query:
            speak("in block 9 , you can find , chemical department")
        elif "where is library" in query:
            speak("from the entrance point A proceed till G turn left there you can find the library")
            
        elif "your website" in query:
            webbrowser.open("nandhaengg.org")
           
        elif "who are you" in query:
            speak("i am nandha the assistant for this college and you")

        elif "block 3" in query:
            speak("in block three information technology and computer science engineering depertments ")

        elif "admin block" in query:
            speak("You can find the office room, principal sir and Chairman sir room there,  You can also find the waiting hall near the AO sir's room")

        elif "where is the conference hall" in query:
            speak("The conference hall is located at the first floor of block1")
        elif "where is canteen" in query:
            speak("from the entrance, go straight till you reach the point f ,now proceed in the right side path, till you see the tech cafeteria, on your left")
        elif "where is the canteen" in query:
            speak("from the entrance, go straight till you reach the point f ,now proceed in the right side path, till you see the tech cafeteria, on your left")

        elif "breakfast" in query:
            file1= open("breakfast.txt",'r')
            s1=file1.read()
            file1.close()
            b1 = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\breakfast.txt"
            os.startfile(b1)
            speak(f"for breakfast you have {s1} in tech food court")
        elif "lunch" in query:
            file2= open("lunch.txt",'r')
            s2=file2.read()
            file2.close()
            b2 = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\lunch.txt"
            os.startfile(b2)
            speak(f"for lunch you have {s2} in tech food court")
        elif "snacks" in query:
            file3= open("snack.txt",'r')
            s3=file3.read()
            file3.close()
            b3 = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\snack.txt"
            os.startfile(b3)
            speak(f"you have {s3} for snacks in tech cafeteria")
        elif "bytes" in query:
            file3= open("snack.txt",'r')
            s3=file3.read()
            file3.close()
            b3 = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\snack.txt"
            os.startfile(b3)
            speak(f"you have {s3} for snacks in tech cafeteria")
        elif "bites" in query:
            file3= open("snack.txt",'r')
            s3=file3.read()
            file3.close()
            b3 = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\snack.txt"
            os.startfile(b3)
            speak(f"you have {s3} for snacks in tech cafeteria")
        elif "bike" in query:
            file3= open("snack.txt",'r')
            s3=file3.read()
            file3.close()
            b3 = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\snack.txt"
            os.startfile(b3)
            speak(f"you have {s3} for snacks in tech cafeteria")
        elif "bye" in query:
            file3= open("snack.txt",'r')
            s3=file3.read()
            file3.close()
            b3 = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\snack.txt"
            os.startfile(b3)
            speak(f"you have {s3} for snacks in tech cafeteria")

        elif "where is the placement auditorium" in query:
            speak("the placement auditorium is located at the ground floor of block 3")


        elif "today program" in query:
            speak("today  in our college project expo, is going on , the NAAC committee members are invigilating our projects ")    

        elif "open map" in query:
            webbrowser.open("https://www.google.com/maps/d/u/0/viewer?ll=11.285827595625872%2C77.62197704828743&z=19&mid=1A7JxqQG0Y8dd3lDwugSJ4RxHO5Q0ic8")
        elif "menu" in query:
            import menu
            menu.men.start()
        elif "events" in query:
            e1= "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\schedule.xlsx"
            os.startfile(e1)
        elif "even" in query:
            e1= "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\schedule.xlsx"
            os.startfile(e1)

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")


        elif "thank you" in query:
            speak("thanks, for ,using me ")
            break
        elif "where is hostel" in query:
            speak("from the entrance point A, now proceed till you reach the point J, where you will see the hostel")
        elif "schedule" in query:
            import officeadmin
            officeadmin.initi()

        elif "your website" in query:
            webbrowser.open("nandhaengg.org")
           
        elif "who are you" in query:
            speak("i am nandha the assistant for this college and you")
        elif "admin block" in query:
            speak("You can find the office room, principal sir and Chairman sir room there,  You can also find the waiting hall near the AO sir's room")

        elif "where is the conference hall" in query:
            speak("The conference hall is located at the first floor of block1")

        elif "where is the canteen" in query:
            speak("from the entrance, go straight till you reach the point f ,now proceed in the right side path, till you see the tech cafeteria, on your left")        

        elif "where is the placement auditorium" in query:
            speak("the placement auditorium is located at the ground floor of block 3")
        elif "open map" in query:
            
            webbrowser.open("https://www.google.com/maps/d/u/0/viewer?ll=11.285827595625872%2C77.62197704828743&z=19&mid=1A7JxqQG0Y8dd3lDwugSJ4RxHO5Q0ic8")
            
            
        elif "meenu" in query:
            import menu
            menu.men.start()
        elif "minu" in query:
            import menu
            menu.men.start()
        
        elif "event" in query:
            e1= "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Nandha my_assistant\\schedule.xlsx"
            os.startfile(e1)

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")
        elif "thank you" in query:
            speak("thanks, for ,using me ")
            break
        elif "None" in query:
            print("pardon please")
        else:
            speak("you have said a wrong comment , can you pardon please")
        
       
        
        
            
            

        


        #elif 'play music' in query:
            #music_dir = 'C:\music'
            #songs = os.listdir(music_dir)
            #print(songs)    
            #os.startfile(os.path.join(music_dir, songs[0]))

            

        '''elif 'email to arun' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                #to = "arungurusamy2002@gmail.com"    
                #sendEmail(to, content)
                #speak("Email has been sent!")
                conn=smtplib.SMTP("smtp.gmail.com",587)
                type(conn)
                conn.ehlo()
                conn.starttls()
                conn.login("jeevanantham.20it014@nandhaengg.org","necit12345")
                conn.sendmail("jeevanantham.20it014@nandhaengg.org","arunachallam.20it004@nandhaengg.org",content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend arun. I am not able to send this email")
        # if 1:
        

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia%")
            print(results)
            speak(results)
                    
        
            
            
            
        #elif 'brunch' or 'branch' in query:
            #ste1=lunch.start1()
            #st2+=ste1
        #elif 'mouthful'  in query:
            #ste2=start2()
            #st3+=snacks.ste2
'''
                  
        
            

        
       
