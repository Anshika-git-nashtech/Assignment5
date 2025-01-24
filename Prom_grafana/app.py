from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

REQUESTS = Counter('http_requests_total', 'Total HTTP requests')

@app.route('/')
def hello():
    REQUESTS.inc() 
    return "This is Anshika Varshney."

@app.route('/metrics')
def metrics():
    from prometheus_client import generate_latest
    return generate_latest()

if __name__ == "__main__":
    start_http_server(8000)  
    app.run(host='0.0.0.0', port=5000) 

