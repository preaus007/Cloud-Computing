from flask import Flask

app = Flask(__name__)

@app.route("/")
def evenNumber():
    arr = []

    for i in range(1, 50):
        if i%2 == 0:
            arr.append(i)
    
    return arr

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)