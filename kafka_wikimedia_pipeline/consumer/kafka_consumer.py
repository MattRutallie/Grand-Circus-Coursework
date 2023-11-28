from confluent_kafka import Consumer, KafkaError

# Configure Kafka Consumer
consumer_config = {
    'bootstrap.servers': 'kafka:9092',  # Kafka broker address
    'group.id': 'wikimedia-consumer',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(consumer_config)
consumer.subscribe(['latest_events'])

# Function to consume data from Kafka topic
def consume_data():
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        print(f"Consumed message: {msg.value().decode('utf-8')}")

# Run the consumer
if __name__ == '__main__':
    consume_data()
