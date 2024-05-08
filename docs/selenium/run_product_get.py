from get_product import get_data


url_dict = {
    # '식품' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=060000&gnb=b'
    # ,'디지털/가전' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=140000&gnb=b'
    # ,'모바일쿠폰' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=190000&gnb=b'
    # ,'Lady 패션' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=010000&gnb=b'
    # ,'Man 패션' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=020000&gnb=b'
    # ,'Kids 패션' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=030000&gnb=b'
    # ,'생활용품' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=110000&gnb=b'
    # ,'인테리어' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=090000&gnb=b'
    # ,'반려용품' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=200000&gnb=b'
    # ,'유아동용품' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=120000&gnb=b'
    # ,'액세서리' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=080000&gnb=b'
    '가방/잡화' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=050000&gnb=b'
    ,'신발' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=040000&gnb=b'
    ,'캠핑/레저' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=100000&gnb=b'
    ,'화장품/뷰티' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=070000&gnb=b'
}


for k,v in url_dict.items():
    large_category = k
    url = v
    get_data(large_category,url)
