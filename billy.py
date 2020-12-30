import os
from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module


class Billy():
    
    def __init__(self, version):
        self.version = version
        self.modules = []
        
    

    def main(self):
        try:
            while True:
                consoleInput = str(input(f"Billy {self.version}>"))
                if consoleInput == "exit":
                    break
                if not self.sendOff(consoleInput) and consoleInput != '':
                    print("Command Not Found")
        except KeyboardInterrupt:
            quit()
                
            
    def sendOff(self, command):
        for module in self.modules:
            execMain = module.main()
            if execMain.main(command):
                return True
        return False


    def loadMods(self):
        package_dir = './mods'
        for (_, module_name, _) in iter_modules([package_dir]):
            module = import_module(f"mods.{module_name}")
            self.modules.append(module)

    def loadModules(self):
        package_dir = './modules'
        for (_, module_name, _) in iter_modules([package_dir]):
            module = import_module(f"modules.{module_name}")
            self.modules.append(module)