
###YOU HAVE TO PIP INSTALL THE FOLLOWING
#pip install fakeyou playsound os re

import fakeyou #fakeYou lib
from playsound import playsound
from login import * #import everything from login
import os #to handle folder creation
import re #to remove special character for folder saving
#Voice and ID map
voice_map = {
  'MorganFreeman' : 'TM:709ck7g83431',
  'Yoda' : 'TM:fmspb239ea3a',
  'Wednesday' : 'TM:pqv7261xqhjk',
  'PeterGriffin' : 'TM:9yh8jn3p854a',
  'SnoopDog' : 'TM:hqcecn351tpc',
  'HomerSimpson' : 'TM:r9mxvgcybyy5',
  'DarthVader' : 'TM:j764y97vfgbs',
  'ABCWorldReference3DAtlas97Narrator' : 'TM:vxpbzc0g9dqv',
  'AbrahamSimpson' : 'TM:byzk08rq9g0y',
  'AdalRamones' : 'TM:gx0jpfed20b7',
  'AdamDriver' : 'TM:988r6rvf1sy3',
  'AdamIsCoolAndStuff' : 'TM:teswc4g0bvw7',
  'Adamiscoolandstuff' : 'TM:03tm25z0xbjs',
  'Adamiscoolandstuff2' : 'TM:e4rknepgz8t9',
  'AdamIsCoolAndStuff2' : 'TM:cgnkxe7tw7v4',
  'AdmiralBrickell' : 'TM:a790hmn201m5',
  'Adora' : 'TM:xms9q1td9z6p',

}


#function declaration to get the ttsModelToken based on the chosen name
def get_voice_id(name):
    formated_name =  re.sub(r'\W+', '', name)
    for voice_name,voice_id in voice_map.items():
        if voice_name == formated_name:
            return voice_id
    return None

#create the object to hold the FakeYou lib
fy = fakeyou.FakeYou()
#i have another file named login.py that defines them
fy.login(LOGIN, PASSWORD)

#the current voice to be selected (does not work out of nowhere, the voices and IDs are a pre-made list)
chosen_voice_name = "Morgan Freeman"

#the text message to be said
text_message = f"Hello World, I am {chosen_voice_name} and I like coding in Python"

#run the function to search the ttsModelToken ID based on the chosen name
final_voice_id = get_voice_id(chosen_voice_name)

#print the current voice ID
print(final_voice_id) 

#creates a folder with chosen_voice_name as its name
folder_path = f"./output/{chosen_voice_name}"

#checks if there is already a folder
try:
    os.mkdir(f"./output")
except:
    print('output folder already exist')

try:
    os.mkdir(f"./output/{chosen_voice_name}")
except:
    print(f'output/{chosen_voice_name} folder already exist')


#changes special characters into normal ones but keep spaces, to be able to save the file
message_witouth_special_chars = re.sub(r'[^\w\s]', '', text_message) 

#saves the final audio at a folder with the voice name and the message written
final_audio_path = f"./output/{chosen_voice_name}/{chosen_voice_name} {message_witouth_special_chars}.wav"


#ask the API to say (Message to say, The ttsModelToken ID, TM:709ck7g83431 for MorganFreeman)
text_request = fy.say(text_message, ttsModelToken=final_voice_id)
text_request.save(final_audio_path)
#use the playsound library to play our .wav file back
playsound(final_audio_path)
#print the final audio path
print(final_audio_path)


