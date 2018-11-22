import pymysql

lista=list()
#封装一个模块，操作数据库
class MYSQLdbUtil():
    def __init__(self,host='localhost',name='root',pwd='123456',port='3306',dbname='test',charset='utf8'):
        self.__host=host
        self.__name=name
        self.__pwd=pwd
        self.__port=port
        self.__dbname=dbname
        self.__charset=charset
        self.__connection=None
        self.__cursor=None

    def getConnection(self):
        try:
            self.__connection=pymysql.connect(self.__host,self.__name,self.__pwd,self.__dbname,charset=self.__charset)
        except (pymysql.MySQLError,pymysql.DatabaseError):
            pass
        pass



    #DML操作
    def execute(self,sql,params=None,isbatch=False):
        try:
            self.getConnection()
            self.__cursor=self.__connection.cursor()
            if params:
                if isbatch:
                    return self.__cursor.execute(sql,params)
                else:
                    return self.__cursor.execute(sql)
            else:
                return self
                pass
        except:
            self.__cursor.close()
            self.__connection.close()
        pass

    # 查询操作
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.__cursor.fetchall()
        pass

    #关闭方法，为了支持事物
    def close(self):
        if self.__cursor and self.__connection:
            self.__cursor.close()
            self.__connection.close()

    #提交
    def commit(self):
        self.__connection.commit()
        pass
    #回滚
    def rollback(self):
        self.__connection.rollback()


if __name__=='__main__':
    pass
