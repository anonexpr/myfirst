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
    print("Executing on %s as %s" % (env.host, env.user))
    conf_dir = '/tmp/flume-id/conf-tw'
    with settings(warn_only=True):
         if run("test -d %s" % (conf_dir)).failed:
         #if run("test -d /tmp/flume-id/conf-tw").failed:
            abort("%s is missing" % (conf_dir))
         with cd('/tmp/flume-id'):
              run('ls')
        #run('rm -rf /tmp/flume-id/conf-tw')
    

def host_type():
   run('uname -s')
   port_number = prompt("Which port would you like to use?")
   print port_number
   with cd("/tmp"):
        run("ls")
