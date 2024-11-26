import common


def test_전체배송방법택배사서비스코드매핑조회_오키하이사용여부N_성공(rp_logger, headers):
    """
     ● case: 오키하이사용여부 N (=100110) 인 서비스코드 조회
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. 오키하이 사용 설정 표시 여부(isOkihaiAvailable) = false
    """
    res = common.전체배송방법택배사서비스코드매핑조회(headers)

    if res.status_code == 200:
        for dict in res.json():
            serviceCode = dict['serviceCode']
            if serviceCode == '100110':
                rp_logger.debug('〇 객체조회: '+str(dict))
                isOkihaiAvailable = dict['isOkihaiAvailable']
                assert isOkihaiAvailable is False
                rp_logger.info('● 오키하이사용여부N 배송방법(100110): isOkihaiAvailable = false')


def test_전체배송방법택배사서비스코드매핑조회_오키하이사용여부Y_성공(rp_logger, headers):
    """
     ● case: 오키하이사용여부 Y (=100210) 인 서비스코드 조회
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. 오키하이 사용 설정 표시 여부(isOkihaiAvailable) = true
    """
    res = common.전체배송방법택배사서비스코드매핑조회(headers)

    if res.status_code == 200:
        for dict in res.json():
            serviceCode = dict['serviceCode']
            if serviceCode == '100210':
                rp_logger.debug('〇 객체조회: '+str(dict))
                isOkihaiAvailable = dict['isOkihaiAvailable']
                assert isOkihaiAvailable is True
                rp_logger.info('● 오키하이사용여부N 배송방법(100210): isOkihaiAvailable = true')


def test_전체배송방법택배사서비스코드매핑조회_오키하이사용여부선택불가N_성공(rp_logger, headers):
    """
     ● case: 오키하이사용여부 선택불가 N (=100310) 인 서비스코드 조회
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. 오키하이 사용 설정 비활성화 여부(disableOkihaiCheckBox) = false
    """
    res = common.전체배송방법택배사서비스코드매핑조회(headers)

    if res.status_code == 200:
        for dict in res.json():
            serviceCode = dict['serviceCode']
            if serviceCode == '100310':
                rp_logger.debug('〇 객체조회: '+str(dict))
                disableOkihaiCheckBox = dict['disableOkihaiCheckBox']
                assert disableOkihaiCheckBox is False
                rp_logger.info('● 오키하이사용여부N 배송방법(100310): disableOkihaiCheckBox = true')


def test_전체배송방법택배사서비스코드매핑조회_오키하이사용여부선택불가Y_성공(rp_logger, headers):
    """
     ● case: 오키하이사용여부 선택불가 N (=100111) 인 서비스코드 조회
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. 오키하이 사용 설정 비활성화 여부(disableOkihaiCheckBox) = true
    """
    res = common.전체배송방법택배사서비스코드매핑조회(headers)

    if res.status_code == 200:
        for dict in res.json():
            serviceCode = dict['serviceCode']
            if serviceCode == '100111':
                rp_logger.debug('〇 객체조회: '+str(dict))
                disableOkihaiCheckBox = dict['disableOkihaiCheckBox']
                assert disableOkihaiCheckBox is True
                rp_logger.info('● 오키하이사용여부Y 배송방법(100111): disableOkihaiCheckBox = false')


def test_전체배송방법택배사서비스코드매핑조회_오키하이선택시도착시간대선택불가N_성공(rp_logger, headers):
    """
     ● case: 오키하이선택시 도착시간대 선택불가 N (=100111) 인 서비스코드 조회
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. 주문 시 오키하이 도착 시간대 선택 불가 여부(disableArriveConfigCheckBoxWhenOkihaiForOrder) = false
    """
    res = common.전체배송방법택배사서비스코드매핑조회(headers)

    if res.status_code == 200:
        for dict in res.json():
            serviceCode = dict['serviceCode']
            if serviceCode == '100111':
                rp_logger.debug('〇 객체조회: '+str(dict))
                disableArriveConfigCheckBoxWhenOkihaiForOrder = dict['disableArriveConfigCheckBoxWhenOkihaiForOrder']
                assert disableArriveConfigCheckBoxWhenOkihaiForOrder is False
                rp_logger.info('● 오키하이사용여부N 배송방법(100111): disableArriveConfigCheckBoxWhenOkihaiForOrder = false')



def test_전체배송방법택배사서비스코드매핑조회_오키하이선택시도착시간대선택불가Y_성공(rp_logger, headers):
    """
     ● case: 오키하이선택시 도착시간대 선택불가 Y (=100310) 인 서비스코드 조회
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. 주문 시 오키하이 도착 시간대 선택 불가 여부(disableArriveConfigCheckBoxWhenOkihaiForOrder) = true
    """
    res = common.전체배송방법택배사서비스코드매핑조회(headers)

    if res.status_code == 200:
        for dict in res.json():
            serviceCode = dict['serviceCode']
            if serviceCode == '100111':
                rp_logger.debug('〇 객체조회: '+str(dict))
                disableArriveConfigCheckBoxWhenOkihaiForOrder = dict['disableArriveConfigCheckBoxWhenOkihaiForOrder']
                assert disableArriveConfigCheckBoxWhenOkihaiForOrder is True
                rp_logger.info('● 오키하이사용여부N 배송방법(100111): disableArriveConfigCheckBoxWhenOkihaiForOrder = true')