from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

#env.hosts = ['muruganramas01@192.168.56.101','ramaswamy.murugan@192.168.56.102','root@192.168.56.103']

env.roledefs = {
   'servers': ['muruganramas01@192.168.56.101','ramaswamy.murugan@192.168.56.102'],
   'clients': ['root@192.168.56.103']
}

@roles('servers')
def remove_tw_conf():
    run('rm -rf /tmp/flume-id/conf-tw')
    

def host_type():
   run('uname -s')
   port_number = prompt("Which port would you like to use?")
   print port_number
   with cd("/tmp"):
        run("ls")
