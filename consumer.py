import pika

params = pika.URLParameters('amqps://ptavgioq:zqGoD0Tacrty3m283aKTI6nT21pmm3-W@roedeer.rmq.cloudamqp.com/ptavgioq')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, props, body):
    print('-- Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)
print('-- Started Consuming.')
channel.start_consuming()
channel.close()