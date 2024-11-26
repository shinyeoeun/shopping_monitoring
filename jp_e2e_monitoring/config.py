# py.test ./jp_e2e_monitoring/tests --reportportal

# 로그인 아이디와 비밀번호
USER_EMAIL = "nvqa_nshop87@naver.com"
USER_PASSWORD = "qatest123!@#"

SELLER_ID = "nvqa_nshop70@naver.com"
SELLER_PASSWORD = "qatest123"

# URL 설정
URLS = {
    'dev': {
        'MY_홈': ("https://dev.mysmartstore.jp"),
        'MY_로그인': ("https://dev-accounts.mysmartstore.jp/login"),
        'MY_상품상세': ("https://store53.dev.mysmartstore.jp/products/2000111125"),
        'MY_장바구니': ("https://dev.mysmartstore.jp/order/cart")
    },
    'real': {
        'MY_홈': ("https://mysmartstore.jp/my"),
        'MY_로그인': ("https://accounts.mysmartstore.jp/login?url=https://mysmartstore.jp/my"),
        'MY_상품상세': ("https://betanshop70.mysmartstore.jp/products/100479403"),
        'MY_장바구니': ("https://mysmartstore.jp/order/cart"),
        'Center_홈': ("https://smartstorecenter.jp/#/home/about"),
        'Center_대시보드': ("https://smartstorecenter.jp/#/home/dashboard"),
        'Center_상품관리': ("https://smartstorecenter.jp/#/products/origin-list")
    }
}


