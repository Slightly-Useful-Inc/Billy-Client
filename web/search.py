import wikipedia



def find(search = None):
    if search is None:
        return TypeError
    else:
        return wikipedia.search(search)