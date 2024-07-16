import pyttsx3

engine = pyttsx3.init()

answer = input( " what do you want to convert into speech : " )


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 120)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female


engine.say(answer)
engine.runAndWait()
engine.stop()

# We can use file extension as mp3 and wav, both will work
engine.save_to_file( answer , 'speech(7).mp3')
 
# Wait until above command is not finished.
engine.runAndWait()
