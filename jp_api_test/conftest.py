import pytest
from reportportal_client import RPLogger
import logging
import requests as req
import bcrypt
import pybase64
import time
import urllib.request
import urllib.parse
import common


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.fixture(scope="session")
def headers():
    token = get_token(client_id=common.CLIENT_ID, client_secret=common.CLIENT_SECRET)
    headers = {'Authorization': token}
    return headers


def get_token(client_id, client_secret, type_="SELF") -> str:
    timestamp = str(int((time.time()-3) * 1000))
    pwd = f'{client_id}_{timestamp}'
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), client_secret.encode('utf-8'))
    client_secret_sign = pybase64.standard_b64encode(hashed).decode('utf-8')
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data_ = {
        "client_id": client_id,
        "timestamp": timestamp,
        "client_secret_sign": client_secret_sign,
        "grant_type": "client_credentials",
        "type": type_
    }
    query = urllib.parse.urlencode(data_)
    url = common.PARTNER_API_URL + '/v2/oauth2/token?' + query
    res = req.post(url=url, headers=headers)
    res_data = res.json()
    token = res_data['access_token']
    return token

