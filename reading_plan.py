import requests
import webbrowser

reading_plan = 'https://www.biblegateway.com/reading-plans/old-new-testament/next'
html_doc = requests.get( reading_plan )
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc.text, 'html.parser')
link = soup.find_all(href=True ,class_="icon-audio passage-audio")
daily_audio = "https://www.biblegateway.com" + str([a['href'] for a in link]).strip('[]').strip('\'\'')
webbrowser.open_new(daily_audio)
webbrowser.open_new_tab(reading_plan)

