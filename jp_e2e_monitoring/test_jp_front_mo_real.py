import action as a
import pytest
from selenium import webdriver


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
        a.페이지이동(mo_driver, rp_logger, 'real', 'MY_로그인')
        a.LINE로그인(mo_driver, rp_logger)


def test_신용카드결제(mo_driver, rp_logger, 로그인):
        a.페이지이동(mo_driver, rp_logger, 'real', 'MY_상품상세')
        a.상품상세_장바구니추가(mo_driver, rp_logger)
        a.장바구니_주문하기(mo_driver, rp_logger)
        a.주문서_결제(mo_driver, rp_logger, 'mo', '신용카드')
        assert a.주문성공(mo_driver, rp_logger)


def test_Paypay결제(mo_driver, rp_logger, 로그인):
        a.페이지이동(mo_driver, rp_logger, 'real', 'MY_상품상세')
        a.상품상세_장바구니추가(mo_driver, rp_logger)
        a.장바구니_주문하기(mo_driver, rp_logger)
        a.주문서_결제(mo_driver, rp_logger, 'mo', 'Paypay')
        assert a.주문성공(mo_driver, rp_logger)


def test_라인페이결제(mo_driver, rp_logger, 로그인):
        a.페이지이동(mo_driver, rp_logger, 'real', 'MY_상품상세')
        a.상품상세_장바구니추가(mo_driver, rp_logger)
        a.장바구니_주문하기(mo_driver, rp_logger)
        a.주문서_결제(mo_driver, rp_logger, 'mo', '라인페이')
        assert a.주문성공(mo_driver, rp_logger)