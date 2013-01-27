# add gluon to path so it can be included easily
# this si done because web2py wasn't installed and isn't in the pythonpath
import sys
sys.path.append('../../..') # web2py root

from gluon.contrib.webclient import WebClient

client = WebClient('http://127.0.0.1:8000/tuxymat/vending_machines/',
                   postbacks=True)

client.get('index')
assert('ABCDE' in client.text) # uses dev DB ! (incl. already existing data)

data = dict(serial_number = 'ABCDE',
            purchase_price = 10.3
            )
client.post('new',data = data)

data = dict(serial_number = 'ABCDE',
            purchase_price = 10.3
            )
client.post('new',data = data) # doesn't raise error on duplicate record (even though it isn't created due to validation)

data = dict(serial_number = 'ABCDEZZZ',
            purchase_price = 10.3
            )
client.post('new',data = data)

client.get('index')
assert('ABCDEZZZ' in client.text)