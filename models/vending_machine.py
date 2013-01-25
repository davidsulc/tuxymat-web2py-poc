db.define_table('vending_machine',
   Field('serial_number', 'string', required=True, unique=True),
   Field('purchase_price', 'decimal(6,2)'),
   Field('age_verification', 'boolean'),
   format = '%(serial_number)s')
   