import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for voice input from the user."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return None

def handle_command(command):
    """Handle the user's command."""
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {current_time}")
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        speak(f"Today's date is {current_date}")
    elif 'open' in command and 'browser' in command:
        speak("Opening the web browser.")
        webbrowser.open("https://www.google.com")
    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        exit(0)
    else:
        speak("Sorry, I can only tell you the time, date, or open the browser.")

def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = listen()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
