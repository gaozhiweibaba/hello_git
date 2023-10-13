from kafka import KafkaProducer
from time import sleep


def start_producer():
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    for i in range(0, 100000):
        msg = 'msg is ' + str(i)
        producer.send('test-01', msg.encode('utf-8'))
        sleep(1)


if __name__ == '__main__':
    start_producer()