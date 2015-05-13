import requests
from bs4 import BeautifulSoup


class Histrogram:
    def __init__(self):
        self.value_container = {}
        self.register_string = ""
        self.links = []
        self.servers = []

    def add(self, value):
        if value in self.value_container:
            self.value_container[value] += 1
        else:
            self.value_container[value] = 1

    def count(self, value):
        return self.value_container[value]

    def items(self):
        keys = [key for key in self.value_container]
        count = [self.count(key) for key in keys]
        return keys, count

    def get_dict(self):
        return self.value_container

    def get_register_link(self):
        r = requests.get("http://register.start.bg/")
        self.register_string = r.text

    def get_links(self):
        soup = BeautifulSoup(self.register_string)
        for link in soup.find_all('a'):
            real_link = link.get('href')
            if real_link != None and real_link != "#top":
                self.links.append(real_link)
        print(len(self.links))


    def send_requests(self):
        count = 0
        our_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        }
        for link in self.links:
            try:
                print(link)
                r = requests.get(link, timeout=5)
                self.servers.append(r.headers["Server"])
                print(len(self.servers))
            except:
                count += 1
        for item in self.servers:
            print(item)



h = Histrogram()

h.get_register_link()
h.get_links()
h.send_requests()
