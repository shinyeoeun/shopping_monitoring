import common


def test_배송방법수정_okihai_비필수_빈칸_성공(rp_logger, headers):
    """
     ● case: okihai 항목 빈칸 입력하여 수정요청
     ● step:
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. useOkihai="" 로 수정요청
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. useOkihai 디폴트값(false)로 수정됨
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

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
    res = common.배송방법수정(headers, seq, payload)
    status_code = res.status_code
    assert status_code is 200
    rp_logger.info('● status code 일치: '+str(status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) != 0:
            assert useOkihai is False
            rp_logger.info('● useOkihai 디폴트값(false)로 수정성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')


def test_배송방법수정_okihai_비필수_필드없음_성공(rp_logger, headers):
    """
     ● case: okihai 필드없이 수정요청
    ● step:
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. useOkihai 항목 없이 수정요청
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. useOkihai 디폴트값(false)로 수정됨
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

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
    res = common.배송방법수정(headers, seq, payload)
    status_code = res.status_code
    assert status_code is 200
    rp_logger.info('● status code 일치: '+str(status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) != 0:
            assert useOkihai is False
            rp_logger.info('● useOkihai 디폴트값(false)로 수정성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')


def test_배송방법수정_okihai_잘못된데이터타입_실패(rp_logger, headers):
    """
     ● case: okihai 항목 잘못된 데이터타입 입력하여 수정요청
     ● step: 
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. useOkihai 항목 boolean 의외 데이터로 수정요청
     ● result:
        &nbsp;  1. 400
        &nbsp;  2. message: 입력된 정보가 올바르지 않습니다 (入力された情報が正しくありません。)
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

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
            "useOkihai": "TEST"
        }
    }
    res = common.배송방법수정(headers, seq, payload)
    status_code = res.status_code

    assert status_code == 400
    rp_logger.info('● status code 일치: '+str(status_code))
    message = res.json()['message']
    assert message == "入力された情報が正しくありません。"
    rp_logger.info('● message 일치: '+message)

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')


def test_배송방법수정_오키하이등록불가배송서비스_실패(rp_logger, headers):
    """
     ● case: 오키하이사용여부선택불가Y 배송서비스를 오키하이설정=false로 배송방법 수정한 경우
     ● step:
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. 오키하이사용여부선택불가=Y인 배송방법(=100111) & useOkihai=false로 수정
     ● result:
        &nbsp;  1. 400
        &nbsp;  2. message: 오키하이를 지정할 수 없는 배송서비스코드 입니다 (置き配を指定できない配送サービスコードです。)
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

    payload = common.deliveryMethod_payload(100110, True)
    res = common.배송방법수정(headers, seq, payload)
    rp_logger.debug('〇 response: '+res.text)
    status_code = res.status_code

    assert res.status_code == 400
    rp_logger.info('● status code 일치: '+str(status_code))
    message = res.json()['message']
    assert message == "置き配を指定できない配送サービスコードです。"
    rp_logger.info('● message 일치: '+message)

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')


def test_배송방법수정_오키하이사용여부선택불가Y_true_성공(rp_logger, headers):
    """
     ● case: 오키하이사용여부선택불가Y 배송서비스를 오키하이설정=true로 배송방법 수정한 경우
     ● step:
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. 오키하이사용여부선택불가=Y인 배송방법(=100111) & useOkihai=true로 수정
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. 수정값(useOkihai, serviceCode) 정상반영
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

    payload = common.deliveryMethod_payload(100111, True)
    res = common.배송방법수정(headers, seq, payload)
    rp_logger.debug('〇 response: '+res.text)
    message = res.json()['message']

    res = common.배송방법수정(headers, seq, payload)


    assert res.status_code == 200
    rp_logger.info('● status code 일치: '+str(res.status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) != 0:
            assert useOkihai is True
            rp_logger.info('● 수정값 정상반영')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')


def test_배송방법수정_오키하이사용여부선택불가Y_false_실패(rp_logger, headers):
    """
     ● case: 오키하이사용여부선택불가Y 배송서비스를 오키하이설정=false로 배송방법 수정한 경우
     ● step:
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. 오키하이사용여부선택불가=Y인 배송방법(=100111) & useOkihai=false로 수정
     ● result:
        &nbsp;  1. 400
        &nbsp;  2. message: 오키하이를 지정할 수 없는 배송서비스코드 입니다 (置き配を指定できない配送サービスコードです。)
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

    payload = common.deliveryMethod_payload(100111, False)
    res = common.배송방법수정(headers, seq, payload)
    rp_logger.debug('〇 response: '+res.text)
    message = res.json()['message']

    assert res.status_code == 400
    assert message == "置き配で必須設定をしていただく配送サービスコードです。"
    rp_logger.info('● status code 일치: '+str(res.status_code))
    rp_logger.info('● message 일치: '+message)

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')


def test_배송방법수정_오키하이사용여부선택불가Y_필드미지정_성공(rp_logger, headers):
    """
     ● case: 오키하이사용여부선택불가Y 배송서비스를 오키하이설정 필드 미지정상태로 배송방법 수정한 경우
     ● step:
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. 오키하이사용여부선택불가=Y인 배송방법(=100111) & useOkihai 항목 없이 수정
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. useOkihai 필드가 true 인 상태로 생성됨
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

    payload = {
        "deliveryMethodName": "API_오키하이_등록",
        "serviceCode": "100111",
        "feeTable": {
            "areaType": "WIDE",
            "columnType": "COMMON",
            "feeList": [500]
        },
        "deliveryFeeCalculateMethod": "ONCE",
        "description": "오키하이 테스트용",
        "okihai": {}
    }
    res = common.배송방법수정(headers, seq, payload)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 200
    rp_logger.info('● status code 일치: '+str(res.status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) != 0:
            assert useOkihai is True
            rp_logger.info('● useOkihai = true 인 상태로 수정성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')


def test_배송방법수정_오키하이선택시도착시간대선택불가Y_성공(rp_logger, headers):
    """
     ● case: 오키하이선택시도착시간대선택불가=Y 인 배송서비스를 오키하이설정=Y로 배송방법 수정한 경우
     ● step:
        &nbsp;  1. 배송방법 등록
        &nbsp;  2. 오키하이선택시도착시간대선택불가=Y인 배송방법(=100111) & useOkihai=true 로 수정
     ● result:
        &nbsp;  1. 200
        &nbsp;  2. useOkihai 디폴트값(false)로 수정됨
    """
    payload = common.deliveryMethod_payload(100210, True)
    seq = common.배송방법등록(headers, payload).json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(seq))

    payload = common.deliveryMethod_payload(100310, True)
    res = common.배송방법수정(headers, seq, payload)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 200
    rp_logger.info('● status code 일치: '+str(res.status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) != 0:
            assert useOkihai is True
            rp_logger.info('● useOkihai=true 로 수정성공')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, seq)
    rp_logger.debug('〇 배송방법번호 '+str(seq)+' 삭제완료')




