from flask import Flask, request, abort

app = Flask(__name__)

counter = 0

@app.route("/model", methods=['POST'])
def route_model():
    set_counter()

    r = request.get_json()
    if r:
        # Json POST
        method = r['method'] if 'method' in r else ''
        text = r['text'] if 'text' in r else ''
    else:
        # Form POST
        method = request.form['method'] if 'method' in request.form else ''
        text = request.form['text'] if 'text' in request.form else ''

    methods_dict = {
        'upper': set_upper, 
        'lower': set_lower, 
        'swapcase': set_swapcase
    }

    if method not in methods_dict:
    	abort(404)

    return methods_dict[method](text)


@app.route("/stat", methods=['GET'])
def route_stat():
    global counter
    return str(counter)


def set_counter():
    global counter
    counter += 1


def set_upper(s):
    return s.upper()


def set_lower(s):
    return s.lower()


def set_swapcase(s):
    return s.swapcase()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
