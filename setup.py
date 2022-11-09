import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

project_urls = {
    'Homepage': 'https://github.com/D1ffic00lt/textbytesencoder',
    "Source": 'https://github.com/D1ffic00lt/textbytesencoder'
}

setuptools.setup(
    name="textbytesencoder",
    version="0.1.9",
    description="See README.md",
    url="https://github.com/D1ffic00lt/textbytesencoder",
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls=project_urls
)
