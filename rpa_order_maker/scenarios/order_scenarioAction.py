# -*- coding: utf-8 -*-
import time
from rpa_order_maker import xpaths_jp, config, utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rpa_order_maker.scenarios.scenario import ScenarioAction

class LINE로그인(ScenarioAction):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def run(self, target=None):
        self.driver.get(config.URLS['real']['MY_로그인'])
        utils.wait_for_page_load(self.driver)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['로그인']['LINE로그인']).click()
            self.driver.find_element(By.NAME, "tid").send_keys(self.email)
            self.driver.find_element(By.NAME, "tpasswd").send_keys(self.password)
            self.driver.find_element(By.CLASS_NAME, "MdBtn01").click()
            time.sleep(5)
        except Exception as e:
            print("Error occurred while logging in with LINE:", e)

class LINE쿠키로그인(ScenarioAction):

    def __init__(self, cookies):
        self.cookies = cookies

    def run(self, target=None):
        self.driver.get(config.URLS['real']['MY_홈'])
        for c in self.cookies:
            self.driver.add_cookie(c)

class 상품상세_장바구니추가(ScenarioAction):

    def run(self, target=None):
        print("상품상세 ", target)
        self.driver.get(target)
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['상품상세']['장바구니추가']).click()  # 장바구니 추가 버튼
            element = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(
                    (By.XPATH, xpaths_jp.XPATHS['상품상세']['옵션선택팝업_장바구니추가'])))  # 팝업> 장바구니 추가 버튼
            time.sleep(0.1)
            element.click()

            toast = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(
                    (By.XPATH, xpaths_jp.XPATHS['상품상세']['장바구니이동'])))  # 토스트 알림: 상품추가 요청의 반환 시점을 파악하기 위해
            time.sleep(1)
        except Exception as e:
            print("Error occurred while adding item to cart:", e)
            self.run(target)  # 장바구니 담기 재시도

    def require_target(self):
        return True

class 장바구니_주문하기(ScenarioAction):

    def run(self, target=None):
        self.driver.get(config.URLS['real']['MY_장바구니'])
        try:
            self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['장바구니']['주문하기']).click()  # 장바구니> 주문하기 클릭
            self.driver.implicitly_wait(10)
        except Exception as e:
            print("Error occurred while proceeding to checkout from cart:", e)
            print("No items in the cart.")

class 주문서_결제(ScenarioAction):

    def run(self, target=None):
        self.결제방법_수정()
        self.결제방법_선택()
        self.주문내용확인()
        self.결제요청()
        self.welcome_happy_brown()

    def 결제방법_수정(self):
        self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['주문']['결제방법_수정']).click()  # 다음으로 클릭
        self.driver.implicitly_wait(10)

    def 주문내용확인(self):
        self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['주문']['주문내용확인']).click()  # 다음으로 클릭
        self.driver.implicitly_wait(10)
        time.sleep(0.78)

    def welcome_happy_brown(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpaths_jp.XPATHS['주문']['행복한브라운']))).click()  # 행복한 브라운

class 결제수단:

    def 결제방법_선택(self):
        pass

class 결제수단_포인트전액:

    def 결제방법_선택(self):
        self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['주문']['포인트사용']).click()  # 포인트 사용 클릭

class 결제수단_신용카드:

    def 결제방법_선택(self):
        self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['주문']['신용카드']).click()  # 결제수단 > 신용카드

class PG결제:

    def 결제요청(self):
        self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['주문']['PG']).click()  # PG 결제 클릭
        self.driver.implicitly_wait(10)

        main_page = self.driver.current_window_handle
        popup_page = None
        for handle in self.driver.window_handles:
            if handle != main_page:
                popup_page = handle

        if popup_page is not None:
            self.driver.switch_to.window(popup_page)  # 팝업 창으로 컨텍스트 전환
            time.sleep(1)
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(
                    (By.XPATH, xpaths_jp.XPATHS['주문']['PG팝업']['PG_주문확정']))).click()  # PG팝업> 결제 버튼
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(
                    (By.XPATH, xpaths_jp.XPATHS['주문']['PG팝업']['PG_결제확인']))).click()  # PG팝업> 결제 버튼> 알럿> 확인 버튼

            self.driver.switch_to.window(main_page)  # 바닥 페이지로 컨텍스트 전환
            self.driver.implicitly_wait(10)

class TestPG결제:

    def 결제요청(self):
        self.driver.find_element(By.XPATH, xpaths_jp.XPATHS['주문']['TestPG']['real']).click()
        self.driver.implicitly_wait(10)



class 신용카드_PG결제(주문서_결제, 결제수단_신용카드, PG결제):
    pass

class 포인트전액_PG결제(주문서_결제, 결제수단_포인트전액, PG결제):
    pass

class 신용카드_TestPG결제(주문서_결제, 결제수단_신용카드, TestPG결제):
    pass