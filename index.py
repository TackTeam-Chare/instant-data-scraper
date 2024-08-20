import pandas as pd
import json

# ข้อมูล JSON ที่ได้รับ
data_json = '''
[{"name":"Somtam Papaya salad, Spicy Salad by Aunt Ae","description":4.7,"location":"https:\/\/lh5.googleusercontent.com\/p\/AF1QipO2O18J3BQmzf6TZkyNBG4QfSIIoRBu_1M4djmM=w163-h92-k-no","latitude":"16.950375","longitude":"104.7253988","category":"·","service_option1":"·","service_option2":"Takeaway"},{"name":"Qhun Qhun Kitchen","description":4.5,"location":"https:\/\/lh5.googleusercontent.com\/p\/AF1QipPC9r4tx1hC9lFwHpRIcS_I9E5EYIkiritU0cU=w122-h92-k-no","latitude":"16.9350557","longitude":"104.7099568","category":"·","service_option1":"·","service_option2":"Takeaway"},...] 
'''

# โหลดข้อมูล JSON
data = json.loads(data_json)

# สร้างคำสั่ง SQL INSERT
insert_statements = []
for record in data:
    name = record.get('name', '').replace("'", "''")
    description = record.get('description', 'NULL')
    location = record.get('location', '').replace("'", "''")
    latitude = record.get('latitude', 'NULL')
    longitude = record.get('longitude', 'NULL')
    category = record.get('category', '').replace("'", "''")
    service_option1 = record.get('service_option1', '').replace("'", "''")
    service_option2 = record.get('service_option2', '').replace("'", "''")
    
    # หากค่าใดเป็น NULL ก็เปลี่ยนให้เป็น NULL ใน SQL
    description = 'NULL' if description == 'NULL' else f"'{description}'"
    latitude = 'NULL' if latitude == 'NULL' else f"'{latitude}'"
    longitude = 'NULL' if longitude == 'NULL' else f"'{longitude}'"
    
    sql = f"INSERT INTO places (name, description, location, latitude, longitude, category, service_option1, service_option2) VALUES ('{name}', {description}, '{location}', {latitude}, {longitude}, '{category}', '{service_option1}', '{service_option2}');"
    insert_statements.append(sql)

# แสดงผลคำสั่ง SQL
for stmt in insert_statements:
    print(stmt)
