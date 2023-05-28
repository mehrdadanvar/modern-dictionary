import requests as r
from bs4 import BeautifulSoup as bs

sheaders = {
    'authority': "www.thesaurus.com",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    'accept-language': "en-GB,en;q=0.6",
    'cache-control': "max-age=0",
    'cookie': "usprivacy=1---; sid=262556-1668392889782; bid=262556-1668392889782; spanids=1; OneTrustWPCCPAGoogleOptOut=true; OptanonConsent=isGpcEnabled=1&datestamp=Sun+Nov+13+2022+18%3A28%3A10+GMT-0800+(Pacific+Standard+Time)&version=6.36.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false",
    'if-none-match': "W/302c6-ol60VaUq/z3Ydp1gqWnV7qOh5G8",
    'referer': "https://www.thesaurus.com/",
    'sec-ch-ua': "Brave;v=107,Chromium;v=107,Not = A?Brand;v=24",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "Linux",
    'sec-fetch-dest': "document",
    'sec-fetch-mode': "navigate",
    'sec-fetch-site': "same-origin",
    'sec-fetch-user': "?1",
    'sec-gpc': "1",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_word(word):
    url = f"https://www.thesaurus.com/browse/{word}"
    response = r.get(url, headers=sheaders)
    print(url)
    print(response.status_code)
    page = bs(response.text, "lxml")
    interest = page.select("div.css-1fsijta.eebb9dz0")
    print(len(interest))
    listitems = interest[0].select("li")
    items = [x.get_text() for x in listitems]
    print(items)


get_word("disaster")
