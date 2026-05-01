import functions_framework
from flask import jsonify

@functions_framework.http
def hello_json(request):
    # Mengambil parameter 'name' dari query string atau body JSON
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    # Mengembalikan respons dalam format JSON
    return jsonify({"message": f"Hello, {name}!"})