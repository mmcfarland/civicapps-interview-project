from flask import (Flask, request, jsonify, Response)

app = Flask(__name__)

DATA_STORE = {}

"""
Serve up a welcome page at the root url
"""
@app.route('/', methods=['GET'])
def homepage():

    return Response('Hello, world. Looks like everything is working. \
                     You got this!')


"""
Save key and value pairs from the query string
   http://localhost:8080/set?key=value
"""
@app.route('/set/')
def set():
    # Loop through each key in the query string and add it to our dictionary
    for key, value in request.args.items():
        DATA_STORE[key] = value

        # Log the values to the debug console
        print(f'recieved {key} with value of {value}')

    # Let the client know the operation was successful
    return Response(f'saved {len(request.args)} value(s)')


"""
Return all saved keys to the client
"""
@app.route('/keys/')
def keys():
    if len(DATA_STORE) > 0:
        all_values = [f'{key}={value}' for key, value in DATA_STORE.items()]

        return Response((', ').join(all_values))
    else:
        return Response('No keys have been set.')


# Set up the server and serve content at http://localhost:8080
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)
