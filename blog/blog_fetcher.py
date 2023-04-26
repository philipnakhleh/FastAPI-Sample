from bs4 import BeautifulSoup
from requests import get


def get_blogs():
    r = get('https://medium.com/@tradinos-ug/feed')

    soup = BeautifulSoup(r.content, 'lxml')

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

        img = i.find('img')
        item['image_url'] = img['src']

        content = i.find('content:encoded')

        last = str(content).replace('<content:encoded>&lt;![CDATA[', '').replace(']]&gt;</content:encoded>', '')
        last = '<html><head><meta charset="utf-8"></head><body>' + last + '</body></html>'

        item['content'] = last

        item['descripion'] = content.text.replace('<![CDATA[', '').replace(']]>', '')[:100] + '...'


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
