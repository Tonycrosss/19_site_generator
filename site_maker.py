import markdown
from livereload import Server


def convert_md_to_html():
    with open('./articles/0_tutorial/7_codenvy.md', 'r', encoding='utf-8') as md_file_handler:
        html = markdown.markdown(md_file_handler.read())
    with open('./html.html', 'w', encoding='utf-8') as html_file_handler:
        html_file_handler.write(html)
        # TODO сохранение всех мд в хтмл


def make_site():
    print(1)


if __name__ == '__main__':
    convert_md_to_html()
    server = Server()
    server.watch('templates/*.html', make_site)
    # TODO watch for changes in markdown articles
    server.serve(root='site/') # folder to serve html files from
