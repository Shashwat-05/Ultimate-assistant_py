from os import system as run
from subprocess import getstatusoutput


def status(cmd):
    op=getstatusoutput(cmd)
    return op
def c():
    run('clear')

def tc(color):
    run(f'tput setaf {color}')

#-----------ansible-menu----------

def ansible_menu():
    aloop=True
    while aloop:
        tc(5)
        c()
        a1=input('''
                 __________________________________
                 | Press 1: yum configuration     |
                 | Press 2: httpd configuration   |
                 | Press 3: docker configuration  |
                 | Press b: prev menu             |
                 """"""""""""""""""""""""""""""""""
        enter the option :''')
        c()
        if a1=='b':
            aloop=False
        elif a1=='1':
            c()
            tc(6)
            run('ansible-playbook /python_menu/yumcfg.yml')
            run('sleep 4')
        elif a1=='2':
            c()
            tc(2)
            run('ansible-playbook /python_menu/httpdcfg.yml')
            run('sleep 4')
        elif a1=='3':
            c()
            tc(3)
            run('ansible-playbook /python_menu/dockercfg.yml')
            run('sleep 4')
        else:
            print('wrong input . try again!!')
   













