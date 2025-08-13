import os

# Lista de dicionários que armazena os restaurantes. Cada dicionário representa um restaurante
# com suas propriedades: 'nome', 'categoria' e 'ativo' (indicando se está em funcionamento).
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

# --- Funções de interface e utilitárias ---

# Exibe o nome do programa em arte ASCII.
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
""")

# Exibe as opções do menu principal para o usuário.
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

# Exibe uma mensagem de finalização e encerra o aplicativo.
def finalizar_app():
    exibir_subtitulo('Finalizar app')

# Pausa a execução e aguarda o usuário pressionar uma tecla para retornar ao menu principal.
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

# Exibe uma mensagem de opção inválida e retorna ao menu principal.
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

# Exibe um subtítulo formatado com linhas de asteriscos e limpa a tela.
def exibir_subtitulo(texto):
    # 'os.system('cls')' limpa a tela no Windows. Para outros sistemas, pode ser 'os.system('clear')'.
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# --- Funções do Menu ---

# Função para cadastrar um novo restaurante.
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    # Cria um novo dicionário com os dados do restaurante. Por padrão, 'ativo' é False.
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    
    # Adiciona o novo dicionário à lista de restaurantes.
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

# Função para listar todos os restaurantes.
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    # Exibe o cabeçalho da tabela de listagem.
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

    # Itera sobre a lista de restaurantes para exibir cada um.
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        # Condicional para exibir 'ativado' ou 'desativado' com base no valor booleano de 'ativo'.
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        
        # Formata a string de saída para criar uma tabela alinhada.
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

# Função para alternar o estado de um restaurante (ativo/inativo).
def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    # Itera sobre a lista para encontrar o restaurante pelo nome.
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # Inverte o valor booleano de 'ativo' (True se torna False e vice-versa).
            restaurante['ativo'] = not restaurante['ativo']
            # Define a mensagem de sucesso baseada no novo estado.
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    # Se o loop terminar e o restaurante não for encontrado, exibe uma mensagem de erro.
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()

# Lida com a escolha da opção do menu principal.
def escolher_opcao():
    # Bloco 'try-except' para tratar possíveis erros, como a entrada de texto em vez de um número.
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        # Estrutura condicional para chamar a função correta com base na escolha do usuário.
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            # Caso a opção seja um número válido, mas fora do intervalo 1-4.
            opcao_invalida()
    except:
        # Caso ocorra um erro na conversão para 'int', ou seja, a entrada não é um número.
        opcao_invalida()

# --- Função principal e ponto de entrada ---

# A função principal que inicia o programa.
def main():
    # Limpa a tela.
    os.system('cls')
    # Exibe o título do programa.
    exibir_nome_do_programa()
    # Exibe as opções do menu.
    exibir_opcoes()
    # Solicita a escolha do usuário e direciona para a função correta.
    escolher_opcao()

# O bloco `if __name__ == '__main__':` garante que a função `main()`
# seja chamada apenas quando o script for executado diretamente.
if __name__ == '__main__':
    main()