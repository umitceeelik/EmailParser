from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/triggerKestra', methods=['POST'])
def trigger_kestra():
    print("aaa")
    return jsonify({"status": "success"}), 200


# @app.route('/triggerKestra', methods=['POST'])
# def trigger_kestra():
#     parsed_data = request.get_json()
#     ip_address = parsed_data["ip_address"]
    
#     print(parsed_data)
#     kestra_payload = {
#         "namespace": "test",
#         "flowId": "emailParserTest",
#         "inputs": {
#             "ip_address": ip_address
#         }
#     }

#     # kestra_api_url = "http://89.106.27.76:20080/api/v1/executions/create"
#     kestra_api_url = "http://89.106.27.76:20080/api/v1/executions/trigger/test/emailParserTest"
#     # headers = {"Content-Type": "application/json"}

#     try:
#         response = requests.post(kestra_api_url, json=kestra_payload)
#         # Only attempt to parse JSON if response status is 200 OK
#         if response.status_code == 200:
#             return jsonify({"status": "workflow triggered", "kestra_response": response.json()}), 200
#         else:
#             # Return the raw response content if not 200 OK
#             return jsonify({"status": "error", "message": response.text}), response.status_code
#     except requests.RequestException as e:
#         return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
