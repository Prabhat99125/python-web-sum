from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.json
    if 'number1' in data and 'number2' in data:
        try:
            num1 = float(data['number1'])
            num2 = float(data['number2'])
            result = num1 + num2
            return jsonify({'result': result}), 200
        except ValueError:
            return jsonify({'error': 'Invalid input, please provide valid numbers.'}), 400
    else:
        return jsonify({'error': 'Missing parameters. Please provide both numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
