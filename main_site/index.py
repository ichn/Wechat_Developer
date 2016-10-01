class Index:
    def __init__(self):
        pass
    def GET(self):
        IndexFile = open('static/index.html', 'r').read()
        return str(IndexFile)

