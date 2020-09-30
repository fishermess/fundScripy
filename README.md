fundScripy
基金爬虫requests

需求：

            python3.6
            pip install tqdm
            pip install pgdb
            pip install requests
一：数据库准备

    请先在postgres数据库中构建一个名为FundOrg的数据库，进入数据库后使用本项目提供的table1.txt,table2.txt构建数据表。
二：现有数据信息

    本项目已经获得 员工信息文件（TotalMemberInformation.json），各机构信息文件（TotalOrgInformation.json）
三：手动获取数据信息

    若要手动自己获取TotalMemberInformation.json（建议不用，耗时极长）
    python GetMemberInformation.py 
    
    若要手动自己获取TotalOrgInformation.json(耗时不长，但并不是必须使用)
    python GetOrgInformation.py 
四：将头像图片保存，并将信息导入数据库

    将机构信息导入数据库
    python SaveOrgInfromation2DataBase.py
    
    将从业人员信息导入数据库
    python SaveMemberInformation2DataBase.py
    
    将从业人员头像保存
    python SavePicture.py
五：剪裁图片(Addition)

    若要剪裁图片需要使用深度学习模型https://github.com/1adrianb/face-alignment
    git clone git@github.com:1adrianb/face-alignment.git
    cd face-alignment
    pip install -r requirement
    pip install torch==1.6.0
    pip install face-alignment
    
    安装完成后运行
    python MultiBatchCrop.py
