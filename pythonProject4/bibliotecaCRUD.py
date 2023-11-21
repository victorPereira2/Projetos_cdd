import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302302",
    database = "academiaturmad"
)
print(banco)
def SELECT():

    meucursor = banco.cursor()
    pesquisa = 'select nome,salario,cpf,departamento,filhos from func;'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    for i in resultado:
        print(i)
def InsertInto()


meucursor.execute(sql,data)
banco.commit()
meucursor.close()
