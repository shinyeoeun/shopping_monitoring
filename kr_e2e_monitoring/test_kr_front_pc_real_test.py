import action_product as ap
from selenium import webdriver
import pytest

# DRIVER_OPTIONS = ['disable-gpu', '--window-size=1920,1080', '--start-maximized', '--log-level=3', 'headless']
DRIVER_OPTIONS = ['disable-gpu', '--window-size=1920,1500', '--log-level=3']

@pytest.fixture(scope="module")
def driver():
        options = webdriver.ChromeOptions()
        for arg in DRIVER_OPTIONS:
                options.add_argument(arg)
        driver = webdriver.Chrome(options=options)
        yield driver

@pytest.fixture(scope="module")
def 로그인(driver, rp_logger):
        ap.네이버로그인(driver, rp_logger)


def test_스마트스토어_구매하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '스스', '상품상세')
        assert ap.상품상세_이동확인(driver, rp_logger)




