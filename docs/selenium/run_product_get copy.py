from get_product_inside import get_data


url_dict = {
    '귀걸이/피어싱' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=080300&gnb=b'
    ,'반지' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=080400&gnb=b'
    ,'시계' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=080500&gnb=b'
    ,'헤어액세서리' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=080600&gnb=b'
    ,'브로치' : 'https://www.dibidibi.com/Comm/SearchN?cat_cd=080700&gnb=b'
}


for k,v in url_dict.items():
    large_category_name = '액세서리'
    small_category_name = k
    url = v
    get_data(large_category_name,small_category_name,url)
