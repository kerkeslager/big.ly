import urllib.parse

import flask
import requests

app = flask.Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/js/<path:path>')
def send_js(path, methods=['GET']):
    return flask.send_from_directory('static/js', path)

@app.route('/css/<path:path>', methods=['GET'])
def send_css(path):
    return flask.send_from_directory('static/css', path)

def is_absolute(link):
    return bool(urllib.parse.urlparse(link).netloc)

def make_absolute(referrer, link):
    if is_absolute(link):
        return link

    base = '{scheme}://{netloc}'.format(**urllib.parse.urlparse(referrer)._asdict())
    return urllib.parse.urljoin(base, link)

def clean_link(link):
    # TODO Strip UTM parameters
    # TODO Strip site-specific stuff (for example, GET parameters on Amazon product pages can mostly be stripped)
    return link

MAX_REDIRECTS = 16

@app.route('/api/v1/expand-link', methods=['GET'])
def expand_link():
    link = clean_link(flask.request.args.get('link'))

    history = []
    response = requests.get(link, allow_redirects=False)

    while response.status_code in [301, 302, 308]:
        history.append(link)

        if len(history) == MAX_REDIRECTS:
            response = flask.jsonify({
                'message': 'Too many redirects',
                'history': history,
            })
            response.status_code = 404
            return response

        link = response.headers.get('Location')

        # TODO Handle if link is None or malformed

        link = make_absolute(history[-1], link)
        link = clean_link(link)

        if link in history:
            response = flask.jsonify({
                'message': 'Circular redirect detected',
                'history': history,
                'result': link,
            })
            response.status_code = 404
            return response

        response = requests.get(link, allow_redirects=False)

    return flask.jsonify({
        'result': link,
        'history': history,
    })

if __name__ == '__main__':
    app.run()
