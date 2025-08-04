Sistema de Chat TCP

Este repositório contém um exemplo de um sistema de chat baseado em sockets, onde clientes e o servidor se comunicam via TCP para enviar e receber mensagens. Cada cliente pode enviar mensagens para o servidor, que as retransmitirá para todos os outros clientes conectados. O código está dividido em duas partes principais: uma para o cliente e outra para o servidor.

🚀 Funcionalidades

Cliente

O cliente é responsável por:

•
Criar um socket para se conectar ao servidor em localhost na porta 3001.

•
Iniciar um thread (recibe_thread) para receber e imprimir mensagens do servidor de forma assíncrona.

•
Permitir que o usuário insira mensagens via terminal.

•
Codificar as mensagens em UTF-8 antes de enviá-las para o servidor.

•
Encerrar a conexão se a mensagem digitada for 'x'.

Servidor

O servidor é responsável por:

•
Criar um socket para receber conexões de clientes na porta 3001.

•
Iniciar um thread (server_thread) para tratar o envio de mensagens a partir do próprio servidor para os clientes (embora o texto fornecido não detalhe essa funcionalidade, é uma inferência comum para um server_thread).

•
Aceitar novas conexões de clientes em um loop infinito.

•
Iniciar um thread (cliente_thread) para lidar com as mensagens de cada cliente conectado.

•
Adicionar o socket de cada cliente conectado a uma lista (list_clients) para gerenciamento.

•
Dentro do cliente_thread:

•
Receber mensagens do cliente.

•
Encerrar a conexão com o cliente se a mensagem recebida for 'x'.

•
Imprimir a mensagem recebida no console do servidor.

•
Retransmitir a mensagem para todos os outros clientes conectados (exceto o remetente).



🛠️ Tecnologias

•
Python

•
Sockets (módulo socket)

•
Threads (módulo threading)

⚙️ Como Usar

Para executar este sistema de chat, você precisará ter o Python instalado em sua máquina.

1.
Clone o repositório (se aplicável):

2.
Execute o Servidor:
Abra um terminal e execute o arquivo do servidor:

3.
Execute o Cliente(s):
Abra um ou mais terminais separados e execute o arquivo do cliente em cada um:

4.
Interaja:
No terminal do cliente, digite suas mensagens e pressione Enter. As mensagens serão enviadas para o servidor e retransmitidas para os outros clientes.
Para sair, digite 'x' e pressione Enter.

