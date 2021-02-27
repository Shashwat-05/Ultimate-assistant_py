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

def hadoop_setup():
    hdp=True
    while hdp:
        run('tput bold') 
        c()
        tc(3)
        hmenu=input("""
                __________________________________
		| Press 1: Datanode Setup        |
		| Press 2: Namenode Setup        |
		| Press 3: I am a Client !       |
		| Press 4: Cluster Report        |
		| Press 5: Start/Stop Datanode   |
		| Press 6: Start/Stop Namenode   |
		| Press b: prev menu             |
                ----------------------------------
enter the option :""")
        tc(7)
        if hmenu=='1':
            c()
            jdk = status("jps")
            if jdk[0]==127:
                print("jdk installing")
                run("rpm -ivh jdk-8u171-linux-x64.rpm")
            else:
                pass
            hdp_ = status("hadoop version")
            if hdp_[0]==127:
                run("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
            else:
                pass
            c()
            tc(2)
            lvm=input('make dynamic storage setup of datanode? y/n :')
            if lvm=='y':
                run('lsblk')
                storage_size=int(input("ENTER THE STORAGE SIZE YOU WANT TO SHARE : "))
                run(f"pvcreate {disk_name};vgcreate dn_vg {disk_name};lvcreate --size +{storage_size}G ---name dn_lvm dn_vg;mkfs.ext4 /dev/dn_vg/dn_LVM")
                run('lsblk')
                c()
                tc(1)
                dataip=input("ENTER THE IP ADDRESS OF NAMENODE : ")
                print()
                dataport=int(input("ENTER THE PORT NO :"))
                print()
                datadir=input("ENTER THE DIRECTORY NAME YOU WANT : ")
                run(f"mkdir /{datadir};mount /dev/dn_vg/dn_LVM /{datadir};df -h;echo 3 >/proc/sys/vm/drop_caches")
                c()
                tc(6)  
                datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
                datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{datadir}</value>
</property>
</configuration>''')
                datafile.close()
                datafile1=open("/etc/hadoop/core-site.xml", 'w')
                datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
                datafile1.close()
                c()
                tc(5)
                dnstart=input('start the datanode ? y/n :')
                if dnstart=='y':
                    run("systemctl stop firewalld;setenforce 0")
                    run("hadoop-daemon.sh start datanode;jps")
                    s(3)
                else:
                    continue
            else:
                tc(4)
                dataip=input("ENTER THE IP ADDRESS OF NAMENODE : ")
                print()
                dataport=int(input("ENTER THE PORT NO :"))
                print()
                datadir=input("ENTER THE DIRECTORY NAME YOU WANT : ")
                run(f"mkdir /{datadir};echo 3 >/proc/sys/vm/drop_caches")
                c()
                tc(7)  
                datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
                datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{datadir}</value>
</property>
</configuration>''')
                datafile.close()
                datafile1=open("/etc/hadoop/core-site.xml", 'w')
                datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
                datafile1.close()
                c()
                tc(6)
                dnstart=input('start the datanode ? y/n :')
                if dnstart=='y':
                    run("systemctl stop firewalld;setenforce 0")
                    run("hadoop-daemon.sh start datanode;jps")
                    s(3)
                else:
                    continue
        elif hmenu=='2': 
            c()
            tc(2) 
            jdk = status("jps")
            if jdk[0]==127:
                print("jdk installing")
                run("rpm -ivh jdk-8u171-linux-x64.rpm")
            else:
                pass
            hadoop_ = status("hadoop version")
            if hadoop_[0]==127:
                status("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
            else:
              pass
            c()
            tc(6)
            nameip=input("\nENTER THE IP ADDRESS TO GIVE MASTER : ")
            nameport=int(input("\nENTER THE PORT NO :"))
            namedir=input("\nENTER THE DIRECTORY NAME YOU WANT : ")
            run(f"rm -rf /{namedir};mkdir /{namedir}")  
            datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
            datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{namedir}</value>
</property>
</configuration>''')
            datafile.close()
            datafile1=open("/etc/hadoop/core-site.xml", 'w')
            datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{nameip}:{nameport}</value>
</property>
</configuration>''')
            datafile1.close()
            c()
            tc(2)
            run("hadoop namenode -format;echo 3>/proc/sys/vm/drop_caches;systemctl stop firewalld;setenforce 0")
            asknn=input('start the namenode ? y/n :')
            if asknn=='y':
                run("hadoop-daemon.sh start namenode")
                run("jps")			
                s(3)
            else:
                pass			
        elif hmenu=='3':
            c()
            tc(1)
            jdk = status("jps")
            if jdk[0]==127:
                print("jdk installing")
                run("rpm -ivh jdk-8u171-linux-x64.rpm")
            else:
                pass
            hadoop_ = status("hadoop version")
            if hadoop_[0]==127:
                run("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
            else:
                pass
            c()
            tc(6)
            dataip=input("ENTER THE IP ADDRESS OF NAMENODE : ")
            dataport=int(input("ENTER THE PORT NO :"))
            datafile1=open("/etc/hadoop/core-site.xml", 'w')
            datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
            datafile1.close()
            c()			
            run("systemctl stop firewalld;setenforce 0")			
            print("\n\n--------------Client Service Started----------")
        elif hmenu=='4':
            tc(6)			
            run("hadoop dfsadmin -report")
            input('Press any key continue :')
        elif hmenu=='5':
            ss=input('''
               press 1 to start datanode
               press 1 to stop datanode
     enter : ''')
            if ss=='1':
                run("hadoop-daemon.sh start datanode;jps")
            else:
                run("hadoop-daemon.sh stop datanode;jps")
        elif hmenu=='6':
            ss=input('''
               press 1 to start namenode
               press 1 to stop  namenode
     enter : ''')
            if ss=='1':
                run("hadoop-daemon.sh start namenode;jps")
            else:
                run("hadoop-daemon.sh stop namenode;jps")
        elif hmenu=='b':
            hdp=False
        else:
            print("Wrong option, try again........")
            c()
			

