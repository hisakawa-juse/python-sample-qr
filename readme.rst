QRコードサーバサンプル
==========================

qrコード作成
---------------

- 以下の指定でa.pngを作成する
  
.. code-block:: none

   % python make-qr.py <文字列>

サーバ
-------

- サーバ立ち上げ
  
.. code-block:: none

    % uvicorn qr-restapi:app --reload

エンコードした情報作成
-----------------------

- 以下の指定でQR画像をエンコードした情報作成
  
.. code-block:: none

   % python base64-png.py a.png

explorerから以下のようにアクセス

.. code-block:: none

    http://127.0.0.1:8000/decode?qr=iVBORw0KGgoAAAANSUhEUgAAASIAAAEiAQAAAAB1xeIbAAABfklEQVR4nO2aS46DMAyGP0%2BQuoQb9ChwszlTbwBH6QFGapaVqP5ZBFo6D81seDXOCswn5ZfjOI6Fib9H9/YPCJxyyimnnNo6ZcMoktGaOFqaVXVlQdWSpAuYVTcDgiRJz9TyurKg4j3GCcnjj22wffX7pIpvlmiION%2BMTv1GqQWsWXDGfKkx7ktBivbyggFML11bVb9vavB9ZwAErD4XPXCzdXXlQCXfT2K8O15t2AZr6sqBIpWSQ40Z0hMQpHb8qnar6vdNjd4tJWr1DAtwX4XafT8blXKO1eeiV2dg9elm6o49EKsxGW1V/b4pptfXckw3D5vH/dyUdAG10cbqJhakPLSurtempvV9LTDKDwMCEIt%2BNV05UEO%2BH95CL%2BJBVp8qE%2BD5fgHq3seE8mqks3YDurKgHn3MeEg1pr3ral%2Bo5XVlRT1CvquCn7XLUrFAbSyY7oUt6Ho96sc%2BJpQ96prgdc6c1NPdiqDk9kmLwe9Ws1Hm/0Y55ZRTTmVBfQI0j8EorlZv1wAAAABJRU5ErkJggg%3D%3D		
   
