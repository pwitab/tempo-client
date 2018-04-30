============
tempo-client
============

A Python client to Tempo Timesheet REST API

Simple Client for interfacing to Tempo Timesheet.

We use it to pull worklogs and aggregate to our billing system, so all endpoints
are not implemented. If you want more functions we would love a pull request.

We don't use the full OAuth2 authorization, just the API token generated from within JIRA.

See `Tempo Timesheet Documentation <http://www.python.org/>`_ for more details.

Supported functions
===================

* Get all accounts
* Get account info
* Get worklogs for account


Example
=======

.. code-block:: python

    import iso8601
    from tempo_client.client import TempoClient

    client = TempoClient(access_token='xxxxxxxxx')

    from_date = iso8602.parse_date('2018-02-01')
    end_date = iso8602.parse_date('2018-02-28')

    worklogs = client.get_account_worklogs(
        account_key='ACCOUNT', start=from_date, stop=end_date)
