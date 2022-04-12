import urllib3
from lxml.html import fromstring
from lxml.cssselect import CSSSelector
from typing import TextIO, overload
from urllib.parse import urlparse
from json import dump


class Gooder:
    captcha: bool = False
    raw_results: list

    def __init__(self) -> None:
        # Init main class
        self.pool = urllib3.PoolManager(num_pools=10)

    def parse(
        self,
        query: str,
        page: int = 0,
        ignore_google: bool = True,
        clear_old: bool = True,
    ) -> bool:
        # Add page field on end
        if page:
            query += f"&start={10 * page}"

        # Make request
        r = self.pool.request(
            "GET",
            f"https://google.com/search?q={query}",
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                "accept": "*/*",
            },
        )

        p = fromstring(str(r.data))

        if clear_old:
            self.raw_results = []
        for element in CSSSelector("a")(p):
            url = element.get("href")
            if url is None:
                continue
            if len(url) < 3 or url.startswith("/search?"):
                continue
            if ignore_google and "google" in url:
                continue
            self.raw_results.append([url, element.text_content()])

        return not self.captcha

    @overload
    def get_hostname(self, links: list[str]) -> list[str | None]:
        ...

    @overload
    def get_hostname(self, links: str) -> str | None:
        ...

    def get_hostname(self, links: str | list[str]) -> str | None | list[str | None]:
        """
        Get hostname(s) from string or list
        """
        if isinstance(links, str):
            return urlparse(links).hostname

        hosts = []
        for url in links:
            hosts.append(urlparse(url).hostname)
        return hosts

    def get_links(self, repeats: bool = False) -> list:
        """
        Get only links from parsing results

        repeats = True, if you want get links with repeats hostnames
        Example: https://google.com/firstpage, https://google.com/secondpage
        """
        urls: list[str] = []
        for element in self.raw_results:
            url = element[0]
            if not repeats:
                if self.get_hostname(url) in self.get_hostname(urls):
                    continue
            urls.append(url)

        return urls

    def get_titles(self) -> list:
        """
        Get only titles from parsing results
        """
        titles = []
        for element in self.raw_results:
            end = element[1].find("http")
            if end == -1:
                continue

            titles.append(element[1][:end])

        return titles

    def save_to_file(
        self,
        only_urls: bool = True,
        override: bool = True,
        to_json: bool = False,
        file: str = "urls.txt",
    ) -> TextIO:
        """
        Save parsering results to file
        """
        if override:
            f = open(file, "w+", encoding="utf-8")
        else:
            f = open(file, "a+", encoding="utf-8")

        if not to_json:
            f.writelines(
                "\n".join(self.get_links())
                if only_urls
                else [f"{k} {v}\n" for k, v in dict(self.raw_results).items()]
            )
        else:
            dump(self.get_links() if only_urls else dict(self.raw_results), f)

        return f
