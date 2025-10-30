________________________________________
🌡️ API de Conversão de Temperatura (FastAPI)
Esta é uma API simples e rápida, construída com FastAPI e Python, projetada para converter temperaturas entre as escalas Celsius e Fahrenheit.
O projeto utiliza Uvicorn como servidor ASGI e está configurado para Integração/Entrega Contínua (CI/CD) usando Azure DevOps.
🚀 Tecnologias
•	Linguagem: Python 3.9+
•	Framework: FastAPI
•	Servidor ASGI: Uvicorn
•	Controle de Dependências: pip e requirements.txt
•	Implantação: Azure App Service (Linux)
•	CI/CD: Azure DevOps Pipelines (azure-pipelines.yml)
🛠️ Configuração do Projeto Local
Siga estes passos para configurar e rodar a API em sua máquina local.
Pré-requisitos
•	Python 3.9+
•	pip (gerenciador de pacotes Python)
1. Clonar o Repositório
Bash
git clone https://github.com/SEU_USUARIO/conversor-temperatura-api.git
cd conversor-temperatura-api
2. Criar e Ativar o Ambiente Virtual
É uma boa prática isolar as dependências do projeto.
Bash
# Cria o ambiente virtual (venv)
python -m venv .venv

# Ativa o ambiente virtual
# No Windows:
.\.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate
3. Instalar as Dependências
Instale todas as bibliotecas listadas no requirements.txt:
Bash
pip install -r requirements.txt
4. Rodar a API
Inicie o servidor de desenvolvimento com uvicorn:
Bash
uvicorn main:app --reload
O servidor estará rodando em http://127.0.0.1:8000.
________________________________________
🧭 Documentação e Uso
O FastAPI gera automaticamente a documentação interativa (Swagger UI) para todos os endpoints.
•	Documentação Interativa (Swagger UI): http://127.0.0.1:8000/docs
•	Documentação Alternativa (ReDoc): http://127.0.0.1:8000/redoc
Endpoints Disponíveis
Método	Caminho da Rota	Descrição	Exemplo de Uso
GET	/	Retorna uma mensagem de boas-vindas.	/
GET	/convert/celsius-to-fahrenheit/{celsius}	Converte uma temperatura de Celsius para Fahrenheit.	/convert/celsius-to-fahrenheit/25
GET	/convert/fahrenheit-to-celsius/{fahrenheit}	Converte uma temperatura de Fahrenheit para Celsius.	/convert/fahrenheit-to-celsius/77
Exemplo de Resposta (C to F)
Ao acessar /convert/celsius-to-fahrenheit/25:
JSON
{
  "celsius_input": 25.0,
  "fahrenheit_result": 77.0
}
Exemplo de Resposta (F to C)
Ao acessar /convert/fahrenheit-to-celsius/77:
JSON
{
  "fahrenheit_input": 77.0,
  "celsius_result": 25.0
}
________________________________________
☁️ Implantação e CI/CD (Azure DevOps)
O projeto está configurado para implantação automatizada no Azure App Service (Linux) usando o Azure DevOps Pipelines.
Arquivo de Pipeline
O arquivo azure-pipelines.yml define o fluxo de CI/CD:
1.	Estágio Build (Integração Contínua):
o	Instala o Python e as dependências.
o	Compacta o código-fonte e o ambiente virtual (exceto o que está no .gitignore) em um arquivo .zip.
o	Publica o .zip como um artefato de build.
2.	Estágio Deploy (Entrega Contínua):
o	Baixa o artefato de build.
o	Utiliza a AzureWebApp@1 task para implantar o pacote no Azure App Service.
o	O comando de inicialização (startupCommand) configura o servidor Gunicorn com Uvicorn workers para rodar a aplicação:
Bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
Variáveis de Configuração
As seguintes variáveis devem ser definidas no Azure DevOps Pipeline:
Variável	Descrição	Exemplo
azureSubscription	Nome da Service Connection configurada no Azure DevOps.	ConexaoAzure
webAppName	Nome do Azure App Service onde a aplicação será hospedada.	api-conversor-temp-prod
URL de Produção
Após um deploy bem-sucedido, a API estará acessível em:
https://SEU_WEBAPP_NAME.azurewebsites.net/
________________________________________
🤝 Contribuições
Contribuições são bem-vindas! Se você encontrar um bug ou tiver sugestões de melhoria (como adicionar conversão Kelvin), sinta-se à vontade para abrir uma Issue ou enviar um Pull Request.
1.	Faça o fork do projeto.
2.	Crie uma branch para sua funcionalidade (git checkout -b feature/NovaConversao).
3.	Faça o commit das suas alterações (git commit -m 'feat: Adiciona conversão Kelvin').
4.	Faça o push para a branch (git push origin feature/NovaConversao).
5.	Abra um Pull Request.
________________________________________
📄 Licença
Este projeto está licenciado sob a Licença MIT.
________________________________________
Desenvolvido com ❤️ por Simone Diana
