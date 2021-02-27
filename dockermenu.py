from os import system as run
from subprocess import getstatusoutput


def status(cmd):#result,output
    op=getstatusoutput(cmd)
    return op
def c():#clear screen
    run('clear')

def tc(color):#terminal color
    run(f'tput setaf {color}')

def s(timer):#hold screen
    run(f'sleep {timer}')

def docker_menu():


    ld=True
    while ld:
        tc(1)
        c()
        run('tput bold')
        inp = input('''
                    ________________________________
                    |   press 1: Docker configure  |
                    |   press 2: Launch a container|
                    |   press 3: Docker Images     |
                    |   press 4: Docker container  |
                    |   press 5: Docker logs       |
                    |   press b: back to main menu |
                    """"""""""""""""""""""""""""""""
        Enter the option : ''')
                                 #docker configure block
        if inp=='1':
            
            ld1=True
            while ld1:
                tc(2)
                c()
                run('tput bold')
                inp1 = input('''
	             _________________________________________
	             |   press 1: Install docker             |
	             |   press 2: Uninstall docker           |
	             |   press 3: Activate docker services   |
	             |   press 4: deactivate docker services |
	             |   press b: previous menu              | 
	             """""""""""""""""""""""""""""""""""""""""
                Enter the option : ''')
            
                tc(3)
                if inp1=='1':
                    run('yum install docker-ce --skip-broken')
                elif inp1=='2':
                    run('yum remove docker-ce')
                elif inp1=='3' :
                    run('systemctl start docker')
                    run('systemctl status docker')
                    inputd=('make it permanent [y/n]: ')
                    if inputd=='y' :
                        run('systemctl enable docker')


                elif inp1=='4':
                    run(f'systemctl stop docker')
                    run('systemctl status docker')
                    inputd = ('make it permanent [y/n]: ')
                    if inputd == 'y':
                        run('systemctl disable docker')
                elif inp1=='b':
                    ld1=False
                else:
                    print('Wrong option! Try Again.')


                            #launch a container block

        elif inp=='2':
            ld2= True
            while ld2:
                tc(6)
                run('tput bold')
                c()
                images=status('docker images')
                print('available images',images[1])
                osimg=input('''
                *press b: previous menu*
                enter the proper image name : ''')
                if osimg=='b':
                    ld2=False
                else:
                    tc(4)
                    osname=input('enter your OS name :')
                    use=input('need customisation? yes/no! :')

                    if use=='no' or use=='No' or use=='NO':
                        run(f'docker run -it --name {osname} {osimg}')
                        print(' container launched succesfully......')
                        run('docker ps -a')
                        
                        
                        s(3)
                    else:
                        tc(6)
                        typ=input('''available customisation
                        1.detached container
                        2.one time container 
                        3.single process container 
                        press \'23\' for opt2 + opt3
                        press the option : ''')
                        if typ=='1':
                            run(f'docker run -dit --name {osname} {osimg}')
                            print('container launched succesfully')
                        elif typ=='2':
                            run(f'docker run -rit --name {osname} {osimg}')
                        elif typ=='23':
                            pro=input('enter one time process name :')
                            run(f'docker run -rit --name {osname} {osimg} {pro}')
                        elif typ=='3':
                            pro=input('enter the process name :')
                            run(f'docker run -it --name {osname} {osimg} {pro}')
                        else:
                            print('Wrong Input!Try Again.')




                            #docker image block

        elif inp=='3':
            ld3=True
            while ld3:
                run('tput bold')
                c()
                tc(7)
                img=input('''
			 ____________________________________________________                        
			 |   Press 1: Show all docker images in the system  |
			 |   Press 2: Search for docker images              |
			 |   Press 3: Download a docker image               |
			 |   Press 4: Upload your docker image              |
			 |   Press 5: Remove an image                       |
			 |   Press b: previous menu                         | 
			 """"""""""""""""""""""""""""""""""""""""""""""""""""
                 Enter a option : ''')
                if img=='b':
                    ld3=False
                    c()
                elif img=='1':
                    run('docker images')
                    s(4)
                elif img=='2':
                    iname=input('enter the image name to search : ')
                    run(f'docker search {iname}')
                    s(3)
                elif img=='3':
                    imgd=input('enter the image name to download [latest by default] : ')
                    run(f'docker pull {imgd}')
                    run('docker images')
                    s(3)
                elif img=='4':
                    print('login to docker hub first ..........')
                    run('docker login')
                    imgu=input('enter the name of image to upload [should be pressent in the system ] :')
                    run(f'docker push {imgu}')
                elif img=='5':
                    rmi=input('enter the image name/ID to delete')
                    run(f'docker rmi -f {rmi}')
                else:
                    print('Wrong Input! Try Again.')




                        #docker container block

        elif inp=='4':
            ld4=True
            while ld4:
                run('tput bold')
                c()
                tc(1)
                dc=input('''    
                _____________________________________________________________    
                |   press 1: show all running containers                    |
                |   press 2:show all the container present in the system    |    
                |   press 3:remove a container                              |
                |   press 4:remove all containers                           |
                |   press 5: create an image out of a container             |
                |   press b: Previous menu                                  |
                """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                Enter the option : ''')
                if dc=='b':
                    ld4=False
                elif dc=='1':
                    run('docker ps')
                    s(5)
                elif dc=='2':
                    run('docker ps -a')
                    s(5)
                elif dc=='3':
                    cname=input('enter container name to remove :')
                    run(f'docker rm -f  {cname}')
                    s(2)
                elif dc=='4':
                    run('docker rm -f `docker ps -aq`')
                    s(3)
                elif dc=='5':
                    cname=input('enter the container name to clone :')
                    iname=input('enter your custom  image name:V [eg-myOS:version]')
                    run(f'docker commit {cname} {iname}')
                    print('cloning done successfully')
                else:
                    print('Wrong input ! Try Again.')


                                           #docker logs block

        elif inp=='5':
            ld5=True
            while ld5:
                tc(6)
                c()
                run('tput bold')
                cn=input('''
                  [press b for prev menu]
                  enter the container name : ''')
                if cn=='b':
                    ld5=False
                else:
                    run(f'docker logs {cn}')
                                            #exit block

        elif inp=='b':
            ld=False
            c()
                                            #try again block
        else:
            c()
            print('Wrong Input , Try Again!')
            

