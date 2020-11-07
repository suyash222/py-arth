import sys, subprocess

def vgparse(out):
    
    result = {}
    for line in out.split('\n'):
        line = line.strip()
        if("VG Name" in line):
            result['vg name'] = line[7::].strip()
        if("Alloc" in line):
            result['allocated'] = line[line.rindex('/')::].strip()
        if("Free" in line):
            result['free'] = line[line.rindex('/')::].strip()
    return(result)

def vgdisplay(content='0'):


    if(content != '0'):
        name = input("Enter vg name: ")
        proc = subprocess.Popen(["vgdisplay", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:
        proc = subprocess.Popen(["vgdisplay"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, error = proc.communicate()

    if (not out):
        print(error.decode(sys.stdout.encoding))
        return

    out = out.decode(sys.stdout.encoding).split("  --- Volume group ---")
    out = [i for i in out if i]

    for entry in out:
        lines = vgparse(entry)
        [print (key, value) for key, value in lines.items()]
        print('\n')

def pvparse(out):
    result = {}
    for line in out.split('\n'):
        line = line.strip()
        if("VG Name" in line):
            result['vg name'] = line[7::].strip()
        if("PV Size" in line):
            try:
                result['pv size'] = line[7:line.index('/'):].strip()
            except ValueError:
                result['pv size'] = '0'

        if("PV Name" in line):
            result['pv path'] = line[7::].strip()
    return(result)

def pvdisplay(content='0'):

    if(content != '0'):
        name = input("Physical volume name: ")
        proc = subprocess.Popen(["pvdisplay", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:
        proc = subprocess.Popen(["pvdisplay"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, error = proc.communicate()
    out = out.decode(sys.stdout.encoding).split("  --- Physical volume ---")
    out = [i for i in out if i]

    if(not out):
        print(error.decode(sys.stdout.encoding))
        return

    for entry in out:
        lines = pvparse(entry)
        [print (key, value) for key, value in lines.items()]
        print('\n')

def lvparse(out):
    result = {}
    for line in out.split('\n'):
        line = line.strip()
        if("VG Name" in line):
            result['vg name'] = line[7::].strip()
        if("LV Name" in line):
            result['lv name'] = line[7::].strip()
        if("LV Size" in line):
            result['vg size'] = line[7::].strip()
        if("LV Path" in line):
            result['lv path'] = line[7::].strip()
    return(result)

def lvdisplay(content='0'):

    name = ''

    if(content != '0'):
        name = input("Volume group name: ")
        name += '/' + input("Enter Logical volume name: ")
        proc = subprocess.Popen(["lvdisplay", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:
        proc = subprocess.Popen(["lvdisplay"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, error = proc.communicate()

    out = out.decode(sys.stdout.encoding).split("  --- Logical volume ---")
    out = [i for i in out if i]

    if(not out):
        print(error.decode(sys.stdout.encoding))
        return

    for entry in out:
        lines = lvparse(entry)
        [print (key, value) for key, value in lines.items()]
        print('\n')

def fdisk_parse(out):
    result = {}
    result["Disk name"] = "/dev" + out[:out.index(':')].strip()
    result["Disk Size"] = out[out.index(':')+1:out.index(','):].strip()
    return(result)

def fdiskdisplay():

    proc = subprocess.Popen(["fdisk", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = proc.communicate()

    if(not out):
        print(error.decode(sys.stdout.encoding))
        return

    out = out.decode(sys.stdout.encoding).split("Disk /dev")
    out = [i for i in out if i]

    for entry in out:
        lines = fdisk_parse(entry)
        [print (key, value) for key, value in lines.items()]
        print('\n')
