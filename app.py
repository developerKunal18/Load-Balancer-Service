from flask import Flask, jsonify
from itertools import cycle

app = Flask(__name__)

# Backend servers
servers = [
    "Server-1",
    "Server-2",
    "Server-3"
]

# Round Robin iterator
server_pool = cycle(servers)

# Server statistics
server_requests = {
    "Server-1": 0,
    "Server-2": 0,
    "Server-3": 0
}


# ---------- Route Request ----------
@app.route("/request")
def route_request():

    server = next(server_pool)

    server_requests[server] += 1

    return jsonify({
        "message": "Request processed",
        "server": server
    })


# ---------- Server Stats ----------
@app.route("/stats")
def stats():

    return jsonify(
        server_requests
    )


# ---------- Add Server ----------
@app.route("/add/<server_name>")
def add_server(server_name):

    global server_pool

    servers.append(server_name)

    server_requests[server_name] = 0

    server_pool = cycle(servers)

    return jsonify({
        "message": f"{server_name} added"
    })


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":

    app.run(debug=True)
