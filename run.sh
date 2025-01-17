basedir=$(cd "$(dirname "$0")";pwd)
cd $basedir

mqtthost=122.190.143.158
mqttport=9701
mqttusername=sunoff_oid_client
mqttpassword=123456

#python sniff_receiver.py -l -e -mq --mqtthost $mqtthost --mqttport $mqttport --mqttusername $mqttusername --mqttpassword $mqttpassword
#python sniff_receiver.py -l -e -mq

#sleep 5

nohup ./sniff_receiver -l -e -mq --mqtthost $mqtthost --mqttport $mqttport --mqttusername $mqttusername --mqttpassword $mqttpassword 1>/dev/null 2>error.log &