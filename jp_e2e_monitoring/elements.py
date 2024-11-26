XPATHS = {
    '로그인': {
      'LINE로그인': "//*[text()='LINEでログイン']",
      '센터로그인': "//*[@id='navbar']/div/ul/li[2]/button",
      '비즈니스계정으로로그인': "//a[text()='비즈니스 계정으로 로그인']",
      'biz로그인버튼': "//button[contains(text(), '로그인')]"
    },
    'MY홈': {
      '로그인email': "//div/div[1]/div[2]/div[1]/div[1]/div[3]"
    },
    '상품상세': {
        '장바구니추가': "//*[text()='カートに入れる']",
        '옵션선택팝업_장바구니추가': "//*[text()='カートに入れる']",
        '장바구니이동': "//*[text()='カートに移動する']",
    },
    '장바구니': {
        '주문하기': "//*[text()='ご注文手続きへ']"
    },
    '주문서': {
        # 결제방법 수정 버튼
        '결제방법_수정': "(//button[contains(text(), '編集')])[3]",

        # 결제 방법 옵션들
        '신용카드': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[1]",
        'Paypay': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[2]",
        '편의점결제': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[3]",
        '라인페이': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[4]",
        '로손': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[3]/div[2]/div[1]/span[2]",

        # 주문서 내용 관련 요소들
        '주문내용확인': "//*[@id='__next']/div/div[2]/div[2]/div/a",
        '주문확정하기': "//*[@id='__next']/div/div[2]/div[2]/div/a",
        '주문번호': "//div/div[2]/div/div[2]/div[3]/div/em",

        # TestPG 결제 확정 버튼
        'TestPG_결제확정': "//button[contains(text(), '결제 성공 후 주문생성 성공처리')]"
    },
    '상품관리': {
        '상품관리_타이틀': "//text()[contains(., '商品検索/編集')]/.."
    }
}
XPATHS_MO = {
    '로그인': {
        'LINE로그인': "//*[text()='LINEでログイン']"
    },
    'MY홈': {
        '로그인email': "//div/div[1]/div[2]/div[1]/div[1]/div[3]"
    },
    '상품상세': {
        '장바구니추가': "//*[text()='カートに入れる']",
        '옵션선택팝업_장바구니추가': "//*[text()='カートに入れる']",
        '장바구니이동': "//*[text()='カートに移動する']",
    },
    '장바구니': {
        '주문하기': "//*[text()='ご注文手続きへ']"
    },
    '주문서': {
        '결제방법_수정': "(//button[contains(text(), '編集')])[3]",
        '포인트사용': "//button[contains(text(), 'すべて利用')]",
        '신용카드': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[1]",
        'Paypay': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[2]",
        '편의점결제': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[3]",
        '라인페이': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[4]",
        '로손': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[3]/div[2]/div[1]/span[2]",
        '주문내용확인': "//*[@id='__next']/div/div[2]/div[2]/div/a",
        '주문확정하기': "//*[@id='__next']/div/div[2]/div[2]/div/a",
        'TestPG_결제확정': "//button[contains(text(), '결제 성공 후 주문생성 성공처리')]",
        '주문번호': "//div/div[2]/div/div[2]/div[3]/div/em"
    },
}
