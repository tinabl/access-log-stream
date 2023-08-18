from kafka import KafkaProducer
import json
import time
import datetime
from datetime import datetime, timedelta
import csv
import random
import pandas as pd
from random import randint
from json import dumps

if __name__ == '__main__':

    def generate_random_ip():
        return '.'.join(
            str(randint(0, 255)) for _ in range(4))




    with open('log.csv') as file:
        producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'))
        reader = list(csv.reader(file))

        while True:

            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            ip = generate_random_ip()
            e = random.choice(range(15780))
            url = reader[e][3]
            status = reader[e][4]



            producer.send('quickstart-events',
                          {'IP_address': ip, 'date_time': date_time, 'method_URL': url,
                           'resp_code': status})

            print('end')
            producer.flush()