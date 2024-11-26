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



def test_비로그인_구매하기(driver, rp_logger):
        ap.페이지이동(driver, rp_logger, '스스', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '구매하기')
        ap.alert_확인(driver, rp_logger)
        ap.네이버로그인_팝업(driver, rp_logger, 'pc')
        assert ap.주문서_이동확인(driver, rp_logger)

def test_스마트스토어_구매하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '스스', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '구매하기')
        assert ap.주문서_이동확인(driver, rp_logger)

def test_브랜드스토어_구매하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '브스', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '구매하기')
        assert ap.주문서_이동확인(driver, rp_logger)


def test_윈도_리빙_구매하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '윈도(리빙)', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '구매하기')
        assert ap.주문서_이동확인(driver, rp_logger)

def test_윈도_패션타운_구매하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '윈도(패션타운)', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '구매하기')
        assert ap.주문서_이동확인(driver, rp_logger)


def test_버티컬_럭셔리_구매하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '버티컬(럭셔리)', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '구매하기')
        assert ap.주문서_이동확인(driver, rp_logger)


def test_도착보장_구매하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '도착보장', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '구매하기')
        assert ap.주문서_이동확인(driver, rp_logger)


def test_장보기_장바구니담기_주문하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '장보기', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '장바구니담기')
        ap.alert_확인(driver, rp_logger)
        ap.장바구니_클릭(driver, rp_logger,  '건주문하기')
        assert ap.배송시간선택_확인(driver, rp_logger)
        ap.장바구니초기화(driver, rp_logger, '지정배송')


def test_브랜드스토어_장바구니담기_주문하기(driver, rp_logger, 로그인):
        ap.페이지이동(driver, rp_logger, '브스', '상품상세')
        ap.상품상세_클릭(driver, rp_logger, 'pc', '장바구니담기')
        ap.alert_확인(driver, rp_logger)
        ap.장바구니_클릭(driver, rp_logger,  '건주문하기')
        assert ap.주문서_이동확인(driver, rp_logger)
        ap.장바구니초기화(driver, rp_logger, '일반배송')



