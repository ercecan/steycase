# steycase
###Stey case for long term internship.

- In the first commit I have implemented a basic script calling websocket API and then
after listening it will simply print the messages.
In order to see the resulst simply install the requirements via cli with the command
below:


``` $ pip install -r requirements.txt ```

- and then run main.py using:

```$ python main.py ``` 

------------------------

- In my next commit I have used publisher/subscriber pattern with redis. On this pattern
I have used two scripts. One of them 'publisher.py' will publish messages to a stream
and the other script called 'subscriber.py' will listen to the messages.

- In order to start the scripts first install redis on your local machine
- On your cli run below command to start a local redis server

```$ redis-server```

- Install requirements

``` $ pip install -r requirements.txt ```

- Then run the following scripts

````$ python susbcriber.py````

- Then run 

```$ python publisher.py```

------------

- In my last commit I have used Rabbitmq basic queue system as it has
acknowledgement property which can prevent fatal data loss in the cases
where server may crash during transactions.

- Rabbitmq is the best option amongst the three implementations as Redis has no acknowledgement.

- In order to run this implementation you will first need to install RabbitMQ to your
local machine and run it via cli with the following  command.

````$ rabbitmq-server````

- Install requirements

``` $ pip install -r requirements.txt ```

- Then go in the directory 'rabbitmq' and run the following scripts:

````$ receive.py````

````$ send.py````
