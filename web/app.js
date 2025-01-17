import MqttClient from './mqttClient.js';

const map = new AMap.Map('container', {
    viewMode: '2D', // 默认使用 2D 模式，如果希望使用带有俯仰角的 3D 模式，请设置 viewMode: '3D'
    zoom:15, // 初始化地图层级
    center: [116.397428, 39.90923] // 初始化地图中心点
});

// 初始化无人机标记
var droneMarker = new AMap.Marker({
	icon: "//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png",
    offset: new AMap.Pixel(-13, -30),
    map: map
});


// MQTT连接配置
const brokerUrl = 'ws://192.168.3.86:9703/mqtt'; 
const options = {
    username: 'sunoff_oid_client',
    password: '123456',
    reconnectPeriod: 10000, 
    clientId: 'mqttjs_' + Math.random().toString(16).substr(2, 8),
    rejectUnauthorized: false, 
};

// 初始化MQTT客户端
const mqttClient = new MqttClient(brokerUrl, options);

// 设置消息回调
mqttClient.setOnMessageCallback((topic, message) => {
    if (topic === 'drone/position') {
        const position = JSON.parse(message.toString());
        const { lat, lng } = position;
        console.log('Received drone position:', lat, lng);
        // droneMarker.setPosition([lng, lat]); // 更新无人机位置
        // // map.setCenter([lng, lat]); // 将地图中心点移动到无人机位置
    }
});

// 连接MQTT Broker并订阅Topic
mqttClient.connect();
mqttClient.subscribe('drone/position'); // 指定订阅的Topic