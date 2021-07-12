HttpStatusCodeOk = 200
#Cloud generic infomation
SERVER_HOST = "https://iot-dev.truesight.asia"

#SignalR connection option
SIGNALR_SERVER_URL = "/rpc/iot-ebe/signalr/sync"
SIGNSLR_HEARDBEAT_URL = "/rpc/iot-ebe/sync/time"
SIGNALR_APP_COMMAND_ENTITY = "Command"
SIGNALR_APP_RESPONSE_ENTITY = "DeviceResponse"
SIGNALR_CLOUD_RESPONSE_ENTITY = "HC-DeviceAttributeValue"

#pull,push data url
CLOUD_PUSH_DATA_URL = "/rpc/iot-ebe/sync/hc/merge-device-attribute-value"
CLOUD_PULL_DEVICE_URL = "/rpc/iot-ebe/sync/list-device"
CLOUD_PULL_GROUPING_URL = "/rpc/iot-ebe/sync/list-grouping"
CLOUD_PULL_SCENE_URL = "/rpc/iot-ebe/sync/list-scene"
CLOUD_PULL_RULE_URL = "/rpc/iot-ebe/sync/list-rule"
#Mqtt connection option
MQTT_PORT = 1883
MQTT_QOS = 2
MQTT_KEEPALIVE = 60
MQTT_CONTROL_TOPIC = "HC.CONTROL"
MQTT_RESPONSE_TOPIC = "HC.CONTROL.RESPONSE"
MQTT_USER = "RD"
MQTT_PASS = "1"

#Server connection option
TOKEN_URL = "/rpc/iot-ebe/account/renew-token"

#Sqlite connection option
DB_NAME = "rd.Sqlite"

#Led
LED_SERVICE_PIN_ON = '/bin/echo "1" > /sys/class/leds/linkit-smart-7688:orange:service/brightness'
LED_SERVICE_PIN_OFF = '/bin/echo "0" > /sys/class/leds/linkit-smart-7688:orange:service/brightness'