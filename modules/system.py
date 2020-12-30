import os



class main():

    def main(self, command):
        if 'clear' == command:
            os.system('clear')
            return True
        else:
            return False