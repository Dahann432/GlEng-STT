import os
ffmpeg_path = "C:/ffmpeg/bin/ffmpeg.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(audio_file_path):
    audio = AudioSegment.from_wav(audio_file_path)
    audio.export("audio.wav", format="wav")  # 임시 오디오 파일로 저장

    r = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio_data = r.record(source)
    
    text = r.recognize_google(audio_data)
    
    return text

audio_file_path = "Reading-LC-1.wav"
audio_text = transcribe_audio(audio_file_path)
print(audio_text)

'''
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

def transcribe_audio(audio_file_path):

    r = sr.Recognizer()
    audioFile = sr.AudioFile(audio_file_path)
    with audioFile as source:
        audio = r.record(source, duration = 30)

    result = r.recognize_google(audio)

    return result

def split_sentences_text(text):
    # 문장 분리
    sentences = text.split(". ")

    return sentences

# 오디오 파일 경로
audio_file_path = "Reading-LC-1.wav"

# 오디오 텍스트 변환
audio_text = transcribe_audio(audio_file_path)

# silence 기반 문장 분리
audio = AudioSegment.from_wav(audio_file_path)

# silence 기준으로 오디오를 문장 단위로 분리
chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-30)

# 분리된 문장 출력
for i, chunk in enumerate(chunks):
    print(f"Sentence {i+1}:")
    print(chunk.text)
    print("---")
'''