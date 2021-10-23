import requests
from bs4 import BeautifulSoup
from .export import run_export
def run_scraper(url):
    results = []
    page = requests.get(url)
    soup =BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all('div', class_="card-content")
    for element in elements:
        title = element.find("h2", class_="title")
        location = element.find("p", class_="location")
        results.append([title.text.strip(), location.text.strip()])
    
    run_export(results)
    
