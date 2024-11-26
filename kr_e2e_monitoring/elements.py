CLASS = {
    '상품상세': {
        '구매하기': "_2-uvQuRWK5",
        '장바구니담기': "_3g6Aiz5G_O"
    },
    '장바구니': {
        '총주문하기': "link_buy--jXvxZ8Agr-",
        '건주문하기': "link_buy--KOU5pZhUVG",
        '선택삭제': "btn_delete--3P5eHI2eDa",
        '배송시간선택': "header--KNKcCL-UFw"
    }
}

XPATHS = {
    '상품상세': {
        '찜하기': "//fieldset/div[8]/div[2]/div[2]",
    },
    '장바구니': {
        '일반배송': {
            '총주문하기': "//div/div[9]/div/div[2]/button[2]",
            '주문하기': "//div/div[5]//div[2]/div[3]/a",
            '전체선택': "//*[@id='check-all']/span[1]/svg",
            '선택삭제': "//*[@id='app']/div/div[4]/div/div/button"
        },
        '지정배송': {
            '주문하기': "//div/div[6]//div[4]/div[3]/a",
            '배송시간선택': "//div/div[9]/div/div[1]",
            '선택삭제': "//*[@id='app']/div/div[5]/div/div/button"
        }
    },
    'MY찜한상품': {
        '최근상품': "//div[2]/ul/li[1]/div[2]/a",
        '삭제': "//div[2]/ul/li[1]/div[2]/button"
    }
}

XPATHS_MO = {
    '상품상세': {
        '구매하기': "//*[text()='구매']",
        '바로구매': "//*[text()='바로구매']",
        '장바구니담기': "//*[text()='장바구니 담기']",
        '찜하기': "//fieldset/div[8]/div[2]/div[2]",
    },
    '장바구니': {
        '일반배송': {
            '주문하기': "//*[text()='건 주문하기']",
            '총주문하기': "//*[text()='총 주문하기']",
            '전체선택': "//*[text()='전체 선택']",
            '선택삭제': "//*[text()='삭제']",
        },
        '지정배송': {
            '상품없음': "//*[text()='장바구니에 담긴 상품이 없습니다.']",
            '주문하기': "//*[text()='건 주문하기']",
            '배송시간선택': "//*[text()='배송시간 선택']"
        }
    },
    'MY찜한상품': {
        '최근상품': "//div[2]/ul/li[1]/div[2]/a",
        '삭제': "//div[2]/ul/li[1]/div[2]/button"
    }
}
