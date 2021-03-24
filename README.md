Tera Beer Recommendations
Esse é um projeto desenvolvido ao longo do Bootcamp de Ciência de Dados e Machine Learning da Tera. Trata-se de um primeiro esboço utilizando Python/Streamlit 
para gerar uma listas de recomendação de cervejas artesanais brasileiras com base no paladar do usuário.
Parte de recomendações ainda nao implementada.

Ambiente de desenvolvimento
Para criar o ambiente de desenvolvimento, é recomendado utilizar o conda.

Utilize os comandos a seguir para deixar o ambiente pronto para desenvolver

conda create -n ENVIRONMENT_NAME python=3.6
conda activate ENVIRONMENT_NAME
pip install -r requirements.txt
Será necessário configurar as seguintes variáveis de ambiente:

export FROM_EMAIL=[EMAIL]
export EMAIL_PASSWORD=[PASSWORD]
Recriação do modelo
Para adicionar contemplar mais respostas no sistema de recomendação, substitua o arquivo raw_dataset.xlsx na pasta data e execute os scripts

python data/build_dataset.py
python model/create_recommender.py
O sistema de recomendação será salvo em 4 arquivos na pasta model/recommending_system.

Execução local
Para executar a aplicação streamlit em servidor local, utilize o comando

streamlit run app.py
URL da Aplicação
