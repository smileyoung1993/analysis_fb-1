import collect
import analyze
import visualize

if __name__ == '__main__':
    items = [
        {'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-12-31'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}
    ]

    # 데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile

    # 데이터 분석(analyze)
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        print(data)
        # item['count_wordfreq'] = analyze.count_wordfreq(data)

    # 데이터 시각화(visualize)


