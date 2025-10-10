import subprocess
user_cmd = input("Command to run: ")
subprocess.check_output(f"echo result && {user_cmd}", shell=True)  # BAD
