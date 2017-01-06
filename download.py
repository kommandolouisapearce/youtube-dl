import subprocess
import sys

input = sys.argv[1]
output = subprocess.check_output(["./youtube-dl",'-F', input])

lines = output.split('\n')
stream = lines[len(lines)-2].split(' ')[0]
print(stream)
cmd = ['./youtube-dl', '-f', stream, input]
subprocess.call(cmd)


