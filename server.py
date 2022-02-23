# encoding: utf-8

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def registry_service(request):
    return Response('🙇‍♀️ Sorry, this is not the registry service')


def main():
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(registry_service, route_name='home')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()


if __name__ == '__main__':
    main()
