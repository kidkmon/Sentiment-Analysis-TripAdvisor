# Sentiment-Analysis-TripAdvisor ✈️📈 📊 📙 💻

<center> <img src="https://static.tacdn.com/img2/brand_refresh/application_icons/post-image-550x370.png"> </center>

### Visão Geral

<p align="justify"> Comentários de usuários são uma parte significativa da imagem organizacional, pois medeiam a experiência. Os usuários gostam de compartilhar suas experiências boas ou ruins, mas também consultam sobre outras experiências semelhantes de outros usuários. As coisas que ouvem os
afetam e refletem em seus comentários. Conforme os usuários publicam mais informações sobre um determinado tópico, eles intensificam o quadro dominante da história. Quanto mais os usuários estão envolvidos na comunicação sobre um determinado tópico, mais as suas avaliações produzirão uma avaliação mais criteriosa de um produto, serviço, organização ou pessoa. O número total de comentários de usuários representados em um determinado site captura uma imagem online momentânea. </p>

### Objetivos

<p align="justify"> O objetivo das equipes consiste em analisar os comentários
postados por usuários sobre restaurantes, com o intuito de realizar uma análise exploratória e
visualização de dados, passando também pelas etapas de limpeza e organização. Mais especificamente,
as equipes devem explorar os comentários postados pelos usuários, pois arguimos que seja um
tipo de mensagem apropriado para se compreender a maneira pela qual os clientes enxergam os
estabelecimentos comerciais. </p>

###  Metodologia Geral

1. Processamento de Dados
2. Análise de Exploratória
3. Análise de Sentimentos
4. Visualização de Dados

### Estrutura do projeto

```
|-- app
|   |-- config
|   |-- data
|   |-- utils
|   |-- geopandas_dataset.py
|   |-- georeserver.py
|-- data
|   |-- random_sentences.csv
|-- notebooks
|   |-- Analise_sentimentos_TripAdvisor.ipynb
|   
|-- requirements.txt
`-- README.md
```

### Setup
Este projeto requer **Python 3.+**. Para instalar as dependências do projeto, execute: 

```bash
pip install -r requirements.txt
```

### Para executar o script para latitude e longitude

Faça o clone deste projeto e execute:

```bash
$ git clone https://github.com/kidkmon/Sentiment-Analysis-TripAdvisor.git
$ cd Sentiment-Analysis-TripAdvisor
$ python geopandas_dataset.py
```

### Para executar o script para conseguir outros dados de endereço

Faça o clone deste projeto e execute:

```bash
$ git clone https://github.com/kidkmon/Sentiment-Analysis-TripAdvisor.git
$ cd Sentiment-Analysis-TripAdvisor
$ python georeserver.py
```

### Para executar os notebooks

Clique neste link para executar diretamente no [Google Colab](https://colab.research.google.com/github/kidkmon/Sentiment-Analysis-TripAdvisor/blob/main/Analise_sentimentos_TripAdvisor.ipynb)



Desenvolvidor por: 

- [Andrea Monicque Dos Santos Silva](https://github.com/DevNicque)
- [Juliany Rodrigues Raiol](https://github.com/julianyraiol)
- [Kid Mendes de Oliveira Neto](https://github.com/kidkmon)
