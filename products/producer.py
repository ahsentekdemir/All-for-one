import pika

params = pika.URLParameters('amqps://ptavgioq:zqGoD0Tacrty3m283aKTI6nT21pmm3-W@roedeer.rmq.cloudamqp.com/ptavgioq')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='testdata')


