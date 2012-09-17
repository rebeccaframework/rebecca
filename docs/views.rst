==================
ビュー
==================


リストビュー
=====================

:class:`rebecca.views.ListView` は汎用的なリストビューです。
モデルクラス、セッション、グリッド定義とともに利用します。

.. code-block:: python

   class UserListView(ListView):
       model = User
       session = DBSession
       grid = Grid([
                    (u'', helpers.checkboxmaker('user_name')),
                    (u'#', 'id'),
                    (u'Name', helpers.linkmaker('user_name', 
                              helpers.urlmaker('user', [('user_name', 'user_name')]))),
                   ],
                   table_attrs={'class': 'table table-striped'})

この例では、 ``User`` がモデルクラス、 ``DBSession`` がセッションオブジェクトです。
:class:`rebecca.helpers.Grid` で、リスト表示する項目を指定します。
項目の指定は2要素タプルのリストです。
第一要素が項目名で、第二要素が項目の内容です。
第二要素は通常、モデルデータを受け取る呼び出し可能なオブジェクトです。
ただし、項目の内容が文字列で指定された場合は、 モデルデータの属性が指定されたものとして扱われます。

``(u'#', 'id')`` という項目定義は、 ``(u'#', operator.attrgetter('id'))`` と定義したのと同じことになります。


.. note::

   セッションオブジェクトは、`scoped_session` を前提としています。

.. autoclass:: rebecca.views.ListView

.. autoclass:: rebecca.helpers.Grid
