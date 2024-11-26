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
        a.페이지이동(driver, rp_logger, 'real', 'Center_홈')
        a.비즈니스로그인(driver, rp_logger)


def test_상품관리_진입(driver, rp_logger, 로그인):
        a.페이지이동(driver, rp_logger, 'real', 'Center_상품관리')
        assert a.상품관리_페이지진입성공(driver, rp_logger)

