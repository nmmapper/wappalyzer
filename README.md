
# python3-wappalyzer


[![image](https://badge.fury.io/py/python-Wappalyzer.svg)](https://pypi.org/project/python3-webappalyzer/)


Python implementation of the Wappalyzer web application detection utility.

# Install

    $ pip install python3-webappalyzer

Require Python3.6 or later.

# Usage

The API exposes two objects: `Wappalyzer.Wappalyzer` and
`Wappalyzer.WebPage`.
```py
>>> from webappalyzer.Wappalyzer import Wappalyzer
>>> from webappalyzer.webpage._bs4 import WebPage
```
First create a WebPage. The following code creates a webpage with the
`request` module.
```py
>>> webpage = WebPage.new_from_url('http://example.com')
```

Then analyze it with Wappalyzer.

```py
>>> wappalyzer = Wappalyzer.latest() 
>>> wappalyzer.analyze(webpage) 
{'Docker', 'Azure CDN', 'Amazon WebServices', 'Amazon ECS'}
```
To download and use the latest technologies file from AliasIO/wappalyzer
repository, create the Wappalyzer driver with the `update=True`
parameter.

```py
>>> wappalyzer = wappalyzer.latest(update=True)
```

The Wappalyzer object exposes more methods that returns metatada for the
detected technologies.

```py
>>> wappalyzer.analyze_with_categories(webpage) {'Amazon ECS':
{'categories': ['IaaS']}, 'Amazon Web Services':
{'categories': ['PaaS']}, 'Azure CDN': {'categories':
['CDN']}, 'Docker': {'categories': ['Containers']}}

>>> webpage = WebPage.new_from_url('http://wordpress-example.com')

>>> wappalyzer.analyze_with_versions_and_categories(webpage) 
{'FontAwesome': {'categories': ['Font scripts'], 'versions': ['5.4.2']}, 'Google Font API': {'categories': ['Fontscripts'], 'versions': []}, 'MySQL': {'categories':['Databases'], 'versions': []}, 'Nginx': {'categories':['Web servers', 'Reverse proxies'], 'versions': []}, 'PHP':
{'categories': ['Programming languages'], 'versions':['5.6.40']}, 'WordPress': {'categories': ['CMS', 'Blogs'],'versions': ['5.4.2']}, 'Yoast SEO': {'categories':['SEO'], 'versions': ['14.6.1']}}
```
## Making asynchronous calls

```py
from webappalyzer.webpage._bs4 import WebPage
from webappalyzer.Wappalyzer import Wappalyzer
import aiohttp

async with aiohttp.ClientSession() as session:
    page = await WebPage.new_from_url_async("https://yourdomain-here.com/", aiohttp_client_session=session)

wappalyzer = Wappalyzer.latest()
wappalyzer.analyze_with_versions_and_categories(page)
```
