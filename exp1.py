import subprocess
python2_command = "git status"
process = subprocess.Popen(python2_command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
networks=(output.strip()).decode()
print(networks)