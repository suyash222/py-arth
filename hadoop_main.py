import hadoop_config, os, subprocess, sys, pathlib

end_color = "\033[0;38;49m\033[39;49m "
bright_cyan = "\033[1;96;49m"

def hadoop_main():

    while True:
        os.system('clear')
        print(f"""{bright_cyan}
    ██╗  ██╗ █████╗ ██████╗  ██████╗  ██████╗ ██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ██║  ██║██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ███████║███████║██║  ██║██║   ██║██║   ██║██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██╔══██║██╔══██║██║  ██║██║   ██║██║   ██║██╔═══╝     ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ██║  ██║██║  ██║██████╔╝╚██████╔╝╚██████╔╝██║         ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝         ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
    {end_color}

    1). To name node setup
    2). To data node setup
    3). To client setup
    4). To see cluster report
    5). To List file in cluster
    6). To Upload file in cluster
    7). To Delete file in cluster
    8). Back to Main menu
        """)

        ch = input("Enter your choice: ")

        if ch == '1':

            while True:
                dire = input("Enter directory name: ")
                cdir = os.path.join(os.curdir, dire)
                print(f"Hadoop Namenode directory is {cdir}, (yes or no)")
                y = input("enter yes or no: ")
                if y != 'yes':
                    continue
                break

            hadoop_config.hdfs('name', cdir)
            ip = input("Enter master ip address (default 0.0.0.0): ")

            if not ip:
                print("IP 0.0.0.0 is going to use")
                ip = '0.0.0.0'

            port = input("Enter master port number (default 9001): ")

            if not port:
                print("Port Number 9001 is going to use")
                port = 9001
            hadoop_config.core(ip, port)
            hadoop_config.start('namenode')

        elif ch == '2':

            while True:
                dire = input("Enter directory name: ")
                cdir = os.path.join(os.curdir, dire)
                print(f"Hadoop Datanode directory is {cdir}, (yes or no)")
                y = input("enter yes or no: ")
                print(y)
                if y != 'yes':
                    continue
                break

            hadoop_config.hdfs('data', cdir)
            ip = input("Enter master ip address: ")
            port = input("Enter master port number: ")

            hadoop_config.core(ip, port)
            hadoop_config.start('datanode')

        elif ch == '3':

            ip = input("Enter master ip address: ")
            port = input("Enter master port number: ")
            hadoop_config.core(ip, port)

        elif ch == '4':
            try:
                out = subprocess.run(['hadoop', 'dfsadmin', '-report'], timeout=7, stdout=subprocess.PIPE)

            except subprocess.TimeoutExpired:
                print("Timeout unable to retrive cluster information:")

            else:
                print(out.stdout.decode(sys.stdout.encoding))

        elif ch == '5':
            dire = input("Enter base directory name (default /): ")
            if not dire:
                print("/ directory is selected")
                dire = '/'

            try:
                out = subprocess.run(['hadoop', 'fs', '-ls', dire], timeout=10, stdout=subprocess.PIPE)

            except subprocess.TimeoutExpired:
                print("Timeout unable to retrive cluster information:")

            else:
                print(out.stdout.decode(sys.stdout.encoding))

        elif ch == '6':

            dire = input("Enter base directory name (default /): ")
            if not dire:
                print("/ directory is selected")
                dire = '/'

            while True:
                fname = input("Enter file name and path: ")

            if  not pathlib.Path.is_file(fname):
                print(f"{fname} does not exists\nEnter file again")
                continue

            try:
                out = subprocess.run(['hadoop', 'fs', '-put', fname, dire], stdout=subprocess.PIPE)

            except subprocess.TimeoutExpired:
                print("Timeout unable to upload file in cluster")

            else:
                print(out.stdout.decode(sys.stdout.encoding))

        elif ch == '7':

            fname = input("Enter file name to delete: ")

            try:
                out = subprocess.run(['hadoop', 'fs', '-rm', fname], stdout=subprocess.PIPE)

            except subprocess.TimeoutExpired:
                print("Timeout unable to upload file in cluster")

            else:
                print(out.stdout.decode(sys.stdout.encoding))

        elif ch == '8':
            break

        else:
            print("Wrong choice")

        input("Enter to continue")
        os.system('clear')
