'''
excel 文件读写工具类
'''
import openpyxl
import os
from utils.handle_path import *
class Handle_Excel():
    def __init__(self,filename,sheetname):
        self.wk=openpyxl.load_workbook(filename)#openpyxl库中的load_workbook函数打开指定的excel文件
        self.st=self.wk[sheetname]#获取文件流对象中的指定sheet页对象
        self.filename=filename

    def read_data(self):
        '''
        读取指定sheet页对象中所有的数据方法
        :return:
        '''
        list1=list(self.st.rows)
        title_list=[i.value for i in list1[0]]
        all_datas=[]
        for j in list1[1:]:
            data_list=[k.value for k in j]
            data_dict=dict(zip(title_list,data_list))
            all_datas.append(data_dict)
            return all_datas


if __name__ == '__main__':
    e_file=os.path.join(data_path,'case_data.xlsx')
    h=Handle_Excel(e_file,'login')
    h.read_data()
