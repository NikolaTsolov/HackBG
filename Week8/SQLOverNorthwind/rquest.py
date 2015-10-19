import requests
import json


def requestor(url, header):
    r = requests.get(url, headers=header)
    return r.text

def file_writer(filname, info):
    with open(filname, "w") as f:
        f.write(info)


def main():
    url = "https://raw.githubusercontent.com/HackBulgaria/Programming101-3/master/week8-Team-Work/2-SQL-Over-Northwind/Northwind.sql"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }
    file_writer("sql_requests.sql", requestor(url, headers))

if __name__ == '__main__':
    main()
