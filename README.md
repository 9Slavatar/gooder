# <b>GOO</b>gle spi<b>DER</b>
Google search engine parser on python3

## Instruction
> Requirement python 3.10+

> python3 -m pip install -r requirements.txt

```python
import gooder

gooder = Gooder()
# Make request on google.com/search?q=Hello+World
gooder.parse(query="Hello World")

# Print only result links
print(gooder.get_links())

# Print only result titles
print(gooder.get_titles())

# Print all results list[tuple[link,title]]
print(gooder.raw_results)

# Save urls to json file
gooder.save_to_file(only_urls=True, to_json=True, override=True, file="results.json")
```

## Methods & Fields
| Method/Field | Args | Example | Result |
|---|---|---|---|
| Gooder.parse | query: str, page: int=0, ignore_google: bool=True, clear_old: bool=True | gooder.parse("hello",  clear_old=False) | See below |
| Gooder.raw_results | **Field** | **Field** | [[link, title], ...] |
| Gooder.get_links | repeats: bool = False | gooder.get_links() | [unique_link, ...] |
| Gooder.get_titles | *None* | gooder.get_titles() | [title, title, ...] |
| Gooder.save_to_file | only_urls: bool = True override: bool = True to_json: bool = False file: str = "urls.txt"  | gooder.save_to_file() | New file with urls |
| Gooder.get_hostname | links: str \| list | gooder.get_hostname( https://google.com/) | google.com |