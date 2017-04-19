from pprint import pprint
import csv
import numpy as np
import json

# dat = np.genfromtxt('allpillar.csv',delimiter=',')

dat = []
with open('allpillar.csv','rb') as f:
	reader = csv.reader(f)
	for row in reader:
		dat.append(row)
#print np.array(dat)
#print dat 
dic={'timeBins':[{'data':[],'t':2010}]}
#input to dic['timeBins'][0]['data']

count = 0
for i in range(1,len(dat)):
	count += int(dat[i][3])
	if dat[i][2] == 'ASD' or dat[i][2] == 'HASS':
		continue
	pillar_dic = {'ESD':'mil','EPD':'civ','ISTD':'ammo'}
	dic['timeBins'][0]['data'].append({'e':dat[i][0],'i':dat[i][1],'v':int(dat[i][3])*1000000,'wc':pillar_dic[dat[i][2]]})

#jdic = json.dumps(dic)
#loaded_jdic = json.loads(jdic)
#print type(jdic) #Output str
#type(loaded_jdic) #Output dict

jdic = json.dumps(dic)
# print dic['timeBins'][0].keys()

print dic
with open('jdic.json', 'w') as f:
     json.dump(json.JSONDecoder().decode(jdic), f)



