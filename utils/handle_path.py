import os

#定义项目路径
base_path=os.path.dirname(os.path.dirname(__file__)) #获取项目路径
print(base_path)

#定义config包的路径
conf_path=os.path.join(base_path,'conf')
#print(conf_path)

#定义data包路径
data_path=os.path.join(base_path,'data')
#print(data_path)
#定义lib包路径
lib_path=os.path.join(base_path,'lib')
#print(lib_path)
#定义report包路径
report_path=os.path.join(base_path,'report')
#print(report_path)
#定义run包路径
run_path=os.path.join(base_path,'run')
#print(run_path)
#定义testcase包路径
case_path=os.path.join(base_path,'testcase')
#print(case_path)
#utils包路径
utils_path=os.path.join(base_path,'utils')
#print(utils_path)

