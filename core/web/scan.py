import requests
import pandas as pd

class WebScan:

    def __init__(self, url: str, keyword_list: list = None) -> None:
        self.url = url
        if keyword_list is None:
            self.keyword_list = [
                ".git",
                "config.ini",
                "config.json",
                ".idea",
                ".gitignore",
                "README.md",
                "openapi.json",
                "docker-compose.yml",
                "Dockerfile",
                ".dockerignore"
            ]
        else:
            self.keyword_list = keyword_list

    def scan(self):
        global result
        found_resources = []
        if self.keyword_list is not None:
            for keyword in self.keyword_list:
                url = self.url + '/' + keyword
                try:
                    result = requests.get(url=url)
                    if result.status_code == 200:
                        found_resources.append(url)
                    else:
                        print('Could not find resource: ' + keyword + ' in web root of: ' + self.url)
                except Exception as x:
                    print('Could not find resource: ' + keyword + ' in web root of: ' + self.url)
            print(found_resources)
        else:
            raise Exception('No Keyword list provided for web scan')
        return pd.DataFrame(data=found_resources, columns=['URL'])
