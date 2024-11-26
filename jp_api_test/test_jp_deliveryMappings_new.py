import common



def test_전체배송방법택배사서비스코드매핑조회(rp_logger, headers):
    """
    테스트 서비스 매핑 쿼리

    케이스:
        - 서비스코드 조회
    결과:
        1. 200
        2. 조회 결과 확인
    """
    # 서비스 코드 조회
    res = common.전체배송방법택배사서비스코드매핑조회(headers)

    # 응답 상태코드가 200인지 확인
    if res.status_code == 200:
        # 예상 결과
        expected_results = [
            {'serviceCode': '100110', 'isOkihaiAvailable': False},
            {'serviceCode': '100210', 'isOkihaiAvailable': True},
            {'serviceCode': '100310', 'disableOkihaiCheckBox': False},
            {'serviceCode': '100111', 'disableOkihaiCheckBox': True},
            {'serviceCode': '100310', 'disableArriveConfigCheckBoxWhenOkihaiForOrder': True},
            {'serviceCode': '100111', 'disableArriveConfigCheckBoxWhenOkihaiForOrder': False}
        ]

        # 예상 결과 확인
        for expected_result in expected_results:
            for dict in res.json():
                serviceCode = dict['serviceCode']
                if serviceCode == expected_result['serviceCode']:

                    # 필드명이 서로 다르므로 확인
                    for key in expected_result:
                        rp_logger.debug(f"{key}: Expected - {expected_result[key]}, Actual - {dict[key]}")
                        assert dict[key] == expected_result[key]

                    rp_logger.info(f'● 서비스코드({serviceCode}) 조회 결과 확인')
                    break
