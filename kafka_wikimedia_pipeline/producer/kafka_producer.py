from confluent_kafka import Producer
import json
import requests

# Configure Kafka Producer
producer_config = {
    'bootstrap.servers': '9092',  # Kafka broker address
    'client.id': 'wikimedia-producer',
}

producer = Producer(producer_config)

# Function to fetch data from Wikimedia stream
def fetch_wikimedia_data():
    response = requests.get('https://stream.wikimedia.org/v2/stream/recentchange')
    for line in response.iter_lines():
        if line:
            yield json.loads(line)

# Function to produce data to Kafka topic
def produce_data():
    for event in fetch_wikimedia_data():
        producer.produce('latest_events', key=event['id'], value=json.dumps(event))
        producer.poll(0)

# Run the producer
if __name__ == '__main__':
    produce_data()
