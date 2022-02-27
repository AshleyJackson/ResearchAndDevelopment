from flask import Flask, Response, send_from_directory, request, redirect
from gui import nav

globalnav = nav.nav
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return Response(
        globalnav,
        mimetype='text/html'
    )


# Public files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    port = 6100
    domain = "http://localhost:" + str(port)
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
