import subprocess

output = subprocess.check_output('ps -ef', shell=True).decode().split("\r\n")
pids = [ line.split()[1] for line in output if 'chrome.exe' in line]

for pid in pids:
    subprocess.call('ps -ef /f /pid' + pid)


## The above program is a summarized version of below code; provides same output as below;

#print(type(output))
#output = output.decode()
#print(type(output))
#print(output[:500])
#print(len(output))

#output_lines = output.split("\r\n")
#print(type(output_lines))
#print(output_lines[:5])
#print(len(output_lines))

#chrome_lines = list(filter(lambda x : 'chrome.exe' in x , output_lines))
#print(len(chrome_lines))
#print(chrome_lines)
#chrome_lines = [ line for line in output_lines if 'chrome.exe' in line]
#print(len(chrome_lines))
#print(chrome_lines)

#pids = list(map(lambda x : x.split()[1], chrome_lines))
#print(pids)
#pids = [line.split()[1] for line in chrome_lines]
#print(pids)

#for pid in pids:
#   subprocess.call('ps -ef /f /pid ' + pid)