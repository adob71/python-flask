from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    event = input("Enter an event:") or "event"
    producer.send('linux-events', bytes(event, 'ascii'))
    producer.flush()
