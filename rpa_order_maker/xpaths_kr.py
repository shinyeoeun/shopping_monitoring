
# XPATH 설정
XPATHS = {
    '상품상세': {
        '스스브스윈도_구매하기': "//*[@id='content']/div/div[2]/div[2]/fieldset/div[8]/div[1]",
        '스스브스윈도_장바구니담기': "//*[@id='content']/div/div[2]/div[2]/fieldset/div[8]/div[2]/div[3]",
        '스스브스윈도_찜하기': "//*[@id='content']/div/div[2]/div[2]/fieldset/div[8]/div[2]/div[2]",
        '장보기_장바구니담기': "//*[@id='content']/div[3]/div[2]/fieldset/div[9]/div[1]",
        '버티컬_구매하기': "//*[@id='content']/div[2]/div[3]/fieldset/div[10]/div[1]"
    },
    '장바구니': {
        '일반배송': {
            '주문하기': "//*[@id='app']/div/div[5]/div/div/div[2]/div[2]/div[3]/a"
        },
        '지정배송': {
            '주문하기': "//*[@id='app']/div/div[6]/div/div/div[2]/div[4]/div[3]/a",
            '배송시간선택': "//*[@id='app']/div/div[9]/div/div[1]"
        }
    },
    'MY찜한상품': {
        '최근상품': "//*[@id='content']/div[2]/ul/li[1]/div[2]/a",
        '삭제': "//*[@id='content']/div[2]/ul/li[1]/div[2]/button"
    }
}