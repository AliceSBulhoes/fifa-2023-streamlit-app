# Aplicação Streamlit FIFA 2023 ⚽

## Visão Geral 💻
Este projeto é uma aplicação web baseada em Streamlit, projetada para visualizar e analisar dados relacionados ao jogo FIFA 2023. A aplicação utiliza conjuntos de dados para fornecer insights sobre estatísticas de jogadores, desempenho de times ou outras métricas relevantes por meio de visualizações interativas e interfaces amigáveis.

## Funcionalidades 🧰
- **Painéis Interativos**: Explore os dados do FIFA 2023 com visualizações dinâmicas.
- **Análise de Dados**: Veja estatísticas de jogadores e times com opções de filtros e ordenação.
- **Framework Streamlit**: Construído com Streamlit para uma experiência de usuário fluida e responsiva.

## Instalação 📁

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git (opcional, para clonar o repositório)

### Passos
1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/AliceSBulhoes/fifa-2023-streamlit-app.git
   cd fifa-2023-streamlit-app
   ```

2. **Criar um Ambiente Virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instalar Dependências**

4. **Executar a Aplicação**:
   ```bash
   streamlit run app.py
   ```

   Isso abrirá a aplicação no seu navegador padrão em `http://localhost:8501`.

## Uso 🖨️
- Abra a aplicação no seu navegador.
- Navegue pela barra lateral para selecionar diferentes visualizações ou filtros.
- Interaja com os gráficos e tabelas para explorar os dados do FIFA 2023.
- Modifique o código em `1_home` ou adicione novos conjuntos de dados para expandir as funcionalidades.

## Estrutura do Projeto 🏗️
```
fifa-2023-streamlit-app/
│
├── 1_home.py                # Script principal da aplicação Streamlit
├── data/                    # Diretório para armazenar conjuntos de dados
├── pages/                   # Páginas do projeto
└── README.md                # Este arquivo
```
