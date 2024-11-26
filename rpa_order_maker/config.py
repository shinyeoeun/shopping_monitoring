import pandas as pd

# 크롬 드라이버 옵션
DRIVER_OPTIONS = ['disable-gpu', '--start-maximized', '--log-level=3', 'headless']
# DRIVER_OPTIONS = ['disable-gpu', '--start-maximized', '--log-level=3']

# 쌓으려는 데이터 수
EPOCHS = 1

# 로그인 아이디와 비밀번호
USER_EMAIL = "nvqa_nshop87@naver.com"
USER_PASSWORD = "qatest123!@#"

SELLER_ID = "nvqa_gncp_70@naver.com"
SELLER_PASSWORD = "gncp70"

# URL 설정
URLS = {
    'dev': {
        'MY_홈': ("https://dev.mysmartstore.jp"),
        'MY_로그인': ("https://dev-accounts.mysmartstore.jp/login"),
        'MY_상품상세': ("https://store53.dev.mysmartstore.jp/products/2000111125"),
        'MY_장바구니': ("https://dev.mysmartstore.jp/order/cart"),
        'MY_상품상세_리스트': [
            "https://store53.dev.mysmartstore.jp/products/2000111125",
        ]
    },
    'real': {
        'MY_홈': ("https://mysmartstore.jp/my"),
        'MY_로그인': ("https://accounts.mysmartstore.jp/login?url=https://mysmartstore.jp/my"),
        'MY_상품상세': ("https://betanshop70.mysmartstore.jp/products/100479403"),
        'MY_장바구니': ("https://mysmartstore.jp/order/cart"),
        'MY_상품상세_리스트': [
            "https://betanshop70.mysmartstore.jp/products/100479403",
        ]
    }
}

