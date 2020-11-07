import sys, subprocess

def vgextend():
    vg_name = input("Enter drive name: ")
    pv_name = input("Enter PV name: ")

    proc = subprocess.Popen(['vgextend', vg_name, pv_name])

    proc.communicate()

def lvextend():
    lv_name = input("Enter logical volume name: ")
    size = input("Enter logical volume size to increases (eg 2gb): ")
    vg_name = input("Enter volume group name: ")

    name = f'{vg_name}/{lv_name}'
    size = f'+{size[:-1:].upper()}'

    proc = subprocess.Popen(['lvcreate', '--size', size, '--name', name])
    proc.communicate()

def vgshrink():
    vg_name = input("Enter drive name: ")
    pv_name = input("Enter PV name: ")

    proc = subprocess.Popen(['vgreduce', vg_name, pv_name])

    proc.communicate()

def lvshrink():
    lv_name = input("Enter logical volume name: ")
    size = input("Enter logical volume size to increases (eg 2gb): ")
    vg_name = input("Enter volume group name: ")

    name = f'{vg_name}/{lv_name}'
    size = f'-{size[:-1:].upper()}'

    proc = subprocess.Popen(['lvreduce', '--size', size, '--name', name])
    proc.communicate()

def vgremove():

    vg_name = input("Enter drive name to remove: ")
    pv_name = input("Enter PV name: ")
    proc = subprocess.Popen(['vgremove', vg_name, pv_name])
    proc.communicate()

def pvremove():

    name = input("Enter drive name: ")
    proc = subprocess.Popen(['pvremove', name])
    proc.communicate()


def lvremove():
    lv_name = input("Enter logical volume name: ")
    vg_name = input("Enter volume group name: ")

    name = f'{vg_name}/{lv_name}'

    proc = subprocess.Popen(['lvremove', name])
    proc.communicate()

def vgcreate():
    vg_name = input("Enter drive name: ")
    pv_name = input("Enter PV name: ")

    proc = subprocess.Popen(['vgcreate', vg_name, pv_name], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    out, error = proc.communicate()
    error = error.decode(sys.stdout.encoding)

    if (out):
        print("The volume group been successfully created")


    if("exists" in error):
        print("A volume group called {vg_name} already exists")

    elif("filter" in error):
        drive = error[error.rindex('Device')+6:error.index("excluded") -2:].strip()
        print(f"The drive {drive} can't be used for volume group")

    else:
        print(error.split('\n')[0].strip())

def pvcreate():
    name = input("Enter drive name: ")

    proc = subprocess.Popen(['pvcreate', name], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out, error = proc.communicate()

    error = error.decode(sys.stdout.encoding)

    if (out):
        print("The physical volume been successfully created")

    if("filter" in error):
        drive = error[error.rindex('Device')+6:error.index("excluded") -2:].strip()
        print(f"The drive {drive} can't be used for creating physical volume")

    elif("initialize" in error):
        drive = error[error.index('"')+1:error.index("of") -2:].strip()
        vg = error[error.rindex('group')+7:error.rindex('"'):].strip()
        print(f"The drive {drive} is already the part of volume group {vg}")

    elif("not found" in error):
        print(error.strip())

def lvcreate():
    lv_name = input("Enter logical volume name: ")
    size = input("Enter logical volume size eg (2gb): ")
    vg_name = input("Enter volume group name: ")

    size = size[:-1:].upper()

    proc = subprocess.Popen(['lvcreate', '--size', size, '--name', lv_name, vg_name], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out, error = proc.communicate()

    error = error.decode(sys.stdout.encoding)

    if (out):
        print("The logical volume been successfully created")

    if("space" in error):
        print(error[:error.index("space") +5:].strip())

    else:
        print(error.split('\n')[0].strip())
