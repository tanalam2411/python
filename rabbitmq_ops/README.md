

1 ) RabbitMQ - Message broker

   ![rmq1](https://github.com/tanalam2411/python/blob/master/static/rabbitmq/rmq1.png)

2 ) 
- P - publisher, C - consumer
  - Once the P publishes the message(say m1)  it gets stored in the queue and notifies the P back.
  - If P doesn't recevies the nofification back, it retires to publish message(m1) back again which will make duplicate entries of same message within the queue.

 - Redilivery
   - At consumer end once consumer reveives message from queue it acks back to the broker and message gets dequeued from the queue.
   - But if consumer fails to ack back then message broker will send the message again until it reveives ack back from consumer.
   - Message broker sends a flag on resending of the message. But the consumer should be able to handle duplicate messages.
   
3 ) Horizontal scaling - 

   ![rmq1](https://github.com/tanalam2411/python/blob/master/static/rabbitmq/rmq2.png)
