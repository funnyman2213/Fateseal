import sys

sys.path.append('..')
import fateseal as fs
from fateseal.models import Error



cardstuff = fs.cards.Search(query='island').get()

if not isinstance(cardstuff, Error):
    test = cardstuff[0]
    print(test)