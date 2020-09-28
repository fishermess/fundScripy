import json
from pgdb import Connection
from tqdm import tqdm

fp = open("TotalOrgInformation.json",'r')
org_list = json.load(fp)

# 导入数据库
connection = Connection(user='postgres', database='FundOrg', host='172.17.0.2', password='123456')
# 清空数据库
connection.execute("truncate table org")
connection.execute("alter sequence org_id_seq restart with 1")

for dic in tqdm(org_list, desc="正在将信息导入org数据库"):
    # print('{0},{1},{2},{3},{4},{5},{6}'.format(dic["机构名称"], dic["机构类型"],
    #                                       dic["员工人数"], dic["从业资格人数"],
    #                                       dic["销售业务资格人数"], dic["基金经理数目"],
    #                                       dic["投资经理数目"])
    #       )

    connection.execute("insert into org"
                       "(orgname,orgType,extworkertotalnum,opernum"
                       ",salesmannum,fundmangernum,investmentmangernum)"
                       " values "
                       "('{0}','{1}',{2},{3},{4},{5},{6})".format(dic["机构名称"], dic["机构类型"],
                                                                  dic["员工人数"], dic["从业资格人数"],
                                                                  dic["销售业务资格人数"], dic["基金经理数目"],
                                                                  dic["投资经理数目"]
                                                                  )
                       )

b = connection.query('select * from org')
print(b)