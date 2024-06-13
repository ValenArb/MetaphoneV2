import pyaudio
import wave
import subprocess
import os
from libs.sub_libs.ignore import noalsaerr
import shutil
import threading

class Recorder():
    #Defines sound properties like frequency and channels
    def __init__(self, chunk=512, channels=1, rate=44100):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []

    #Start recording sound
    def start(self):
        threading._start_new_thread(self.__recording, ())

    def __recording(self):
        #Set running to True and reset previously recorded frames
        self._running = True
        self._frames = []
        #Create pyaudio instance
        try:
            with noalsaerr():
                p = pyaudio.PyAudio()
        except:
            p= pyaudio.PyAudio()
        #Open stream
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        # To stop the streaming, new thread has to set self._running to false
        # append frames array while recording
        while(self._running):
            data = stream.read(self.CHUNK, exception_on_overflow = False)
            self._frames.append(data)

        # Interrupted, stop stream and close it. Terinate pyaudio process.
        stream.stop_stream()
        stream.close()
        p.terminate()

    # Sets boolean to false. New thread needed.
    def stop(self):
        self._running = False

    #Save file to filename location as a wavefront file.
    def save(self, filename):
        with noalsaerr():
            p = pyaudio.PyAudio()
        if not filename.endswith(".wav"):
            filename = filename + ".wav"
        recordings_dir = "/home/FuegoAustral/Metaphone/recordings"
        src_file = os.path.join(recordings_dir, filename)
        if os.path.exists(src_file):
            records_dir = os.path.join(recordings_dir,"records")
            os.makedirs(records_dir, exist_ok=True)
            shutil.move(src_file,os.path.join(records_dir, filename))
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()
        src_dir = "/home/FuegoAustral/Metaphone"
        src_file= os.path.join(src_dir, filename)
        dst_file= os.path.join(recordings_dir, filename)
        shutil.move(src_file,dst_file)

    # Delete a file
    @staticmethod
    def delete(filename):
        os.remove(filename)

    # Convert wav to mp3 with same name using ffmpeg.exe
    @staticmethod
    def wavTomp3(wav):
        mp3 = wav[:-3] + "mp3"
        # Remove file if existent
        if os.path.isfile(mp3):
            Recorder.delete(mp3)
        # Call CMD command
        subprocess.call('ffmpeg -i "'+wav+'" "'+mp3+'"')