import requests
import pymysql

print("Conectando ao banco...")
conexao = pymysql.connect(host='localhost' ,database='testelev',user='root', password='1234', port=3306)
print("Conectado ao banco testelev")
url = " https://api-teste-lewe.herokuapp.com/api/basedata"
login={"usuario":"teste","senha":"teste@Lewe123"}
response= requests.post(url,json=login)
print("Conectado na API")
dados=response.json()
countries=dados["country"]
cursor = conexao.cursor()
print("Incrementando ao banco...")
for i in countries:

    if countries[i]=="Brazil":
        query = f'insert into vacinas ( id, date, total_vaccinations, daily_vaccinations, vaccines) values ({i},"{dados["date"][i]}",{int(dados["total_vaccinations"][i] or 0)},{int(dados["daily_vaccinations"][i] or 0)},"{dados["vaccines"][i]}")'
        cursor.execute(query)
        conexao.commit()
cursor.close()
print("Feito")