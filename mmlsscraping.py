from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

URL = 'https://mmls.mmu.edu.my'
s = requests.Session()

def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content

soup = BeautifulSoup(fetch(URL))
form = soup.find('form')
fields = form.findAll('input')

formdata = dict( (field.get('stud_id'), field.get('stud_pswrd')) for field in fields)

formdata['stud_id'] = u''
formdata['stud_pswrd'] = u''

# print(formdata)
posturl = urljoin(URL, form['action'])
# print(posturl)

r = s.post(posturl, data=formdata)
print(r.text)

# print(s.get(URL).text)