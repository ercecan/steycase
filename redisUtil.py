import redis


class RedisUtil():

    def __init__(self):
        self.subscriber = redis.Redis(host='localhost', port=6379, db=0)
        self.publisher = redis.Redis(host='localhost', port=6379, db=0)  # connect with redis server as publisher

    def getsub(self):
        return self.subscriber.pubsub()

    def getpub(self):
        return self.publisher

    #sub.subscribe('stream')





    #publisher.publish('classical_music', 'Alice Music')