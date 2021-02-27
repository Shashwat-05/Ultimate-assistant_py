from os import system as run


def status(cmd):
    op=getstatusoutput(cmd)
    return op
def c():
    run('clear')
def s(timer):
    run(f'sleep {timer}')
def tc(color):
    run(f'tput setaf {color}')


def aws():
    laws=True
    while laws :
        c()
        tc(1)
        run('tput bold')#aws menu
        i1 = input('''
                        ___________________________
                        |   press 1 : ec2         |
                        |   press 2 : ebs         |
                        |   press 3 : iam user    |
                        |   press 4 : s3          |
                        |   press 5 : cloud front |
                        |   press 6 : snapshot    |
                        |   press b : prev menu   |
                        """""""""""""""""""""""""""
        enter the option : ''')

        if i1=='b':
            laws=False #back to main menu

#-------------------------------------ec2-------------------------------------------
        elif i1=='1' :
            laws1=True
            while laws1:
                c()
                tc(3)
                run('tput bold')
                i2=input('''
                        _______________________________
                        |   press 1 : instances       |
                        |   press 2 : security groups |
                        |   press 3 : key-pair        |
                        |   press b : prev menu       |
                        """""""""""""""""""""""""""""""
          enter the option : ''')
                if i2=='1':
                    m=True
                    while m:
                        tc(6)
                        c()
                        run('tput bold')
                        i3=input('''
                        ____________________________________
                        |   press 1 : launch instances      |
                        |   press 2 : show instances        |
                        |   press 3 : terminate instances   |
                        |   press 4 : start instances       |
                        |   press 5 : stop instances        |
                        |   press b : prev menu             |    
                        """""""""""""""""""""""""""""""""""""
                 enter the option : ''')
                        if i3=='1':
                            count = int(input('enter the amount of instances:'))
                            image = input('provide the image ID pls:')
                            kname = input('enter key name:')
                            sid = input('enter the security group id :')
                            run(f'aws ec2 run-instances --image-id {image} --instance-type t2.micro --key-name {kname} --security-group-ids {sid} --count {count}  ')
                            print('instanced launched successfully')

                        elif i3=='2':
                            t=input('all/particular?')
                            if t=='all':
                                run('aws ec2 describe-instances')
                            else:
                                g = input('enter instance ID : ')
                                run(f'aws ec2 describe-instances --instance-ids {g}')

                        elif i3=='3':
                            rmid=input('enter the instance id to remove : ')
                            run(f'aws ec2 terminate-instances {rmid}')
                            #remove instance
                        elif i3== '4':
                            iid = input('enter instance id/s :')
                            run(f'aws ec2 start-instances  --instance-ids {iid}')
                            print('instance started successfully....')
                        elif i3=='5':
                            iid = input('enter instance id/s :')
                            run(f'aws ec2 stop-instances  --instance-ids {iid}')
                            print('instance stopped successfully....')
                        elif i3=='b':
                            m=False
                        else:
                            print('wrong input! try again.')

                elif i2=='2':
                    tc(7)
                    sgname = input('enter security group name to add :')
                    dpt = input('fill the description :')
                    print('creating security group')
                    run(f'aws ec2 create-security-group --description {dpt} --group-name {sgname}')
                    print('created security group successfully')
                elif i2=='3':
                    tc(1)
                    kname = input('enter key name to add :')
                    print('creating new key pair')
                    run(f'aws ec2 create-key-pair --key-name {kname}  --output text > {kname}.pem')
                    print('key pair created successfully')

                elif i2=='b':
                    laws1=False
                else:
                    print('wrong input ! try again.')


#---------------------------------ebs-------------------------------------------------------------

        elif i1=='2':
            l=True
            while l:
                tc(3)
                c()
                run('tput bold')
                izz=input('''
		        ______________________________
		        |   press 1 : create volume  |
		        |   press 2 : add volume     |
		        |   press b:  prev menu      |
		        """"""""""""""""""""""""""""""
                enter a option : ''')

                if izz=='1':
                    tc(7)
                    az = input('enter the availability zone :')
                    vsize = input('enter the volume size [min 1 gb] :')
                    print('creating new volume ')
                    run(f'aws ec2 create-volume --volume-type gp2 --size {vsize} --availability-zone {az}  ')
                    print('created new volume successfully ')

                elif izz=='2':
                    tc(4)
                    inid = input('which instance [id]:')
                    vid = input('volume to attach [id] :')
                    de = input('enter the name of device [sd<f-p>] :')
                    print(' attaching new volume')
                    run(f'aws ec2 attach-volume --device {de} --instance-id {inid}  --volume-id {vid}')
                    print(' volume attached successfully')
                elif izz=='b':
                    l=False
                else:
                    print('wrong input! try again.')
#-------------------------------------iam----------------------------------------------

        elif i1=='3':
            l=True
            while l:
                c()
                tc(5)
                run('tput bold')
                iz=input('''
		        ___________________________________
		        |   press 1 : create user         |
		        |   press 2 : create access-key   |
		        |   press b : prev menu           |
		        """""""""""""""""""""""""""""""""""
                enter a option : ''')
                if iz=='1':
                    tc(7)
                    uname = input('enter username to add :')
                    print('creating new user')
                    run(f'aws iam create-user --user-name {uname}')
                    print('created new IAM user successfully')
                elif iz=='2':
                    tc(4)
                    kuname = input('enter access key username  :')
                    print('creating new access key')
                    run(f'aws iam create-access-key --username {kuname}')
                    print('created a new access key successfully')
                elif iz=='b':
                    l=False
                else:
                    print('wrong input! try again.')

#---------------------------------------s3------------------------------------------
        elif i1=='4':
            l=True
            while l:
                tc(1)
                c()
                run('tput bold')
                s3=input('''
		        ______________________________________
		        |   press 1 : create bucket          |
		        |   press 2 : add object to a bucket |  
		        |   press b : prev menu              |
		        """"""""""""""""""""""""""""""""""""""
                enter a option : ''')
                if s3=='1':
                    tc(6)
                    bname=input('enter bucket name : ')
                    region=input('enter region : ')
                    run(f'aws s3api create-bucket --bucket {bname} --region {region}')
                elif s3=='2':
                    fp=input('enter bucket name : ')
                    bn=input('enter object  path : ')
                    fname=input('enter the name for this object : ')
                    run(f'aws s3 cp {fp} {s3://}{bn}/{fname}')
                elif s3=='b':
                    l=False
                else:
                    print('wrong input! try again.')

#-----------------------------------------cf----------------------------------------
        elif i1=='5':
            tc(7)
            c()
            dn=input('''
[press b for prev menu]
enter the domain name : ''')
            if dn=='b':
                continue
            else:
                run(f'aws cloudfront create-distribution --origin-domain-name {dn}')


#--------------------------------------snapshot-----------------------------------
        elif i1=='6':
            c()
            dn=input('''
[press b for prev menu]
enter the domain name : ''')
            if dn=='b':
                continue
            else:
                run(f'aws cloudfront create-distribution --origin-domain-name {dn}')
        else:
            print('wrong option! try again.')




