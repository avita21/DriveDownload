'''
 Dumb script to download google drive png files
 To use: dump this file in a folder with the TTS save state
 (Or another json file with google drive links)
 Run the script
 Wait a few hours to download all files in save state
 Once completed, copy all files to the Images folder in TTS,
 delete the Images Raw folder
 Ensure mod caching is on
 Run TTS!
'''
import re
import json
from flatten_json import flatten
import time
import random
import gdown
import os
import datetime

def download_file(image_url):
    filename = re.sub(r'[^a-zA-Z0-9]', '', image_url) + '.png'
    if filename in os.listdir():
        print("Already downloaded", filename, "moving onwards...")
        return False
    lowspeed = 300 * 1024
    highspeed = 1024 * 1024 
    speed = int(random.uniform(lowspeed,highspeed))
    sleeptime = random.uniform(5.0,12.0)
    gdown.download(image_url + "&confirm=t", filename, use_cookies=False, speed=speed)
    print("Sleeping for", sleeptime, "seconds...")
    time.sleep(sleeptime)
    return True

def main():
    save_state = ''
    start_time = time.time()
    for file in os.listdir():
        if file.endswith('.json'):
            save_state = file
            break
    with open(save_state, "r") as read_file:
        print("Reading", save_state)
        save_file = json.load(read_file)
        flat_save = flatten(save_file)
        download_counter = 0
        index = 0
        drive_list = [val for key, val in flat_save.items() if 'drive' in str(val)]
        drive_list = list(set(drive_list))
        print("Downloading", len(drive_list), "Drive files...")
        for file in drive_list:
            print(len(drive_list) - index, "files left")
            if download_file(file):
                download_counter += 1
            index += 1
        end_time = time.time()
        dt = datetime.timedelta(seconds=end_time-start_time)
        print("Downloaded", download_counter, "files in", dt, "time")
        input()

if __name__ == "__main__":
    main()