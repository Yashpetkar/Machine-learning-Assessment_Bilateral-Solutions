def aggregate_weather_data(records):
    city_data = {}
    
    for record in records:
        city = record['city']
        if city not in city_data:
            city_data[city] = {'temperature_sum': 0, 'humidity_sum': 0, 'temp_count': 0, 'humidity_count': 0}
        
        if 'temperature' in record:
            city_data[city]['temperature_sum'] += record['temperature']
            city_data[city]['temp_count'] += 1
        
        if 'humidity' in record:
            city_data[city]['humidity_sum'] += record['humidity']
            city_data[city]['humidity_count'] += 1
    
    for city, data in city_data.items():
        data['average_temperature'] = data['temperature_sum'] / data['temp_count'] if data['temp_count'] > 0 else None
        data['average_humidity'] = data['humidity_sum'] / data['humidity_count'] if data['humidity_count'] > 0 else None
    
    return city_data

records = [
    {'city': 'New York', 'temperature': 22, 'humidity': 55},
    {'city': 'New York', 'temperature': 25},
    {'city': 'Los Angeles', 'temperature': 30, 'humidity': 60},
    {'city': 'Los Angeles', 'humidity': 58},
    {'city': 'Chicago', 'humidity': 65}
]

print(aggregate_weather_data(records))
