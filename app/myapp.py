from flask import Flask, jsonify, request
from prometheus_client import start_http_server, Gauge

app = Flask(__name__)

GAUGE_METRIC = Gauge('my_gauge_metric', 'Description of gauge metric')

@app.route('/')
def hello_world():
    app.logger.info('Hello World endpoint was reached')
    return jsonify(message="Hello, World!")

@app.route('/event', methods=['POST'])
def log_event():
    data = request.json
    GAUGE_METRIC.set(int(data["value"]))
    return jsonify(message="Event logged")

if __name__ == '__main__':
    start_http_server(9091)

    app.run(host='0.0.0.0', port=5000)