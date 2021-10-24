import socket
from pynput import keyboard


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 5050))       # Connecting to the server

print("Set a desired speed ")
print("Press 'ESC' key to terminate the program")

# Keyboard Listener. This function listens to the buttons pressed and will send the data to the server


def button_pressed(key):
    try:
        server.send(bytes(format(key.char),"utf-8"))
    except AttributeError:
        if key == keyboard.Key.esc:
            print("Terminated")
            server.close()
            listener.stop()

