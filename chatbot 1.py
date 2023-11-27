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

def marine_management_chatbot(user_input):
    # Implement marine management chatbot logic based on user_input
    if "fish species" in user_input:
        response_text = "I can provide information about different fish species in your marine environment."
    elif "fishing activity" in user_input:
        response_text = "I can help you with details about recent fishing activities and catches."
    elif "marine habitats" in user_input:
        response_text = "I can provide information about various marine habitats and their conservation status."
    else:
        response_text = "I'm sorry, I didn't understand your request. Please ask about fish species, fishing activities, or marine habitats."

    print("Marine Management Chatbot:", response_text)
    speak(response_text)

def chatbot():
    print("Marine Management Voice Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = listen()

        if user_input == 'exit':
            print("Marine Management Voice Chatbot: Goodbye!")
            speak("Goodbye!")
            break
        elif user_input:
            marine_management_chatbot(user_input)

if __name__ == "__main__":
    chatbot()
