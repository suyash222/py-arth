import hadoop_main, lvm_main, installer, os, fdisk_main

while True:

    print(f"""{lvm_main.bright_cyan}

    ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ████╗ ████║██╔══██╗██║████╗  ██║    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██╔████╔██║███████║██║██╔██╗ ██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
    {lvm_main.end_color}
    1).To install Software
    2).For Hadoop
    3).Create Partition
    4).For LVM
    5).Exit""")

    ch = input("Enter your choice: ")

    if ch == '1':
        installer.installer()

    elif ch == '2':
        hadoop_main.hadoop_main()

    elif ch == '3':
        fdisk_main.parcreate()

    elif ch == '4':
        lvm_main.lvm_main()

    elif ch == '5':
        exit()

    else:
        print("Wrong Choice")

    input("Enter to continue")
    os.system('clear')
