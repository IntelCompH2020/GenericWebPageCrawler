
from bs4 import BeautifulSoup
from langdetect import detect
from global_handlers import is_javascript
from collections import Counter
import re

def lang_detect_on_txt_par(txt_par):
    try:
        le_lang = detect(txt_par)
        return le_lang
    except:
        return 'unsure'

def lang_detect_on_html(html_text):
    html = re.sub('<script.*?</script>', '', html_text, flags=re.DOTALL)
    #######################################################################################
    soup = BeautifulSoup(html, 'lxml')
    all_text = soup.text.strip()
    paragraphs = all_text.split('\n\n')
    paragraphs = [p for p in paragraphs if len(p.strip()) > 0]
    long_paragraphs = [p for p in paragraphs if len(p.strip()) > 100]
    #######################################################################################
    page_langs = []
    if len(long_paragraphs) > 0:
        long_paragraphs_text = '\n'.join(long_paragraphs)
        ####################################################################################
        if is_javascript(long_paragraphs_text):
            page_langs.append('unsure')
            return Counter(page_langs)
        ####################################################################################
        for lp in long_paragraphs:
            try:
                le_lang = detect(lp)
                page_langs.append(le_lang)
            except:
                le_lang = 'unsure'
                page_langs.append(le_lang)
        ####################################################################################
    else:
        le_lang = 'unsure'
        page_langs.append(le_lang)
    return Counter(page_langs)

def lang_detect_on_html_file(html_path):
    #######################################################################################
    with open(html_path, 'r', encoding='utf-8') as fp:
        html = fp.read().strip()
        html = html.replace('</p>', '</p> <br>', )
        fp.close()
    return lang_detect_on_html(html)

