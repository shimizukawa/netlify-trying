=====================================
netlifyでSphinxを自動デプロイする実験
=====================================

*reStructuredText* で書きます。略して **reST**

.. contents::
   :local:


reSTの例
=========

文字列をいれる

* 箇条書き１
* 箇条書き２

  1. foo
  2. bar

コードハイライト
----------------

.. code-block:: ruby

   class Foo
     def initialize(value)
       puts "value = #{value}"
     end
   end


他のファイルへリンク
---------------------

.. toctree::
   :numbered:
   :maxdepth: 2

   20110304_osc_tokyo_spring
   sphinx-users-q-and-a
   pages/index

数式
-----

.. math:: (a + b)^2 = a^2 + 2ab + b^2

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}


ソースコードから生成
---------------------

.. automodule:: person
   :members:

索引
--------

.. index::
   データベースアクセス
   セッション

このsessionモジュールでは...



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

