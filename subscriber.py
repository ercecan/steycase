from redisUtil import RedisUtil


redisObj = RedisUtil()
sub = redisObj.getsub()
sub.subscribe('stream')


def main():
    while True:
        message = sub.get_message()
        if message:
            msg = str(str(message['data']))
            print(msg)


if __name__ == '__main__':
    main()