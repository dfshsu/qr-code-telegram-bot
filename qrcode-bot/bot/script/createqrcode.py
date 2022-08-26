import requests
from bs4 import BeautifulSoup as Soup

def create(data, file):
    url = "https://www.qrrd.ru/?action=ajaxfunc&sa=createqr"

    fields={
            'textqr': data,
            'qrsize': 4,
            'color_back': '#ffffff',
            'color_code': '#000000',
        
        }

    response = requests.post(url=url, data=fields)
    soup = Soup(response.content, 'html.parser')

    for link in soup.find_all('img'):
        image = link.get('src')

    with open(file,'wb') as target:
        a = requests.get(image)
        target.write(a.content)
    return image