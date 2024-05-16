import time

import speech_recognition
import os
import openai
import webbrowser
import datetime
import pytz
from googletrans import Translator
from speak import say
import weather
from key import apikey

empty_input_count = 0

chats = ""  # create a variable which stores each chat history for future

# chat() generate the ans of a query
def chat(query):
    global chats
    openai.api_key = apikey
    chats += f"\nSaif : {query}\nJarvis : "
    # this is the formate of conversation Saif ask Jarvis completes it by running function "chat(query)" which is written bottom
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                # role "user" indicating that the content of that message is provided by the user not a bot
                "content": chats
            }
        ],
        temperature=0.2,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response['choices'][0]['message']['content'])

    text = f"GPT response for prompt: {query}\n\n\n"  # this is the first line of a txt file stored in openai folder
    text += response['choices'][0]['message']['content']
    if not os.path.exists("openai"):
        os.mkdir("openai")
    # the following line generate the file name where the generated text will be saved in directory openai
    with open(f"openai/{query}.txt", "w") as f:
        f.write(text)

    say(response['choices'][0]['message']['content'])
    chats += f"{response['choices'][0]['message']['content']}\n"  # this added the chat to chats variable which is written above
    return response['choices'][0]['message']['content']

# Listen() takes input voice form from mic
def Listen():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        # r.pause_threshold = 0.8  # it determines how long the recognizer should wait for audio input to be considered complete
        audio = r.listen(source)
        # audio = r.listen(source, 0, 10)  # if we write this then the Listen function must wait 10sec for taking input
        try:  # now let's recognize the audio
            print("Recognizing...")
            query = r.recognize_google(audio, language="bn-BD")
            print(f"User Input Voice: {query}")
            return query

        except Exception as e:
            return "No Voice Command"  # when no input is given this message will be passed

# translateToEnglish() translate the bangla query to english
def translateToEnglish(text):
    try:
        line = str(text)
        translate = Translator()
        result = translate.translate(line)  # by default, it translates to English
        data = result.text
        # print(f"In English: {data}")  # print the english translation sentence
        return data
    except Exception as e:
        return "Translation Failed"

# micConnection() build a connection between the Listen() and translateToEnglish()
def micConnection():
    query = Listen()
    translatedQuery = translateToEnglish(query)
    return translatedQuery


if __name__ == '__main__':
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t   \033[1;1;34;40mJarvis AI by Saif\033[0m")
    say("... hello, i am jarvis, how may i assist you sir.")
    while True:
        # print the voice input in voice output form
        print("Listening...")
        query = micConnection()  # text is the user input command
        if query == "No Voice Command":
            empty_input_count += 1
            if empty_input_count >= 10:
                say("sir i think you have no questions, i am going to shut down myself.")
                break
            continue  # skip the "try" block and continue to the next iteration when no input voice command
        else:
            empty_input_count = 0  # Reset the count when there is valid input

        sites = [["youtube", "https://www.youtube.com"], ["torrent bd", "https://www.torrentbd.net"],
                 ["google", "https://www.google.com"], ["facebook", "https://www.facebook.com"]]  # sample website
        if any(f"jarvis open {site[0]}" in query.lower() for site in sites):
            for site in sites:
                if f"jarvis open {site[0]}" in query.lower():
                    say(f"opening {site[0]} confirmed...")
                    webbrowser.open(site[1])

        elif "jarvis play music".lower() in query.lower():
            musicPath = r"ENTER PATH"
            say("opening music sir...")
            os.startfile(musicPath)

        elif "play the movie".lower() in query.lower():
            moviePath = r"ENTER PATH"
            say("opening movie sir...")
            os.startfile(moviePath)

        elif "jarvis what is the time".lower() in query.lower():
            bangladesh_timezone = pytz.timezone('Asia/Dhaka')
            bd_time = datetime.datetime.now(bangladesh_timezone).strftime("%I:%M %p")
            say(f"sir, it's {bd_time}")

        elif "jarvis what is the weather condition in dhaka".lower() in query.lower():
            say(f"the weather in dhaka is, {weather.weather}, and the temperature is {weather.temp}degree celsius.")

        elif "thank you for your information".lower() in query.lower():
            say("your are welcome saif, is there anything else i can assist you")

        elif "jarvis open chrome".lower() in query.lower():
            appPath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            say("opening chrome confirmed...")
            os.startfile(appPath)

        elif "jarvis power off".lower() in query.lower():
            say("i am going to shut down myself sir...")
            exit()

        elif "search jarvis on youtube".lower() in query.lower():
            say("ok sir, i am opening the youtube")
            import ytsearch
            print("Listening...")
            searchContent = micConnection()
            ytsearch.search(searchContent)
            say("sir, youtube search has been completed, go and check out")

        elif "jarvis delete chat".lower() in query.lower():
            say("i have clear all the chat, sir.")
            chats = ""  # this will turn the chats into blank

        else:
            say("thank you for your concern sir.")
            print("Generating...")
            chat(query)
            print(chats)  # this will print the conversation

        # say(query)  # it repeats the query which is being tell by user
