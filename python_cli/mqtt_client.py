import paho.mqtt.client as mqtt
import queue
import time
import threading

class SimpleMQTTClient:
    def __init__(self, broker_address, port=1883, keepalive=60, topic="test/topic",
                 username=None, password=None, ca_certs=None, certfile=None, keyfile=None):
        self.broker_address = broker_address
        self.port = port
        self.keepalive = keepalive
        self.topic = topic
        self.message_queue = queue.Queue()
        self.connected = False
        self.running = False
        
        client_id = f'sunoff_oid-mqtt-{int(time.time())}'
        self.client = mqtt.Client(
            client_id=client_id
        )

        if username and password:
            self.client.username_pw_set(username=username, password=password)

        if ca_certs:
            self.client.tls_set(ca_certs=ca_certs, certfile=certfile, keyfile=keyfile)
            self.client.tls_insecure_set(False)
                  
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.connected = True
        else:
            print(f"Failed to connect, return code {rc}")

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected from MQTT Broker")
        self.connected = False
        self.reconnect()

    def reconnect(self):          
        while not self.connected and self.running:
            print("Reconnecting to MQTT Broker...")
            try:
                self.client.reconnect()
            except Exception as e:
                print(f"Reconnection failed: {e}")
            time.sleep(5)

    def start(self):
        self.running = True
        self.client.connect(self.broker_address, self.port, self.keepalive)
        self.client.loop_start()

        threading.Thread(target=self.process_queue, daemon=True).start()

    def process_queue(self):
        while self.running:
            try:
                message = self.message_queue.get(timeout=10)
                self.client.publish(self.topic, message)
                print(f"Published message: {message}")
            except queue.Empty:
                continue

    def send_message(self, message):
        if self.connected:
            self.message_queue.put(message)
        else:
            # print("Not connected, message not sent")
            pass

    def stop(self):
        self.running = False
        self.client.loop_stop()
        self.client.disconnect()
        print("MQTT client stopped.")
        
        
        
if __name__ == "__main__":
    # 配置MQTT代理地址和主题
    broker_address = "222.190.143.158"  # 使用公共MQTT代理进行测试
    port = 9701
    topic = "rid_mq"
    username = "sunoff_oid_client"
    password = "123456"
    # ca_certs = "path/to/ca.crt"  # 替换为你的CA证书路径

    # 创建MQTT客户端实例
    mqtt_client = SimpleMQTTClient(
        broker_address, 
        port=port, 
        topic=topic,
        username=username,
        password=password
    )

    # 启动客户端
    mqtt_client.start()

    # 发送一些消息
    for i in range(100):
        message = f"Hello MQTT {i}"
        mqtt_client.send_message(message)
        time.sleep(0.09)

    # 等待一段时间，确保消息发送完成
    time.sleep(2)

    # 停止客户端
    mqtt_client.stop()