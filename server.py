from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    with open("registrations.txt", "a") as f:
        f.write(f"{data['name']} - {data['time']}\n")
    return "Registration saved!", 200

if __name__ == '__main__':
    app.run(debug=True)
