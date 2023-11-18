import json #Importa a biblioteca json
import os #Importa a biblioteca os

# Inicia o Código
def iniciar():
    exibir_menu()

# Cria um dicionário chamado dados
dados = {}

# Cria um arquivo json se ele não for encontrado na pasta local
if not os.path.isfile('procedimentos.json'):
    arquivo_json = open('procedimentos.json', 'w')
    json.dump(dados, arquivo_json)
    arquivo_json.close()

# Atualiza o dicionário "dados" com o arquivo json selecionado
def atualiza_json():
    arquivo_json = open('procedimentos.json', 'r')
    tamanho_json = arquivo_json.read()
    arquivo_json.close()
    # Se o arquivo json possuir mais de um registro, a variavel dados recebe o valor do json
    if len(tamanho_json) > 1:
        global dados
        arquivo_json = open('procedimentos.json', encoding="utf-8")
        objeto_json = json.load(arquivo_json)
        arquivo_json.close()
        dados = objeto_json
        return dados

def dump_arquivo():
    arquivo_json = open("procedimentos.json", "w", encoding="utf-8")
    json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
    arquivo_json.close()

# Função que Imprime o menu de opções
def exibir_menu():
    while True:
        atualiza_json() #Inicia a função atualiza_json
        global dados
        #Imprime o menu de opções
        print(''' 
        
<<<<<<<<<<<<<<<<Opções>>>>>>>>>>>>>>>>
1 - Cadastrar Procedimento
2 - Pesquisar Procedimento
3 - Alterar Procedimento
4 - Excluir Procedimento (ainda não implementado)
5 - Realizar Backup do Arquivo
6 - Puxar Backup para o Arquivo
0 - Sair
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
''')

        # Pede para o Usuário escolher qual opção quer realizar
        while True:
            try:
                escolha = int(input("Digite a opção escolhida: "))
                break
            except ValueError:
                print("ERRO! Valor inválido, Digite um número inteiro")

        # Realiza funções de acordo com a escolha do usuário
        if escolha == 1: #Criar
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            # Recebe o valor nome do procedimento que servirá como uma chave/identificador no dicionário
            print("Digite o nome do procedimento")
            nome_procedimento = (input("-----------:"))
            cadastrar_procedimento(nome_procedimento)
            dump_arquivo()

        elif escolha == 2: #Ler
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            if len(dados) < 1:
                print("Nenhum procedimento cadastrado")
            else:
                while True:
                    listar_procedimento()
                    pesquisar_procedimento()
                    print("\nDigite 'sim' para continuar a pesquisa")
                    continuar = input("-----------:")
                    if continuar.lower() != "sim" and continuar.lower() != "s":
                        break

        elif escolha == 3: #Atualizar
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            if len(dados) < 1:
                print("Nenhum procedimento cadastrado")
            else:
                while True:
                    listar_procedimento()
                    alterar_procedimento()
                    dump_arquivo()
                    print("\nDigite 'sim' para continuar à alterar")
                    continuar = input("-----------:")
                    if continuar.lower() != "sim" and continuar.lower() != "s":
                        break
        elif escolha == 4: #Excluir
            dados.pop("Corte Curt")
            dump_arquivo()
        elif escolha == 5: #Fazer Backup
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            fazer_backup()
            print("<<<<<Backup Realizado Com Sucesso>>>>>")
        elif escolha == 6:
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            try:
                puxar_backup()
                dump_arquivo()
                print("<<<<Arquivo Atualizado Com Sucesso>>>>")
            except:
                print("Você não possui nenhum Arquivo de Backup")
        elif escolha == 0: # Sair
            print("\n<<<<<<<<<<<<<<Volte Logo>>>>>>>>>>>>>>")
            break


def cadastrar_procedimento(nome_procedimento):
    global dados
    # Cria um dicionário de Procedimentos
    dict_procedimento = {}

    # Cadastra a duração do procedimento
    print("Digite a duração média do procedimento (min)")
    while True:
        try:
            duracao_procedimento = int(input("-----------:"))
            dict_procedimento["Duração"] = ("%d min"%duracao_procedimento)
            break
        except ValueError:
            print("ERRO! Valor inválido, Digite um número inteiro")
    

    # Cadastrar valor do procedimento
    print("Digite o valor do procedimento (moeda: R$)")
    while True:
        try:
            valor = float(input("-----------:"))
            dict_procedimento["Valor"] = ("R$%.2f"%valor)
            break
        except ValueError:
            print("ERRO! Valor inválido, Digite um número real\n(separação dos decimais deve ser realizada com '.')")
    

    # Cadastrar materiais utilizados
    print("Digite os materiais utilizados ('fim' para sair)")
    materiais = []
    while True:
        material = input("-----------:")
        if material.lower() == "fim" or material.lower() == "f" or material.lower() == "":
            break
        else:
            materiais.append(material.title())
    dict_procedimento["Materiais"] = materiais
    

    # Cadastrar os profissionais autorizados a realizar o procedimento
    print("Digite quais os profissionais autrizados a\nrealizar o procedimento ('fim' para sair)")
    profissionais = []
    while True:
        profissional = input("-----------:")
        if profissional.lower() == "fim" or profissional.lower() == "f" or profissional.lower() == "":
            break
        else:
            profissionais.append(profissional.title())
    dict_procedimento["Profissionais"] = profissionais
    #Adisciona os dados no dicionário dados
    dados[nome_procedimento.title()] = dict_procedimento

def listar_procedimento():
    global dados
    for chave, valor in dados.items():
        print(chave)

def pesquisar_procedimento():
    global dados
    print("\nQual procedimento deseja pesquisar?")
    procedimento = input("-----------:")
    chave_dados = dados.get(procedimento.title())
    try:
        if chave_dados == dados[procedimento.title()]:
            for chave, valor in chave_dados.items():
                print(chave, "-", valor)
    except KeyError:
        print("Chave não encontrada")

def alterar_procedimento():
    global dados
    print("\nQual procedimento deseja alterar?")
    procedimento = input("-----------:")
    chave_dados = dados.get(procedimento.title())
    try:
        if chave_dados == dados[procedimento.title()]:
            while True:
                x = 1
                for chave, valor in chave_dados.items():
                    print(x, "-", chave, "-", valor)
                    x += 1
                print(9, "-", "Fim")

                print("\nO que deseja alterar?")
                alterar = input("-----------:")
                match alterar.lower():

                    case ("1"|"duração"|"duracao"|"duracão"|"duraçao"):
                        print("Digite a duração média do procedimento (min)")
                        while True:
                            try:
                                duracao_procedimento = int(input("-----------:"))
                                chave_dados["Duração"] = ("%d min" % duracao_procedimento)
                                break
                            except ValueError:
                                print("ERRO! Valor inválido, Digite um número inteiro")
                        

                    case ("2"|"valor"):
                        print("Digite o valor do procedimento (moeda: R$)")
                        while True:
                            try:
                                valor = float(input("-----------:"))
                                chave_dados["Valor"] = ("R$%.2f" % valor)
                                break
                            except ValueError:
                                print("ERRO! Valor inválido, Digite um número real\n(separação dos decimais deve ser realizada com '.')")
                        

                    case ("3"|"materiais"):
                        print('''
1 - Adicionar
2 - Alterar
3 - Remover
                        ''')
                        escolha = input("-----------:")

                        if escolha.lower() == "1" or escolha.lower() == "adicionar":
                            materiais = chave_dados["Materiais"]
                            print("Digite os materiais utilizados ('fim' para sair)")
                            while True:
                                material = input("-----------:")
                                if material.lower() == "fim" or material.lower() == "f" or material.lower() == "":
                                    break
                                else:
                                    if materiais.index(material.title()):
                                        print("Valor já existente")
                                    else:
                                        materiais.append(material.title())
                            chave_dados["Materiais"] = materiais
                            

                        elif escolha.lower() == "2" or escolha.lower() == "alterar":
                            materiais = chave_dados["Materiais"]
                            for valor in materiais:
                                print(valor)
                            print("Digite os materiais deseja alterar")
                            material = input("-----------:")
                            try:
                                print("Digite o novo material ('fim' para sair):")
                                novo_material = input("-----------:")
                                materiais[materiais.index(material.title())] = novo_material.title()
                            except ValueError:
                                print("Valor não encontrado")

                        elif escolha.lower() == "3" or escolha.lower() == "remover":
                            materiais = chave_dados["Materiais"]
                            for valor in materiais:
                                print(valor)
                            print("Digite os materiais deseja remover ('fim' para sair)")
                            while True:
                                material = input("-----------:")
                                if material.lower() == "fim" or material.lower() == "f" or material.lower() == "":
                                    break
                                else:
                                    try:
                                        materiais.pop(materiais.index(material.title()))
                                    except ValueError:
                                        print("Valor não encontrado")

                        else:
                            print("Opção inválida")


                    case ("4"|"profissionais"):
                        print('''
1 - Adicionar
2 - Alterar
3 - Remover
                        ''')
                        escolha = input("-----------:")

                        if escolha.lower() == "1" or escolha.lower() == "adicionar":
                            profissionais = chave_dados["Profissionais"]
                            print("Digite os profissionais autorizados ('fim' para sair)")
                            while True:
                                profissional = input("-----------:")
                                if profissional.lower() == "fim" or profissional.lower() == "f" or profissional.lower() == "":
                                    break
                                else:
                                    if profissionais.index(profissional.title()):
                                            print("Valor ja existente")
                                    else:
                                        profissionais.append(profissional.title())
                            chave_dados["Profissionais"] = profissionais

                        elif escolha.lower() == "2" or escolha.lower() == "alterar":
                            profissionais = chave_dados["Profissionais"]
                            for valor in profissionais:
                                print(valor)
                            print("Digite os profissionais que deseja alterar")
                            profissional = input("-----------:")
                            try:
                                print("Digite o novo profissional ('fim' para sair):")
                                novo_profissional = input("-----------:")
                                profissionais[profissionais.index(profissional.title())] = novo_profissional.title()
                            except ValueError:
                                print("Valor não encontrado")

                        elif escolha.lower() == "3" or escolha.lower() == "remover":
                            profissionais = chave_dados["Profissionais"]
                            for valor in profissionais:
                                print(valor)
                            print("Digite os profissionais deseja remover ('fim' para sair)")
                            while True:
                                profissional = input("-----------:")
                                if profissional.lower() == "fim" or profissional.lower() == "f" or profissional.lower() == "":
                                    break
                                else:
                                    try:
                                        profissionais.pop(profissionais.index(profissional.title()))
                                    except ValueError:
                                        print("Valor não encontrado")

                        else:
                            print("Opção inválida")

                    case ("9" | "fim" | "f"):
                        break

    except KeyError:
        print("Chave não encontrada")


# Cria um novo documento de backup do arquivo existente
def fazer_backup():
    arquivo_json = open("procedimentos.json", encoding="utf-8")
    carregamento_json = json.load(arquivo_json)
    arquivo_json.close()
    backup_json = open("backup_procedimentos.json", "w", encoding="utf-8")
    json.dump(carregamento_json, backup_json, ensure_ascii=False, indent=4)

#Puxa os valores do backup para o arquivo existente
def puxar_backup():
    global dados
    backup_json = open("backup_procedimentos.json", encoding="utf-8")
    carregamento_json = json.load(backup_json)
    backup_json.close()
    dados = carregamento_json
    return dados