import subprocess
import sys

input = sys.argv[1]
output = subprocess.check_output(["./youtube-dl",'-F', input])
lines = output.split('\n')
stream = lines[len(lines)-2].split(' ')[0]
print(stream)
print(input)
downloadCommand = ['./youtube-dl', '-f', stream, input]
subprocess.check_output(downloadCommand)

if(len(sys.argv) < 3):
        print('easy')
else:
        print('hard')
        destFolder = '/home/fredrik/' + sys.argv[2] + '/' + sys.argv[3] + '-'
        nameCommand = ['./youtube-dl', '--get-filename',  input]
        getFilename = subprocess.check_output(nameCommand)
        name = getFilename.strip('\n')
        print(name)
        print(destFolder)
        moveCommand = ['mv', name, destFolder+name]
        subprocess.call(moveCommand)

