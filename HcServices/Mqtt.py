import paho.mqtt.client as mqtt
import asyncio
import queue
import Constant.Constant as const
from Cache.GlobalVariables import GlobalVariables
import logging
import threading
import socket
from Constract.ITransport import ITransport

class MqttConfig():
    host: str
    port: int
    qos: int
    keepAlive: int
    username: str
    password: str
    
    def __init__(self): 
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.host = ip
        self.port = const.MQTT_PORT
        self.qos = const.MQTT_QOS
        self.keepAlive = const.MQTT_KEEPALIVE
        self.username = const.MQTT_USER
        self.password = const.MQTT_PASS


class Mqtt(ITransport):
    __mqttConfig: MqttConfig
    __client: mqtt.Client
    mqttDataQueue: queue.Queue
    __globalVariables: GlobalVariables
    __logger: logging.Logger
    __lock: threading.Lock
    
    def __init__(self, log: logging.Logger):
        self.__logger = log
        self.__mqttConfig = MqttConfig()
        self.__client = mqtt.Client()
        self.mqttDataQueue = queue.Queue()
        self.__globalVariables = GlobalVariables()
        self.__lock = threading.Lock()
    
    def __on_message(self, client, userdata, msg):
        """[summary]

        Args:
            client ([type]): [description]
            userdata ([type]): [description]
            msg ([type]): [description]
        """
        message = msg.payload.decode("utf-8")
        topic = msg.topic
        item = {"topic": topic, "msg": message}
        with self.__lock:
            self.mqttDataQueue.put(item)
        return
    
    def __on_connect(self, client, userdata, flags, rc):
            self.__client.subscribe(topic=const.MQTT_CONTROL_TOPIC, qos=self.__mqttConfig.qos)

    def _connect(self):
        """  Connect to mqtt broker

        Returns:
            [bool]: [connect status: false/true]
        """
      
        self.__client.on_message = self.__on_message
        self.__client.on_connect = self.__on_connect
        self.__client.username_pw_set(username=self.__mqttConfig.username, password=self.__mqttConfig.password)
        try:
            self.__client.connect(self.__mqttConfig.host, self.__mqttConfig.port)
            self.__client.loop_start()
        except Exception as err:
            self.__logger.error(f"Exception in connect to mqtt: {err}")
            print(f"Exception in connect to mqtt: {err}")

    def send(self, destination, send_data):
        self.__client.publish(destination, payload=send_data, qos=const.MQTT_QOS)
             
    def disconnect(self):
        self.__client.disconnect()

    def connect(self):
        self._connect()

    def reconnect(self):
        pass
    
    def receive(self):
        pass

