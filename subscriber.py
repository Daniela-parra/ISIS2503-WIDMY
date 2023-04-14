import json
import pika
from sys import path
from os import environ
import django

rabbit_host = '10.128.0.5'
rabbit_user = 'perzi'
rabbit_password = 'r'
exchange = 'monitoring_measurements'
topics = ['Medery.#.Glucosa', 'Medery.#.Peso', 'Medery.#.Temperatura']


path.append('monitoring/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')
django.setup()

from measurements.logic.logic_measurement import create_measurement_object
from measurements.services.services_measurements import check_alarm, check_alarm_Peso, check_alarm_Temperatura
from variables.services.services_variables import get_variable

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting measurements. To exit press CTRL+C')


def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    topic = method.routing_key.split('.')
    variable = get_variable(topic[2])
    create_measurement_object(
        variable, payload['value'], payload['unit'], topic[0] + topic[1])
    if variable.name == 'Glucosa':
        check_alarm(payload['value'])
    elif variable.name == 'Peso':
        check_alarm_Peso(payload['value'])
        print("Peso: %r" % (str(payload)))
    elif variable.name == 'Temperatura':
        check_alarm_Temperatura(payload['value'])
        print("Temperatura: %r" % (str(payload)))
    
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
