import common



def test_배송방법등록_okihai_비필수_빈칸_성공(rp_logger, headers):
    """
     ● case: 배송방법등록시 okihai 항목 비필수 처리되는지 여부 확인
     ● step: okihai 항목 없이 요청
     ● result:
        &nbsp;  1. 201
        &nbsp;  2. useOkihai 디폴트값(false)으로 등록됨
    """
    payload = {
        "deliveryMethodName": "API_오키하이_등록",
        "serviceCode": "100210",
        "feeTable": {
            "areaType": "WIDE",
            "columnType": "COMMON",
            "feeList": [500]
        },
        "deliveryFeeCalculateMethod": "ONCE",
        "description": "오키하이 테스트용",

        "okihai": {
            "useOkihai": ""
        }
    }
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))
    assert res.status_code == 201
    rp_logger.info('● status code 일치: '+str(res.status_code))

    serchDeliveryMethod = common.최신배송방법검색(headers)
    for res_body in serchDeliveryMethod.json()['result']:
        useOkihai = res_body['useOkihai']
    assert useOkihai == False
    rp_logger.info('● useOkihai 디폴트값(false)으로 등록성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')


def test_배송방법등록_okihai_비필수_필드없음_성공(rp_logger, headers):
    """
     ● case: 배송방법등록시 okihai 항목 비필수 처리되는지 여부 확인
     ● step: okihai 항목 없이 요청

     ● result:
        &nbsp;  1. 201
        &nbsp;  2. useOkihai 디폴트값(false)으로 등록됨
    """
    payload = {
        "deliveryMethodName": "API_오키하이_등록",
        "serviceCode": "100210",
        "feeTable": {
            "areaType": "WIDE",
            "columnType": "COMMON",
            "feeList": [500]
        },
        "deliveryFeeCalculateMethod": "ONCE",
        "description": "오키하이 테스트용",
        "okihai": {}
    }
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))
    assert res.status_code == 201
    rp_logger.info('● status code 일치: '+str(res.status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) is not 0:
            assert useOkihai is False
    rp_logger.info('● useOkihai 디폴트값(false)으로 등록성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')



def test_배송방법등록_okihai_잘못된데이터타입_실패(rp_logger, headers):
    """
    ● case: 배송방법등록 okihai항목에 잘못된데이터타입 입력한 경우
    ● step:
        &nbsp;  1. useOkihai 항목 boolean 의외 데이터로 등록
    ● result:
        &nbsp;  1. 400
        &nbsp;  2. message: 입력된 정보가 올바르지 않습니다 (入力された情報が正しくありません。)
    """
    payload = common.deliveryMethod_payload(100210, "TEST")
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 400
    rp_logger.info('● status code 일치: '+str(res.status_code))
    message = res.json()['message']
    assert message == "入力された情報が正しくありません。"
    rp_logger.info('● message 일치: '+message)


def test_배송방법등록_오키하이등록불가Y_true_실패(rp_logger, headers):
    """
     ● case: 오키하이등록불가 배송서비스를 오키하이설정=Y로 배송방법등록하여 실패할 경우
     ● step: 오키하이등록불가 배송서비스(서비스코드: 100110) & useOkihai=true 로 배송방법 등록
     ● result:
        &nbsp;  1. 400
        &nbsp;  2. message: 오키하이를 지정할 수 없는 배송서비스코드 입니다 (置き配を指定できない配送サービスコードです。)
    """
    payload = common.deliveryMethod_payload(100110, True)
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 400
    rp_logger.info('● status code 일치: '+str(res.status_code))

    message = res.json()['message']
    assert message == "置き配を指定できない配送サービスコードです。"
    rp_logger.info('● message 일치: '+message)



def test_배송방법등록_오키하이사용여부선택불가Y_true_성공(rp_logger, headers):
    """
     ● case: 오키하이등록불가Y 배송서비스를 오키하이설정=true로 배송방법등록 한 경우
     ● step: 오키하이등록불가Y 배송서비스(서비스코드: 100110) & useOkihai=true로 배송방법 등록
     ● result:
        &nbsp;  1. 201
        &nbsp;  2. useOkihai 디폴트값(false)으로 등록됨
    """
    payload = common.deliveryMethod_payload(100111, True)
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 201
    rp_logger.info('● status code 일치: '+str(res.status_code))
    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))

    res = common.최신배송방법검색(headers)
    for data in res.json()['result']:
        useOkihai = data['useOkihai']
    assert useOkihai == True
    rp_logger.info('● useOkihai 디폴트값(false)으로 등록성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')




def test_배송방법등록_오키하이사용여부선택불가Y_false_실패(rp_logger, headers):
    """
     ● case: 오키하이등록불가Y 배송서비스를 오키하이설정=false로 배송방법등록 한 경우
     ● step: 오키하이등록불가Y 배송서비스(서비스코드: 100110) & useOkihai=false로 배송방법 등록
     ● result:
        &nbsp;  1. 400
        &nbsp;  2. message: 오키하이로 필수설정해야하는 배송서비스코드 입니다 (置き配で必須設定をしていただく配送サービスコードです。)
    """
    payload = common.deliveryMethod_payload(100111, False)
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 400
    rp_logger.info('● status code 일치: '+str(res.status_code))

    message = res.json()['message']
    assert message == "置き配で必須設定をしていただく配送サービスコードです。"
    rp_logger.info('● message 일치: '+message)


def test_배송방법등록_오키하이사용여부선택불가Y_필드미지정_성공(rp_logger, headers):
    """
     ● case: 오키하이등록불가Y 배송서비스를 오키하이설정 값 미지정상태로 배송방법등록 한 경우
     ● step: 오키하이등록불가Y 배송서비스(서비스코드: 100110) & useOkihai 항목 없이 배송방법 등록
     ● result:
        &nbsp;  1. 201
        &nbsp;  2. useOkihai 디폴트값(false)으로 등록됨
    """
    payload = {
        "deliveryMethodName": "API_오키하이_등록",
        "serviceCode": "100210",
        "feeTable": {
            "areaType": "WIDE",
            "columnType": "COMMON",
            "feeList": [500]
        },
        "deliveryFeeCalculateMethod": "ONCE",
        "description": "오키하이 테스트용",
        "okihai": {}
    }
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))
    assert res.status_code == 201
    rp_logger.info('● status code 일치: '+str(res.status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) is not 0:
            assert useOkihai is False
    rp_logger.info('● useOkihai 디폴트값(false)으로 등록성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')



def test_배송방법등록_오키하이선택시도착시간대선택불가Y_useOkihai_true_성공(rp_logger, headers):
    """
     ● case: 오키하이등록불가 배송서비스를 오키하이설정=Y로 배송방법등록하여 실패할 경우
     ● step: 오키하이등록불가 배송서비스(서비스코드: 100310) & useOkihai=true 로 배송방법 등록
     ● result:
        &nbsp;  1. 201
        &nbsp;  2. 등록한 정보 일치확인
    """
    payload = common.deliveryMethod_payload(100310, True)
    res = common.배송방법등록(headers, payload)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 201
    rp_logger.info('● status code 일치: '+str(res.status_code))

    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))

    res = common.최신배송방법검색(headers)
    rp_logger.debug('〇 response: '+res.text)
    for body in res.json()['result']:
        serviceCode = body['serviceCode']
    assert serviceCode == payload["serviceCode"]
    rp_logger.info('● 등록한 정보 일치: '+serviceCode)

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')

