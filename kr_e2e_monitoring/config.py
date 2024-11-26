# py.test ./kr_e2e_monitoring --reportportal

# 로그인 아이디/비밀번호
USER_EMAIL = "nvqa_nshop99@naver.com"
USER_PASSWORD = "qatest"

SELLER_ID = "ns2qa100@naver.com"
SELLER_PASSWORD = "qatest123"

# URL 설정
URLS = {
    'real': {
        '네이버로그인': ("https://nid.naver.com/nidlogin.login"),
        '쇼핑홈': ("https://shopping.naver.com/home"),
        '브스_상품상세': ("https://brand.naver.com/philips/products/7368213343"),
        '스스_상품상세': ("https://smartstore.naver.com/daddypetdr/products/6970591942"),
        '윈도(리빙)_상품상세': ("https://shopping.naver.com/window-products/homeliving/4645032722"),
        '윈도(패션타운)_상품상세': ("https://shopping.naver.com/window-products/outlet/9969687134"),
        '장보기_상품상세': ("https://shopping.naver.com/window-products/emart/5905730767"),
        '버티컬(럭셔리)_상품상세': ("https://shopping.naver.com/luxury/boutique/products/5728751926"),
        '도착보장_상품상세': ("https://shopping.naver.com/logistics/products/6042668419"),
        '장바구니_지정배송': ("https://shopping.naver.com/cart/mart"),
        '장바구니_일반배송': ("https://shopping.naver.com/cart"),
        'MY찜한상품': ("https://shopping.naver.com/my/keep-products")
    }
}


