import time
import pygame

hour = input("Enter hour (0-23): ")
minute = input("Enter minute (0-59): ")
second = input("Enter second (0-59): ")

alarm_time = f"{hour}:{minute}:{second}"
print(f"Alarm set for {alarm_time}")

pygame.mixer.init()
pygame.mixer.music.load("Ringtone(MP3).mp3")

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time, end="\r")

    if current_time == alarm_time:
        print(f"\nTime matched: {current_time}. Alarm ringing...")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        break

    time.sleep(1)
