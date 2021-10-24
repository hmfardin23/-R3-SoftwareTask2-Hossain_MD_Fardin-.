import socket
from pynput import keyboard

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Ways to open up to other connections

server.bind((socket.gethostname(), 5050))  # Binding the Port and Server
server.listen(10)

server, address = server.accept()

print(f"Connection from {address} has been initiated")

# List of the motor speed

speed_limits = ['0', '1', '2', '3', '4', '5']

# The while loop will process the inputs given in the client.py. If numbers 0-5
# are pressed, and if it matches with the list created, the motor speed will change accordingly and
# pressing (wasd) will move the rover forward,backward,left or right accordingly

while True:
    client_data = server.recv(1024).decode()

    for i in range(6):

        if client_data == speed_limits[i]:

            global motor_speed

            motor_speed = int(client_data) * 51

            print(f"The speed has been set to {client_data}")

    if client_data == 'w':
        print(f"[f{motor_speed}][f{motor_speed}][f{motor_speed}][f{motor_speed}]")

    elif client_data == 'a':
        print(f"[r{motor_speed}][r{motor_speed}][f{motor_speed}][f{motor_speed}]")

    elif client_data == 's':
        print(f"[r{motor_speed}][r{motor_speed}][r{motor_speed}][r{motor_speed}]")

    elif client_data == 'd':
        print(f"[f{motor_speed}][f{motor_speed}][r{motor_speed}][r{motor_speed}]")
