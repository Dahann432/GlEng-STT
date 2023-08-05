from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment, silence
from pydub.silence import detect_silence, split_on_silence
import speech_recognition as sr
import os

def get_fileName():
    global fileName
    fileName = filedialog.askopenfilename(parent=file_window, defaultextension='.wav')
    file_window.quit()
    file_window.destroy()
    return fileName

# File Selection Winow
file_window = Tk()
file_window.geometry("300x50")
file_window.resizable(width=False, height=False)
file_window.title("Audio File")
Label(file_window, text="File").grid(row=0, pady=10)
Button(file_window, text="파일 선택", command=get_fileName).grid(row=0, column=1, padx=10, pady=10)

file_window.mainloop()

# Result Window
result_window = Tk()
result_window.title("Result")
result_window.resizable(True, True)

text = Text(result_window)
text.pack(text.pack(expand=True, fill=BOTH))

sound = AudioSegment.from_mp3(fileName)

# spliting audio files
audio_chunks = split_on_silence(sound, min_silence_len=2000, silence_thresh=-100 )

for i, chunk in enumerate(audio_chunks, start=1):
   section_count = i
   output_file = "section{0}.wav".format(i)
   print("Exporting file", output_file)
   chunk.export(output_file, format="wav")

for i in range(1, section_count + 1):
   section_file_name = "section{0}.wav".format(i)

   # Detecting Index of Silence
   section = AudioSegment.from_wav(section_file_name)
   silence = detect_silence(section, min_silence_len=100, silence_thresh=-16)

   silence = [stop for stop in silence]

   # Speech Recognition
   r = sr.Recognizer()
   section_file = sr.AudioFile(section_file_name)
   with section_file as source:
      audio = r.record(source)

   result = r.recognize_google(audio)

   text.insert("end", result + "\n\n")

result_window.mainloop()