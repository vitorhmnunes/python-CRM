
<<<<<<< HEAD
=======

>>>>>>> 80582cfc9bdd0f5cd3fab0ec963872be40d5f3fe
<h1 align="Center"> Python Rental Car CRM </h1>

![Uma descrição da imagem aqui.](https://github.com/user-attachments/assets/cb3a1ae6-aea2-4fa9-b313-4ee747d26c84)

- Aplicação CRM (Customer Relantionship Management), responsável por uma loja locadora de veículos.
- Essa aplicação é a evolução de um projeto feito na faculdade -> https://github.com/vitorhmnunes/rental-car-CRM

## Documentação

 * [Visão Geral](#Visão-Geral)
 * [Views](#Views)
 * [Constructors](#Constructors)
 * [Models](#Models)
 * [Controllers](#Controllers)

## Visão Geral

  - Feita em python, a aplicação está estruturada com a arquitetura MVC e foi totalmente orientada a objetos.
  - Possui interface para interação com o cliente, feita com a biblioteca Custom TKinter, perpetuação dos dados por meio do banco de dados MySQL e as interações por meio dessas duas 
    partes feitas na pasta controllers.
  - Nessa aplicação é possível cadastras Clientes, Veículos e Aluguéis (interação entre clientes e veículos), alterá-los e excluí-los.

## Views

  - Uso da biblioteca Custom TKinter.
  - O funcionamento das janelas consiste em um frame principal, Root, em que todas as demais janelas estarão sobrepostas.

    ### Estruturação

    * [Base Structures](#Base-Structures)
    * [Start Window](#Start-Window)
    * [Client Window](#Client-Window)
    * [Vehicle WIndow](#Vehicle-Window)
    * [Rent Window](#Rent-Window)

    ### Base Structures

     #### Base Frame

       **Base Frame**

       - Como foi dito, o funcionamento das janelas consiste em um frame principal (Root) em que todas as demais janelas estarão sobrepostas. 
       - Todavia, a sobreposição só pode acontecer de uma janela por vez. Assim, na transição entre uma janela e outra, se faz necessário que se exclua a primeira janela sobreposta, 
         para que a nova janela seja sobreposta. (OBS.: Não se exclui o Root)
       - Então, esse é o motivo da existência do frame "Base Frame", ele é o frame principal que se sobrepõe ao Root, onde todos os Widgets das demais janelas estarão inseridos. 
       - Ao trocar de uma janela para outra, o base frame com os widgets atuais é excluído e outro base frame é gerado com os widgets da nova janela.

       **Right Frame**

       - O Right Frame é o frame utilizado sobre o Base Frame, e ocupa a porção direita do Base Frame.
       - Ele serve para que o menu das janelas Client, Vehicle e Rent, que fica na posição esquerda, não precise ser excluído. Assim, ao trocar de janelas, somente a porção direita do 
         Base Frame, o Right Frame, é excluído e a porção esquerda do Base Frame (que contém o menu), se mantém.

       **Upper Frame**

       - Tem a mesma funcionalidade do Base Frame.
       - Ocupa a parte superior do Root, e tem um menu inserido nele, onde se navega entre as janelas Client, Vehicle e Rent.
       - Assim ao transicionar entre uma janela e outra, o menu do Upper Frame se mantém e somente a parte de baixo, Base Frame, é excluído e recriado.
    
      #### Upper Menu Buttons

       - São os botões presentens no Upper Frame referentes ao menu para navegação entre as janelas Client, Vehicle Rent.

      #### Left Crud Buttons

       - São os botões presentes na porção esquerda do Base Frame, serve para navegação entre as opções CRUD de cada janela (Client, Vehicle e Rent)

      #### Go Back Button
  
       - Botão que permite voltar para a janela inicial, Start Window

      #### Basic Components

       - São os widgets básicos das janelas (Read, Update e Delete), de cada objeto (Client, Vehicle e Rent).

      #### Alert Window

       - É a janela de alerta para confirmação de exclusão de qualquer objeto.
    
     ### Start Window

      - É a jenela inicial da aplicação.
      - Nela é possível pesquisar por algum cliente, ou aluguel.

     ### Client Window

      - É a pasta referente as janelas da seção Client.
      - Possui as jenelas CRUD refentes a Client.

     ### Vehicle Window

      - É a pasta referente as janelas da seção Vehicle.
      - Possui as jenelas CRUD refentes a Vehicle.

     ### Rent Window

      - É a pasta referente as janelas da seção Rent.
      - Possui as jenelas CRUD refentes a Rent.
    

## Constructors

  - São os construtores das views.
  - Eles que inicializam os views objects

## Models

  - Parte de tratamento e estruturação de dados.
  - Possui as entidades/objetos Client, Vehicle e Rent.
  - Faz a conexão com o banco de dados e realiza as operações CRUD

## Controllers

  - Conecta a interação do usuário nas Views, com o tratamento e perpetuação no banco de dados no Models.
<<<<<<< HEAD
=======

<h4 align="center"> 
	:construction:  Projeto em construção  :construction:
</h4>
>>>>>>> 80582cfc9bdd0f5cd3fab0ec963872be40d5f3fe
