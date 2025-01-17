import json

json_str = '''
[{"Basic ID": {"protocol_version": "F3411.22", "id_type": "Serial Number (ANSI/CTA-2063-A)", "ua_type": "Aeroplane", "id": "2051FEABPT0000000208"}}, {"System Message": {"operator_location_type": "Takeoff", "classification_type": "Undeclared", "latitude": 0.0, "longitude": 0.0, "area_count": 1, "area_radius": 0, "area_ceiling": "0.0 m", "area_floor": "0.0 m", "ua_classification_category_type": "Undefined", "ua_classification_category_class": "Class 1", "geodetic_altitude": "0.0 m", "timestamp": "1999-12-01 00:00 UTC", "timestamp_raw": -602294400, "protocol_version": "F3411.22"}}]
'''

json_obj = json.loads(json_str)

print(json_obj)



