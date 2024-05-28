"""
Konsument RabbitMQ do przetwarzania zadań wykrywania ludzi na obrazach zdalnych.
"""

import pika
import requests
import cv2
import numpy as np
import json
from people_detection import detect_people


def callback(ch, method, properties, body):
    """
    Funkcja zwrotna obsługująca wiadomości z kolejki RabbitMQ.

    Args:
        ch: Kanał AMQP.
        method: Metoda dostarczenia wiadomości.
        properties: Właściwości wiadomości.
        body (bytes): Treść wiadomości zawierająca zadanie w formacie JSON.

    """
    task = json.loads(body)
    task_id = task['id']
    image_url = task['url']

    response = requests.get(image_url)

    if response.status_code != 200:
        print(f"Failed to fetch image from URL {image_url}")
        ch.basic_reject(delivery_tag=method.delivery_tag)
        return

    img_format = response.headers['Content-Type'].split('/')[1]
    image = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    person_count = detect_people(image, img_format, task_id)
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print(f"Processed {task_id}, detected {person_count} people.")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='image_tasks')

channel.basic_consume(queue='image_tasks', on_message_callback=callback, auto_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
