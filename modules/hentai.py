import webbrowser, re

class main():

    def __init__(self):
        self.chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'


    def main(self, command):

        commandSearch = re.findall(r'\d+\d+\d+\d+\d+\d+', command)
        if commandSearch != [] and 'sauce ' in command:
            webbrowser.get(self.chrome_path).open_new(f'https://nhentai.net/g/{commandSearch[0]}')
