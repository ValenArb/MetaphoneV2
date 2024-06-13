import pyaudio
import wave
from libs.sub_libs.ignore import noalsaerr
import numpy as np
from variables import *

def Player(file_path: str , recorded = False):
    """Plays the audio file. in the path given

    Args:
        file_path (str): Path tho the audio file
        recorded (bool, optional): Whether the audio is recorded beforehand or not. Defaults to False.
    """
    if recorded:
        Volume_Multiplier = Audio_Multiplier
    else:
        Volume_Multiplier = Recording_Multiplier
    # Make sure the user is reading a wav file
    if (file_path[-4:] != ".wav"):
        wf = wave.open(file_path + ".wav", "rb")
    else:
        wf = wave.open(file_path, "rb")
    try:
        with noalsaerr():
            pa = pyaudio.PyAudio()
    except:
        pa = pyaudio.PyAudio()
    stream_out = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True,
        output_device_index = 1,
        frames_per_buffer = 512
    )
    data = wf.readframes(512)
    # Will loop until there is no more remaining audio
    while len(data) > 0:
        # Play the audio file
        npdata = np.frombuffer(data,dtype=np.int16)
        npdata = (npdata * Volume_Multiplier).astype(np.int16)
        newdata = npdata.tobytes()
        stream_out.write(newdata)
        data = wf.readframes(512)
    stream_out.stop_stream()
    stream_out.close()
    pa.terminate()
	
