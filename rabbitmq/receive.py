import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='stream', durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        #ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='stream', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()