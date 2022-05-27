from kafka import KafkaConsumer
consumer = KafkaConsumer('linux-events')
for message in consumer:
    print (message)
