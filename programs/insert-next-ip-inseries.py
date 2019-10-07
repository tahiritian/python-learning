
#Program
ui = input("Enter an ip address: ")
ip = ui.split('.')
if len(ip)!=4:
    print ("Wrong ip format")
    exit (-9)
ip[-1] = str(int(ip[-1]) + 1)
print("Next IP: " , ".".join(ip))


########## Function1  (Change the last IP +1)
#ui = input("Enter an ip address: ")
#ip = ui.split('.')
#ip[-1] = str(int(ip[-1]) + 1)
#print("Next IP: " , ".".join(ip))
#print(b) --> 4 lines will be executed; 5th line program realize an error

#output : function1
#Enter an ip address: 2.2.2.2
#Next IP:  2.2.2.3

##########  Function-2
#if len(ip) !=4     #if length of IP is not equal to 4
#   print ("Wrong ip format")
#  exit (-9)  exit the statement
# un intended else
# elif used in python for IF
# 4 spaces equal to one tab in python, have to use either spaces or tabs throughout the program to be consistence.

#output function-2:
#Enter an ip address: 4.4.4.4.5  --> Five digits instead of 4
#Wrong ip format

