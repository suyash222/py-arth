import lv_display, lv_utility
import sys, os

end_color = "\033[0;38;49m\033[39;49m "
bright_cyan = "\033[1;96;49m"


def lvm_main():
    while True:

        os.system('clear')
        print(bright_cyan, """
    ██╗    ██╗   ██╗███╗   ███╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ██║    ██║   ██║████╗ ████║    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██║    ██║   ██║██╔████╔██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║    ╚██╗ ██╔╝██║╚██╔╝██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ███████╗╚████╔╝ ██║ ╚═╝ ██║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚══════╝ ╚═══╝  ╚═╝     ╚═╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
        """, end_color)

        print("""
    1).List all disk
    2).List Physical volume
    3).List Volume Group
    4).List Logical Volume
    5).Create Physical Volume
    6).Create Volume Group
    7).Create Logical Volume
    8).Extend Volume Group
    9).Extend Logical Volume
    10).Erase Physical Volume
    11).Erase Volume Group
    12).Erase Logical Volume
    13).Shrink Volume Group
    14).Shrink Logical Volume
    15).Go Back""")

        n = input("Enter your choice: ")

        if(n == '1'):
            lv_display.fdiskdisplay()

        elif(n == '2'):
            print("All or specific Physical Volume", "0)for all", "1)for specific", sep='\n')
            output = input("Enter option: ")
            lv_display.pvdisplay(output)

        elif(n== '3'):
            print("All or specific Volume Group", "0)for all", "1)for specific", sep='\n')
            output = input("Enter option: ")
            lv_display.vgdisplay(output)

        elif(n== '4'):
            print("All or specific Logical volume", "0)for all", "1)for specific", sep='\n')
            output = input("Enter option: ")
            lv_display.lvdisplay(output)

        elif(n == '5'):
            lv_utility.pvcreate()

        elif(n == '6'):
            lv_utility.vgcreate()

        elif(n == '7'):
            lv_utility.lvcreate()

        elif(n == '8'):
            lv_utility.vgextend()

        elif(n == '9'):
            lv_utility.lvextend()

        elif(n == '10'):
            lv_utility.pvremove()

        elif(n == '11'):
            lv_utility.vgremove()

        elif(n == '12'):
            lv_utility.lvremove()

        elif(n == '13'):
            lv_utility.vgshrink()

        elif(n == '14'):
            lv_utility.lvshrink()

        elif(n == '15'):
            break

        else:
            print("Wrong Option")

        input("Press Enter to continue")
        os.system('clear')
