import requests
from lxml import html

def user_info(user_id):
    url= 'https://www.shiyanlou.com/users/{}/'.format(user_id)
    content = requests.get(url)
    if content.status_code != 200 :
        return None, None, None
    tree = html.fromstring(content.text)
    user_name = tree.xpath('//div[@class="user-meta"]/span[1]/text()')[0].strip()
    user_level = int(tree.xpath('//div[@class="user-meta"]/span[2]/text()')[0].strip()[1:])
    join_date = tree.xpath('//span[@class="user-join-date"]/text()')[0].strip()[:10]
    
    
    
    
    return user_name, user_level, join_date



print("1 :",user_info('214893'))
print("2 :",user_info("1234567890"))
