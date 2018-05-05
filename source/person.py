# -*- coding: utf-8 -*-

"""
Personモジュールです。


"""


class Person(object):
    """
    Personクラスは人の情報を保持します。
    """

    def __init__(self, name, age=0):
        """initです"""
        self.name = name
        self.age = age

    def meth(self):
        """
        ドキュメント化されるか実験
        """
        return self.age
