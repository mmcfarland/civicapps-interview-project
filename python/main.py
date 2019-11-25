from flask import Flask, request, Response

app = Flask(__name__)

DATA_STORE = {}


@app.route("/", methods=["GET"])
def home():
    """Serve up a welcome page at the root URL."""
    return Response("Hello, world. Looks like everything is working. \
                     You got this!", mimetype="text/plain")


@app.route("/set/")
def set_value():
    """Save key and value pairs from the query string.

       Try: http://localhost:8080/set?key=value
    """
    # Loop through each key in the query string and add it to our dictionary
    for key, value in request.args.items():
        DATA_STORE[key] = value

        # Log the values to the debug console
        print(f"recieved {key} with value of {value}")

    # Let the client know the operation was successful
    return Response(f"saved {len(request.args)} value(s)", mimetype="text/plain")


@app.route("/keys/")
def get_keys():
    """Return all saved keys to the client.

       Try: http://localhost:8080/keys/
    """
    if DATA_STORE:
        all_values = []
        for key, value in DATA_STORE.items():
            all_values.append(f"{key}={value}")
        return Response(("\n").join(all_values), mimetype="text/plain")

    return Response("No keys have been set.", mimetype="text/plain")
