// 等待高德地图API加载完成
window.onload = function () {
    if (typeof AMap !== 'undefined') {
        initMap();
    } else {
        console.error('高德地图API未加载');
    }
};


function initMap() {

    const map = new AMap.Map('container', {
        viewMode: '2D', // 默认使用 2D 模式，如果希望使用带有俯仰角的 3D 模式，请设置 viewMode: '3D'
        zoom:15, // 初始化地图层级
        center: [116.397428, 39.90923] // 初始化地图中心点
    });

    // 初始化无人机标记
    var droneMarker = new AMap.Marker({
        // icon: "https://a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png",
        // anchor: 'bottom-center'

        icon: "flight.svg",
        // offset: new AMap.Pixel(-16, -16)
        anchor: 'center'
    });
    var setInitPos = false;


    var infoWindow = new AMap.InfoWindow({
        offset: new AMap.Pixel(30, 0),
        anchor: 'middle-left',
    });

    // MQTT连接配置
    const options = {
        username: 'sunoff_oid_client', // 替换为你的MQTT用户名
        password: '123456', // 替换为你的MQTT密码
        protocol: 'ws', // 使用WebSocket协议
        host: '192.168.3.86', // 替换为你的MQTT Broker地址
        port: 9703, // WebSocket端口（通常为8083或8084）
        path: '/mqtt', // MQTT over WebSocket的路径
    };

    // 连接MQTT Broker
    const client = mqtt.connect(options);

    client.on('connect', () => {
        console.log('Connected to MQTT Broker');
        client.subscribe('drone/position', (err) => {
            if (!err) {
                console.log('Subscribed to drone/position');
            }
        });
    });

    // 接收MQTT消息并更新无人机位置
    client.on('message', (topic, message) => {
        if (topic === 'drone/position') {
            const position = JSON.parse(message.toString());
            // console.log('Received drone position:', position);
            const angle = Number(position[0].flyDirection);
            const lng = Number(position[0].uavLongitude);
            const lat = Number(position[0].uavLatitude);
            const pos = [lng, lat];
            console.log('Received drone position:', pos);
            droneMarker.setAngle(angle);
            droneMarker.setPosition(pos);

            var info = [];
            info.push("<div>");
            info.push("<p> SN:        " + position[0].uavSn + "</p>")
            info.push("<p> altitude:  " + position[0].altitude + "m </p>")
            info.push("<p> direction: " + position[0].flyDirection + "°</p>")
            info.push("<p> timestamp: " + timestampToYMDHMS(position[0].timestamp * 1000) + "</p>")
            info.push("</div>");
            infoWindow.setContent(info.join(" "));
            infoWindow.open(map, pos);
            
            if(!setInitPos) {
                droneMarker.setMap(map);
                map.setCenter(pos);
                setInitPos = true;   
            }
        }
    });

    client.on('error', (err) => {
        console.error('MQTT Error:', err);
    });


    function timestampToYMDHMS(timestamp) {
        const date = new Date(timestamp);
  
        const year = date.getFullYear();
        const month = (date.getMonth() + 1 < 10 ? '0' : '') + (date.getMonth() + 1);
        const day = (date.getDate() < 10 ? '0' : '') + date.getDate();
        const hours = (date.getHours() < 10 ? '0' : '') + date.getHours();
        const minutes = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
        const seconds = (date.getSeconds() < 10 ? '0' : '') + date.getSeconds();
    
        return `${year}/${month}/${day} ${hours}:${minutes}:${seconds}`;
    }
}