import subprocess

def clean():
    subprocess.check_call(['rm','-f', './Uploads/*.pdf'])