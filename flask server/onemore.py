from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/receive_json', methods=['POST'])
def receive_json():
    try:
        # Get JSON data from the incoming request
        json_data = request.get_json()

        # Assuming the JSON data contains a key called 'message'
        message = json_data.get('message', 'No message found')

        return jsonify({'received_message': message})

    except Exception as e:
        return jsonify({'error': str(e)})



    


    
@app.route('/submit',methods=['GET','POST'])
def sub():
    if request.method=="POST":
        data=request.json
        up={"name":18,"age":88}
        data.update(up)
        return jsonify(data)
    else:
        return jsonify({"message":"get req ask"})

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)