from url_utils import gen_from_urls
urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
for resp_len, status, url in gen_from_urls(urls):
     print(resp_len,'->', status,'->', url)


# dictcomp
urls_res = {url: size for size, _, url in gen_from_urls(urls)} 

import pprint

pprint.pprint(urls_res)