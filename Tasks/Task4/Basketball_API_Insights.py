import json
import pandas as pd
import requests
from flatten_json import flatten
import matplotlib.pyplot as plt
import seaborn as sns
url = 'https://www.balldontlie.io/api/v1/season_averages?season=2018&player_ids[]=237&player_ids[]=23&player_ids[]=14' \
      '&player_ids[]=15&player_ids[]=1'
req = requests.get(url)
req = json.loads(req.content)
data = req['data']
ap = []
gp = []
pi = []
for i in data:
    pi.append(i['player_id'])
    gp.append(i['games_played'])
    flt = flatten(i)
    ap.append(flt)
s = pd.json_normalize(ap)
print(pi)
print(gp)
# bar plot
sns.barplot(x=pi, y=gp)
plt.xlabel('player_id')
plt.ylabel('games_played')
plt.title('games_played vs player_id')
plt.show()
plt.savefig('games_played vs player_id.png')

# scatterplot
sns.scatterplot(x=s['games_played'], y=s['turnover'])
plt.xlabel('games_played')
plt.ylabel('turnover')
plt.title('games_played vs turnover')
plt.show()
plt.savefig('games_played vs turnover.png')

# piecharts
a = dict(s['player_id'])
plt.pie(s['ast'], labels=a.values(), autopct='% 1.1f %%', shadow=True)
plt.title('percentage of assists')
plt.show()
plt.savefig('percentage of assists.png')

sns.barplot(x=s['player_id'], y=s['pts'])
plt.xlabel('player_id')
plt.ylabel('pts')
plt.title('points of players')
plt.show()
plt.savefig('player_id vs pts.png')
