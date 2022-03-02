
import os, requests, random, json
from bs4 import BeautifulSoup
from collections import Counter
from tqdm import tqdm
from my_lang_detect import lang_detect_on_txt_par
from timeout import timeout
from global_handlers import filter_urls_2, fix_the_html
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--max_pages_to_visit", type=int, default=1000, help="Maximum pages to visit.",     required=False)
parser.add_argument("--inpath",             type=str,               help="input json file.",            required=True)
parser.add_argument("--out_dir",            type=str,               help="output root directory path.", required=True)

args                = parser.parse_args()
inpath              = args.inpath
out_dir             = args.out_dir
max_pages_to_visit  = args.max_pages_to_visit

def clear_url(url):
    while(url.endswith('/')):
        url = url[:-1]
    if(url.startswith('www')):
        url = 'http://{}'.format(url)
    if not (url.startswith('http://') or url.startswith('https://')):
        try:
            page    = requests.get('http://{}'.format(url))
            url     = 'http://{}'.format(url)
        except:
            url     = 'https://{}'.format(url)
    return url

@timeout(30)
def get_the_html(url):
    page = requests.get(url)
    return page

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

to_crawl    = json.load(open(inpath,'r',encoding='utf-8'))
random.shuffle(to_crawl)

def get_languages(soup):
    page_langs      = []
    all_text        = soup.text.strip()
    paragraphs      = all_text.split('\n\n')
    paragraphs      = [p for p in paragraphs if len(p.strip()) > 0]
    long_paragraphs = [p for p in paragraphs if len(p.strip()) > 100]
    if len(long_paragraphs) > 0:
        for lp in long_paragraphs:
            try:
                le_lang = lang_detect_on_txt_par(lp)
                page_langs.append(le_lang)
            except:
                le_lang = 'unsure'
                page_langs.append(le_lang)
    else:
        le_lang = 'unsure'
        page_langs.append(le_lang)
    return Counter(page_langs)

pbar = tqdm(to_crawl)
for (pic_type, base_url, pic_id) in pbar:
    pic_dir = os.path.join(out_dir, pic_type, pic_id)
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)
    else:
        continue
    ################################################
    base_url = clear_url(base_url)
    pbar.set_description(base_url)
    ################################################
    already_visited = set()
    to_visit        = [base_url]
    ################################################
    visited_counter = 0
    ################################################
    c = 0
    pages_visited   = open(os.path.join(pic_dir, 'pages_visited.txt'),   'a', encoding='utf-8')
    pages_error     = open(os.path.join(pic_dir, 'pages_error.txt'),     'a', encoding='utf-8')
    pages_discarded = open(os.path.join(pic_dir, 'pages_discarded.txt'), 'a', encoding='utf-8')
    while(len(to_visit)>0):
        pbar.set_description('{}:{}:{}'.format(os.path.join(pic_type, pic_id), base_url,len(to_visit)))
        url         = to_visit[0]
        to_visit    = to_visit[1:]
        already_visited.add(url)
        ################################################
        try:
            page = get_the_html(url)
        except:
            print('Error for page: {}'.format(url))
            pages_error.write('{}\n'.format(url))
            continue
        ################################################
        soupa       = BeautifulSoup(fix_the_html(page.text), features='lxml')
        page_langs  = get_languages(soupa)
        ################################################
        c       += 1
        pic_page_dir = os.path.join(pic_dir, str(c))
        if not os.path.exists(pic_page_dir):
            os.makedirs(pic_page_dir)
        ################################################
        with open(os.path.join(pic_page_dir,'source_of_page.html'), 'w', encoding='utf-8') as fp:
            fp.write(page.text)
            fp.close()
        with open(os.path.join(pic_page_dir,'webpage_visited.txt'), 'w', encoding='utf-8') as fp:
            fp.write(url)
            fp.close()
        ################################################
        with open(os.path.join(pic_page_dir,'languages.json'), 'w', encoding='utf-8') as of:
            of.write(json.dumps(dict(page_langs), indent=4, sort_keys=False))
            of.close()
        ####################################################################################
        accepted_links, discarded_links = filter_urls_2(
            base_url,
            [
                a.get('href')
                for a in soupa.findAll('a')
            ]
        )
        ################################################
        to_visit = to_visit + list(accepted_links - set(to_visit) - already_visited)
        ################################################
        pages_visited.write('{}\n'.format(url))
        for disc_page in discarded_links:
            pages_discarded.write('{}\n'.format(disc_page))
        ################################################
        visited_counter +=1
        if(visited_counter >= max_pages_to_visit):
            break
    pages_visited.close()
    pages_discarded.close()
    pages_error.close()




