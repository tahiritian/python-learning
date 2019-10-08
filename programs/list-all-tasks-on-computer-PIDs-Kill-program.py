#tasklist  (mac or linux : ps -ef)
#taskkill /f /pid <pid>   (mac or linux : kill -9 <pid> )

#module used:   subprocess
#take the output and save to python program using stdout/stderr or .check
#output length; output[:500]

#get output not as string, but get as a List of lines;
     #output_lines = output.split("\r\n")
     #print(type)output_lines))
     #print(output[:500])
     #print(len(output))

#from a bunch of lines; just choose related to specific application (i-e, chrome); filter to specific
    #chrome_lines = list(filter(lambda x : 'chrome.exe' in x , output_lines))
    #print(len(chrome_lines))
    #print(chrome_lines)
#---- same can be done using comprehesion;
    #chrome_lines = [ line for line in output_lines if 'chrome.exe' in line]
    #print(len(chrome_lines))
    #print(chrome_lines)


#intrested to specific PID from all lines from chrome list (list all pIDs;
    #pids = list(map(lambda x : x.split()[1], chrome_lines))
    #print(pids)
    #pids = [line.split()[1] for line in chrome_lines]
    #print(pids)


#Kill PID;
#for pid in pids:
 #   subprocess.call('ps -ef /f /pid' + pid)

import subprocess

output = subprocess.check_output('ps -ef', shell=True)
print(type(output))
output = output.decode()
print(type(output))
print(output[:500])
print(len(output))

output_lines = output.split("\r\n")
print(type(output_lines))
print(output_lines[:5])
print(len(output_lines))

chrome_lines = list(filter(lambda x : 'chrome.exe' in x , output_lines))
print(len(chrome_lines))
print(chrome_lines)
chrome_lines = [ line for line in output_lines if 'chrome.exe' in line]
print(len(chrome_lines))
print(chrome_lines)

pids = list(map(lambda x : x.split()[1], chrome_lines))
print(pids)
pids = [line.split()[1] for line in chrome_lines]
print(pids)

for pid in pids:
    subprocess.call('ps -ef /f /pid ' + pid)