import requests, json, time, os
from tqdm import tqdm
from bs4 import BeautifulSoup
import markdownify

try:
    with open('./config/config.json', 'r') as f:
        config = json.load(f)
        plugins = config['plugins']
except:
    config = {}
    plugins = {}

for plugin in tqdm(plugins):
    url = plugins[plugin]
    response = requests.get(url)

    if (response.status_code != 200):
        continue

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    title = ''
    description = ''
    try:
        title = soup.select('h1.info--title')[0].contents[0].strip()
    except:
        pass

    try:
        description = soup.select('.product--description')[0].decode_contents()
        description_md = markdownify.markdownify(description, heading_style="ATX")
    except:
        pass

    with open(os.path.join(config['plugin_docs_dir'], plugin, 'index.md'), 'w') as f:
        f.write('<a href="{}" target="_blank">Im Shopware Community Store anzeigen</a>\n\n'.format(url))
        f.write('\n'.join([l.strip() for l in description_md.split('\n')]))

    time.sleep(2)