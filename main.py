import socket
import threading
from mqtt_handler import setup_mqtt_client, mqtt_topic, mqtt_on_message
from mongo_handler import mongo_collection

# MQTT configuration
mqtt_host = 'localhost'

# Set up MQTT client
mqtt_client = setup_mqtt_client()

# Socket configuration
socket_host = 'localhost'
socket_port = 9999

# Socket message handler
def handle_socket_message(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode().strip()
        mqtt_client.publish(mqtt_topic, message)
    client_socket.close()

# Socket server
def socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((socket_host, socket_port))
        server_socket.listen(5)
        print("Socket server listening on port", socket_port)
        while True:
            client_socket, address = server_socket.accept()
            print("Accepted connection from", address)
            socket_thread = threading.Thread(target=handle_socket_message, args=(client_socket,))
            socket_thread.start()

# Start socket server in a separate thread
socket_thread = threading.Thread(target=socket_server)
socket_thread.start()

# Connect to the socket server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((socket_host, socket_port))
    print("Connected to the socket server.")

    # Send messages until user exits
    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
