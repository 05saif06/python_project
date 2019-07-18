import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goog morning!")
    elif hour>=12 and hour<16: 
        speak("goog afternoon!")
    else:
        speak("goog evening!") 

    speak("i am HULK what i can do for u sir")   
def takeCommand():
    #it takes microphone input from the user and return string ouput

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_ratio = 1.5
        r.pause_threshold = 0.5
 
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")    
    except Exception as e:
        #print(e)

        print("say that again please....") 
        return "None"  
    return query     

if __name__ == "__main__":
    wishMe() 
    #while True:   
    if 1:
     query=takeCommand().lower()


     if 'wikipedia' in query:
        speak("searching wikipedia....")
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query,sentences=2)
        speak("wikipedia")
        print(results)
        speak(results)
     elif 'open whatsapp' in query:
        webbrowser.open("whatsapp.com")   
     elif 'open google' in query:
        webbrowser.open("google.com")  
     elif 'dilsefoodi' in query:
        webbrowser.open("https://www.youtube.com/watch?v=11dA1p4Pj4s")     
     elif 'open facebook' in query:
        webbrowser.open("facebook.com")
     elif 'open instagram' in query:
        webbrowser.open("instagram.com") 
     elif 'open cricbuzz' in query:
        webbrowser.open("https://www.bing.com/cricketdetails?q=Australia%20vs%20England%20cricket&IsCricketV3=1&QueryTimeZoneId=India%20Standard%20Time&ResponseType=Commentary&Intent=Scores&Provider=SI&ScenarioName=SingleGame&CricketTournamentId=2995&GameId=186723&")
     elif 'open mail' in query:
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox")      

     elif 'play music' in query:
         music_dir='C:\\Users\\SAIF KHAN\\Music\\Playlists\\songs' 
         songs = os.listdir(music_dir) 
         print(songs)
         os.startfile(os.path.join(music_dir,songs[1]))

     elif 'play video' in query:
         video_dir='S:\\videofiles' 
         videofiles = os.listdir(video_dir) 
         print(videofiles)
         os.startfile(os.path.join(video_dir,videofiles[0])) 
     elif 'what is the time' in query:
         strTime=datetime.datetime.now().strftime("%H:%M")
         print(strTime)
         speak(f"sir the time is:{strTime}")
        
     elif ' open camera' in query:
         Camera="C:\\Users\\SAIF KHAN\\Desktop\\Camera"  
         os.startfile(Camera)  
     elif 'open youtube' in query:
         youtube="C:\\Users\\SAIF KHAN\\Desktop\\YouTube"  
         os.startfile(youtube)  
     elif 'gate lecture' in query:
         gate="S:\\gate_2021"  
         os.startfile(gate)    
     elif 'open video file' in query:
         v="S:\\videofiles"  
         os.startfile(v)    
     elif 'open photo' in query:
         p_dir='E:\\image' 
         p = os.listdir(p_dir) 
         print(p)
         os.startfile(os.path.join(p_dir,p[0]))        
             


                     


