import os
import modules.hentai


class Billy():
    
    def __init__(self):
        self.modules = [modules.hentai]
    

    def main(self):
        
        while True:
            consoleInput = str(input("Billy v1.0>"))
            for module in self.modules:
                sendOff = module.main()
                sendOff.main(consoleInput)
            



    def loadModule(self, module, id):
        module.main()