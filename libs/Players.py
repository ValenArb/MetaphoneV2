from libs.sub_libs.Player import *
import time
import random
import os


def busy():
    """Player for busy tone"""
    dir='/home/FuegoAustral/Metaphone/Tones/busy.wav'
    while True:
        Player(dir, True)
        time.sleep(2)


def dial(times = 2):
    """Player for tone dialing

    Args:
        times (int, optional): Amount of times to play the tone. Defaults to 2.
    """
    dir='/home/FuegoAustral/Metaphone/Tones/dial.wav'
    i = 0
    while i < times:
        Player(dir, True)
        i += 1
        time.sleep(1)
    return

def languages():
    """Player for language menu"""
    while True:
        dir='/home/FuegoAustral/Metaphone/Audios/languages.wav'
        Player(dir, True)
        time.sleep(5)
        
def main_menu(language = 0):
    """Plays the selection menu in the language specified

    Args:
        language (int, optional): Language to play the selection menu in. Defaults to 0 (English).
    """
    if language == 0:
        base_dir='/home/FuegoAustral/Metaphone/Audios/English/'
    elif language == 1:
        base_dir='/home/FuegoAustral/Metaphone/Audios/Spanish/'
    dir = base_dir + "Welcome.wav"
    Player(dir, True)
    Options = ["Send.wav", "Receive.wav", "Code.wav"]
    while True:
        for option in Options:
            dir = base_dir + option
            Player(dir, True)
            time.sleep(0.5)
        time.sleep(5)
        
def record(language = 0):
    if language == 0:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/English/'
    elif language == 1:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/Spanish/'
    dir = base_dir + "Record.wav"
    Player(dir, True)
    return

def reminder(language = 0):
    if language == 0:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/English/'
    if language == 1:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/Spanish/'
    dir = base_dir + "Reminder.wav"
    Player(dir, True)
    return

def beep():
    dir = '/home/FuegoAustral/Metaphone/Tones/beep.wav'
    Player(dir, True)
    return

def random_instruction(language = 0):
    if language == 0:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/English'
    if language == 1:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/Spanish'
    file = random.choice(os.listdir(base_dir))
    dir = base_dir +"/" + file
    Player(dir, True)
    return

def finish_r(language = 0):
    if language == 0:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/English'
    if language == 1:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/Spanish'
    dir = base_dir +"/" + "Finished.wav"
    Player(dir, True)
    return

def success_r(language = 0):
    if language == 0:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/English'
    if language == 1:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/Spanish'
    dir = base_dir +"/" + "Success.wav"
    Player(dir, True)
    return

def message_code(language = 0, Code: int = 0):
    if language == 0:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/English/Numbers'
    if language == 1:
        base_dir = '/home/FuegoAustral/Metaphone/Audios/Spanish/Numbers'
    for digit in str(Code):
        dir = base_dir + "/" + digit + ".wav"
        Player(dir, True)
        time.sleep(0.5)
    return

