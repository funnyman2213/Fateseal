# Fateseal

Fateseal is a python package designed to help wrap the Scryfall API and other various MTG concepts


# Usage

## Requests
Fateseal is split into the endpoints of the Scryfall API. 
You may request different aspects of the Scryfall API with the request sub module, calling the `get()` method the type of data you wish to recive. 

```python
import fateseal.request as req

all_bulk_data = req.bulkdata.All().get()
# returns an ObjList[BulkData]

smothering_t = req.card.Named(fuzzy="smothering t").get()
# returns a Card 
```

All requests have a corisponding `async_get()` method implimented with `aiohttp` to perform asyncronous requests.

## Models

Fateseal exposes the different models and structures of data returned by Scryfall in the models sub module. Considering each request may return an error this is useful for understanding the data returned

```python
import fateseal.models as mod
import fateseal.request as req

non_existant_card = req.card.Named(fuzzy="nonexistant").get()

if not isinstance(non_existant_card, mod.Error):
    # do stuff
else:
    # handle error
```

## Conclusion

Thank you for your interest in fateseal.