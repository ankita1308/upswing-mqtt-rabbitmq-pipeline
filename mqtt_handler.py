import paho.mqtt.client as mqtt
from mongo_handler import mongo_collection

# MQTT configuration
mqtt_topic = 'rabbitmq_topic'

# MQTT message receiver
def mqtt_on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message from MQTT: {message}")
    # Store message in MongoDB
    mongo_collection.insert_one({'message': message})


# Set up MQTT client
def setup_mqtt_client():
    mqtt_client = mqtt.Client()
    mqtt_client.on_message = mqtt_on_message
    mqtt_client.connect('localhost', 1883)
    mqtt_client.subscribe(mqtt_topic)
    mqtt_client.loop_start()
    return mqtt_client
