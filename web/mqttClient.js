// mqttClient.js
const mqtt = window.mqtt;

class MqttClient {
    constructor(brokerUrl, options) {
        this.brokerUrl = brokerUrl;
        this.options = options;
        this.client = null;
        this.onMessageCallback = null;
    }

    // 连接MQTT Broker
    connect() {
        this.client = mqtt.connect(this.brokerUrl, this.options);

        this.client.on('connect', () => {
            console.log('Connected to MQTT Broker');
        });

        this.client.on('message', (topic, message) => {
            if (this.onMessageCallback) {
                this.onMessageCallback(topic, message);
            }
        });

        this.client.on('error', (err) => {
            console.error('MQTT Error:', err);
        });

        this.client.on('close', () => {
            console.log('MQTT connection closed');
            this.reconnect(); // 自动重连
        });
    }

    // 订阅Topic
    subscribe(topic) {
        if (this.client && this.client.connected) {
            this.client.subscribe(topic, (err) => {
                if (err) {
                    console.error('Failed to subscribe to topic:', topic, err);
                } else {
                    console.log('Subscribed to topic:', topic);
                }
            });
        } else {
            console.error('MQTT client is not connected');
        }
    }

    // 设置消息回调
    setOnMessageCallback(callback) {
        this.onMessageCallback = callback;
    }

    // 自动重连
    reconnect() {
        setTimeout(() => {
            console.log('Reconnecting to MQTT Broker...');
            this.connect();
        }, 5000); // 5秒后重连
    }

    // 断开连接
    disconnect() {
        if (this.client) {
            this.client.end();
        }
    }
}

export default MqttClient;