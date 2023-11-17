import sqlite3

# cria uma conexao com o Banco de Dados ModuloAcad.db
conexao = sqlite3.connect('ModuloAcad.db')

# obtem um cursor desta conexao
cursor = conexao.cursor()

# executa um script SQL para criar uma tabela no DB
cursor.execute('CREATE TABLE ALUNOS(NOME TEXT, IDADE INT, ALTURA FLOAT, PESO FLOAT, RGM INT, ID_ALUNO INT,  PRIMARY KEY(ID_ALUNO));')
cursor.execute('CREATE TABLE PROFESSORES(NOME TEXT, IDADE INT, ALTURA FLOAT, PESO FLOAT, MATRICULA INT, ID_PROFESSOR INT,  PRIMARY KEY(ID_PROFESSOR));')
cursor.execute('CREATE TABLE DISCIPLINAS(NOME TEXT, CARGAHORARIA INT, TURMA TEXT, NOTAMINIMA FLOAT, CODIGO INT, ID_DISCIPLINA INT, PRIMARY KEY(ID_DISCIPLINA));')

# confirma a execução do comando acima no DB.
conexao.commit()

# fecha a conexao com o DB
conexao.close()
print("DB Construido!")