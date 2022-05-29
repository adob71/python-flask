from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    str = input("Enter an event:") or "event"
    producer.send('linux-events', bytes(str, 'ascii'))
    producer.flush()
