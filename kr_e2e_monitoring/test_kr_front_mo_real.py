import pytest
from selenium import webdriver
import action_product as ap


@pytest.fixture(scope="module")
def mo_driver():
        mobile_emulation = {
                "deviceMetrics": {"width": 400, "height": 1000, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        mo_driver = webdriver.Chrome(options=chrome_options)

        yield mo_driver
        mo_driver.quit()


@pytest.fixture(scope="module")
def 로그인(mo_driver, rp_logger):
        ap.네이버로그인(mo_driver, rp_logger)


def test_비로그인_구매하기(mo_driver, rp_logger):
        ap.페이지이동(mo_driver, rp_logger, '스스', '상품상세')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        ap.alert_확인(mo_driver, rp_logger)
        ap.네이버로그인_팝업(mo_driver, rp_logger, 'mo')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        assert ap.주문서_이동확인(mo_driver, rp_logger)


def test_스마트스토어_구매하기_바로구매(mo_driver, rp_logger, 로그인):
        ap.페이지이동(mo_driver, rp_logger, '스스', '상품상세')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo',  '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        assert ap.주문서_이동확인(mo_driver, rp_logger)


def test_브랜드스토어_구매하기(mo_driver, rp_logger, 로그인):
        ap.페이지이동(mo_driver, rp_logger, '브스', '상품상세')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo',  '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        assert ap.주문서_이동확인(mo_driver, rp_logger)


def test_윈도_리빙_구매하기(mo_driver, rp_logger, 로그인):
        ap.페이지이동(mo_driver, rp_logger, '윈도(리빙)', '상품상세')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo',  '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        assert ap.주문서_이동확인(mo_driver, rp_logger)

def test_윈도_패션타운_구매하기(mo_driver, rp_logger, 로그인):
        ap.페이지이동(mo_driver, rp_logger, '윈도(패션타운)', '상품상세')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo',  '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        assert ap.주문서_이동확인(mo_driver, rp_logger)


def test_버티컬_럭셔리_구매하기(mo_driver, rp_logger, 로그인):
        ap.페이지이동(mo_driver, rp_logger, '버티컬(럭셔리)', '상품상세')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo',  '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        assert ap.주문서_이동확인(mo_driver, rp_logger)


def test_도착보장_구매하기(mo_driver, rp_logger, 로그인):
        ap.페이지이동(mo_driver, rp_logger, '도착보장', '상품상세')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo',  '구매하기')
        ap.상품상세_클릭(mo_driver, rp_logger, 'mo', '바로구매')
        assert ap.주문서_이동확인(mo_driver, rp_logger)