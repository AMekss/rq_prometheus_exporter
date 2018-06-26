from flask import Flask, make_response

api = Flask(__name__)

# Route definitions
@api.route('/healthz', methods=['GET'])
def get_healthcheck():
    return '', 200

@api.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = "prometheus metrics goes here"
    response = make_response(metrics, 200)
    response.headers['Content-Type'] = 'text/plain; version=0.0.4'
    response.headers['Cache-Control'] = 'no-cache'
    return response
