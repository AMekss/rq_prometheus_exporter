from flask import Flask, make_response
import stats, template

api = Flask(__name__)

# Route definitions
@api.route('/healthz', methods=['GET'])
def get_healthcheck():
    return '', 200

@api.route('/metrics', methods=['GET'])
def get_metrics():
    response = make_response(template.render(*stats.scrape()), 200)
    response.headers['Content-Type'] = 'text/plain; version=0.0.4'
    response.headers['Cache-Control'] = 'no-cache'
    return response
