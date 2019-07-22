def make_url(key, targetDt):
    base = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    result = f'{base}?key={key}&targetDt={targetDt}'
    return result
