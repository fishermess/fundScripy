import requests
import json
import time, datetime
from tqdm import tqdm
from pgdb import Connection
if __name__ == "__main__":
    #获取所有企业ID、

    fp = open("TotalMemberInformation.json", 'w')
    user_information_list = []
    userid_list = []#用于存储所有企业ID
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Content-Type': 'application/json',
    }
    for page1 in tqdm(range(21),desc="获取企业ID"):#首页分页
        #print("第{}页".format(page1+1))
        url = "https://gs.amac.org.cn/amac-infodisc/api/pof/personOrg?rand=0.21821422787959&page={}&size=10".format(page1)
        payload = "{\"page\":1,\"orgType\":\"公募基金管理公司\"}"
        payload = payload.encode("utf-8")

        dic_obj = requests.post(url=url,headers=headers,data=payload,verify=False).json()

        for dic in dic_obj["content"]:
            userid_list.append(dic["userId"])

    # 获取单公司所有员工ID
    for i,uid in enumerate(tqdm(userid_list,desc="爬取所有员工信息")):
        accountid_list = []#存储单公司所有员工ID
        flag = True
        page2 = 0
        while(flag):
            flag = False
            url = "https://gs.amac.org.cn/amac-infodisc/api/pof/person?page={}&size=10".format(page2)
            payload = ('{'+'"userId": "{}","page":"1"'.format(uid)+'}').encode("utf-8")
            dic_obj = requests.post(url=url,data=payload,headers=headers,verify=False).json()
            if len(dic_obj["content"])!=0:
                print("公司ID："+str(uid)+' Page={}'.format(page2+1))
                #print(dic_obj["content"])
                flag = True
            for dic in dic_obj["content"]:
                accountid_list.append(dic["accountId"])
            page2 += 1
        #单公司所有员工ID获取完毕

        #获取单公司所有员工详细信息
        for aid in accountid_list:
            url = "https://gs.amac.org.cn/amac-infodisc/api/pof/person/{}".format(aid)
            dic_obj = requests.get(url=url,headers=headers,verify=False).json()
            #保存员工详细信息


            personCertHistoryList=[]    #证书变更记录
            for i in range(int(dic_obj["certStatusChangeTimes"])):
                CertHistory = {
                    "证书编号":dic_obj["personCertHistoryList"][i]["certCode"],
                    "变更时间":dic_obj["personCertHistoryList"][i]["certObtainDate"],
                    "从业机构":dic_obj["personCertHistoryList"][i]["orgName"],
                    "从业资格类别":dic_obj["personCertHistoryList"][i]["certName"],
                    "证书状态":dic_obj["personCertHistoryList"][i]["statusName"]
                }
                personCertHistoryList.append(CertHistory)

            user_information={
                "姓名":dic_obj["userName"],"性别":dic_obj["sex"],
                "从业机构":dic_obj["orgName"],"证书编号":dic_obj["certCode"],
                "从业资格类别":dic_obj["certName"],"证书状态":dic_obj["statusName"],
                "证书取得时间":time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(dic_obj["certObtainDate"]/1000)),

                "证书状态变更记录":personCertHistoryList,

                "头像地址":dic_obj["personPhotoBase64"]
            }
            user_information_list.append(user_information)
    json.dump(user_information_list,fp=fp,ensure_ascii=False)
    fp.close()