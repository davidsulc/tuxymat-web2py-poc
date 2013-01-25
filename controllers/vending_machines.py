def index():
    vending_machines = db().select(db.vending_machine.ALL, orderby=db.vending_machine.serial_number)
    return dict(vending_machines=vending_machines)
  
def show():
  vending_machine = db.vending_machine(request.args(0,cast=int)) or redirect(URL('index'))
  #db.post.image_id.default = image.id
  #form = SQLFORM(db.post)
  #if form.process().accepted:
      #response.flash = 'your comment is posted'
  #comments = db(db.post.image_id==image.id).select()
  #return dict(image=image, comments=comments, form=form)
  return dict(vending_machine=vending_machine)
