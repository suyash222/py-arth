import os
from subprocess import Popen, PIPE

def parcreate():

    os.system('clear')

    dname = input("Enter hard disk name: ")
    size = input("Enter size hard disk size(eg 1gb): ")

    ec = f"n\n\n\n\n+{size[:-1].upper()}\nw"

    p1 = Popen(['echo','-e', ec], stdout=PIPE)
    p2 = Popen(['fdisk', dname], stdin=p1.stdout, stdout=PIPE)

    p1.stdout.close()
    out, err = p2.communicate()
