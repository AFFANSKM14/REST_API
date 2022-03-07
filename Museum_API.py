import pandas as pd
import requests as r
from flatten_json import flatten
import csv
#objectIDs upto 20
url1='https://collectionapi.metmuseum.org/public/collection/v1/objects'
q=r.get(url1)
q=q.json()
f=flatten(q)
l=list(q['objectIDs'])[:20]
ap=[]
l_url=[url1 + '/' + str(i) for i in l]
for url in l_url:
    re=r.get(url)
    re=re.json()
    flt=flatten(re)
    df=pd.DataFrame.from_dict(flt,orient='index')
    ap.append(df)
d=pd.concat(ap,axis=1)
d=d.transpose()
d.to_csv('MUSEUM2.csv',index=False,encoding='utf-8-sig',date_format=None)


