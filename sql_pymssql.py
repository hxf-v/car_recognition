from sql_serach import MSSQL
import json

ms = MSSQL(host='172.16.254.196',
           user='sa',
           pwd='ahu123',
           db='VMWare', )

user_id = '610103196407040078'
res_list = ms.ExecQuery("SELECT * FROM ahu_Teacher WHERE sfzh='%s' " % user_id)  # 获取数据库中用户名和密码,查询用户是否在表内
# for tuple_name in res_list:
#     for str_name in tuple_name:
#         if str_name is not None:
#             str_name.strip()
#             print(str_name)

res_na = []
for tuple_name in res_list:
    for str_name in tuple_name:
        if str_name is not None:
            str_name.strip()
            res_na.append(str_name.strip())
            # print(str_name)

print(res_na)
res_dict = {"name": res_na[1], "xueyuan": res_na[2]}
print(res_dict)
