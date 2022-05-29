from kafka import KafkaConsumer
consumer = KafkaConsumer('linux-events')
for message in consumer:
    print(str(message.value, 'ascii'))

