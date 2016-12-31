from vagrant import Vagrant

def start():
  v = Vagrant()
  v.up()
  return v

