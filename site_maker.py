import markdown
from livereload import Server
import jinja2
import json


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'))


def convert_md_to_html(filepath):
    with open(str(filepath), 'r', encoding='utf-8') as md_file_handler:
        html = markdown.markdown(md_file_handler.read())
        return html


def create_index_page(topics_data, articles_data):
    index_template = env.get_template('index.html')
    with open('./docs/index.html', 'w', encoding='utf-8') as index_handler:
        index_handler.write(index_template.render(topics_data=topics_data,
                                                  articles_data=articles_data))


def make_site(json_data):
    create_index_page(topics_data=json_data['topics'],
                      articles_data=json_data['articles'])
    create_static_pages(json_data)


def create_static_pages(json_data):
    page_template = env.get_template('page.html')
    for article in json_data['articles']:
        html = convert_md_to_html('./articles/{}'.format(article['source']))
        html_file_name = './docs/{}.html'.format(article['title'])
        with open(html_file_name, 'w', encoding='utf-8') as html_page_handler:
            html_page_handler.write(page_template.render(html_content=html))


def load_config():
    with open('./config.json', 'r', encoding='utf-8') as file_handler:
        json_data = json.load(file_handler)
    return json_data


if __name__ == '__main__':
    json_data = load_config()
    server = Server()
    server.watch('templates/*.html', make_site(json_data))
    server.serve(root='./')  # folder to serve html files from
