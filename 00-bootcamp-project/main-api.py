import configparser
import csv

import requests


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("api_config", "host")
port = parser.get("api_config", "port")

API_URL = f"http://{host}:{port}"
DATA_FOLDER = "data"

### Events
data = "orders"
date = "2021-02-10"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/orders.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

### orders
data = "orders"
date = "2020-10-23"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE

### Orders
data = "orders"
date = "2021-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE