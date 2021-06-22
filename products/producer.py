import pika

params = pika.URLParameters('amqps://')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    channel.basic_publish(exchange='', routing_key='admin', body='test')


