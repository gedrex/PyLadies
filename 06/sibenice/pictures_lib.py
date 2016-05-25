#!/usr/bin/python3.4
def fault1():
    return '\n~~~~~~~\n------------------'

def fault2():
    return '\033[1;31m\n|\n|\n|\n|\n|\033[1;m' + fault1()

def fault3():
    return '\033[1;31m+---.\033[1;m' + '\n|\n|\n|\n|\n|' + fault1()

def fault4():
    return '+---.\n|   \033[1;31m|\033[1;m\n|\n|\n|\n|' + fault1()

def fault5():
    return '+---.\n|   |\n|   \033[1;31mO\033[1;m\n|\n|\n|' + fault1()

def fault6():
    return '+---.\n|   |\n|   O\n|   \033[1;31m|\033[1;m\n|\n|' + fault1()

def fault7():
    return '+---.\n|   |\n|   O\n| \033[1;31m--\033[1;m|\n|\n|' + fault1()

def fault8():
    return '+---.\n|   |\n|   O\n| --|\033[1;31m--\033[1;m\n|\n|' + fault1()

def fault9():
    return '+---.\n|   |\n|   O\n| --|--\n|  \033[1;31m/\033[1;m\n|' + fault1()

def fault10():
    return '+---.\n|   |\n|   O\n| --|--\n|  / \033[1;31m\\033[1;m \n|' + fault1()

def fault10():
    return '\033[1;31m+---.\n|   |\n|   O\n| --|--\n|  / \ \n|\n' + fault1() + '\033[1;m'

def fault(num):
    faults = [fault1(), fault2(), fault3(), fault4(), fault5(), fault6(), fault7(), fault8(), fault9(), fault10()] 
    return faults[num]
