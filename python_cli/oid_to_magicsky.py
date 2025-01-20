import json
import time


# received data from xiaofang (Dynamic)
_xiaofang_json_datas = [
'''[
    {
        "Basic ID": 
        { 
            "protocol_version": "F3411.22", 
            "id_type": "Serial Number (ANSI/CTA-2063-A)", 
            "ua_type": "Aeroplane", 
            "id": "2051FEABPT0000000208"
        }
    }, 
    {
        "Location/Vector Message": 
        { 
            "protocol_version": "F3411.22", 
            "op_status": "Airborne", 
            "height_type": "Above Takeoff", 
            "ew_dir_segment": "East", 
            "speed_multiplier": "0.25", 
            "direction": 0, 
            "speed": "0.0 m/s", 
            "vert_speed": "0.0 m/s", 
            "latitude": "32.1572862", 
            "longitude": "118.8639275", 
            "pressure_altitude": "Undefined", 
            "geodetic_altitude": "230.0 m", 
            "height_agl": "-47.0 m", 
            "vertical_accuracy": "<3 m", 
            "horizontal_accuracy": "<10 m", 
            "baro_accuracy": ">=150 m or Unknown", 
            "speed_accuracy": "<3 m/s", 
            "timestamp": "9 min 50.0 s", 
            "timestamp_accuracy": "0.1 s"
        }
    }, 
    {
        "System Message": 
        {
            "operator_location_type": "Takeoff",
            "classification_type": "Undeclared", 
            "latitude": 32.1571196, 
            "longitude": 118.8641543, 
            "area_count": 1, 
            "area_radius": 0, 
            "area_ceiling": "0.0 m", 
            "area_floor": "0.0 m", 
            "ua_classification_category_type": "Undefined", 
            "ua_classification_category_class": "Class 1", 
            "geodetic_altitude": "277.0 m", 
            "timestamp": "2025-01-16 02:09 UTC",
            "timestamp_raw": 190692590, 
            "protocol_version": "F3411.22"
        }
    }
]'''
,
'''[
    {
        "Basic ID": 
        {
            "protocol_version": "F3411.22", "id_type": "Serial Number (ANSI/CTA-2063-A)", 
            "ua_type": "Aeroplane", 
            "id": "2051FEABPT0000000208"
        }
    }, 
    {
        "Location/Vector Message": 
        {
            "protocol_version": "F3411.22", 
            "op_status": "Airborne", 
            "height_type": "Above Takeoff", 
            "ew_dir_segment": "West", 
            "speed_multiplier": "0.25", 
            "direction": 281, 
            "speed": "0.0 m/s", 
            "vert_speed": "0.0 m/s", 
            "latitude": "32.1575628", 
            "longitude": "118.8619308", 
            "pressure_altitude": "Undefined", 
            "geodetic_altitude": "156.5 m", 
            "height_agl": "-120.5 m", 
            "vertical_accuracy": "<3 m", 
            "horizontal_accuracy": "<3 m", "baro_accuracy": ">=150 m or Unknown", "speed_accuracy": "<3 m/s", 
            "timestamp": "35 min 51.0 s", "timestamp_accuracy": "0.1 s"
        }
    }, 
    {
        "System Message": 
        {
            "operator_location_type": "Takeoff", "classification_type": "Undeclared", 
            "latitude": 32.1571196, "longitude": 118.8641543, 
            "area_count": 1, "area_radius": 0, "area_ceiling": "0.0 m", "area_floor": "0.0 m", 
            "ua_classification_category_type": "Undefined", "ua_classification_category_class": "Class 1", 
            "geodetic_altitude": "277.0 m", 
            "timestamp": "2025-01-16 02:35 UTC", 
            "timestamp_raw": 190694151, 
            "protocol_version": "F3411.22"
        }
    }
]'''
]

_project_json_datas = '''
[
    [
        {
            "MAC": "11:22:33:44:55:66"
        },
        {
            "ADI": 4571
        },
        {
            "Basic ID": {
                "protocol_version": "F3411.19",
                "id_type": "Serial Number (ANSI/CTA-2063-A)",
                "id": "18656A24303",
                "ua_type": "Helicopter (or Multirotor)"
            }
        },
        {
            "Basic ID": {
                "protocol_version": "F3411.19",
                "id_type": "CAA Assigned Registration ID",
                "id": "DJI",
                "ua_type": "Helicopter (or Multirotor)"
            }
        },
        {
            "Location Vector": {
                "protocol_version": "F3411.22",
                "op_status": "Airborne",
                "height_type": "Above Takeoff",
                "ew_dir_segment": "East",
                "speed_multiplier": "0.25",
                "coord": {
                    "direction": 94,
                    "speed": 1,
                    "vert_speed": 0,
                    "latitude": 336577004,
                    "longitude": -822156164,
                    "pressure_altitude": 0,
                    "geodetic_altitude": 2152,
                    "height_agl": 1982,
                    "horizontal_accuracy": "<1 m",
                    "vertical_accuracy": "<10 m",
                    "baro_accuracy": "<10 m",
                    "speed_accuracy": "<0.3 m/s",
                    "timestamp": 5470,
                    "timestamp_accuracy": 2
                }
            }
        },
        {
            "Authentication": {
                "protocol_version": "F3411.19",
                "auth_type": "Message Set Signature",
                "page_number": 0,
                "last_page_index": 0,
                "timestamp": 170716129,
                "auth_data": "0000000000000000000000000000000000"
            }
        },
        {
            "Self ID": {
                "protocol_version": "F3411.22",
                "text_type": "Text Description",
                "text": "Drones ID test flight"
            }
        },
        {
            "System": {
                "protocol_version": "F3411.22",
                "classification_type": "EU",
                "operator_location_type": "Takeoff",
                "latitude": 336631981,
                "longitude": -822205112,
                "area_count": 1,
                "area_radius": 0,
                "area_ceiling": 2000,
                "area_floor": 2000,
                "ua_classification_category_type": "Open",
                "ua_classification_category_class": "Class 1",
                "geodetic_altitude": 2170,
                "timestamp": 170716129
            }
        },
        {
            "Operator ID": {
                "protocol_version": "F3411.22",
                "id_type": "Operator ID",
                "id": ""
            }
        }
    ],
    [
        {
            "Basic ID": {
                "protocol_version": "F3411.19",
                "id_type": "Serial Number (ANSI/CTA-2063-A)",
                "id": "SSEVTFG93700070",
                "ua_type": "Helicopter (or Multirotor)"
            }
        },
        {
            "Location Vector": {
                "protocol_version": "F3411.19",
                "op_status": "Airborne",
                "height_type": "Above Takeoff",
                "ew_dir_segment": "West",
                "speed_multiplier": "0.25",
                "coord": {
                    "direction": 180,
                    "speed": 255,
                    "vert_speed": 120,
                    "latitude": 0,
                    "longitude": 0,
                    "pressure_altitude": 1891,
                    "geodetic_altitude": 0,
                    "height_agl": 1999,
                    "horizontal_accuracy": ">=18.52 km (10 NM) or Unknown",
                    "vertical_accuracy": ">=150 m or Unknown",
                    "baro_accuracy": 5,
                    "speed_accuracy": ">= 10 m/s or Unknown",
                    "timestamp": 0,
                    "timestamp_accuracy": 1
                }
            }
        },
        {
            "Self ID": {
                "protocol_version": "F3411.19",
                "text_type": "Text Description",
                "text": "Drone ID demo"
            }
        },
        {
            "System": {
                "protocol_version": "F3411.19",
                "classification_type": "EU",
                "operator_location_type": "Takeoff",
                "latitude": 0,
                "longitude": 0,
                "area_count": 1,
                "area_radius": 0,
                "area_ceiling": 0,
                "area_floor": 0,
                "ua_classification_category_type": "Open",
                "ua_classification_category_class": "Class 0",
                "geodetic_altitude": 0,
                "timestamp": 0
            }
        },
        {
            "Operator ID": {
                "protocol_version": "F3411.19",
                "id_type": "Operator ID",
                "id": "FIN87astrdge12kxyz8"
            }
        }
    ]
]
'''



def oid_to_magicsky_v1(oid_packtet: list):
   
    magicsky_packets = []
    
    for msg_lv1 in oid_packtet:
        
        basicIds = []
        LocationVector = None
        System = None
        
        for item_lv2 in msg_lv1:     
            if 'Basic ID' in item_lv2:
                basicIds.append(item_lv2['Basic ID'])
            elif 'Location Vector' in item_lv2:
                LocationVector = item_lv2['Location Vector']
            elif 'System' in item_lv2:
                System = item_lv2['System']
            else:
                continue

        if len(basicIds) and LocationVector and System:
            
            id = None
            ua_type = None
            for basicId in basicIds:
                if basicId['id_type'] == 'Serial Number (ANSI/CTA-2063-A)':
                    uav_id = basicId['id']
                    ua_type = basicId['ua_type']

            coord = LocationVector['coord']
            ewDir = LocationVector['ew_dir_segment'] == 'East'
            mult = LocationVector['speed_multiplier'] 

            # ref: 
            #     file: OpenDroneID/decoder.py
            #     url: https://github.com/opendroneid/opendroneid-core-c/blob/master/libopendroneid/opendroneid.c
        
            magicsky_packet = dict()
            
            magicsky_packet['uavSn'] = uav_id
            magicsky_packet['productType'] = ua_type
            val = coord['longitude']
            magicsky_packet['uavLongitude'] = 'Unknow' if val == 0 else "%.7f" % (val / 10**7)
            val = coord['latitude']
            magicsky_packet['uavLatitude'] = 'Unknow' if val == 0 else "%.7f" % (val / 10**7)
            # magicsky_packet['altitude'] = coord['height_agl'] *.5 - 1e3
            val = coord['height_agl']
            magicsky_packet['altitude'] = 'Unknow' if val == 0 else "%.2f" % (val *.5 - 1000)  
            val = coord['direction']
            magicsky_packet['flyDirection'] =val if ewDir else val - 180 
            val = coord['speed']
            magicsky_packet['flySpeed'] = 'Unknow' if val == 255 else "%.2f" % ( val *.25 if mult == '0.25' else val *.75 + 255 *.25)
            magicsky_packet['timestamp'] = System['timestamp'] + 1546300800
            
            magicsky_packets.append(magicsky_packet)
            
    return magicsky_packets


# def oid_to_magicsky_v2(json_string):   
#     oid_packtet = json.loads(json_string)

def oid_to_magicsky_v2(oid_packtet: list, dev_sn = None):
     
    magicsky_packets = []
    
    for msg_lv1 in oid_packtet:
        
        BasicIds = []
        LocationVector = None
        System = None
               
        for item_lv2 in msg_lv1:     
            if 'Basic ID' in item_lv2:
                BasicIds.append(item_lv2['Basic ID'])
            elif 'Location/Vector Message' in item_lv2:
                LocationVector = item_lv2['Location/Vector Message']
            elif 'System Message' in item_lv2:
                System = item_lv2['System Message']
            else:
                continue

        if len(BasicIds) and LocationVector and System:
            
            id = None
            ua_type = None
            for basicId in BasicIds:
                if basicId['id_type'] == 'Serial Number (ANSI/CTA-2063-A)':
                    uav_id = basicId['id']
                    ua_type = basicId['ua_type']
            
            # NO NEED decode using xiaofang datas
            magicsky_packet = dict()
            
            if dev_sn:
                magicsky_packet['deviceSn'] = dev_sn
               
            magicsky_packet['uavSn'] = uav_id
            magicsky_packet['productType'] = ua_type
            magicsky_packet['uavLongitude'] = LocationVector['longitude']
            magicsky_packet['uavLatitude'] = LocationVector['latitude']
            magicsky_packet['altitude'] = LocationVector['geodetic_altitude'].split(' m')[0]
            magicsky_packet['flyDirection'] = int(LocationVector['direction'])
            magicsky_packet['timestamp'] = System['timestamp_raw'] + 1546300800
            
            magicsky_packets.append(magicsky_packet)

    return magicsky_packets


def oid_to_magicsky(json_string: str, device_sn = None):
    # return oid_to_magicsky_v1(json_string)
    
    json_data = json.loads(json_string)    
    if type(json_data[0]) != list:
        json_data = [json_data]   
    json_packet = oid_to_magicsky_v2(json_data, device_sn)
    return json.dumps(json_packet)


def test_project_data():
    
    json_data = json.loads(_project_json_datas)
    magicsky_packets = oid_to_magicsky_v1(json_data)    
    if len(magicsky_packets):
        print(json.dumps(magicsky_packets))
        
        
    print('')
        
    with open('drone.json','r', encoding='utf-8') as json_file: 
        json_data = json.load(json_file)
        magicsky_packets = oid_to_magicsky_v1(json_data)     
        if len(magicsky_packets):
            print(json.dumps(magicsky_packets))

def test_xiaofang_data():
    
    for json_string in _xiaofang_json_datas:
         
        json_data = json.loads(json_string)

        if type(json_data[0]) != list:
            json_data = [json_data]
        
        magicsky_packets = oid_to_magicsky_v2(json_data)
        if len(magicsky_packets):
            print(json.dumps(magicsky_packets))
    
    
    print('')
    
    json_string = '[' + ','.join(_xiaofang_json_datas) + ']'
    
    json_data = json.loads(json_string)

    if type(json_data[0]) != list:
        json_data = [json_data]
    
    magicsky_packets = oid_to_magicsky_v2(json_data)
    if len(magicsky_packets):
        print(json.dumps(magicsky_packets))


if __name__ == '__main__':
    
    # test_project_data() 
    test_xiaofang_data()