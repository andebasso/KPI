KPI Gerador

Descrição
Este projeto é um aplicativo Python para processar dados de um arquivo CSV, calcular os dias úteis entre datas de início e término associadas a cada card e gerar um relatório com a soma total e a média de dias úteis por card. O aplicativo possui uma interface gráfica para fácil interação com o usuário.

Instalação
Para executar este projeto, você precisará ter Python instalado em seu sistema. Siga estas etapas para configurar o ambiente:

1.Clone o repositório para o seu computador local ou faça o download dos arquivos fonte.
2.Navegue até o diretório do projeto.
3.Recomenda-se criar um ambiente virtual Python para instalar as dependências. Você pode fazer isso com o seguinte comando:

python -m venv venv

4.Ative o ambiente virtual. No Windows, use:

venv\Scripts\activate

No Linux ou macOS, use:

source venv/bin/activate

5.Instale as dependências necessárias (se houver):

pip install -r requirements.txt

Uso
Para usar o aplicativo, execute o arquivo ui.py com Python. Isso abrirá a interface gráfica, onde você pode:

Selecionar um arquivo CSV para processamento.
Escolher um ou mais responsáveis listados.
Clicar em "OK" para processar os dados e gerar o relatório.
O relatório será salvo no mesmo diretório do arquivo CSV com o nome do arquivo original seguido pela data e hora atuais.

Contribuições
Contribuições para este projeto são bem-vindas. Sinta-se à vontade para forkar o repositório, fazer suas alterações e enviar um pull request.
