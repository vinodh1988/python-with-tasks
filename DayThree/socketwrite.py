import socket

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vinodhpc', 12345))
    return s
def send_message(s, message):
        s.sendall(message.encode('utf-8'))

import time
s = create_socket()
send_message(s, "Hello, World!")
time.sleep(5)
s=create_socket()
send_message(s, "Goodbye, World!")

s.close()