from pydub import AudioSegment, silence
from pydub.silence import detect_silence, split_on_silence
from pydub.playback import play
import speech_recognition as sr

def play_audio_segment(audio_file, start_time):
    # 오디오 파일 로드
    audio = AudioSegment.from_file(audio_file)

    # 시작 지점 지정
    start_ms = start_time * 1000

    # 시작 구간 추출
    segment = audio[start_ms:]

    # 구간 재생
    play(segment)

#reading from audio mp3 file
sound = AudioSegment.from_mp3("Reading LC 1.mp3")

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

   print(i, result)
