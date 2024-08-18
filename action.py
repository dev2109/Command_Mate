import webbrowser
import text_to_speech
import speech_to_text
import datetime
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual Assistant") 
        return "My name is virtual Assistant"
    elif "hello" in user_data or "hii" in user_data:
        text_to_speech.text_to_speech("Hey, sir how can i help you ")
        return "Hey, sir how can i help you"
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + " Hour :", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you")
        return "gaana.com is now ready for you"
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"
    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
    else:
        text_to_speech.text_to_speech("I am not able to run this ! sorry")
        return "I am not able to run this ! sorry"