import sys
sys.path.append('..')
import fateseal as fs
from fateseal.models import Error



cardstuff = fs.Request[fs.cards.Named.return_type](fs.cards.Named(fuzzy="island")).get()

fs.Request(fs.bulkdata.All()).get()

all_bulk_data = fs.bulkdata.All()

if not isinstance(all_bulk_data, Error):
    for thing in all_bulk_data:
        print(thing)

card_name_catalog = fs.Request[fs.catalog.CardNames.return_type](fs.catalog.CardNames()).get()

if not isinstance(card_name_catalog, Error):
    for i in card_name_catalog:
        print(i)

some_collection = fs.Request[fs.cards.Collection.return_type](fs.cards.Collection(identifiers=[{"name":"Ancient tomb"},{"name":"mox opal"},{"name":"pox"}])).get()

if not isinstance(some_collection, Error):
    for i in some_collection.not_found:
        print("didn't find: ", i)

    for i in some_collection.data:
        print(i)