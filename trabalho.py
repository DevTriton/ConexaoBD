import json
import sqlite3

class ModuloAcademico:
    def __init__(self):
        self.listaAlunos = []
        self.listaProfessor = []
        self.listaDisciplinas = []
        self.opcao = 0
        self.opcaoGer = 0
        self.index = 0
        #for cont in range (2):
            #if cont == 2:
                #self.Recuperar()
        #coloquei com o contador pois se não tiver um arquivo ja pré criado e com dados o script da erro, esqueci de perguntar quando tive a chancer :D        

# GERAL 

    def menu_geral(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Qual lista deseja manipular?")
        print("1) Aluno")
        print("2) Professor")
        print("3) Disciplinas")
        print("4) sair")
        self.opcaoGer=int(input("digite a opção desejada "))

    def Executar_geral(self):
        while self.opcaoGer !=4:
            self.menu_geral() 
                        
            if self.opcaoGer==1:
                self.ExecutarAluno()
            elif self.opcaoGer==2:
                self.ExecutarProfessor()
            elif self.opcaoGer==3:
                self.ExecutarDisciplinas()           
            elif self.opcaoGer==4:
                break

    def cadastrar(self):
        
        if self.opcaoGer==1 or self.opcaoGer==2:
            nome = input("digite o nome: ")
            idade = int(input("digite a idade: "))
            altura = float(input("digite a altura (metros): "))
            peso = float(input("digite o peso: "))
            ID = int(input("digite o numero id: "))

            if self.opcaoGer==1:
                RGM = input("digite o RGM do aluno: ")
                conexao = sqlite3.connect('ModuloAcad.db')
                cursor = conexao.cursor()
                cursor.execute("INSERT INTO ALUNOS (NOME, IDADE, ALTURA, PESO, RGM, ID_Aluno) VALUES ('"+nome+"', "+str(idade)+", "+str(altura)+", "+str(peso)+", "+str(RGM)+", "+str(ID)+"); ")
                conexao.commit()
                conexao.close()
                print("comando Inserido!!! ")
                return Aluno(nome, idade, altura, peso, RGM, ID) 

            if self.opcaoGer==2:
                matricula = int(input("digite a matricula desse Professor: "))
                conexao = sqlite3.connect('ModuloAcad.db')
                cursor = conexao.cursor()
                cursor.execute("INSERT INTO PROFESSORES (NOME, IDADE, ALTURA, PESO, MATRICULA, ID_PROFESSOR) VALUES ('"+nome+"', "+str(idade)+", "+str(altura)+", "+str(peso)+", "+str(matricula)+", "+str(ID)+"); ")
                conexao.commit()
                conexao.close()
                print("comando Inserido!!! ")
                return Professor(nome, idade, altura, peso, matricula, ID)
                
        if self.opcaoGer==3:
            nome = input("digite o nome da Disciplina: ")
            cargaHoraria = int(input("digite a carga horaria da Disciplina: "))
            turma = input("digite a turma da Disciplina: ")
            notaMinima = float(input("digite a nota minima da Disciplina: "))
            codigo = int(input("digite o codigo dessa Disciplina: "))
            ID = int(input("digite o ID dessa Disciplina: "))
            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO DISCIPLINAS (NOME, CARGAHORARIA, TURMA, NOTAMINIMA, CODIGO, ID_DISCIPLINA) VALUES ('"+nome+"', "+str(cargaHoraria)+", '"+turma+"', "+str(notaMinima)+", "+str(codigo)+", "+str(ID)+"); ")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")
            return Disciplinas(nome, cargaHoraria, turma, notaMinima, codigo, ID)    

    def imprimir(self):

        if self.opcaoGer==1:
            print("----------------------------------------")
            #for cont in self.listaAlunos:
               # print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso, "/", cont.ID, "/", cont.RGM)  
            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            retorno = cursor.execute('SELECT * FROM ALUNOS;')
            lista = []
            for linha in retorno:
                lista.append(linha[:])
            print(lista)
            conexao.close()  
            print("----------------------------------------")

        if self.opcaoGer==2:
            print("----------------------------------------")
            #for cont in self.listaProfessor:
                #print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso, "/", cont.matricula)  
            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            retorno = cursor.execute('SELECT * FROM PROFESSORES;')
            lista = []
            for linha in retorno:
                lista.append(linha[:])
            print(lista)
            conexao.close()    
            print("----------------------------------------")

        if self.opcaoGer==3:
            print("----------------------------------------")
            #for cont in self.listaDisciplinas:
                #print(cont.nome, "/", cont.cargaHoraria, "/", cont.turma, "/", cont.notaMinima, "/", cont.codigo)
            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            retorno = cursor.execute('SELECT * FROM DISCIPLINAS;')
            lista = []
            for linha in retorno:
                lista.append(linha[:])
            print(lista)
            conexao.close()      
            print("----------------------------------------")    

    def Salvar(self):
        if self.opcaoGer==1:
            lista = []
            arquivo = open("alunos.json", 'w')
            for cont in self.listaAlunos :
                lista.append(cont.Serializar())
            json.dump(lista, arquivo) 

        if self.opcaoGer==2:
            lista = []
            arquivo = open("professores.json", 'w')
            for cont in self.listaProfessor :
                lista.append(cont.Serializar())
            json.dump(lista, arquivo) 

        if self.opcaoGer==3:  
            lista = []
            arquivo = open("Disciplinas.json", 'w')
            for cont in self.listaDisciplinas :
                lista.append(cont.Serializar())
            json.dump(lista, arquivo)   

    def Recuperar(self):
        if self.opcaoGer==1:
            self.listaAlunos.clear()
            arquivo = open("alunos.json", 'r')
            lista_de_jsons_text = json.load(arquivo)
            for text in lista_de_jsons_text:
                a = Aluno()
                a.Deserializar(text)
                self.listaAlunos.append(a)

        if self.opcaoGer==2:
            self.listaProfessor.clear()
            arquivo = open("professores.json", 'r')
            lista_de_jsons_text = json.load(arquivo)
            for text in lista_de_jsons_text:
                a = Professor()
                a.Deserializar(text)
                self.listaProfessor.append(a)

        if self.opcaoGer==3:            
            self.listaDisciplinas.clear()
            arquivo = open("Disciplinas.json", 'r')
            lista_de_jsons_text = json.load(arquivo)
            for text in lista_de_jsons_text:
                a = Disciplinas()
                a.Deserializar(text)
                self.listaDisciplinas.append(a)

    def Remover(self):
        if self.opcaoGer==1:
            resp = int(input("digite o Rgm do aluno: "))
            #for cont in self.listaAlunos:
                #if resp == cont.RGM:
                    #index = cont.ID - 1
                    #self.listaAlunos.pop(index)

            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            cursor.execute(" DELETE FROM ALUNOS WHERE RGM = "+str(resp)+" ;")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")        

        if self.opcaoGer==2:
            resp = int(input("digite a matricula do professor que deseja remover: "))
            #for cont in self.listaProfessor:
                #if resp == cont.matricula:
                    #index = cont.ID - 1
                    #self.listaProfessor.pop(index)

            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            cursor.execute(" DELETE FROM PROFESSORES WHERE MATRICULA = "+str(resp)+" ;")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")              

        if self.opcaoGer==3:
            resp = int(input("digite o codigo do Disciplinas que deseja remover: "))
            #for cont in self.listaDisciplinas:
                #if resp == cont.codigo:
                    #index = cont.ID - 1
                    #self.listaDisciplinas.pop(index)

            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            cursor.execute(" DELETE FROM DISCIPLINAS WHERE CODIGO = "+str(resp)+" ;")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")              

    def atualizar(self):
        if self.opcaoGer==1:
            resp= int(input("digite o rgm do aluno que deseja alterar"))
            #for cont in self.listaAlunos:
                #if resp == cont.RGM:
                    #index = cont.ID - 1
                    #self.listaAlunos.pop(index)
                    #aluno = self.cadastrarAluno()
                    #self.listaAlunos.append(aluno)
                    #self.SalvarAluno()
            nome = input("digite o nome: ")
            idade = int(input("digite a idade: "))
            altura = float(input("digite a altura (metros): "))
            peso = float(input("digite o peso: "))
            ID = int(input("digite o numero id: "))
            RGM = input("digite o RGM do aluno: ")

            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE ALUNOS SET NOME = '"+nome+"', IDADE = "+str(idade)+", ALTURA = "+str(altura)+", PESO = "+str(peso)+", RGM = "+str(RGM)+", ID_ALUNO = "+str(ID)+" WHERE RGM = "+str(resp)+";")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")        

        if self.opcaoGer==2:            
            resp= int(input("digite a matricula do professor que deseja alterar"))
            #for cont in self.listaProfessor:
                #if resp == cont.matricula:
                    #index = cont.ID - 1
                   # self.listaProfessor.pop(index)
                    #Professor = self.cadastrarProfessor()
                    #self.listaProfessor.append(Professor)
                    #self.SalvarProfessor()
            nome = input("digite o nome: ")
            idade = int(input("digite a idade: "))
            altura = float(input("digite a altura (metros): "))
            peso = float(input("digite o peso: "))
            ID = int(input("digite o numero id: "))
            Matricula = input("digite a matricula do professor: ")

            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE PROFESSORES SET NOME = '"+nome+"', IDADE = "+str(idade)+", ALTURA = "+str(altura)+", PESO = "+str(peso)+", MATRICULA = "+str(Matricula)+", ID_PROFESSOR = "+str(ID)+" WHERE MATRICULA = "+str(resp)+";")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")            

        if self.opcaoGer==3:
            resp= int(input("digite o codigo do Disciplinas que deseja alterar"))
            #for cont in self.listaDisciplinas:
                #if resp == cont.codigo:
                    #index = cont.ID - 1
                    #self.listaDisciplinas.pop(index)
                    #Disciplinas = self.cadastrarDisciplinas()
                    #self.listaDisciplinas.append(Disciplinas)
                    #self.SalvarDisciplinas()
            nome = input("digite o nome da Disciplina: ")
            cargaHoraria = int(input("digite a carga horaria da Disciplina: "))
            turma = input("digite a turma da Disciplina: ")
            notaMinima = float(input("digite a nota minima da Disciplina: "))
            codigo = int(input("digite o codigo dessa Disciplina: "))
            ID = int(input("digite o ID dessa Disciplina: "))

            conexao = sqlite3.connect('ModuloAcad.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE DISCIPLINAS SET NOME = '"+nome+"', CARGAHORARIA = "+str(cargaHoraria)+", TURMA = '"+str(turma)+"', NOTAMINIMA = "+str(notaMinima)+", CODIGO = "+str(codigo)+", ID_DISCIPLINA = "+str(ID)+" WHERE CODIGO = "+str(resp)+";")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")       
                    
    def consultar65(self):
        i=0
        for cont in self.listaAlunos:
            if cont.peso>65:
                i=i+1
        print(f"a quantidade de alunos com mais de 65kg são {i}")

    def maisp(self):
        i=0
        j=""
        for cont in self.listaAlunos:
            if cont.peso>i:
                i=cont.peso
                j=cont.nome
        print(f"o aluno mais pesado é: {j}") 

    def menosp(self):
        j=""
        i=500
        for cont in self.listaAlunos:
            if cont.peso<i:
                i=cont.peso
                j=cont.nome
        print(f"o aluno menos pesado é: {j}")

    def qtdmaior(self):
        i=0
        for cont in self.listaAlunos:
            if cont.idade>=18:
                i=i+1
        print(f"A quantidade de alunos maiores de idade é {i}")        

    def qmaior(self):
        i=[]
        for cont in self.listaAlunos:
            if cont.idade>=18:
                i.append(cont.nome)
        print(f"o alunos maiores de idade são {i}")  

    def qmenor(self):
        i=[]
        for cont in self.listaAlunos:
            if cont.idade<18:
                i.append(cont.nome)
        print(f"o alunos menores de idade são {i}")  

    def imc(self):
            i=""
            resp=input("digite o nome do aluno: ")
            for cont in self.listaAlunos:
                if cont.nome == resp:
                    resultado = cont.peso / (cont.altura * cont.altura)
                if resultado < 18.5:
                    i="abaixo do peso normal"
                elif resultado > 18.5 and resultado < 24.9:
                    i = "Peso Normal"
                elif resultado > 25.0 and resultado < 29.9:
                    i="Excesso de peso"
                elif resultado > 30.0 and resultado < 34.9:
                    i="obesidade grau 1"
                elif resultado > 35.0 and resultado < 39.9:
                    i="obesidade grau 2"
                elif resultado >= 40.0:
                    i="obesidade grau 3"    
            print(f"o imc desse aluno é {resultado} é a situação dele é {i}")            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ALUNO  
    def menuAluno(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Aluno")
        print("2) Imprimir Alunos")
        print("3) Consulta Alunos > 65 Kg:")
        print("4) Aluno mais pesado")
        print("5) Aluno menos pesado")
        print("6) qtd de alunos maiores de idade")
        print("7) quem são os alunos maiores de idade")
        print("8) quem são os alunos menores de idade")
        print("9) calcular imc")
        print("10) excluir um aluno")
        print("11) atualizar um aluno")
        print("12) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))

    def ExecutarAluno(self):
        while self.opcao != 12:
            self.menuAluno() 
            
            if self.opcao==1:
                aluno = self.cadastrar()
                self.listaAlunos.append(aluno)
                #self.Salvar()
            elif self.opcao==2:
                self.imprimir()
            elif self.opcao==3:
                self.consultar65()
            elif self.opcao==4:
                self.maisp() 
            elif self.opcao==5:
                self.menosp() 
            elif self.opcao==6:
                self.qtdmaior() 
            elif self.opcao==7:
                self.qmaior() 
            elif self.opcao==8:
                self.qmenor() 
            elif self.opcao==9:
                self.imc()
            elif self.opcao==10:
                self.Remover()
                self.Salvar()
            elif self.opcao==11:
                self.atualizar()
                self.Salvar()             
            elif self.opcao==12:
                break

     
      
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
# PROFESSOR
 
    def menuProfessor(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Professor")
        print("2) Imprimir Professor")
        print("3) excluir um Professor")
        print("4) atualizar um Professor")
        print("5) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))

    def ExecutarProfessor(self):
        while self.opcao != 5:
            self.menuProfessor() 
            
            if self.opcao==1:
                Professor = self.cadastrar()
                self.listaProfessor.append(Professor)
                #self.Salvar()
            elif self.opcao==2:
                self.imprimir()
            elif self.opcao==3:
                self.Remover()
                self.Salvar()
            elif self.opcao==4:
                self.atualizar()
                self.Salvar()             
            elif self.opcao==5:
                break
          
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#  
# DISCIPLINAS

    def menuDisciplinas(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Disciplina")
        print("2) Imprimir Disciplinas")
        print("3) excluir uma Disciplina")
        print("4) atualizar uma Disciplina")
        print("5) Sair")
        self.opcao=int(input("digite a opção que deseja fazer: "))

    def ExecutarDisciplinas(self):
        while self.opcao != 5:
            self.menuDisciplinas() 
            
            if self.opcao==1:
                disciplina = self.cadastrar()
                self.listaDisciplinas.append(disciplina)
                #self.Salvar()
            elif self.opcao==2:
                self.imprimir()
            elif self.opcao==3:
                self.Remover()
                self.Salvar()
            elif self.opcao==4:
                self.atualizar()
                self.Salvar()             
            elif self.opcao==5:
                break   
                                   
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#          

class Aluno(ModuloAcademico):
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0.0,  ID=0, RGM=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.ID = ID
        self.RGM = RGM

    def Serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["idade"] = self.idade
        dic["altura"] = self.altura
        dic["peso"] = self.peso
        dic["RGM"] = self.RGM
        dic["ID"] = self.ID
        texto_json = json.dumps(dic, indent = 3)
        return texto_json

    def Deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.idade = dic["idade"]
        self.altura = dic["altura"]
        self.peso = dic["peso"]
        self.RGM = dic["RGM"] 
        self.ID = dic["ID"]                                   

class Professor(ModuloAcademico):
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0, matricula = 0, ID = 0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.matricula = matricula
        self.ID = ID

    def Serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["idade"] = self.idade
        dic["altura"] = self.altura
        dic["peso"] = self.peso
        dic["matricula"] = self.matricula
        dic["ID"] = self.ID
        texto_json = json.dumps(dic, indent = 3)
        return texto_json

    def Deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.idade = dic["idade"]
        self.altura = dic["altura"]
        self.peso = dic["peso"]
        self.matricula = dic["Matricula"]
        self.ID = dic["ID"] 

class Disciplinas(ModuloAcademico):
    def __init__(self, nome = "", cargaHoraria = 0, turma = "", notaMinima = 0.0, codigo = 0, ID = 0):
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        self.turma = turma
        self.notaMinima = notaMinima
        self.codigo = codigo
        self.ID = ID

    def Serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["cargaHoraria"] = self.cargaHoraria
        dic["turma"] = self.turma
        dic["notaMinima"] = self.notaMinima
        dic["ID"] = self.ID
        texto_json = json.dumps(dic, indent = 3)
        return texto_json

    def Deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.cargaHoraria = dic["cargaHoraria"]
        self.turma = dic["turma"]
        self.notaMinima = dic["notaMinima"]
        self.ID = dic["ID"] 

moduloA = ModuloAcademico()
moduloA.Executar_geral()