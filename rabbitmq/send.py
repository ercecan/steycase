import pika, websocket


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='stream', durable=True)


def main():
    levels = '20'
    symbol = 'btcusdt'
    endpoint = f'wss://stream.binance.com:9443/ws/{symbol}@depth{levels}'

    ws = websocket.WebSocketApp(endpoint,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()


def on_message(ws, message):
    msg = message
    channel.basic_publish(exchange='',
                          routing_key='stream',
                          body=str(msg),
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


if __name__ == '__main__':
    main()