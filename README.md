# flask_test
A flask testing project

使用flask 實現 RESTful API , API 服務內容包括DB的資料 新增,修改,刪除,查詢

DB 採用 MySQL + pysql + flask_sqlalchemy 串接, 使用flask 原生ORM工具 flask_sqlalchemy 與 DB連結,

查詢所有會員功能API 需要先透過資料驗證取得Token, Token設計為 HASH256編碼格式使用期限為5分鐘, 5分鐘過後過期需要再重新取得一次

How to use:
(1) Create docker MySQL
1. docker pull mysql
2. docker run --name mysql_test -e MYSQL_ROOT_PASSWORD=123 -d mysql:latest
3. docker exec -it mysql_test mysql -u root -p
4. create database demo;

(2) Build dockerfile
1. edit Dockerfile DATABASE_URL use your ip to catch mysql
2. docker build -t my_flask .
3. docker run --rm -d my_flask:latest



Todo list:

- [x] 1.RESTful 風格的API 
 
- [x] 2.MySQL資料庫建制, 與flask進行連接 
 
- [x] 3.Token 設計,某些API使用前需要先驗證Token 
 
- [x] 4.Docker包裝flask 與MySQL 

- [ ] 5.Docker-compose  not yet

