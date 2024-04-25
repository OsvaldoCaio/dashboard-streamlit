import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import urllib.request
import requests
from PIL import Image
from io import BytesIO

#determina cor da FIAP
st.markdown(
    """
    <style>
    body {
        background-color: #FF0066;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Variação do Preço do Petróleo')
#st.write('# Dados')

opcoes_abas = ['O Desafio', 'O Negócio', 'O Projeto']
aba_selecionada = st.sidebar.selectbox('Escolha uma aba', opcoes_abas)

if aba_selecionada == 'O Desafio':
    st.write('# > O Desafio')
    paragraphs = [
        "Você foi contratado(a) para uma consultoria, e seu trabalho envolve analisar os dados de preço do petróleo Brent, que pode ser encontrado no site do Ipea.",
        "Essa base de dados histórica envolve duas colunas: data e preço (em dólares).",
        "Um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo e que gere insights relevantes para tomada de decisão.",
        "Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo.",
    ]
    
    for paragraph in paragraphs:
        st.write(paragraph)
    st.write('Clique [aqui](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) para acessar os dados do IPEA')
    st.write("Clique [aqui](https://github.com/OsvaldoCaio/dashboard-streamlit/tree/main/Dashboard_streamlit) e acesse todo o conteúdo do trabalho no GitHub")

elif aba_selecionada == 'O Negócio':
    st.write('# > O Negócio')
    paragraphs = [
        "De todos os fatores que influenciam a economia global, o preço do petróleo é, sem dúvida, um dos mais importantes.",
        "Uma das commodities mais valiosas do mundo, o petróleo é um insumo imprescindível para a economia moderna e seu valor afeta virtualmente todas as cadeias de produção mundiais.",
        "Dada a sua importância estratégica, o petróleo é alvo de interesse de todos os países do planeta e seu preço está sujeito a uma série de variáveis geopolíticas e econômicas.",
        "Quer entender por que a gasolina, por exemplo, está custando tão caro no Brasil? Quais são as causas que levam a um aumento do preço do petróleo?",
        "Neste artigo, você vai conhecer melhor o peso do petróleo na economia mundial e quais são as principais forças que movem o preço do petróleo.",
        "Boa leitura!",
        "",
        "Como é definido o preço do petróleo?",
        "A definição do preço do petróleo no mercado internacional pode ser resumida de uma forma muito objetiva: a boa e velha lei da oferta e da demanda.",
        "Como o petróleo é uma commodity — ou seja, um bem pouco industrializado com pouca variação de características —, ele é negociado a preços padronizados em todo o planeta.",
        "No entanto, não existe apenas um tipo de petróleo bruto extraído no mundo.",
        "Para fins de padronização, o mercado global adota duas referências (benchmarks):",
        "- Brent: é o tipo mais comum e serve como referência para cerca de dois terços do petróleo em circulação global.",
        "- West Texas Intermediate (WTI): extraído no Golfo do México, tem qualidade superior ao Brent e é exportado principalmente pelos EUA. O barril de petróleo padrão no mercado global corresponde a 42 galões americanos, o equivalente a aproximadamente 159 litros.",
        "Devido aos avanços na tecnologia de extração nos EUA, o barril do petróleo WTI tem menor custo de produção e costuma ser mais barato do que o Brent.",
        "O valor do Brent também sofre forte influência dos interesses da Organização dos Países Exportadores de Petróleo (Opep), que controla boa parte de sua produção.",
        "Como a commodity é precificada em dólares, a oscilação da moeda americana também afeta o preço do petróleo no mercado internacional.",
        "Agentes importantes na precificação do petróleo",
        "Como a distribuição geográfica das reservas de petróleo no planeta é desigual, alguns países tendem a concentrar muito mais bacias e jazidas do que outros.",
        "As maiores reservas de petróleo comprovadas do mundo estão concentradas na Venezuela, Arábia Saudita e Canadá, que juntos correspondem a mais de 40% das reservas globais.",
        "Vale ressaltar que as reservas comprovadas dependem da capacidade de exploração de cada país e que as estimativas variam conforme a fonte das estatísticas.",
        "Dessa maneira, alguns dos agentes com maior influência sobre o preço do petróleo são:",
        "- Organização dos Países Exportadores de Petróleo (Opep e Opep+)",
        "A Opep (ou OPEC, na sigla em inglês) é um grupo composto por 13 dos principais países exportadores de petróleo em todo o mundo.",
        "Os atuais membros da Opep são:",
        "- Arábia Saudita",
        "- Emirados Árabes Unidos",
        "- Irã",
        "- Iraque",
        "- Líbia",
        "- Argélia",
        "- Venezuela",
        "- Angola",
        "- Kuwait",
        "- Congo",
        "- Nigéria",
        "- Gabão",
        "- Guiné Equatorial",
        "Fundada em 1960, a Opep surgiu com o objetivo de coordenar a produção de petróleo entre nações para exercer maior influência sobre o preço do petróleo global.",
        "Sob a liderança efetiva da Arábia Saudita, a Opep atua orientando seus membros a cortar ou elevar a produção para controlar a oferta e manter os preços estáveis.",
        "Em 2016, um grupo formado por dez outros países relevantes no setor de petróleo colabora extraoficialmente com as estratégias da Opep, embora não sejam membros da organização.",
        "Este bloco, chamado informalmente de Opep+, é liderado pela Rússia e inclui México, Sudão, Sudão do Sul, Azerbaijão, Malásia, Omã, Brunei, Cazaquistão e Bahrein."
    ]
    
    for paragraph in paragraphs:
        st.write(paragraph)
    st.write('[Clique aqui para acessar a fonte](https://warren.com.br/magazine/preco-do-petroleo/)')
    # Adicione o conteúdo que deseja exibir na Aba 2

elif aba_selecionada == 'O Projeto':
    st.write('# > O Projeto')
    url = "https://github.com/OsvaldoCaio/dashboard-streamlit/blob/main/Dashboard_streamlit/dtat_tech_challenge_grupo(final).py"
    with urllib.request.urlopen(url) as response:
        dados = response.read().decode('utf-8')
    #with open("dtat_tech_challenge_grupo(final).py", "r") as file:
        #dados = file.read()
    #--------------------------------------------------
    #    file_path = "C:\\Users\\osval\\Downloads\\_DataVizandProductionModels_\\Preço - petróleo bruto - Brent (FOB).xlsx"
    #    df = pd.read_excel(file_path)
    # Exibe o DataFrame
    #    st.write(df)
    #-----------------------------------  
        st.write('## Preço do Petróleo')
        paragraphs = [
            "Análise da Flutuação do Preço do Petróleo ao Longo do Tempo.",
            "Este estudo examina a dinâmica do preço do petróleo em diferentes períodos. É possível ajustar as datas de referência e observar a tabela e o gráfico correspondentes à variação do preço conforme a data selecionada."
        ]
    
        for paragraph in paragraphs:
            st.write(paragraph)

        excel = "C:\\Users\\osval\\Downloads\\_DataVizandProductionModels_\\Preço - petróleo bruto - Brent (FOB).xlsx"
        df = pd.read_excel(excel)

        #file_path = "C:\\Users\\osval\\Downloads\\_DataVizandProductionModels_\\Preço - petróleo bruto - Brent (FOB).xlsx"
        #df = pd.read_excel(file_path)

        data_inicial_padrao = pd.to_datetime('1987-05-20').date() 
        data_final_padrao = pd.to_datetime('2024-03-18').date() 

        data_inicial = st.date_input("Data Inicial", value=data_inicial_padrao, min_value=data_inicial_padrao)
        data_final = st.date_input("Data Final", value=data_final_padrao, max_value=pd.to_datetime('2024-03-18').date())

        df['data'] = pd.to_datetime(df['data']).dt.date

        df_filtrado = df[(df['data'] >= data_inicial) & (df['data'] <= data_final)]

        st.write(df_filtrado)
    #------------------------------------
        #file_path = "C:\\Users\\osval\\Downloads\\_DataVizandProductionModels_\\Preço - petróleo bruto - Brent (FOB).xlsx"
        #df = pd.read_excel(file_path)

        x = df_filtrado['data']
        y = df_filtrado['preco']

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, marker='o', linestyle='-')
        plt.title('Preço do Petróleo Bruto - Brent (FOB)')
        plt.xlabel('Data')
        plt.ylabel('Preço (USD)')
        plt.xticks(rotation=45)
        plt.grid(True)

        st.pyplot(plt)

    #------------------------------------------------------------------------
    #-----------------------------------
        # Adiciona um divisor horizontal
        st.markdown("<hr>", unsafe_allow_html=True)

        st.write('## Power Bi')
        paragraphs = [
            "Painel Power Bi que apresenta a evolução do preço do petróleo e a variação da taxa de câmbio US$.",
            "Nota - Devido à limitação de recursos, a visualização está disponível apenas como imagem, pois não possuo uma conta PRO para publicar a todos os usuários"
        ]
    
        for paragraph in paragraphs:
            st.write(paragraph)

    # Carrega a foto
    img_path = "C:/Users/osval/Downloads/_DataVizandProductionModels_/powerbi_foto.png"
    st.image(img_path, caption='Power BI Foto')

    #-----------------------------------powerbi
    #    def main():
    #        st.title("Visualização do Power BI")

    #    url_powerbi = "https://app.powerbi.com/groups/me/reports/82bf3b3c-d6d2-4c15-a51e-786c0072ac31?ctid=c56c8edc-eeb7-4c14-a1c4-c7215b5b0ad6&pbi_source=linkShare"

    #st.markdown(f'<iframe width="800" height="600" src="{url_powerbi}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

    #def main():
    #    caminho_codigo = r'C:\Users\osval\Downloads\_DataVizandProductionModels_\dtat_tech_challenge_grupo(final).py'
    #    subprocess.Popen(['streamlit', 'run', caminho_codigo])

    st.write("Clique [aqui](https://github.com/OsvaldoCaio/dashboard-streamlit/blob/main/Dashboard_streamlit/Postech_tc4.pbix) para abrir o arquivo do Power Bi no GitHub e conseguir ver suas funcionalidades.")
    # Adicione o conteúdo que deseja exibir na Aba 3
#---------------------------------------------------------
    #-----------------------------------
        # Adiciona um divisor horizontal
    st.markdown("<hr>", unsafe_allow_html=True)

    st.write('## Predição')
    paragraphs = [
            "Desenvolvido um modelo de Machine Learning em Python para análise de séries temporais, utilizando a base de dados de preços do petróleo Brent - US$.",
            "Devido às flutuações durante a pandemia, foram selecionados os dados para previsão e projeção dentro do intervalo especificado abaixo:",
            "Data de Início: 01/01/2023",
            "Data de Término: 28/03/2024",
            "",
            "",
            "Gráficos da Predição e Forecast."


        ]
    
    for paragraph in paragraphs:
        st.write(paragraph, format="markdown")

    # Carrega a foto
    img_path = "C:/Users/osval/Downloads/_DataVizandProductionModels_/predicao.png"
    #url_predicao = "https://github.com/OsvaldoCaio/dashboard-streamlit/raw/main/predicao.png"
    st.image(img_path, caption='Predição Foto')

    img_path = "C:/Users/osval/Downloads/_DataVizandProductionModels_/forecast.png"
    #url_forecast = "https://github.com/OsvaldoCaio/dashboard-streamlit/raw/main/forecast.png"
    st.image(img_path, caption='Forecast Foto')

    st.write('Fonte: Código Python disponível no GitHub')

    # Adiciona um divisor horizontal
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write('### Predição - 30 dias')

    paragraphs = [

        "É importante observar que, devido à conclusão deste trabalho antes de abril de 2024, a previsão refere-se a datas posteriores a essa marca. Foi realizada uma previsão de apenas um mês adicional a partir da última data disponível na base de dados."

    ]
    
    for paragraph in paragraphs:
        st.write(paragraph, format="markdown")
#---------------------------------------------------------
    file_path = "C:/Users/osval/Downloads/_DataVizandProductionModels_/forecast_postech_tc4.xlsx"
    df = pd.read_excel(file_path)
    #urlf = "https://github.com/OsvaldoCaio/dashboard-streamlit/raw/main/forecast_postech_tc4.xlsx"
    #df = pd.read_excel(urlf)

    st.write(df.head(30))

    plt.figure(figsize=(10, 6))
    plt.plot(df['data'], df['Forecast'], marker='o', linestyle='-')
    plt.title('Forecast')
    plt.xlabel('Data')
    plt.ylabel('Forecast Value')
    plt.xticks(df['data'][::2], rotation=45)
    plt.grid(True)

    st.pyplot(plt)

    st.write("Clique [aqui](https://github.com/OsvaldoCaio/data-analytics-postech-fiap/tree/main/Fase%204%20-%20Data%20Viz%20and%20Production%20Models) e acesse todo o conteúdo do trabalho no GitHub")
#---------------------------------------------------------
# Adiciona um divisor horizontal
st.markdown("<hr>", unsafe_allow_html=True)
#---------

#img_path1 = "C:/Users/osval/Downloads/_DataVizandProductionModels_/precopetroleo.png"
#url = "https://github.com/OsvaldoCaio/dashboard-streamlit/blob/ab2065762ae7badfe2da4d9ff4de7655322d1d7e/Dashboard_streamlit/precopetroleo.png"
#image = Image.open("https://raw.githubusercontent.com/OsvaldoCaio/dashboard-streamlit/ab2065762ae7badfe2da4d9ff4de7655322d1d7e/Dashboard_streamlit/precopetroleo.png")

image_url = "https://raw.githubusercontent.com/OsvaldoCaio/dashboard-streamlit/ab2065762ae7badfe2da4d9ff4de7655322d1d7e/Dashboard_streamlit/precopetroleo.png"

# Baixar a imagem usando requests
response = requests.get(image_url)

# Abrir a imagem com o Pillow a partir dos bytes obtidos
image = Image.open(BytesIO(response.content))

st.image(image,
#st.image(img_path1,
         width=10, 
         caption="",  # Adicione uma descrição para a imagem aqui
         output_format="PNG", 
         use_column_width=True,
)


st.markdown('<p class="footer">Turma: 2TDAT - Tech Challenge - Grupo 82</p>', unsafe_allow_html=True)
