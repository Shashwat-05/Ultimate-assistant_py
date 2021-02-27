import getpass
from os import system as run
from subprocess import getstatusoutput


def status(cmd):
    op=getstatusoutput(cmd)
    return op
def c():
    run('clear')
def tc(color):
    run(f'tput setaf {color}')


def g_mail():
	# smtplib module send mail
    import smtplib
    TO = input("enter Receiver's email :")
    SUBJECT = input('enter the subject :')
    TEXT = input('enter the text :')

	# Gmail Sign In
    
    gmail_sender = input("enter Sender's email :")
    gmail_passwd = getpass.getpass("enter the sender's password :")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    BODY = '\r\n'.join(['To: %s' % TO,
                    	'From: %s' % gmail_sender,
                    	'Subject: %s' % SUBJECT,
                    	'', TEXT])
    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent successfully')
    except:
        print ('error sending mail !')
        
    server.quit()



def w_app():
    import webbrowser
    new = 2 
    url = "https://web.whatsapp.com/"
    webbrowser.open(url,new=new)

def tools_menu():
    tloop=True
    while tloop:
        c()
        tc(3)
        t1=input('''
	    ________________________________
            | Press 1: Send a Gmail        |
            | Press 2: Send whatsapp text  |
            | Press 3: Join a chat         |
            | Press b: prev menu           |
            """"""""""""""""""""""""""""""""
	enter the option :''')
        c()
        if t1=='b':
            tloop=False

        elif t1=='1':
            tc(1)
            g_mail()
        elif t1=='2':
            tc(7)
            w_app()
        elif t1=='3':
            tc(2)
            import udp_chat
            
        else:
            print('try again....')
