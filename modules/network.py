import subprocess
import re




class main():

    def main(self, command):
        if 'ping ' in command:
            print(subprocess.getoutput(command))
            return True
        else:
            return False 