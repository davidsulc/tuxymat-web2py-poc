db.define_table('vending_machine',
   Field('serial_number', 'string', required=True, unique=True),
   Field('purchase_price', 'decimal(6,2)'),
   Field('age_verification', 'boolean'),
   format = '%(serial_number)s')
   
db.vending_machine.requires = IS_NOT_EMPTY()
db.vending_machine.serial_number.requires = IS_NOT_IN_DB(db, 'vending_machine.serial_number')
db.vending_machine.purchase_price.requires = [IS_FLOAT_IN_RANGE(0.01, 9999.99)]

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)
