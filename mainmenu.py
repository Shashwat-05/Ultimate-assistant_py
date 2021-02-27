from os import system as run
#import dockermenu
#import tools
#import awsmenu
#import hadoop
from subprocess import getstatusoutput


def status(cmd):
    op=getstatusoutput(cmd)
    return op
def c():
    run('clear')

def tc(color):
    run(f'tput setaf {color}')

#-------------------------------------------local-main-menu------------------------------------------------
def lmenu():
    localloop=True
    while localloop:
        c()
        run('tput bold')
        tc(2)
        i=input('''
		__________________________________    
		|    welcome to the py-menu      |
		|--------------------------------|
		|   Press 1: Hadoop              |   
		|   Press 2: Docker              |
		|   Press 3: AWS                 |
		|   Press 4: Ansible             |
		|   Press 5: Other Tools         |
		|   Press b: prev menu           |
		""""""""""""""""""""""""""""""""""
        Enter your option : ''')
        c()
        tc(6)
        if i == '1' :
            hdp=status('hadoop version')
            jdk=status('jps')
            if jdk[0]!=0:
                print('downloading jdk.rpm ......')
                run('wget https://hadoopdocker.s3.us-east-2.amazonaws.com/hadoop/jdk-8u171-linux-x64.rpm')

            if hdp[0]!=0:
                print('downloading hadoop.rpm ..........')
                run('wget https://hadoopdocker.s3.us-east-2.amazonaws.com/hadoop/hadoop-1.2.1-1.x86_64.rpm')
            import hadoop
            hadoop.hadoop_setup()

        elif i=='2':
            dkr=status('docker --version')
            if dkr[0]!=0:
                print('downloading docker repository.....')
                run('rm -f /etc/yum.repo.d/docker.repo')
                run('wget https://hadoopdocker.s3.us-east-2.amazonaws.com/docker/docker.repo -o /etc/yum.repos.d/')
            import dockermenu
            dockermenu.docker_menu()

        elif i=='3':
            aws=status('aws --version')
            if aws[0]!=0:
                run('wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip')
                run('unzip awscli-exe-linux-x86_64.zip')
                run('./aws/install')
            import awsmenu
            awsmenu.aws()

        elif i=='4':
            import ansiblee
            ansible=status('ansible --version')
            if ansible[0]!=0:
                print('installing ansible......')
                run('pip3 install ansible')
            ansiblee.ansible_menu()

        elif i=='5':
            import tools
            tools.tools_menu() #python tools menu 

        elif i=='6':
            k8s.k8smenu() #kubernetes menu
        elif i=='b':
            localloop=False

        else:
            print('Wrong option! Try Again...')

def rmenu():
    #rlogin
    ip=input('enter the IP of server : ')
    passwd=input('enter the pass')
    ll=True
    while ll:
        c()
        run('tput bold')
        i = input('''
		__________________________________    
		|    welcome to the py-menu      |
		|''''''''''''''''''''''''''''''''|
		|   Press 1: Hadoop              |   
		|   Press 2: Docker              |
		|   Press 3: AWS                 |
		|   Press 4: Ansible             |
		|   Press 5: Other Tools         |
		|   Press b: prev menu           |
		""""""""""""""""""""""""""""""""""
        Enter your option : ''')
        c()
        if i == '1':
            hdp = status('hadoop --version')
            jdk = status('jdk --version')
            if jdk[0] != 0:
                print('downloading jdk.rpm from s3 bucket')
                wb('http://d3qdlzfkcnorle.cloudfront.net/hadoop/jdk-8u171-linux-x64.rpm')

            if hdp[0] != 0:
                print('downloading hadooop.rpm from s3 bucket')
                wb('http://d3qdlzfkcnorle.cloudfront.net/hadoop/hadoop-1.2.1-1.x86_64.rpm')
            # hadoop_menu()


        elif i == '2':
            dkr = status('docker --version')
            if dkr[0] != 0:
                print('downloading docker repo')
                run('rm /etc/yum.repo.d/docker.repo')
                wb('http://de9thero5n994.cloudfront.net/docker/docker.repo')
            # docker_menu()


        elif i == '3':
            aws = status('aws --version')
            if aws[0] != 0:
                run('wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip')
                run('unzip awscli-exe-linux-x86_64.zip')
                run('./aws/install')
            # aws_menu


        elif i == '4':
            ansible = status('ansible --version')
            if ansible[0] != 0:
                print('installing ansible......')
                run('pip3 install ansible')
            # ansible_menu()
        elif i == '5':

            print('ml()')

        elif i == 'x':
            ll = False

        else:
            print('Wrong option! Try Again...')


while True:
    c()
    login=input('\n(Type "exit" to leave)\nwhat kinda login is required ? [local/remote] : ')
    if login=='local':
        lmenu()
    elif login=='remote':
        rmenu()
    elif login=='exit':
        tc(1)
        print('\n\n\n closing the application....')
        run('sleep 3')
        tc(7)
        break
    else:
        print(' wrong input ...try again')
