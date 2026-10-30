'''
对ini配置文件进行操作
'''
from configparser import ConfigParser #导入configerparser类

class Handle_Ini(ConfigParser):
    def __init__(self,filename):
        super().__init__()#继承init
        self.read(filename)
        self.filename=filename
    def get_value(self,section,option):
        '''
        获取指定ini下指定section下option对应的值
        :param section:要提取的是ini中的哪个模块
        :param option:ini模块下的内容
        :return:返回内容
        '''
        v=self.get(section,option)
        return v
    def write_data(self,section,option,value):
        '''
        通过当前类对象调用set方法设定section中的option值
        :param section:要提取的是ini中的哪个模块
        :param option:ini模块下的内容
        :param value:写入的值
        :return:
        '''
        self.set(section,option,value)
        f=open(self.filename,'w')
        self.write(f)
        f.close()

if __name__ == '__main__':
    i_file=r'../conf/config.ini'
    h=Handle_Ini(i_file)
    h.get_value('test_env','url')
    h.write_data('test_env','token','123456')



