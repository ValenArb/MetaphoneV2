#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#
#                                                                                                               #
#                               METAPHONE rev.N2 by Codeiro - ValenArb                                                 #
#                                                                                                               #
#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#-=-#

import time
import random
from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
from libs.matrix import Matrix
from libs.Addons import *
from libs.sub_libs. Recorder import *
from libs.Players import *

def keypad():
    """Creates a keypad process and checks when the number changes to play the tone audio"""
    mem = SharedMemory(name="Memory", create = False)
    mem.buf[0] = 11
    process = Process(target=Matrix)
    process.start()
    while True: # Que funcion cumple?
        if mem.buf[0] != 11:
            mem.buf[0] = 11

def lang_sel():
    """Plays the language audio while waiting for the user to select a language

    Returns:
        Boolean: Wheter or not the user selected a language
    """
    lang_audio = Process(target=languages)
    lang_audio.start()
    mem = SharedMemory(name="Memory", create = False)
    mem.buf[100] = None
    end_time = time.time() + Max_Timeout_Menus
    while True:
        keypad = mem.buf[0]
        if time.time() > end_time or mem.buf[6] == 1:
            break
        if keypad == English_Key:
            mem.buf[100] = 0
            break
        elif keypad == Spanish_Key:
            mem.buf[100] = 1
            break
    try:
        lang_audio.terminate()
    except:
        pass
    if mem.buf[100] == None:
        return False
    else:
        return True
        

def main_sel():
    mem = SharedMemory(name="Memory", create = False)
    language = mem.buf[100]
    mem.buf[101] = None
    main_audio = Process(target=main_menu, args=(language,))
    main_audio.start()
    end_time = time.time() + Max_Timeout_Menus
    keypress = None
    while True:
        keypad = mem.buf[0]
        if time.time() > end_time or mem.buf[6] == 1:
            break
        if keypad == Send_Message_Key:
            mem.buf[101] = 0
            keypress = 0
            break
        elif keypad == Random_Message_Key:
            mem.buf[101] = 1
            keypress = 1
            break
        elif keypad == Code_Message_Key:
            mem.buf[101] = 2
            keypress = 2
            break
    main_audio.terminate()
    if keypress == Send_Message_Key: # Send a message (Record a message)
        record(language)
        time.sleep(0.5)
        random_instruction(language)
        rec = Recorder()
        beep()
        rec.start()
        filename = file()
        endtime = time.time() + Max_Record_Time
        while True:
            if time.time() > endtime() or mem.buf[0] == Stop_Record_Key:
                finished = True
                break
            elif  mem.buf[6] == 1:
                finished = False
                break
        rec.stop()
        rec.save(filename)
        if finished == True:
            finishing = Process(target=finish_r, args=(language,))
            finishing.start()
            time_end = time.time() + Max_Timeout_Record_Menu
            while True:
                if time.time() > time_end:
                    finishing.terminate()
                    break
                elif mem.buf[0] == Retry_Record_Key:
                    finishing.terminate()
                    reminder()
                    rec = Recorder()
                    endtime = time.time() + Max_Record_Time
                    beep()
                    rec.start()
                    while True:
                        if time.time() > endtime() or mem.buf[0] == Stop_Record_Key:
                            finished = True
                            break
                        elif  mem.buf[6] == 1:
                            finished = False
                            break
                    rec.stop()
                    rec.save(filename)
                    break
            if finished == True:
                success_r(language)
                time.sleep(0.5)
                message_code(language, filename)
            else:  
                kill_children()
            success_r(language)
            time.sleep(0.5)
            message_code(language, filename)
        else:
            kill_children()

    elif keypress == Random_Message_Key: # Hear a random message
        
    elif keypress == Code_Message_Key: # Insert a code to find a message
        ...
    return keypress

    #TODO GOODBYE AUDIO

def main_process():
    ...

def kill_children():
    """Kill all proceses that are not important to the program"""
    inmortal_children = ["Keypad", "Inputs"]
    for process in Process.active_children():
        if not process.name in inmortal_children:
            process.terminate()

if __name__ == "__main__":
    mem = SharedMemory(name="Memory", create = True, size = 1024) # Creates the shared memory to use between processes
    keyboard = Process(target=keypad, name = "Keypad") 
    keyboard.start()
    time.sleep(1) # Sleeps the program for 1 second to give time for the start of the keyboard
    inputs = Process(target = Input, args= (6,11), name="Inputs")
    inputs.start()
    busy = None
    while True:
        if mem.buf[11] == 0:
            # If the phone is deactivated (switch to the right)
            if mem.buf[6] == 0 and busy == None:
                # If they picked up and no busy tone is playing starts it
                busy = Process(target=busy)
                busy.start()
            elif mem.buf[6] == 1 and busy != None:
                # When phone is hanged up stops the busy tone
                busy.terminate()
                busy = None
        elif mem.buf[11] == 1:
            if busy != None:
                busy.terminate()
                busy = None
            # If the phone is activated (switch to the left)
            if mem.buf[6] == 0:
                times = random.randint(1, 3)
                dial(times)
                lang_menu = lang_sel()
                if lang_menu == False:
                    if mem.buf[6] == 1:
                        kill_children() 
                        #Kills all proceses just in case any that are not necesary stayed
                    else:
                        #TODO go to finishing audio
                        ...
                else:
                    selection_menu = Process()
                    ...
