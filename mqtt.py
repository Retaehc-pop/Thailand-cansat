import time
import random
import paho.mqtt.client as mqtt


# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))


def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, obj, level, string):
    print(string)


def Initialise_client():
    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.connect("139.162.43.212")
    mqttc.on_log = on_log
    mqttc.loop_start()
    return mqttc


def sendserver(mqttc, Data):
    if Data[0] == "C":
        mqttc.publish('Altitude_c', Data[2])
        mqttc.publish('Temperature_c', Data[5])
        mqttc.publish('Battery_c', Data[8])
        mqttc.publish('Humidity_c', Data[6])
        mqttc.publish('Pressure_c', Data[7])
        mqttc.publish('PM10_c', Data[9])
        mqttc.publish('PM25_c', Data[10])
        mqttc.publish('lat_c', Data[3])
        mqttc.publish('lon_c', Data[4])
        mqttc.publish('Accx_c', Data[11])
        mqttc.publish('Accy_c', Data[12])
        mqttc.publish('Accz_c', Data[13])
        mqttc.publish('Gyrox_c', Data[14])
        mqttc.publish('Gyroy_c', Data[15])
        mqttc.publish('Gyroz_c', Data[16])
    elif Data[0] == "R":
        mqttc.publish('Altitude_r', Data[2])
        mqttc.publish('Temperature_r', Data[5])
        mqttc.publish('Battery_r', Data[6])
        mqttc.publish('lat_r', Data[3])
        mqttc.publish('lon_r', Data[4])
        mqttc.publish('Accx_r', Data[7])
        mqttc.publish('Accy_r', Data[8])
        mqttc.publish('Accz_r', Data[9])
        mqttc.publish('Gyrox_r', Data[10])
        mqttc.publish('Gyroy_r', Data[11])
        mqttc.publish('Gyroz_r', Data[12])
    time.sleep(0.01)


def test():
    i=0
    while True:
        i+=1
        mqttc.publish('Altitude_c',str(random.randint(0,100)))
        mqttc.publish('Temperature_c',str(random.randint(0,100)))
        mqttc.publish('Battery_c', str(random.randint(0,100)))
        mqttc.publish('Humidity_c',str(random.randint(0,100)))
        mqttc.publish('Pressure_c',str(random.randint(0,100)))
        mqttc.publish('PM10_c',str(random.randint(0,100)))
        mqttc.publish('PM25_c',str(random.randint(0,100)))
        mqttc.publish('lat_c',str(random.randint(0,100)))
        mqttc.publish('lon_c',str(random.randint(0,100)))
        mqttc.publish('Accx_c',str(random.randint(0,100)))
        mqttc.publish('Accy_c',str(random.randint(0,100)))
        mqttc.publish('Accz_c',str(random.randint(0,100)))
        mqttc.publish('Gyrox_c',str(random.randint(0,100)))
        mqttc.publish('Gyroy_c',str(random.randint(0,100)))
        mqttc.publish('Gyroz_c',str(random.randint(0,100)))

        mqttc.publish('Altitude_r', str(random.randint(0,100)))
        mqttc.publish('Temperature_r', str(random.randint(0,100)))
        mqttc.publish('Battery_r', str(random.randint(0,100)))
        mqttc.publish('lat_r', str(random.randint(0,100)))
        mqttc.publish('lon_r', str(random.randint(0,100)))
        mqttc.publish('Accx_r', str(random.randint(0,100)))
        mqttc.publish('Accy_r', str(random.randint(0,100)))
        mqttc.publish('Accz_r', str(random.randint(0,100)))
        mqttc.publish('Gyrox_r', str(random.randint(0,100)))
        mqttc.publish('Gyroy_r', str(random.randint(0,100)))
        mqttc.publish('Gyroz_r', str(random.randint(0,100)))
        time.sleep(1)
        print(i)

if __name__ == "__main__":
    mqttc = Initialise_client()
    test()
