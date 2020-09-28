import requests
import json

if __name__ == "__main__":
    url = "http://gs.amac.org.cn/amac-infodisc/api/pof/person?rand=0.12105985915997475&page=1&size=10"
    payload = '{"userId": "1700000000699069", "page": "1"}'.encode("utf-8")
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Content-Type': 'application/json',
    }
    dic_obj = requests.post(url=url, headers=headers, data=payload).json()
    print(dic_obj)
    accountId_list = []
    for dic in dic_obj["content"]:
        accountId_list.append(dic["accountId"])
    print("UserId=", accountId_list)

    fp = open("./accountId_list.json", 'w', encoding="utf-8")
    json.dump(accountId_list, fp=fp, ensure_ascii=False)
    print("over")
