import json #Importa a biblioteca json
import os #Importa a biblioteca os

##############################################################################################################

# Inicia o Código
def iniciar():
    #Chama a função exibir_menu
    exibir_menu()

##############################################################################################################

# Cria um dicionário chamado dados
dados = {}

##############################################################################################################

# Verifica se não existe o arquivo procedimentos.json
if not os.path.isfile('procedimentos.json'):
    # Cria um arquivo procedimentos.json
    arquivo_json = open('procedimentos.json', 'w')
    # Adiciona o valor de dados no arquivo json
    json.dump(dados, arquivo_json)
    # Fecha o arquivo json
    arquivo_json.close()

##############################################################################################################

# Atualiza o dicionário "dados" com o arquivo json selecionado
def atualiza_json():
    # Abre o arquivo json para leitura
    arquivo_json = open('procedimentos.json', 'r')
    # Lê o arquivo json
    tamanho_json = arquivo_json.read()
    # Fecha o arquivo json
    arquivo_json.close()
    # Se o arquivo json possuir mais de um registro, a variavel dados recebe o valor do json
    if len(tamanho_json) > 1:
        # Utiliza o dicionário dados dentro da função
        global dados
        # Abre o arquivo json com todas as acentuações e caracteres especiais do português
        arquivo_json = open('procedimentos.json', encoding="utf-8")
        # Carrega o arquivo json para uma variável chamada objeto_json
        objeto_json = json.load(arquivo_json)
        # Fecha o arquivo
        arquivo_json.close()
        # Atribui o valor de objeto_json para o dicionário dados
        dados = objeto_json
        # Retorna o dicionário dados
        return dados

##############################################################################################################

# Salva os arquivos no Json
def dump_arquivo():
    # Abre o arquivo json para escrita com todas as acentuações do português
    arquivo_json = open("procedimentos.json", "w", encoding="utf-8")
    # Envia o dicionário dados para o arquivo json sem alterar os caracteres e já com indentação
    json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
    # Fecha o arquivo json
    arquivo_json.close()

##############################################################################################################

# Função que Imprime o menu de opções
def exibir_menu():
    # Abre um loop
    while True:
        # Atualiza o dicionário dados
        atualiza_json()
        # Utiliza o dicionário dados dentro da função
        global dados

        #Imprime o menu de opções
        print(''' 
        
<<<<<<<<<<<<<<<<Opções>>>>>>>>>>>>>>>>
1 - Cadastrar Procedimento
2 - Pesquisar Procedimento
3 - Alterar Procedimento
4 - Excluir Procedimento
5 - Realizar Backup do Arquivo
6 - Puxar Backup para o Arquivo
0 - Sair
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
''')

        # Abre um loop
        while True:
            # Tenta
            try:
                # Pergunta ao usuário qual a opção escolhida (INTEIRO)
                escolha = int(input("Digite a opção escolhida: "))
                # Fecha o loop
                break
            # Caso dê ValueError
            except ValueError:
                #pede para o usuário escrever um número inteiro
                print("ERRO! Valor inválido, Digite um número inteiro")

        # Realiza funções de acordo com a escolha do usuário
        if escolha == 1: #Criar
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            # Pede para o usuário o nome do procedimento
            print("Digite o nome do procedimento")
            # Armazena o valor numa variável que servirá como uma chave/identificador no dicionário
            nome_procedimento = (input("-----------:"))
            # Se o ultimo valor de nome_procedimento for um '_' ou um espaço
            if nome_procedimento[-1:] == "_" or nome_procedimento[-1:] == " ":
                #apaga o ultimo valor
                nome_procedimento = nome_procedimento[:-1]
            # Se o primeiro valor de nome_procedimento for um '_' ou um espaço
            elif nome_procedimento[:1] == "_" or nome_procedimento[:1] == " ":
                #apaga o primeiro valor
                nome_procedimento = nome_procedimento[1:]
            # Chama a função de cadastrar procedimento já com o nome do procedimento
            cadastrar_procedimento(nome_procedimento)
            # Salva os arquivos no json
            dump_arquivo()

        elif escolha == 2: #Ler
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            # Verifica se o dicionário dados possui conteúdo
            if len(dados) < 1:
                # Se não houver conteúdo fala que não possui procedimento cadastrado
                print("Nenhum procedimento cadastrado")
            # Caso tenha um ou mais procedimentos
            else:
                # Abre um loop
                while True:
                    # Lista os procedimentos
                    listar_procedimento()
                    # Abre as opções para pesquisa
                    pesquisar_procedimento()
                    # Pergunta se o usuário quer continuar a pesquisa
                    print("\nDigite 'sim' para continuar a pesquisa")
                    # Armazena o valor da resposta na variável continuar
                    continuar = input("-----------:")
                    # Se continuar for diferente de sim ou s
                    if continuar.lower() != "sim" and continuar.lower() != "s":
                        # Fecha o loop
                        break

        elif escolha == 3: #Atualizar
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            # Verifica se o dicionário dados possui conteúdo
            if len(dados) < 1:
                # Se não houver conteúdo fala que não possui procedimento cadastrado
                print("Nenhum procedimento cadastrado")
            # Caso tenha um ou mais procedimentos
            else:
                # Abre um loop
                while True:
                    # Lista os procedimentos
                    listar_procedimento()
                    # Realiza as alterações nos procedimentos escolhidos
                    alterar_procedimento()
                    # Salva os arquivos no json
                    dump_arquivo()
                    # Pergunta se o usuário quer continuar a pesquisa
                    print("\nDigite 'sim' para continuar à alterar")
                    # Armazena o valor da resposta na variável continuar
                    continuar = input("-----------:")
                    # Se continuar for diferente de sim ou s
                    if continuar.lower() != "sim" and continuar.lower() != "s":
                        # Fecha o loop
                        break

        elif escolha == 4: #Excluir
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            # Verifica se o dicionário dados possui conteúdo
            if len(dados) < 1:
                # Se não houver conteúdo fala que não possui procedimento cadastrado
                print("Nenhum procedimento cadastrado")
            # Caso tenha um ou mais procedimentos
            else:
                # Abre um loop
                while True:
                    # Lista os procedimentos
                    listar_procedimento()
                    # Exclui os procedimentos selecionados
                    excluir_procedimento()
                    # Salva os arquivos no json
                    dump_arquivo()
                    # Pergunta se o usuário quer continuar a pesquisa
                    print("\nDigite 'sim' para continuar")
                    # Armazena o valor da resposta na variável continuar
                    continuar = input("-----------:")
                    # Se continuar for diferente de sim ou s
                    if continuar.lower() != "sim" and continuar.lower() != "s":
                        # Fecha o loop
                        break

        elif escolha == 5: #Fazer Backup
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            # Tenta
            try:
                # Salva um backup do arquivo json
                fazer_backup()
                # Fala que o backup foi realizado com sucesso
                print("<<<<<Backup Realizado Com Sucesso>>>>>")
            # Caso dê algum erro
            except:
                # Fala que deu um erro ao realizar o backup
                print("Erro ao realizar o backup")

        elif escolha == 6: #Puxar Backup
            print("\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>\n")
            # Tenta
            try:
                # Puxar o arquivo backup para o arquivo json utilizado
                puxar_backup()
                # Salva o arquivo json
                dump_arquivo()
                # Diz que o arquivo foi atualizado com sucesso
                print("<<<<Arquivo Atualizado Com Sucesso>>>>")
            except:
                # Fala que houve um erro ao puxar o arquivo de backup
                print("Erro ao puxar o Arquivo de Backup")

        elif escolha == 0: # Sair
            print("\n<<<<<<<<<<<<<<Volte Logo>>>>>>>>>>>>>>")
            # Fecha o loop
            break

##############################################################################################################

def cadastrar_procedimento(nome_procedimento):
    # Utiliza o dicionário dados dentro da função
    global dados
    # Cria um dicionário de Procedimentos
    dict_procedimento = {}

    # Pede a duração do procedimento
    print("Digite a duração média do procedimento (min)")
    # Abre um loop
    while True:
        # Tenta
        try:
            # Armazena a duração do procedimento numa variável (INTEIRO)
            duracao_procedimento = int(input("-----------:"))
            # Passa os valores pro dicionário de procedimentos de chave: Duração e valor o valor da variável
            dict_procedimento["Duração"] = ("%d min"%duracao_procedimento)
            # Fecha o loop
            break
        # Caso dê ValueError
        except ValueError:
            # Pede para o usuário escrever um número inteiro
            print("ERRO! Valor inválido, Digite um número inteiro")
    

    # Cadastrar valor do procedimento
    print("Digite o valor do procedimento (moeda: R$)")
    # Abre um loop
    while True:
        # Tenta
        try:
            # Armazena o valor do procedimento numa variável (REAL)
            valor = float(input("-----------:"))
            # Passa os valores pro dicionário de procedimentos de chave: Valor e valor o valor da variável
            dict_procedimento["Valor"] = ("R$%.2f"%valor)
            # Fecha o loop
            break
        # Caso dê ValueError
        except ValueError:
            # Pede para o usuário escrever um número real e com as separações dos decimais com pontos
            print("ERRO! Valor inválido, Digite um número real\n(separação dos decimais deve ser realizada com '.')")
    

    # Cadastrar materiais utilizados
    print("Digite os materiais utilizados ('fim' para sair)")
    # Abre uma lista de materiais
    materiais = []
    # Abre um loop
    while True:
        # Armazena o valor do material
        material = input("-----------:")
        # Se material for fim ou f ou enter
        if material.lower() == "fim" or material.lower() == "f" or material.lower() == "":
            # Fecha o loop
            break
        # Se não
        else:
            try:
                # Verifica se o material já está na lista
                if (materiais.index(material.title())+1) == True:
                        # Fala que o valor ja existe na lista
                        print("Valor já existente")
            # Caso dê ValueError
            except ValueError:
                # Realiza o append do material na lista materiais
                materiais.append(material.title())
    # Passa os valores pro dicionário de procedimentos de chave: material e valor a lista de materiais
    dict_procedimento["Materiais"] = materiais

    # Cadastrar os profissionais autorizados a realizar o procedimento
    print("Digite quais os profissionais autrizados a\nrealizar o procedimento ('fim' para sair)")
    profissionais = []
    # Abre um loop
    while True:
        profissional = input("-----------:")
        if profissional.lower() == "fim" or profissional.lower() == "f" or profissional.lower() == "":
            # Fecha o loop
            break
        # Se não
        else:
            # Tenta
            try:
                # Verifica se o profissional já está na lista
                if (profissionais.index(profissional.title())+1) == True:
                        # Fala que o valor ja existe na lista
                        print("Valor já existente")
            # Caso dê ValueError
            except ValueError:
                # Realiza o append do profissional na lista profissionais
                profissionais.append(profissional.title())
    # Passa os valores pro dicionário de procedimentos de chave: profissional e valor a lista de profissionais
    dict_procedimento["Profissionais"] = profissionais

    #Adiciona os dados no dicionário dados
    dados[nome_procedimento.title()] = dict_procedimento

##############################################################################################################

def listar_procedimento():
    # Utiliza o dicionário dados dentro da função
    global dados
    # Para cada chave ou valor dos itens do dicionario dados
    for chave, valor in dados.items():
        # Mostra as chaves
        print(chave)

##############################################################################################################

def pesquisar_procedimento():
    # Utiliza o dicionário dados dentro da função
    global dados
    # Pergunta qual procedimento deseja pesquisar
    print("\nQual procedimento deseja pesquisar?")
    # Armazena o valor em uma variável
    procedimento = input("-----------:")
    # Recebe os valores da chave selecionada com as iniciais em maiusculas e armazena numa variável
    chave_dados = dados.get(procedimento.title())
    # Tenta
    try:
        # Se houver um valor da chave selecionada dentro de dados
        if chave_dados == dados[procedimento.title()]:
            # para cada chave e valor dentro dos itens de chave_dados
            for chave, valor in chave_dados.items():
                # ele imprime as chaves e os valores
                print(chave, "-", valor)
    # Caso não encontre a chave
    except KeyError:
        # Fala que a chave não foi encontrada
        print("Chave não encontrada")

##############################################################################################################

def alterar_procedimento():
    # Utiliza o dicionário dados dentro da função
    global dados
    # Pergunta qual procedimento quer alterar
    print("\nQual procedimento deseja alterar?")
    # Armazena o valor numa variável
    procedimento = input("-----------:")
    # Armazena o valor do procedimento escolhido
    chave_dados = dados.get(procedimento.title())
    # Tenta
    try:
        # Se houver um procedimento com o nome escolhido em dados
        if chave_dados == dados[procedimento.title()]:
            # Abre um loop
            while True:
                # Determina o valor de i
                i = 1
                # Pra cada chave no procedimento
                for chave, valor in chave_dados.items():
                    # Imprime (indice, chave e valor)
                    print(i, "-", chave, "-", valor)
                    # i recebe mais um
                    i += 1
                # Imprime 9 para salvar
                print(9, "-", "Salvar Alterações")

                # Pergunta o que quer alterar no procedimento
                print("\nO que deseja alterar?")
                # armazena o valor
                alterar = input("-----------:")
                # Abre um mach case com o valor em minúsculo
                match alterar.lower():
                    
                    # Caso 1 ou duração
                    case ("1"|"duração"|"duracao"|"duracão"|"duraçao"):
                        # Pede para digitar a duração média do procedimento
                        print("Digite a duração média do procedimento (min)")
                        # Abre um loop
                        while True:
                            # Tenta
                            try:
                                # armazena a duração média do procedimento
                                duracao_procedimento = int(input("-----------:"))
                                # chave_dados recebe a duração média do procedimento
                                chave_dados["Duração"] = ("%d min" % duracao_procedimento)
                                # Fecha o loop
                                break
                            # Caso dê ValueError
                            except ValueError:
                                # Pede para o usuário escrever um número inteiro
                                print("ERRO! Valor inválido, Digite um número inteiro")
                    
                    # Caso 2 ou valor
                    case ("2"|"valor"):
                        # Pede para digitar a duração média do procedimento
                        print("Digite o valor do procedimento (moeda: R$)")
                        # Abre um loop
                        while True:
                            # Tenta
                            try:
                                # Armazena o valor em uma variável
                                valor = float(input("-----------:"))
                                # chave_dados recebe o valor do procedimento
                                chave_dados["Valor"] = ("R$%.2f" % valor)
                                # Fecha o loop
                                break
                            # Caso dê ValueError
                            except ValueError:
                                # Pede para o usuário escrever um número real e com as separações dos decimais com pontos
                                print("ERRO! Valor inválido, Digite um número real\n(separação dos decimais deve ser realizada com '.')")

                    # Caso 3 ou materiais
                    case ("3"|"materiais"):
                        # Imprime as opções
                        print('''
1 - Adicionar
2 - Alterar
3 - Remover
                        ''')
                        # Armazena a escolha numa variável
                        escolha = input("-----------:")

                        # Caso for Adicionar
                        if escolha.lower() == "1" or escolha.lower() == "adicionar":
                            # materiais recebe o valor dos materiais de chave_dados
                            materiais = chave_dados["Materiais"]
                            # Pergunta qual o nome dos materiais que deseja adicinar
                            print("Digite os materiais utilizados ('fim' para sair)")
                            # Abre um loop
                            while True:
                                #armazena o material em uma varíavel
                                material = input("-----------:")
                                # Se material em minúsculo for 'fim' ou 'f' ou 'enter'
                                if material.lower() == "fim" or material.lower() == "f" or material.lower() == "":
                                    # Fecha o loop
                                    break
                                # Se não
                                else:
                                    # Tenta
                                    try:
                                        # Verifica se o material já está na lista
                                        if (materiais.index(material.title())+1) == True:
                                                # Fala que o valor ja existe na lista
                                                print("Valor já existente")
                                    # Caso dê ValueError
                                    except ValueError:
                                        # Realiza o append do material na lista materiais
                                        materiais.append(material.title())
                            # Salva os novos valores de materiais em chave_dados
                            chave_dados["Materiais"] = materiais
                            
                        # Caso escolha alterar
                        elif escolha.lower() == "2" or escolha.lower() == "alterar":
                            # materiais recebe o valor de materiais em chave_dados
                            materiais = chave_dados["Materiais"]
                            # Para cada valor em materiais
                            for valor in materiais:
                                # Imprime o material
                                print(valor)
                            # Pergunta qual materiais deseja alterar
                            print("Digite os materiais deseja alterar")
                            # Armazena o valor em uma variável
                            material = input("-----------:")
                            # Tenta
                            try:
                                # Testa se o material existe
                                teste = materiais.index(material.title())
                                # Pergunta qual o novo material
                                print("Digite o novo material ('fim' para sair):")
                                # Armazena o valor em uma variável
                                novo_material = input("-----------:")
                                # Salva o novo valor no lugar do valor antigo
                                materiais[materiais.index(material.title())] = novo_material.title()
                            # Caso dê ValueError
                            except ValueError:
                                # Fala que o valor não foi encontrado
                                print("Valor não encontrado")

                        # Caso escolha remover
                        elif escolha.lower() == "3" or escolha.lower() == "remover":
                            # materiais recebe o valor dos materiais em chave_dados
                            materiais = chave_dados["Materiais"]
                            # para cada valor em materiais
                            for valor in materiais:
                                # Imprime valor
                                print(valor)
                            # Pergunta quais materiais deseja remover
                            print("Digite os materiais deseja remover ('fim' para sair)")
                            # Abre um loop
                            while True:
                                # Armazena o valor em uma variável
                                material = input("-----------:")
                                # Se material em minusculo for 'fim', 'f' ou 'enter'
                                if material.lower() == "fim" or material.lower() == "f" or material.lower() == "":
                                    # Fecha o loop
                                    break
                                # Se não
                                else:
                                    # Tenta
                                    try:
                                        # remove o material da lista materiais
                                        materiais.pop(materiais.index(material.title()))
                                    # Caso dê ValueError
                                    except ValueError:
                                        # Fala que o valor não foi encontrado
                                        print("Valor não encontrado")

                        # Qualquer valor que não seja uma opção
                        else:
                            print("Opção inválida")

                    # Caso 4 ou profissionais
                    case ("4"|"profissionais"):
                        # Imprime o menu
                        print('''
1 - Adicionar
2 - Alterar
3 - Remover
                        ''')
                        # Armazena o valor na variável
                        escolha = input("-----------:")

                        # se escolher adicionar
                        if escolha.lower() == "1" or escolha.lower() == "adicionar":
                            # profissionais recebe o valor de profissionais em chave_dados
                            profissionais = chave_dados["Profissionais"]
                            # Pergunta qual profissional deseja adicionar
                            print("Digite os profissionais autorizados ('fim' para sair)")
                            # Abre um loop
                            while True:
                                # armazena o valor em uma variável
                                profissional = input("-----------:")
                                # se o valor for 'fim' ou 'f' ou 'enter'
                                if profissional.lower() == "fim" or profissional.lower() == "f" or profissional.lower() == "":
                                    # Fecha o loop
                                    break
                                # Se não
                                else:
                                    # Tenta
                                    try:
                                        # se houver valor de profissional dentro da lista de profissionais
                                        if profissionais.index(profissional.title()):
                                            # imprime valor ja existente
                                            print("Valor ja existente")
                                    # Caso dê ValueError
                                    except ValueError:
                                        # Realiza o append do profissional na lista profissionais
                                        profissionais.append(profissional.title())
                            # chave_dados recebe o valor de profissionais
                            chave_dados["Profissionais"] = profissionais

                        # caso escolha alterar
                        elif escolha.lower() == "2" or escolha.lower() == "alterar":
                            # profissionais recebe o valor de profissionais em chave_dados
                            profissionais = chave_dados["Profissionais"]
                            # para cada valor em profissionais
                            for valor in profissionais:
                                # imprime o valor
                                print(valor)
                            # pergunta os profissionais que deseja alterar
                            print("Digite os profissionais que deseja alterar")
                            # armazena numa variavel
                            profissional = input("-----------:")
                            # Tenta
                            try:
                                #testa se ja existe o valor na lista
                                teste = profissionais.index(profissional.title())
                                # pergunta qual o novo valor de profissional
                                print("Digite o novo profissional ('fim' para sair):")
                                # armazena o valor em uma variável
                                novo_profissional = input("-----------:")
                                # armazena o novo profissional no lugar do antigo
                                profissionais[profissionais.index(profissional.title())] = novo_profissional.title()
                            # Caso dê ValueError
                            except ValueError:
                                # Fala que o valor não foi encontrado
                                print("Valor não encontrado")

                        # caso escolha remover
                        elif escolha.lower() == "3" or escolha.lower() == "remover":
                            # profissionais recebe o valor de profissionais em chave_dados
                            profissionais = chave_dados["Profissionais"]
                            # para cada valor em profissionais
                            for valor in profissionais:
                                # imprime o valor
                                print(valor)
                            # Pergunta qual profissional deseja remover
                            print("Digite os profissionais deseja remover ('fim' para sair)")
                            # Abre um loop
                            while True:
                                # Armazena em uma variável
                                profissional = input("-----------:")
                                # se o valor for 'fim' ou 'f' ou 'enter'
                                if profissional.lower() == "fim" or profissional.lower() == "f" or profissional.lower() == "":
                                    # Fecha o loop
                                    break
                                # Se não
                                else:
                                    # Tenta
                                    try:
                                        # remove o profissional da lista profissionais
                                        profissionais.pop(profissionais.index(profissional.title()))
                                    # Caso dê ValueError
                                    except ValueError:
                                        # Fala que o valor não foi encontrado
                                        print("Valor não encontrado")
                        # Qualquer valor que não seja uma opção
                        else:
                            print("Opção inválida")

                    case ("9" | "salvar" | "salvar alterações" | "salvar alteracoes" | "salvar alteracões" | "salvar alteraçoes"):
                        print("Alterações salvas com sucesso")
                        # Fecha o loop
                        break
    # Caso não encontre a chave                    
    except KeyError:
        # Fala que a chave não foi encontrada
        print("Chave não encontrada")

##############################################################################################################

def excluir_procedimento():
    # Utiliza o dicionário dados dentro da função
    global dados
    # Pergunta qual o procedimento excluir
    print("\nQual procedimento deseja excluir?")
    # Armazena o valor em uma variável
    procedimento = input("-----------:")
    # Recebe os valores da chave selecionada com as iniciais em maiusculas e armazena numa variável
    chave_dados = dados.get(procedimento.title())
    # Tenta
    try:
        # Se houver um valor da chave selecionada dentro de dados
        if chave_dados == dados[procedimento.title()]:
            # Deleta os valores da chave selecionada
            del dados[procedimento.title()]
    # Caso não encontre a chave
    except KeyError:
        # Fala que a chave não foi encontrada
        print("Chave não encontrada")

##############################################################################################################

# Cria um novo documento de backup do arquivo existente
def fazer_backup():
    # Abre o arquivo json com todas as acentuações e caracteres especiais do português
    arquivo_json = open("procedimentos.json", encoding="utf-8")
    # Carrega o arquivo json em uma variável python
    carregamento_json = json.load(arquivo_json)
    # Fecha o arquivo json
    arquivo_json.close()
    # Abre o arquivo de backup com todas as acentuações e caracteres especiais do português
    backup_json = open("backup_procedimentos.json", "w", encoding="utf-8")
    # Envia o valor do arquivo json para o backup sem alterar os caracteres e já com indentação
    json.dump(carregamento_json, backup_json, ensure_ascii=False, indent=4)

##############################################################################################################

#Puxa os valores do backup para o arquivo existente
def puxar_backup():
    # Utiliza o dicionário dados dentro da função
    global dados
    # Abre o arquivo de backup com todas as acentuações e caracteres especiais do português
    backup_json = open("backup_procedimentos.json", encoding="utf-8")
    # Carrega o arquivo de backup em uma variável python
    carregamento_json = json.load(backup_json)
    # Fecha o arquivo de backup
    backup_json.close()
    # Atribui o valor de objeto_json para o dicionário dados
    dados = carregamento_json
    # Retorna o dicionário dados
    return dados