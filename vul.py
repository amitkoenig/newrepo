# vulnerable_demo.py
import subprocess
import tarfile

def ping_host():
    # ⚠️ Command injection: untrusted input used in a shell command
    host = input("Enter a host to ping: ")
    subprocess.run(f"ping -c 1 {host}", shell=True)  # BAD: shell=True with user input

def unpack_tar():
    # ⚠️ Tar “path traversal” (a.k.a. TarSlip) if the TAR is untrusted
    tar_path = input("Path to a .tar file to extract: ")
    with tarfile.open(tar_path) as tf:
        tf.extractall("extracted")  # BAD: may write outside ./extracted

if __name__ == "__main__":
    ping_host()
    unpack_tar()
