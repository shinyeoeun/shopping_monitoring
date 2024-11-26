import pytest
import action as a
from selenium import webdriver

# 크롬 드라이버 옵션
# DRIVER_OPTIONS = ['disable-gpu', '--window-size=1920,1080', '--start-maximized', '--log-level=3', 'headless']
DRIVER_OPTIONS = ['disable-gpu', '--window-size=1920,1100', '--start-maximized', '--log-level=3']


@pytest.fixture(scope="module")
def driver():
        options = webdriver.ChromeOptions()
        for arg in DRIVER_OPTIONS:
                options.add_argument(arg)
        driver = webdriver.Chrome(options=options)
        yield driver


@pytest.fixture(scope="module")
def 로그인(driver, rp_logger):
        a.페이지이동(driver, rp_logger, 'real', 'MY_로그인')
        a.LINE로그인(driver, rp_logger)


def test_신용카드결제(driver, rp_logger, 로그인):
        a.페이지이동(driver, rp_logger, 'real', 'MY_상품상세')
        a.상품상세_장바구니추가(driver, rp_logger)
        a.장바구니_주문하기(driver, rp_logger)
        a.주문서_결제(driver, rp_logger, 'pc', '신용카드')
        assert a.주문성공(driver, rp_logger)


def test_Paypay결제(driver, rp_logger, 로그인):
        a.페이지이동(driver, rp_logger, 'real', 'MY_상품상세')
        a.상품상세_장바구니추가(driver, rp_logger)
        a.장바구니_주문하기(driver, rp_logger)
        a.주문서_결제(driver, rp_logger, 'pc', 'Paypay')
        assert a.주문성공(driver, rp_logger)

def test_라인페이결제(driver, rp_logger, 로그인):
        a.페이지이동(driver, rp_logger, 'real', 'MY_상품상세')
        a.상품상세_장바구니추가(driver, rp_logger)
        a.장바구니_주문하기(driver, rp_logger)
        a.주문서_결제(driver, rp_logger, 'pc', '라인페이')
        assert a.주문성공(driver, rp_logger)