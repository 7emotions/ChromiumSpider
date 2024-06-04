from io import StringIO

import pandas as pd

from chromiumspider.core import get_spider
from chromiumspider.core import find

if __name__ == '__main__':
    url = r'https://www.12306.cn/index/'
    spider = get_spider()

    spider.get(url)

    find(spider, r'//*[@id="fromStationText"]').clear()
    find(spider, r'//*[@id="fromStationText"]').send_keys('nanjing')
    find(spider, r'//*[@id="citem_0"]').click()
    find(spider, r'//*[@id="toStationText"]').clear()
    find(spider, r'//*[@id="toStationText"]').send_keys('hangzhou')
    find(spider, r'//*[@id="citem_1"]').click()
    find(spider, r'//*[@id="isHighDan"]').click()
    find(spider, r'//*[@id="search_one"]').click()

    spider.switch_to.window(spider.window_handles[-1])
    table = find(spider, r'//*[@id="t-list"]/table')
    html = "<table>" + table.get_attribute('innerHTML') + "</table>"

    df = pd.read_html(StringIO(html), header=0)[0]
    print(df.head())
    df.to_excel('12306.xlsx', index=False)
    spider.quit()
