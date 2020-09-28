from tqdm import tqdm
import json
import requests
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        'Content-Type': 'application/json'
    }
#获取json数据列表
fp1 = open("./企业及员工信息汇总.json")
total_list = json.load(fp1)
fp1.close()

for person_dic in tqdm(total_list):
    url = person_dic["头像地址"]
    response = requests.get(url=url,headers=headers,verify=False)
    img_data = response.content

    address="./pg_data/"+person_dic["从业机构"]+"-"+url.split('/')[-1]
    with open(address,"wb") as fp2:
        fp2.write(img_data)