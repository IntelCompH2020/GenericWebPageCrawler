
import re

def filter_urls(urls):
    accepted_links  = set()
    discarded_links = set()
    for url in urls:
        if(url is None):
            continue
        url = url.strip()
        if (
            url.lower().strip() != '#' and
            url.lower().strip() != '/' and
            url.lower().strip() != 'javascript:void(0)' and
            ########################################
            not url.lower().endswith('-pdf')    and
            not url.lower().endswith('/pdf')    and
            not url.lower().endswith('.3ds')    and
            not url.lower().endswith('.tif')    and
            not url.lower().endswith('.eps')    and
            not url.lower().endswith('.dwg')    and
            not url.lower().endswith('.odt')    and
            not url.lower().endswith('.bmp')    and
            not url.lower().endswith('.xml')    and
            not url.lower().endswith('.png')    and
            not url.lower().endswith('.svg')    and
            not url.lower().endswith('.jpg')    and
            not url.lower().endswith('.jpeg')   and
            not url.lower().endswith('.gif')    and
            not url.lower().endswith('.mp3')    and
            not url.lower().endswith('.mp4')    and
            not url.lower().endswith('.pdf')    and
            not url.lower().endswith('.doc')    and
            not url.lower().endswith('.docx')   and
            not url.lower().endswith('.csv')    and
            not url.lower().endswith('.xls')    and
            not url.lower().endswith('.xlsx')   and
            not url.lower().endswith('.zip')    and
            not url.lower().endswith('.txt')    and
            not url.lower().endswith('.rar')    and
            not url.lower().endswith('.7z')     and
            not url.lower().endswith('.tar')    and
            not url.lower().endswith('.gz')     and
            not url.lower().endswith('.sh')     and
            not url.lower().endswith('.exe')    and
            not url.lower().endswith('.dmg')    and
            not url.lower().endswith('.gpg')    and
            not url.lower().endswith('.afdu')   and
            not url.lower().endswith('.psd')    and
            ########################################
            '?attachment_id='not in url.lower() and
            '&file='        not in url.lower()  and
            '/toPdf?'       not in url.lower()  and
            'attachment&'   not in url.lower()  and
            '-foto-'        not in url.lower()  and
            '.jpg&'         not in url.lower()  and
            '/pdf.'         not in url.lower()  and
            'jpg?'          not in url.lower()  and
            '/product_pdf/' not in url.lower()  and
            '=getprint&'    not in url.lower()  and
            '?print=pdf'    not in url.lower()  and
            '&format=pdf'   not in url.lower()  and
            '=attachment&'  not in url.lower()  and
            'download'      not in url.lower()  and
            'sitemap'       not in url.lower()  and
            '.pdf/'         not in url.lower()  and
            '.png?'         not in url.lower()  and
            '/pdf/'         not in url.lower()  and
            'whatsapp://'   not in url.lower()  and
            'skype:'        not in url.lower()  and
            'rss'           not in url.lower()  and
            'docreader.'    not in url.lower()  and
            'openaccess'    not in url.lower()  and
            'sendfile.asp'  not in url.lower()  and
            'javascript'    not in url.lower()  and
            'facebook'      not in url.lower()  and
            'archive.org'   not in url.lower()  and
            'google'        not in url.lower()  and
            'reddit.com'    not in url.lower()  and
            'twitter'       not in url.lower()  and
            'linkedin'      not in url.lower()  and
            'login'         not in url.lower()  and
            'signup'        not in url.lower()  and
            'password'      not in url.lower()  and
            'youtube'       not in url.lower()  and
            'tel:'          not in url.lower()  and
            'mailto:'       not in url.lower()  and
            '/mailto/'      not in url.lower()  and
            '.pdf?'         not in url.lower()  and
            '.pdf&'         not in url.lower()  and
            '.doc?'         not in url.lower()  and
            '.docx?'        not in url.lower()  and
            'jsmode='       not in url.lower()  and
            '/docreader/'   not in url.lower()  and
            '/community/'   not in url.lower()  and
            '/community.'   not in url.lower()  and
            ########################################
            url.count('www.')<2                 and
            ########################################
            len(url) < 150
        ):
            accepted_links.add(url.replace('https://', 'http://'))
        else:
            discarded_links.add(url.replace('https://', 'http://'))
    return accepted_links, discarded_links

def filter_urls_2(base_url, urls):
    accepted_links  = set()
    discarded_links = set()
    maybe_usefull   = base_url.replace('https://', '').replace('http://', '').replace('www.', '')
    for url in urls:
        if(url is None):
            continue
        # if url.startswith('#'):
        #     url = base_url+url
        url = url.strip()
        while(url.endswith('/') or url.endswith('#')):
            url = url[:-1]
        if(url.startswith('/')):
            if('www.' in url):
                discarded_links.add(url)
                continue
            else:
                url = base_url+url
        if (
            url.lower().strip() != '#' and
            url.lower().strip() != '/' and
            url.lower().strip() != 'javascript:void(0)' and
            ########################################
            not url.lower().endswith('-pdf')    and
            not url.lower().endswith('/pdf')    and
            not url.lower().endswith('.3ds')    and
            not url.lower().endswith('.tif')    and
            not url.lower().endswith('.eps')    and
            not url.lower().endswith('.dwg')    and
            not url.lower().endswith('.odt')    and
            not url.lower().endswith('.bmp')    and
            not url.lower().endswith('.xml')    and
            not url.lower().endswith('.png')    and
            not url.lower().endswith('.svg')    and
            not url.lower().endswith('.jpg')    and
            not url.lower().endswith('.jpeg')   and
            not url.lower().endswith('.gif')    and
            not url.lower().endswith('.mp3')    and
            not url.lower().endswith('.mp4')    and
            not url.lower().endswith('.pdf')    and
            not url.lower().endswith('.doc')    and
            not url.lower().endswith('.docx')   and
            not url.lower().endswith('.csv')    and
            not url.lower().endswith('.xls')    and
            not url.lower().endswith('.xlsx')   and
            not url.lower().endswith('.zip')    and
            not url.lower().endswith('.txt')    and
            not url.lower().endswith('.rar')    and
            not url.lower().endswith('.7z')     and
            not url.lower().endswith('.tar')    and
            not url.lower().endswith('.gz')     and
            not url.lower().endswith('.sh')     and
            not url.lower().endswith('.exe')    and
            not url.lower().endswith('.dmg')    and
            not url.lower().endswith('.gpg')    and
            not url.lower().endswith('.afdu')   and
            not url.lower().endswith('.psd')    and
            ########################################
            '?attachment_id='not in url.lower() and
            '&file='        not in url.lower()  and
            '/toPdf?'       not in url.lower()  and
            'attachment&'   not in url.lower()  and
            '-foto-'        not in url.lower()  and
            '.jpg&'         not in url.lower()  and
            '/pdf.'         not in url.lower()  and
            'jpg?'          not in url.lower()  and
            '/product_pdf/' not in url.lower()  and
            '=getprint&'    not in url.lower()  and
            '?print=pdf'    not in url.lower()  and
            '&format=pdf'   not in url.lower()  and
            '=attachment&'  not in url.lower()  and
            'download'      not in url.lower()  and
            'sitemap'       not in url.lower()  and
            '.pdf/'         not in url.lower()  and
            '.png?'         not in url.lower()  and
            '/pdf/'         not in url.lower()  and
            'whatsapp://'   not in url.lower()  and
            'skype:'        not in url.lower()  and
            'rss'           not in url.lower()  and
            'docreader.'    not in url.lower()  and
            'openaccess'    not in url.lower()  and
            'sendfile.asp'  not in url.lower()  and
            'javascript'    not in url.lower()  and
            'facebook'      not in url.lower()  and
            'archive.org'   not in url.lower()  and
            'google'        not in url.lower()  and
            'reddit.com'    not in url.lower()  and
            'twitter'       not in url.lower()  and
            'linkedin'      not in url.lower()  and
            'login'         not in url.lower()  and
            'signup'        not in url.lower()  and
            'password'      not in url.lower()  and
            'youtube'       not in url.lower()  and
            'tel:'          not in url.lower()  and
            'mailto:'       not in url.lower()  and
            '/mailto/'      not in url.lower()  and
            '.pdf?'         not in url.lower()  and
            '.pdf&'         not in url.lower()  and
            '.doc?'         not in url.lower()  and
            '.docx?'        not in url.lower()  and
            'jsmode='       not in url.lower()  and
            '/docreader/'   not in url.lower()  and
            '/community/'   not in url.lower()  and
            '/community.'   not in url.lower()  and
            ########################################
            'the-last-witness-poster' not in url.lower() and
            'adriatica-ionica-race-' not in url.lower() and
            ########################################
            url.count('www.')<2                 and
            ########################################
            len(url) < 150                      and
            ########################################
            maybe_usefull.lower() in url.lower()
        ):
            accepted_links.add(url.replace('https://', 'http://'))
        else:
            discarded_links.add(url.replace('https://', 'http://'))
    return accepted_links, discarded_links

def fix_the_html(html):
    html = html.replace('</p>', '</p> <br><br> ', )
    html = html.replace('</h1>', '</h1> <br><br> ', )
    html = html.replace('</h2>', '</h2> <br><br> ', )
    html = html.replace('</h3>', '</h3> <br><br> ', )
    html = html.replace('</li>', '</li> <br> ', )
    html = html.replace('</ul>', '</ul> <br><br> ', )
    html = re.sub('<script.*?</script>', '', html, flags=re.DOTALL)
    return html

def is_javascript(lp):
    if 'val()' in lp:
        return True
    if ' var ' in lp and ' true;' in lp:
        return True
    if ' var ' in lp and ' false;' in lp:
        return True
    if 'function(' in lp.lower():
        return True
    if '-color:' in lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if '(window.' in lp.lower():
        return True
    if 'copyright' in lp.lower() and 'all rights reserved' in lp.lower():
        return True
    if 'font-size:' in lp or 'padding-bottom:' in lp or 'font-family:' in lp or '#gallery-1 {' in lp:
        return True
    if 'box-shadow:' in lp:
        return True
    if 'border: none' in lp:
        return True
    if ':none;' in lp:
        return True
    if 'height:' in lp and 'width:' in lp and 'border:' in lp :
        return True
    if 'irframe' in lp and 'width:' :
        return True
    if 'height:auto' in lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if '.product-title' in lp :
        return True
    if '.product-wrap' in lp :
        return True
    if '{height:' in lp :
        return True
    if lp.count('{') >= 3 and lp.count('}') >= 3:
        return True
    if '.button.' in lp :
        return True
    if 'display: block'in lp :
        return True
    if '{display:block}' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if '{opacity:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'padding:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp:
        return True
    if 'color:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if '.button,' in  lp :
        return True
    if 'background:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp and '#' in lp :
        return True
    if 'width:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'height:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'display:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'margin:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'iframe' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'clear:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'content:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'content:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if 'hover:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') and '{' in lp :
        return True
    if '.special_amp' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'a:hover' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'padding-left:' in lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if '{border:' in lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if '{visibility:' in lp.lower() :
        return True
    if '{background-image:' in lp.lower() :
        return True
    if 'en.products.notify_form.description' in lp :
        return True
    if 'padding-top:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'border-top:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'margin-top:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'margin-bottom:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'text-transform:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'border-radius:' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    if 'none;}' in  lp.lower().replace(' ','').replace('\n','').replace('\t','') :
        return True
    return False

tm_characters1 = ['Ⓡ','®',u'Ⓡ',u'®']
tm_characters2 = ['™',u'™']

def count_tm_char(text):
    ret = 0
    for c in tm_characters1+tm_characters2:
        ret += text.count(c)
    return ret

def replace_tm_chars(text):
    for c in tm_characters1:
        text = text.replace(c,'_TMR_')
    for c in tm_characters2:
        text = text.replace(c,'_TM_')
    return text
