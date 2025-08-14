# Gerenciador de Restaurantes

Este é um aplicativo de linha de comando simples para gerenciar uma lista de restaurantes. Com ele, você pode cadastrar, listar e alterar o status (ativo/inativo) de seus restaurantes de forma interativa.

-----

### Funcionalidades

  - **Cadastrar Restaurante**: Adicione um novo restaurante à sua lista, informando o nome e a categoria.
  - **Listar Restaurantes**: Visualize todos os restaurantes cadastrados em um formato de tabela organizado, com nome, categoria e status de atividade.
  - **Alternar Estado**: Mude o status de um restaurante de "ativo" para "desativado" e vice-versa, simplesmente informando o nome dele.
  - **Menu Interativo**: Um menu simples e intuitivo que guia o usuário por todas as opções disponíveis.

-----

### Como Usar

1.  **Execute o Script**: Basta rodar o arquivo Python no seu terminal.

    ```bash
    python seu_script.py
    ```

2.  **Navegue pelo Menu**: O programa irá exibir um menu com quatro opções:

      - `1. Cadastrar restaurante`
      - `2. Listar restaurantes`
      - `3. Alternar estado do restaurante`
      - `4. Sair`

3.  **Interaja**: Digite o número da opção desejada e pressione `Enter`. O programa irá guiá-lo para realizar a ação escolhida.

-----

### Estrutura do Código

  - `restaurantes`: Uma lista de dicionários que atua como o "banco de dados" do aplicativo, armazenando as informações de cada restaurante.
  - `exibir_nome_do_programa()`: Exibe a arte ASCII com o título do programa.
  - `exibir_opcoes()`: Mostra as opções do menu principal para o usuário.
  - `exibir_subtitulo(texto)`: Uma função utilitária para limpar a tela e exibir um subtítulo formatado.
  - `cadastrar_novo_restaurante()`: Pede o nome e a categoria do novo restaurante e o adiciona à lista.
  - `listar_restaurantes()`: Itera sobre a lista de restaurantes e exibe seus dados.
  - `alternar_estado_restaurante()`: Procura um restaurante pelo nome e inverte seu status `ativo`.
  - `escolher_opcao()`: Captura a entrada do usuário e direciona para a função correspondente.
  - `main()`: A função principal que inicia o fluxo do programa, chamando o menu e as opções.
