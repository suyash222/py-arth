import os, subprocess, sys

def installer():

    dire = input("Enter Directory where is software: ")

    os.chdir(dire)
    a = os.listdir()

    print()
    print(*a, sep='\n')
    print()

    i = input("Enter line number: ")

    i = a[int(i) - 1]
    proc = subprocess.Popen(['rpm', '-i', i, '--force'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = proc.communicate()

    out = out.decode(sys.stdout.encoding)
    err = err.decode(sys.stdout.encoding)

    proc = subprocess.Popen(['rpm', '-q', i,], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = proc.communicate()
    out = out.decode(sys.stdout.encoding)
    err = err.decode(sys.stdout.encoding)

    if not err:
        print(f"{i} is successfully installed")

    else:
        print(err)
