import mysql.connector
class CRUD:
    def __init__(self):
       self.conexao = mysql.connector.connect(
         host='localhost',
         user='root',
         password='q1w2e3',
         database='metodo_crud'
    )
# objeto para chamar o mysql
       self.meu_cursor = self.conexao.cursor()

    def create(self):
         sql = 'insert into pessoas ' \
               '(nome, dataNasc)' \
               'value' \
               '(%s, %s)'
         valores = ("João", "1989-06-18")
         self.meu_cursor.execute(sql, valores)
         self.conexao.commit()






    def read(self):
         self.meu_cursor.execute('select * from pessoas')

         lista = self.meu_cursor.fetchall()

         for i in lista:
             print(i)

         self.conexao.commit()

# Create
#self.eu_cursor.execute('insert into pessoas '
#                   'value '
 #                  '(1,"Mateus", "1997-07-14")'
#editar o banco de dados
    def update(self):
        comando_sql = 'update pessoas ' \
              'set nome = "Mateus Costa" ' \
              'where nome = "Mateus"'
        self.meu_cursor.execute((comando_sql))
        self.conexao.commit()

# Delete
    def delete(self):
            valor = int(input('Digite o código: '))
            comando_sql = f'delete from pessoas where id = {valor}'
            self.meu_cursor.execute(comando_sql)

            self.conexao.commit()





obj_bd = CRUD()

obj_bd.delete()

