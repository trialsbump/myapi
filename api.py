from flask import Flask, request, jsonify
from bardapi import Bard

app = Flask(__name__)
token = 'Wwi9_Y8YAr5gaQwfpxwYeGWsObezjbZ5C-Gpv5Boe5kVRuORSPa0Szf-KHD5Ke5FIeVsfw.'  # Aquí debes reemplazar 'xxxxxxx' con el valor real de tu __Secure-1PSID
bard = Bard(token=token)

@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        query = data.get('input')
        response = bard.get_answer(query)
        content = response['content']
        return jsonify({'response': content})

    elif request.method == 'GET':
        return 'API is running'

if __name__ == '__main__':
    app.run()
