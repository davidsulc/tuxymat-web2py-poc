def index():
    vending_machines = db().select(db.vending_machine.ALL, orderby=db.vending_machine.serial_number)
    return dict(vending_machines=vending_machines)