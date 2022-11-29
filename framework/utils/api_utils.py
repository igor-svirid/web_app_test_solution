import requests
from websocket import create_connection as websocket_connect

from framework.logger.logger import Logger


def log_request(func):
    """
    Decorator to log api requests
    :arg:
     - func: function to decorate. Should return requests.Response
    """
    def wrapper(url, **params):
        Logger.info(f'Sending {func.__name__} request to {url} url with {params} parameters')

        response = func(url, **params)

        headers = response.headers['Content-Type']
        if 'json' in headers:
            response_content = response.json()
        elif 'text' in headers:
            response_content = response.text
        else:
            response_content = response.content

        Logger.info(f'Received response with [{response.status_code}] status code and [{response_content}] content')
        return response
    return wrapper


class ApiRequests:

    @staticmethod
    @log_request
    def get(url: str, **params) -> requests.Response:
        """
        Sending get request
        :args:
         - url: string representation of request url
         - params: any additional parameters for the request
        :returns: requests.Response
        """
        return requests.get(url, params=params)

    @staticmethod
    @log_request
    def patch(url: str, **params) -> requests.Response:
        """
        Sending patch request
        :args:
         - url: string representation of request url
         - params: any additional parameters for the request
        :returns: requests.Response
        """
        return requests.patch(url, params=params)

    @staticmethod
    def get_websocket_message_with_text(ws_url: str, text: str, max_retries=5) -> str:
        """
        Establish connection with websocket and getting messages till the message not contains required text.
        :args:
         - ws_url: string representation of request websocket url
         - text: required text to be in received message
        :optional arg:
         - max_retries: int -> max number of message requests
        :returns: string interpretation of websocket message with specified text
        :raises: RuntimeError if max number of retries exceeded exception will be raised
        """
        Logger.info(f'Getting websocket message from [{ws_url}] with [{text}] text')
        connection = websocket_connect(ws_url)
        while max_retries:
            message_to_return = connection.recv()
            if text in message_to_return:
                connection.close()
                Logger.info(f'Received message is [{message_to_return}]')
                return message_to_return
            max_retries -= 1
        raise RuntimeError(f'Max number of retries exceeded. Message with [{text}] was not received.')
