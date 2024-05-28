"""
Aplikacja Flask do obsługi wykrywania ludzi na obrazach lokalnych i zdalnych.
"""

import json
import uuid
import cv2
import numpy as np
import pika
from flask import request, jsonify, Flask
from people_detection import detect_people


app = Flask(__name__)


@app.route('/local-image/<filename>', methods=['GET'])
def local_image(filename):
    """
    Obsługuje żądanie GET dla obrazu lokalnego i wykrywa ludzi na obrazie.

    Args:
        filename (str): Nazwa pliku obrazu w folderze obrazy znajdującym się w projekcie.

    Returns:
        jsonify: JSON z liczbą wykrytych osób lub komunikat o błędzie.
    """
    path_in = 'obrazy/' + filename
    img_format = filename.split('.')[1]
    image = cv2.imread(path_in)

    if image is None:
        return jsonify({"error": "Image not found"}), 404

    person_count = detect_people(image, img_format)
    return jsonify({"person_count": person_count})


@app.route('/remote-image', methods=['GET'])
def remote_image():
    """
    Obsługuje żądanie GET dla obrazu zdalnego i wysyła zadania do kolejki RabbitMQ.

    Returns:
        jsonify: JSON z komunikatem o wysłaniu zadania lub komunikat o błędzie.
    """
    image_url = request.args.get('url')

    if not image_url:
        return jsonify({"error": "No URL provided"}), 400

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='image_tasks')

    for _ in range(334):
        task_id = str(uuid.uuid4())
        task = {"id": task_id, "url": image_url}
        channel.basic_publish(
            exchange='',
            routing_key='image_tasks',
            body=json.dumps(task),
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
        print(f" [x] Sent new task. ID: {task['id']}")

    connection.close()
    return jsonify({"message": "Task submitted"})


@app.route('/upload-image', methods=['POST'])
def upload_image():
    """
    Obsługuje żądanie POST dla przesłanego obrazu i wykrywa ludzi na obrazie.

    Returns:
        jsonify: JSON z liczbą wykrytych osób lub komunikat o błędzie.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    img_format = file.content_type
    npimg = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    person_count = detect_people(image, img_format)
    return jsonify({"person_count": person_count})


if __name__ == '__main__':
    app.run(debug=True)
