from gpiozero import DigitalInputDevice
from multiprocessing.shared_memory import SharedMemory
import os

def Input(pin1: int = None, pin2: int = None, pin3: int = None, pin4: int = None):
    """Read the status of the input pins given as arguments.

    Args:
        pin1 (int, optional): GPIO Pin to be checked. Defaults to None.
        pin2 (int, optional): GPIO Pin to be checked. Defaults to None.
        pin3 (int, optional): GPIO Pin to be checked. Defaults to None.
        pin4 (int, optional): GPIO Pin to be checked. Defaults to None.
    """
    pins = [pin1, pin2, pin3, pin4]
    while None in pins:
        pins.remove(None)
    inputs = []
    for pin in pins:
        input = DigitalInputDevice(pin=pin)
        inputs.append(input)
    mem = SharedMemory(name= "Memory", create= False)
    while True:
        for input in inputs:
            pin = input.pin.number
            if input.value == 1:
                mem.buf[pin] = 1
            else:
                mem.buf[pin] = 0
                
def file():
    files = os.listdir('/home/FuegoAustral/Metaphone/Recordings')
    wavs = []
    for file in files:
        if file.endswith('.wav'):
            wavs.append(file)
    wavs.sort()
    for i in range(len(wavs)):
        if wavs[i] != i+1:
            return i+1
    return len(wavs)+1
