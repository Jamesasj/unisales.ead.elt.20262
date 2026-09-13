import json

users = []
objJson = open('./stg/users.json', 'r').read()
users = json.loads(objJson)

lista = []

# Transformação dos dados dos usuários
for u in users:
    lista.append({
        "nome": u["name"],
        "endereco": u["email"],
        "id": u["id"],
        "company": u["company"]["name"]
    })


## LOAD dimensao usuarios
saida = open('./dw/d_users.csv', 'w')
for item in lista:
    linha = f"{item['id']},{item['nome']},{item['endereco']},{item['company']}\n"
    saida.write(linha)
saida.close()

## LOAD dados no banco de dados
cur.execute("insert into d_users (id, nome, endereco, company) values (%s, %s, %s, %s)", 
            [(item['id'], item['nome'], item['endereco'], item['company']) for item in lista])  
conn.commit()
cur.close()
conn.close()