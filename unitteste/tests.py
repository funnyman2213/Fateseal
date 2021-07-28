import sys
sys.path.append('..')

import fateseal

all_bulk_data = fateseal.request.bulkdata.All().get()

if not isinstance(all_bulk_data, fateseal.models.Error):
    for thing in all_bulk_data:
        print(thing)

card_name_catalog = fateseal.request.catalog.CardNames().get()