
from requests_html import HTMLSession
import speech_to_text

def weather():
  s = HTMLSession()
  query = 'patna'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent':'user_agent'})
  temp = r.html.find('span#wob_tm', first=True).text
  unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
  desc = r.html.find('span#wob_dc',first = True).text
  # print(temp,unit,desc)
  return temp + ' ' + unit + ' ' + desc
