===========================================
   GESTARBEM - GUIA DE INSTALAÇÃO
===========================================

📋 PRÉ-REQUISITOS
-----------------
1. Python 3.7 ou superior instalado
2. MySQL Server instalado e rodando
3. Navegador web (Chrome, Firefox, Edge, etc)


🔧 PASSO A PASSO
-----------------

1. CONFIGURAR O BANCO DE DADOS
   - Abra o MySQL (prompt ou Workbench)
   - Execute os comandos do arquivo "gestarbem.sql":
     
     mysql -u root -p < gestarbem.sql
     
   - Ou copie e cole o conteúdo do arquivo no MySQL Workbench


2. VERIFICAR SENHA DO MYSQL
   - Abra o arquivo "database.py"
   - Verifique se a senha está correta (linha 6):
     
     password="root"
     
   - Se sua senha for diferente, altere aqui


3. INSTALAR DEPENDÊNCIAS
   - Abra o terminal/prompt na pasta do projeto
   - Execute:
     
     pip install -r requirements.txt
     
   - Aguarde a instalação de Flask, MySQL Connector e Werkzeug


4. INICIAR O SERVIDOR
   - No terminal, execute:
     
     py app.py
     
   - Ou clique duas vezes no arquivo "start_server.bat"
   - Aguarde a mensagem: "Running on http://127.0.0.1:5000"


5. ACESSAR O SITE
   - Abra seu navegador
   - Digite: http://127.0.0.1:5000
   - Pronto! O GestarBem está funcionando


⚠️ SOLUÇÃO DE PROBLEMAS
------------------------

ERRO: "Access denied for user 'root'"
→ Verifique a senha no arquivo database.py

ERRO: "No module named 'flask'"
→ Execute: pip install -r requirements.txt

ERRO: "Can't connect to MySQL server"
→ Verifique se o MySQL está rodando

ERRO: "Table 'users' doesn't exist"
→ Execute o script: py create_users_table.py


📁 ESTRUTURA DE PASTAS
----------------------
Gestarbem/
├── app.py              (servidor principal)
├── database.py         (conexão com banco)
├── gestarbem.sql       (estrutura do banco)
├── requirements.txt    (dependências)
├── templates/          (páginas HTML)
├── static/             (CSS, JS, imagens)
└── uploads/            (arquivos enviados)


🚀 FUNCIONALIDADES
------------------
✓ Cadastro e login de usuários
✓ Agenda de consultas
✓ Upload de documentos e exames
✓ Listas personalizadas
✓ Perfil editável


📞 SUPORTE
----------
Em caso de dúvidas, verifique os arquivos:
- RELATORIO_VERIFICACAO.md
- GUIA_EXECUCAO.md (se existir)


===========================================
   Desenvolvido com ❤️ para gestantes
===========================================
