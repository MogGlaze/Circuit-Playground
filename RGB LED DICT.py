from gpiozero import RGBLED
from time import sleep

right_eye_led = RGBLED(red="BOARD3", green="BOARD5", blue="BOARD7")
left_eye_led = RGBLED(red="BOARD8", green="BOARD10", blue="BOARD12")

def rgb_eyes(command):
    # Loop through dictionary (only 1 key expected)
    for key, rgb_values in command.items():

        # RGB (0–255 → 0–1)
        normal = tuple(value / 255 for value in rgb_values)

        if key == "set_left_rgb_eye_color":
            left_eye_led.color = normal

        elif key == "set_right_rgb_eye_color":
            right_eye_led.color = normal

        else:
            print("Invalid command:", key)

def main():
    print("Starting Program")

    eye_command = {"set_left_rgb_eye_color": [30, 17, 55]}
    print(eye_command)

    rgb_eyes(eye_command)

    sleep(5)

    #  off
    rgb_eyes({"set_left_rgb_eye_color": [0, 0, 0]})

    print("Ending Program")

main()
