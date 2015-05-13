import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, ulr):
        self.ulr = ulr
        self.internal_links = []
        self.external_links = []
        self.visited = []

    def start(self):
        links = self.get_links_for_ulr(self.ulr)
        self.classify(links)
        self.visited.append(self.ulr)

        for link in self.internal_links:
            print(link)
            if link not in self.visited:
                self.visited.append(link)
                sub_pages = self.get_links_for_ulr(link)
                self.classify(sub_pages)

    def get_links_for_ulr(self, ulr):
        links = []
        try:
            r = requests.get(ulr, timout=3)
            soup = BeautifulSoup(r.text)
            for link in soup.find_all('a'):
                links.append(link.get('href'))
            return links
        except:
            print("WRONNG URL!")

        return links

    def classify(self, links):
        for link in links:
            if link is None:
                continue
            if "start.bg" in link:
                self.internal_links.append(link)
            elif "link.php?" in link:
                self.external_links.append(link)
        return self.internal_links



def main():
    crawler = Crawler("http://register.start.bg/")
    crawler.start()

if __name__ == '__main__':
    main()
