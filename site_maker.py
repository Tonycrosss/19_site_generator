import markdown
from livereload import Server
import jinja2
import json

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'))


def convert_md_to_html():
    with open('./articles/0_tutorial/7_codenvy.md', 'r', encoding='utf-8') as md_file_handler:
        html = markdown.markdown(md_file_handler.read())
    # with open('./html.html', 'w', encoding='utf-8') as html_file_handler:
    #     html_file_handler.write(html)
        # TODO сохранение всех мд в хтмл
        return html


def create_index_page(topics_data):
    index_template = env.get_template('index.html')
    with open('./site/index.html', 'w', encoding='utf-8') as index_handler:
        index_handler.write(index_template.render(topics_data=topics_data))


def make_site(topics_data):
    create_index_page(topics_data)


def load_config():
    with open('./config.json', 'r', encoding='utf-8') as file_handler:
        json_data = json.load(file_handler)
    return json_data


if __name__ == '__main__':
    json_data = load_config()
    print(json_data['topics'])
    create_index_page(topics_data=json_data['topics'])
    server = Server()
    # server.watch('templates/*.html', make_site(topics_data))
    # TODO watch for changes in markdown articles
    server.serve(root='site/') # folder to serve html files from
