from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('linux-events', b'Hello, World!')
producer.send('linux-events', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()
