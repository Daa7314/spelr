#Import dependencies
import pandas as pd
import numpy as np
import whisper
import pyttsx3
import pyaudio
import wave
import time
import streamlit as st

#Streamlit decorations
st.title('Spelling Help')
st.subheader('SPELR: Practices Your Spelling With You!')
st.write("SPELR helps students spell words!!")

st.write("Wait for spelr to tell you it is ready to listen to your spelling before starting!")
#Whisper model initialization
model = whisper.load_model("small")

#Audio recording and speaking settings
CHANNELS = 1
RATE = 44100
#RECORD_SECONDS = 20
FORMAT = pyaudio.paInt16
CHUNK =1024

#Mic and speaker initialization
p = pyaudio.PyAudio()

#Text to speech model initialization
engine = pyttsx3.init()
#Instructions
text = "BOX"
engine = pyttsx3.init()
engine.say("Spell")
engine.say(text)
engine.runAndWait()


# def word_prompt():
    
#     engine.say("Spell")
#     engine.say(text)
#     engine.runAndWait()
   
 
#     stream =p.open(format = FORMAT,
#                   channels = CHANNELS,
#                   rate= RATE,
#                   input = True,
#                   frames_per_buffer=CHUNK)


#     st.write("Start Spelling")

#     frames = []
#     seconds = time
#     for i in range(0, int(RATE/CHUNK * seconds)):
#         data = stream.read(CHUNK)
#         frames.append(data)


#     st.write("Stop Spelling")

#     stream.stop_stream()
#     stream.close()
#     p.terminate()


#     wf = wave.open("output.wav", 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
    
#      #Transcription
#     result = model.transcribe("output.wav", fp16=True)
#     answer = result["text"]

#     disallowed_characters = " ._!-"

#     for character in disallowed_characters:
#         answer = answer.replace(character, "")
#         answer = answer.lower()
        
#     #Validation of answers
#     st.write("Computer said: ", {answer})
#     st.write("You said: ", text)
#     if answer == text.lower():
#         st.write("Yeay!!!!!!, That's correct! You did It")
#     else:
#         st.write("Try again!!!!")



# ft = ["after", "boy"]



# N = len(ft)
# Sum = 0

# # This loop will run forever
# while True:
    
#     print(f"The {Sum} word is {ft[Sum]}")
#     #the time alloted to spell is a function of the length of the word plus 1 sec
#     time = len(ft[Sum]) + 1
#     text = ft[Sum]
#     word_prompt()
#     Sum += 1
#     #print(time)
#     # the below condition will tell
#     # the loop to stop
#     if N == Sum:
#         break
# # print()
# # print(f"All {N} items have been printed")
