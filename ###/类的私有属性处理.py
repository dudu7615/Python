class a:
    __b = 0
    @property
    def b(self):
        """ 访问器 - 获取变量值 """
        return self.__b
    @b.setter
    def b(self, b):
        """ 设置器 - 设置变量值  """
        self.__b = b

    

c = a()
print(c.b)
c.b = 1
print(c.b)