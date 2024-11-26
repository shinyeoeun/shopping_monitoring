import requests

HEADERS = {'tracking-update-key': 'MSS-ty7Q-GJrt-SEzl'}

ENVIRONMENTS = {
    'dev': {
        'GET_TRACKING_INFO_API_URL': 'http://dev-dlvr-api-iapi.gncp-dlvr-jp.svc.ad1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://dev-dlvr-gateway.gncp-dlvr-jp.svc.ad1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    },
    'alpha': {
        'GET_TRACKING_INFO_API_URL': 'http://alpha-dlvr-api-iapi.gncp-dlvr-jp.svc.ad1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://alpha-dlvr-gateway.gncp-dlvr-jp.svc.ad1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    },
    'beta': {
        'GET_TRACKING_INFO_API_URL': 'http://beta-dlvr-api-iapi.gncp-dlvr-jp.svc.jr1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://beta-dlvr-gateway.gncp-dlvr-jp.svc.jr1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    },
    'real': {
        'GET_TRACKING_INFO_API_URL': 'http://dlvr-api-iapi.gncp-dlvr-jp.svc.jr1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://dlvr-gateway.gncp-dlvr-jp.svc.jr1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    }
}

def 배송트래킹정보_취득(tracking_no, env):
    try:
        url = f'{ENVIRONMENTS[env]["GET_TRACKING_INFO_API_URL"]}{tracking_no}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            delivery_info = data[0]
            delivery_no = delivery_info['deliveryNo']
            delivery_company_type = delivery_info['deliveryCompanyType']
            print(f'● 송장번호: {tracking_no}')
            print(f'- 배송트래킹정보취득 요청: {url} | 응답코드: {response.status_code}')
            return delivery_no, delivery_company_type
        else:
            print("처리할 데이터가 없습니다. 송장번호를 다시 확인해주세요.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"배송 정보를 가져오는 중 오류 발생: {e}")
        return None, None


def 배송상태_갱신(delivery_company_type, delivery_no, tracking_stat, tracking_no, env):
    try:
        url = f'{ENVIRONMENTS[env]["UPDATE_STATUS_API_URL"]}{delivery_company_type}/{delivery_no}/{tracking_stat}/{tracking_no}'
        response = requests.put(url, headers=HEADERS)
        response.raise_for_status()
        print(f'- 배송상태갱신 요청: {url} | 응답코드: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f"배송 상태를 업데이트하는 중 오류 발생: {e}")


if __name__ == '__main__':
    # todo 송장번호 / 배송상태 / 환경 입력필요
    tracking_nos = ['202402130001', '202402130002']
    tracking_stat = '배달완료'
    env = 'alpha'

    for tracking_no in tracking_nos:
        delivery_no, delivery_company_type = 배송트래킹정보_취득(tracking_no, env)
        if delivery_no and delivery_company_type:
            배송상태_갱신(delivery_company_type, delivery_no, tracking_stat, tracking_no, env)
