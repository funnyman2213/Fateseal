# Fateseal

Fateseal is a python package designed to help wrap the Scryfall API and other various MTG concepts


# Usage

## Requests
Fateseal is split into the endpoints of the Scryfall API. 
You may request different aspects of the Scryfall API with the sub module of the request you'd like to make, calling the `get()` or `async_get()` method after passing the data type you wish to recieve. 

```python
import fateseal as fs

all_bulk_data = fs.bulkdata.All().get()
# returns an ObjList[BulkData].

smothering_t = fs.cards.Named(fuzzy="smothering t").get()
# returns a Card 
```

All requests have a corisponding `async_get()` method implimented with `aiohttp` to perform asyncronous requests.

```python
await smothering_t = fs.cards.Named(fuzzy="smothering t").async_get()
# returns a Card 
```

## Models

Fateseal exposes the different models and structures of data returned by Scryfall in the models sub module. Considering each request may return an error this is useful for understanding the data returned

```python
import fateseal as fs
from fateseal.models import Error

non_existant_card = fs.cards.Named(fuzzy="nonexistant").get()

if not isinstance(non_existant_card, Error):
    # do stuff
else:
    # handle error
```

## Conclusion

Thank you for your interest in fateseal.

