from flask import *

app = Flask(__name__)

valid_clients = {'pw': 'user'}

@app.route('/', methods=['POST'])
def update():
    ip = request.headers.get('x-forwarded-for')
    if not ip:
        abort(400, 'missing IP')
    key = request.form.get('key')
    if key not in valid_clients:
        abort(401, 'nope')
    host = valid_clients[key]
    return jsonify({
        'host': host,
        'ip': ip,
        'changed': False,
    })
