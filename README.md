

This is a generic website crawler created by ATHENA R.C.


Given a website it collects all html data from the domain.  
The crawler operates on a Breadth-First-Search manner and stops after a specific number of crawled pages. 


In order to run the crawler:

`python3.6 crawler.py --inpath=data2crawl.json --out_dir=./output/  --max_pages_to_visit=1000 `

The data will be collected in files under the director "output"
