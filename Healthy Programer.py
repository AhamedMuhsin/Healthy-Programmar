# importing module use in this program
from pygame import mixer
from datetime import datetime
from time import time

# music loop function to play music
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

# log function to write the things in file
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

#  main functions in this program
if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
#         water drink 
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('Water Pour Into Half Full Sink.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

#             eye exersice
        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('Monster Alien Grunt Sleepy.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

#             pyhsical exersice
        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('Breathing Echo space.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")




