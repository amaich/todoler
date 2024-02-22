import logging
from datetime import datetime


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response

        logging.basicConfig(level=logging.INFO, filename="todo_log.log")

    def __call__(self, req):
        logging.info(f'{datetime.now()} ===> Request: {req.method} {req.get_host()}{req.path}')
        logging.debug(f'{datetime.now()} Headers: {req.headers}')
        logging.debug(f'{datetime.now()} Content params: {req.content_params}')
        logging.debug(f'{datetime.now()} Body: {req.body}')

        resp = self.get_response(req)

        logging.info(f'{datetime.now()} Status code: {resp.status_code}')

        return resp
