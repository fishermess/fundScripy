import json
from pgdb import Connection
from tqdm import tqdm

if __name__ == "__main__":
    fp = open("./企业及员工信息汇总.json",'r')
    Member_list = json.load(fp)

    #导入数据库
    connection = Connection(user='postgres', database='FundOrg', host='172.17.0.2', password='123456')
    #清空数据库
    connection.execute("truncate table memberlist")
    connection.execute("alter sequence memberlist_id_seq restart with 1")


    for ui in tqdm(Member_list):
        #print(str(ui["证书状态变更记录"]).replace('\'',""))
        connection.execute(
        "insert into memberlist"
        "(name,sex,orgname,certcode,certname,"
        "statusname,certobtaindate,image,personcerthistorylist)"
        " values "
        "('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}-{8}','{9}')".format(
            ui["姓名"],ui["性别"],ui["从业机构"],ui["证书编号"],ui["从业资格类别"],
            ui["证书状态"],ui["证书取得时间"],ui["从业机构"],ui["头像地址"].split('/')[-1],str(ui["证书状态变更记录"]).replace("\'",""),
        )
    )