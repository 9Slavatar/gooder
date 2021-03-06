# [<b>GOO</b>gle spi<b>DER</b>](https://pypi.org/project/gooder/)
Google search engine parser on python3

## Instruction
> Requirement python 3.10+

> pip install gooder

```python
from gooder import Gooder

gooder = Gooder()
# Make request on google.com/search?q=Hello+World
parsed = gooder.parse(query="Hello World")

# Print only result links
print(gooder.get_links())

# Print only result titles
print(gooder.get_titles())

# Print all results list[tuple[link,title]]
print(gooder.raw_results)

# If TRUE = parsed, else = captcha/rate limit
if (parsed)
    # Save urls to json file
    gooder.save_to_file(only_urls=True, to_json=True, override=True, file="results.json")
```

## Methods & Fields
| Method/Field | Args | Example | Result |
|---|---|---|---|
| Gooder.parse | query: str, page: int=0, ignore_google: bool=True, clear_old: bool=True | gooder.parse("hello",  clear_old=False) | True \| False |
| Gooder.raw_results | **Field** | **Field** | [[link, title], ...] |
| Gooder.get_links | repeats: bool = False | gooder.get_links() | [unique_link, ...] |
| Gooder.get_titles | *None* | gooder.get_titles() | [title, title, ...] |
| Gooder.save_to_file | only_urls: bool = True override: bool = True to_json: bool = False file: str = "urls.txt"  | gooder.save_to_file() | New file with urls |
| Gooder.get_hostname | links: str \| list | gooder.get_hostname(https://google.com/) | google.com |
| Gooder.get_captcha_url | *None* | gooder.get_captcha_url() | *None* \| google.com/sorry/... |
| Gooder.get_headers | *None* | gooder.get_headers() | *None* \| HTTPHeaderDict({...}) |

## Todo:
 + Add proxy manager
 + Replace `raw_results: list(list())` to `dict()` 