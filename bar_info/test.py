import json

with open('bar_info1.json', 'r', encoding='cp1251') as f:
    bar = json.load(f)
    for k in bar:
        print(
            k['Name'],
            k['Longitude_WGS84'],
            k['Latitude_WGS84'],
            k['Address'],
            k['District'],
            k['AdmArea'],
            k['PublicPhone'][0]['PublicPhone']
        )



