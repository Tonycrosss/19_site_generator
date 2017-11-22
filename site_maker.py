import markdown
from livereload import Server


def convert_md_to_html():
    pass


def make_site():
    print(1)


if __name__ == '__main__':
    server = Server()
    server.watch('templates/*.html', make_site)
    # TODO watch for changes in markdown articles
    server.serve(root='site/') # folder to serve html files from