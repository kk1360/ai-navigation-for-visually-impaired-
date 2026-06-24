import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 170)

last_spoken = {}
COOLDOWN = 3  # seconds

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_direction(x_center, frame_width):
    if x_center < frame_width / 3:
        return "left"
    elif x_center > 2 * frame_width / 3:
        return "right"
    else:
        return "ahead"

def estimate_distance(box_width):
    if box_width > 300:
        return "very close"
    elif box_width > 150:
        return "near"
    else:
        return "far"

def audio_alert(class_name, box_width, x_center, frame_width):
    current_time = time.time()

    if class_name not in last_spoken or current_time - last_spoken[class_name] > COOLDOWN:
        direction = get_direction(x_center, frame_width)
        distance = estimate_distance(box_width)

        message = f"{class_name} {direction}, {distance}"
        speak(message)

        last_spoken[class_name] = current_time
