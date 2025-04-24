
# Análise de Vendas por Região

Este projeto realiza uma análise de vendas por região, apresentando gráficos que mostram o **faturamento por região** e a **participação das regiões no faturamento total**.

## Arquivos

- **`vendas_regiao.csv`**: Contém os dados de vendas por região, com as colunas:
  - `regiao`: Nome da região
  - `quantidade`: Quantidade de produtos vendidos
  - `preco_unitario`: Preço unitário dos produtos
- **`analise.py`**: Script responsável pela análise e geração dos gráficos.
- **`gráficos/`**: Pasta contendo os gráficos gerados pelo script.

## Bibliotecas Utilizadas

- `pandas`: Para manipulação e análise dos dados.
- `matplotlib`: Para criação dos gráficos.
- `seaborn`: Para melhorar a visualização dos gráficos.

## Como Executar

1. Certifique-se de que você tem o **Python** instalado. Caso não tenha, baixe e instale a versão mais recente do [site oficial](https://www.python.org/downloads/).
   
2. Instale as dependências:
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. Faça o download ou clone o repositório e navegue até a pasta onde o arquivo `analise.py` está localizado.

4. Execute o script:
   ```bash
   python analise.py
   ```

   O script irá gerar:
   - Um gráfico de **barras** mostrando o faturamento por região.
   - Um gráfico de **pizza** mostrando a participação de cada região no faturamento total.

5. Os gráficos gerados serão salvos na pasta `gráficos/` e também exibidos na tela.

## Exemplo de Saída

### Gráfico de Barras: Faturamento por Região
![faturamento_regiao](https://github.com/user-attachments/assets/583b99c4-1b4c-4f4f-a942-6ac21f701954)


### Gráfico de Pizza: Participação das Regiões no Faturamento Total
![participação_regiao](https://github.com/user-attachments/assets/2cceda23-3744-468a-8716-cf454f516dd5)


## Observações

- O **faturamento** de cada região é calculado multiplicando a **quantidade** de produtos vendidos pelo **preço unitário** de cada produto.
- O gráfico de barras mostra o **total de faturamento por região**, e o gráfico de pizza exibe a **participação percentual de cada região** no faturamento total.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou sugestões! 
