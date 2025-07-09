from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    """Return the current UTC time."""
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    return jsonify(time=now)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))
