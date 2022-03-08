import matplotlib
import pandas as pd
import requests as r
import json
from flatten_json import flatten
import pdfkit
#objectIDs upto 20
url1='https://collectionapi.metmuseum.org/public/collection/v1/objects'
q=r.get(url1)
q=q.json()
f=flatten(q)
l=list(q['objectIDs'])[:20]
ap=[]
l_url=[url1 + '/' + str(i) for i in l]
i=0
for url in l_url:
    re=r.get(url)
    re=json.loads(re.content)
    flt=flatten(re)
    ap.append(flt)
d=pd.json_normalize(ap)
#to_csv
d.to_csv('MUSEUM3.csv',encoding='utf-8-sig')
#to_html
file=open('MUSEUM2.html','w')
a=d.to_html()
file.write(a)
file.close()
#to xml
file_xml=open('MUSEUM2.xml','w')
a1=d.to_html()
file_xml.write(a1)
file_xml.close()
#to pdf
options={
    'page-height': '1300',
    'page-width' : '300','orientation':'Landscape',
     'margin-top': '0.8in','margin-right': '0.7in','margin-bottom': '0.7in','margin-left': '0.7in',
    'encoding':'utf-8-sig'}
pdfkit.from_file('MUSEUM2.html','MUSEUM2.pdf',options=options)