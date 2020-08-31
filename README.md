# flask_test
A flask testing project

使用flask 實現 RESTful API , API 服務內容包括DB的資料 新增,修改,刪除,查詢

DB 採用 MySQL + pysql + flask_sqlalchemy 串接, 使用flask 原生ORM工具 flask_sqlalchemy 與 DB連結,

查詢所有會員功能API 需要先透過資料驗證取得Token, Token設計為 HASH256編碼格式使用期限為5分鐘, 5分鐘過後過期需要再重新取得一次

Todo list:
1.RESTful 風格的API

2.MySQL資料庫建制, 與flask進行連接

3.Token 設計,某些API使用前需要先驗證Token

4.Docker包裝flask 與MySQL

