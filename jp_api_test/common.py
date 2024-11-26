import requests as req

# py.test ./jp_api_test --reportportal

""" 
# ALPHA (nshop70)
PARTNER_API_URL = "http://alpha-jp-partner.ncpgw.navercorp.com"
CLIENT_ID = '7eqSJZU8L3sxVBrn4260aT'
CLIENT_SECRET = '$2a$04$IVQbl./HCZB15NaVI9uNme'
"""

# BETA (store33)
PARTNER_API_URL = "http://beta-jp-partner.ncpgw.navercorp.com"
CLIENT_ID = '2gXA2PIGFRfUbnfCQsHTp8'
CLIENT_SECRET = '$2a$04$ANxn7CHkr0lvWZ/sbQzbzu'

def send_request(method, url, headers, json=None, timeout=30):
    try:
        response = req.request(method, url, headers=headers, json=json, timeout=timeout)
        response.raise_for_status()
        return response
    except req.exceptions.RequestException as e:
        print(f"Error sending request: {e}")
        return None

def 최신배송방법검색(headers):
    url = f"{PARTNER_API_URL}/v2/delivery/methods/search?pageSize=1&page=1"
    return send_request("GET", url, headers)

def 배송방법등록(headers, payload):
    return req.post(PARTNER_API_URL+'/v2/delivery/methods', headers=headers, json=payload, timeout=30)

def 배송방법수정(headers, seq, payload):
    """
    seq: 배송방법 ID
    """
    return req.patch(PARTNER_API_URL+f'/v2/delivery/methods/{seq}', headers=headers, json=payload, timeout=30)

"""
def 배송방법등록(headers, payload):
    url = f"{PARTNER_API_URL}/v2/delivery/methods"
    return send_request("POST", url, headers, json=payload)


def 배송방법수정(headers, seq, payload):
    url = f"{PARTNER_API_URL}/v2/delivery/methods/{seq}"
    return send_request("PATCH", url, headers, json=payload)
"""

def 배송방법조회(headers, pageSize):
    """
    pageSize: 페이지크기
    """
    url = f"{PARTNER_API_URL}/v2/delivery/methods/search?pageSize={pageSize}&page=1"
    return send_request("GET", url, headers)

def 배송방법삭제(headers, ids):
    """
    ids: 배송방법 ID 목록
    """
    url = f"{PARTNER_API_URL}/v2/delivery/methods?ids={ids}"
    return send_request("DELETE", url, headers)

def 전체배송방법택배사서비스코드매핑조회(headers):
    url = f"{PARTNER_API_URL}/v2/delivery/mappings"
    return send_request("GET", url, headers)

def deliveryMethod_payload(serviceCode, useOkihai):
    """
    serviceCode: 배송서비스코드
    useOkihai: 오키하이 이용여부

    [배송서비스코드 목록]
    100110 야마토운수/야마토택배
    100111 야마토운수/EAZY
    100120 사가와/사가와택배
    100130 일본우편/유팩
    """
    return {
        "deliveryMethodName": "API_오키하이_등록",
        "serviceCode": f"{serviceCode}",
        "feeTable": {
            "areaType": "WIDE",
            "columnType": "COMMON",
            "feeList": [500]
        },
        "deliveryFeeCalculateMethod": "ONCE",
        "description": "오키하이 테스트용",
        "okihai": {
            "useOkihai": f"{useOkihai}"
        }
    }