def index():
    vending_machines = db().select(db.vending_machine.ALL, orderby=db.vending_machine.serial_number)
    return dict(vending_machines=vending_machines)
  
def show():
  vending_machine = db.vending_machine(request.args(0,cast=int)) or redirect(URL('index'))
  return dict(vending_machine=vending_machine)
  
def new():
  form = SQLFORM(db.vending_machine)
  if form.process().accepted:
    session.flash = 'The vending machine was created'
    redirect(URL('show', args=form.vars.id))
  return dict(form=form)
  
def edit():
  vending_machine = db.vending_machine(request.args(0,cast=int)) or redirect(URL('index'))
  form = SQLFORM(db.vending_machine, vending_machine)
  if form.process().accepted:
    session.flash = 'The vending machine was updated'
    redirect(URL('show', args=vending_machine.id))
  return dict(vending_machine=vending_machine, form=form)
