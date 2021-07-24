from setuptools import setup

setup(
    name='fateseal',
    packages=['fateseal', 'fateseal.request'],
    version='1.0.0',
    description="A wrapper for using the Scryfall API",
    url='https://github.com/funnyman2213/Fateseal',
    download_url='',
    author='Justin Baker',
    author_email='bakerjobaker.baker30@gmail.com',
    license='MIT',
    keywords=['Scryfall', 'magic', 'the gathering', 'fateseal', 'wrapper'],
    install_requires=['aiohttp','requests','asyncio','pydantic']
)