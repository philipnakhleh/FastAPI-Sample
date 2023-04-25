from bs4 import BeautifulSoup
from requests import get


def get_blogs():
    r = get('https://medium.com/@tradinos-ug/feed')
    soup = BeautifulSoup(r.content, 'xml')

    items = []

    res = soup.find_all('item')
    for i in res:
        item = {}
        title = i.find('title')
        text = title.text.replace('<![CDATA[', '')
        text = text.replace(']]>', '')

        item['title'] = text

        date = i.find('atom:updated').text[:10]
        item['date'] = date

        content = i.find('content:encoded')

        sp = BeautifulSoup(content.text, 'html')
        item['image_url'] = sp.find('img')['src']

        last = content.text
        last = '<html><head></head><body>' + last + '</body></html>'

        item['content'] = last

        categories = i.find_all('category')
        cate = []
        for cat in categories:
            tx = cat.text.replace('<![CDATA[', '')
            tx = tx.replace(']]>', '')
            cate.append(tx)

        item['categories'] = cate

        items.append(item)

    return {
        'data' : items
    }