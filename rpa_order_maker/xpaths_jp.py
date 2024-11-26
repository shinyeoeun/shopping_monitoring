
# XPATH 설정
XPATHS = {
    '로그인': {
      'LINE로그인': "//*[@id='root']/div/div/div[1]/form/div/section[2]/div/div/div[2]/button"
    },
    '상품상세': {
        '장바구니추가': "//*[@id='content']/div/div[1]/div[2]/div[4]/div/button[1]",
        '옵션선택팝업_장바구니추가': "//*[@id='MODAL_ROOT_ID']/div/div[2]/div/div[4]/button",
        '장바구니이동': "//*[@id='MODAL_ROOT_ID']/div/div[2]/div[2]/button[1]",
    },
    '장바구니': {
        '주문하기': "//*[@id='__next']/div[1]/div[2]/div/div[4]/div/div[2]/button[2]"
    },
    '주문': {
        '결제방법_수정': "//*[@id='__next']/div/div[2]/div[1]/div[3]/div[3]/div/div[2]/div/div/div/button",
        '주문내용확인': "//*[@id='__next']/div/div[2]/div[2]/div/a",
        '포인트사용': "//*[@id='__next']/div/div[2]/div[1]/div[3]/div[2]/div/button",
        '신용카드': "//*[@id='__next']/div/div[2]/div[1]/div[5]/div[2]/div[2]/ul/li[1]/div",
        'PG': "/html/body/div/div/div[2]/div[2]/div/a[1]",
        'TestPG': {
            'dev': "//*[@id='__next']/div/div[2]/div[2]/div/a[1]",
            'real': "//*[@id='__next']/div/div[2]/div[2]/div/a"
        },
        'PG팝업': {
            'TestPG_결제확정': "//*[@id='__next']/div/div[1]/ul/li[2]/button",
            'PG_주문확정': "//*[@id='btnPayment']",
            'PG_결제확인': "//*[@id='lyConfirm']/div[2]/div[2]/button"
        },
        '행복한브라운': "//*[@id='__next']/div/div[2]/div/div[2]/div[1]/img"
    },
}