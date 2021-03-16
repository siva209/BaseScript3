import tornado.ioloop
import tornado.web

from kwikapi.tornado import RequestHandler
from kwikapi import API


# Core logic that you want to expose as a service
class Calc(object):
    def add(self, a: int = 10, b: int = 20) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b


# Standard boilerplate code to define the service. This
# code will remain more or less the same size regardless
# of how big the code/complexity of `BaseCalc` above is.

# Register BaseCalc with KwikAPI
api = API()
api.register(Calc(), 'v1')


# Passing RequestHandler to the KwikAPI
def make_app():
    return tornado.web.Application([
        (r'^/api/.*', RequestHandler, dict(api=api)),
    ])


# Starting the application
if __name__ == "__main__":
    app = make_app()
    print("hi siva")
    app.listen(8000)
    print("server not running")
    tornado.ioloop.IOLoop.current().start()
    print("kk")
