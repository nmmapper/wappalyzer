import setuptools

print(setuptools.find_packages())
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python3-webappalyzer", 
    version="1.1.2",
    author="nmmapper",
    author_email="info@nmmapper.com",
    description="Python implementation of the Wappalyzer web application detection utility.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nmmapper/wappalyzer",
    project_urls={
        'Documentation': 'https://github.com/nmmapper/wappalyzer',
        'How it is used': 'https://www.nmmapper.com/sys/cms-detection/wappalyzer-online/',
        'Homepage': 'https://github.com/nmmapper/wappalyzer',
        'Source': 'https://github.com/nmmapper/wappalyzer',
    },
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data        =   {'webappalyzer': ['data/technologies.json']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['wheel'],
    install_requires=['beautifulsoup4', 'lxml', 'cached_property', 'requests', 'aiohttp','dom_query'],
)
