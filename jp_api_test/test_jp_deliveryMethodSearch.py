import common


def test_배송방법조회_Admin오키하이사용여부N_성공(rp_logger, headers):
    """
    ● case: Admin 오키하이 사용여부 N인 배송방법조회
    ● result: 200
    """
    payload = common.deliveryMethod_payload(100110, False)
    res = common.배송방법등록(headers, payload)
    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))

    res = common.배송방법조회(headers, 1)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 200
    rp_logger.info('● status code 일치: '+str(res.status_code))

    if res.status_code == 200:
        res = common.최신배송방법검색(headers)
        for resbody in res.json()['result']:
            useOkihai = resbody['useOkihai']
            if len(str(useOkihai)) is not 0:
                assert useOkihai is False
                rp_logger.info('● useOkihai = False 노출')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')



def test_배송방법조회_Admin오키하이사용여부Y_Center오키하이사용Y_false노출_성공(rp_logger, headers):
    """
    ● case: Admin 오키하이사용여부N 이면서 Center 오키하이 사용함 인 배송방법조회
    ● result: 200 Success
    """
    payload = common.deliveryMethod_payload(100210, True)
    res = common.배송방법등록(headers, payload)
    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))

    res = common.배송방법조회(headers, 1)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 200
    rp_logger.info('● status code 일치: '+str(res.status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) is not 0:
            assert useOkihai is True
            rp_logger.info('● useOkihai = True 노출')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')



def test_배송방법조회_Admin오키하이사용여부Y_Center오키하이사용N_false노출_성공(rp_logger, headers):
    """
    ● case: Admin 오키하이사용여부N 이면서 Center 오키하이 사용안함 인 배송방법조회
    ● result: 200 Success
    """
    payload = common.deliveryMethod_payload(100210, False)
    res = common.배송방법등록(headers, payload)
    ids = res.json()['id']
    rp_logger.debug('〇 신규등록 배송방법ID: '+str(ids))

    res = common.배송방법조회(headers, 1)
    rp_logger.debug('〇 response: '+res.text)
    assert res.status_code == 200
    rp_logger.info('● status code 일치: '+str(res.status_code))

    res = common.최신배송방법검색(headers)
    for resbody in res.json()['result']:
        useOkihai = resbody['useOkihai']
        if len(str(useOkihai)) is not 0:
            assert useOkihai is False
            rp_logger.info('● useOkihai = False 노출')

    # 후속처리: 배송방법 삭제
    common.배송방법삭제(headers, ids)
    rp_logger.debug('〇 배송방법번호 '+str(ids)+' 삭제완료')

