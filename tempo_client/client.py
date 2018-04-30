import requests


class TempoClient:

    """
    Client class containing the API to integrate with Tempo Timesheets
    """

    BASE_URL = 'https://api.tempo.io/2/'

    def __init__(self, access_token: str, timeout=10):

        self.access_token = access_token
        self.headers = self._format_headers(access_token)
        self.timeout = timeout

    def _get(self, url):
        """Method so all GET requests are done right"""

        # TODO: Add error handling for requests.

        return requests.get(url, headers=self.headers, timeout=self.timeout)

    def _parse_url(self, endpoint: str, params=None):
        _endpoint = endpoint.rstrip('/').lstrip('/')

        url = f'{self.BASE_URL}{_endpoint}'

        if params is None:
            return url

        parameters = ''
        for param, value in params.items():

            parameters += f'{param}={value}&'

        parameters = parameters.rstrip('&')

        return f'{url}?{parameters}'

    @staticmethod
    def _format_headers(access_token):

        auth = f'Bearer {access_token}'

        return {'Accept': 'application/json',
                'Authorization': auth}

    def get_accounts(self):
        """Get a list of all accounts"""

        endpoint = 'accounts'
        url = self._parse_url(endpoint)
        data = self._get(url).json()
        accounts = data.get('results')
        return accounts

    def get_account(self, key):
        """Get info on a certain account"""

        endpoint = f'accounts/{key}'
        url = self._parse_url(endpoint)
        account = self._get(url).json()
        return account

    def get_account_worklogs(self, account_key, start, stop,
                             offset=0, limit=500):
        """Get all worklogs for an account within a given period"""
        # default limit is 50 and that is not enough. Until I implement
        # a pagination function

        endpoint = f'worklogs/account/{account_key}'

        _start = start.strftime('%Y-%m-%d')
        _stop = stop.strftime('%Y-%m-%d')
        params = {
            'from': _start,
            'to': _stop,
            'offset': offset,
            'limit': limit
                  }
        url = self._parse_url(endpoint, params)
        result = self._get(url).json()
        worklogs = result.get('results')
        return worklogs



