import pika, json

params = pika.URLParameters('amqps://ptavgioq:zqGoD0Tacrty3m283aKTI6nT21pmm3-W@roedeer.rmq.cloudamqp.com/ptavgioq')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    
    channel.basic_publish(exchange='', body=json.dumps(body), routing_key='main', body='testdata')


