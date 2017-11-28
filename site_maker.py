import markdown
from livereload import Server
import jinja2
import json


def convert_md_to_html():
    with open('./articles/0_tutorial/7_codenvy.md', 'r', encoding='utf-8') as md_file_handler:
        html = markdown.markdown(md_file_handler.read())
    # with open('./html.html', 'w', encoding='utf-8') as html_file_handler:
    #     html_file_handler.write(html)
        # TODO сохранение всех мд в хтмл
        return html


def make_site():
    print(1)

def load_config():
    with open('./config.json', 'r') as file_handler:
        json_data = json.load(file_handler)
    for topic in json_data['topics']:
        print(topic)
    return json


if __name__ == '__main__':
    load_config()
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('index.html')
    rendered_template = template.render(html=convert_md_to_html())
    print(rendered_template)
    server = Server()
    server.watch('templates/*.html', make_site)
    # TODO watch for changes in markdown articles
    server.serve(root='site/') # folder to serve html files from
