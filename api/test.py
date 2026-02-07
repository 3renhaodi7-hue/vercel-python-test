import json

def main(request, response):
    data = {"status": "ok", "message": "Hello from a brand new project!"}
    response.set_header('Content-Type', 'application/json')
    response.set_body(json.dumps(data))
    return response
