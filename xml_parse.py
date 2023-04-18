import requests
import lxml
from bs4 import BeautifulSoup

SOURCE = 'https://www.theyworkforyou.com/pwdata/scrapedxml/regmem/'


def get_latest_register():
    """Find URL of latest scraped register on theyworkforyou"""
    resp = requests.get(SOURCE)
    html = BeautifulSoup(resp.text, 'html.parser')
    last_link = html.find_all('a')[-1]
    return SOURCE + last_link['href']


def get_xml(url):
    """Download XML from given URL"""
    resp = requests.get(url)
    return BeautifulSoup(resp.text, 'xml')


def main():
    """ Main entry point of the app """
    latest_register_url = get_latest_register()
    xml = get_xml(latest_register_url)
    print(xml)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()