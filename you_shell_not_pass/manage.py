from service_api.app import app

from sanic.server import HttpProtocol


def runserver(host, port):

    class CGDPHttpProtocol(HttpProtocol):

        def __init__(self, *args, **kwargs):
            if "request_timeout" in kwargs:
                kwargs.pop("request_timeout")
            super().__init__(*args, request_timeout=300, **kwargs)

    app.run(host=host, port=port, protocol=CGDPHttpProtocol)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003, debug=True)
