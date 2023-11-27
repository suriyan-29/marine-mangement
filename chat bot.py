CREATE A VOICE CHATBOT

import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Error connecting to Google API: {0}".format(e))
        return ""

def speak(response_text):
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()

def chatbot():
    print("Voice Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = listen()

        if user_input == 'exit':
            print("Voice Chatbot: Goodbye!")
            speak("Goodbye!")
            break
        elif user_input:
            # Implement your chatbot logic based on user_input
            response_text = "You said: " + user_input
            print("Voice Chatbot:", response_text)
            speak(response_text)

if __name__ == "__main__":
    chatbot()

