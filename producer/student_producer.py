from kafka import KafkaProducer
import json
import csv
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('online_course_engagement_data.csv', 'r') as file:
    reader = csv.DictReader(file)   # NOW headers exist ✅

    for row in reader:
        # Add event time
        row["event_time"] = datetime.utcnow().isoformat()

        producer.send("student_activity", value=row)
        print("Sent:", row)

        time.sleep(1)

producer.flush()
producer.close()

