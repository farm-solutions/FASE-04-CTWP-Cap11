
<img src="../assets/logo.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=30% height=30%>

#  Implementando algoritmos de Machine Learning com Scikit-learn

Este projeto utiliza a metodologia CRISP-DM para desenvolver um modelo de aprendizado de máquina capaz de classificar variedades de trigo (Kama, Rosa e Canadian) com base no "Seeds Dataset" do UCI. O trabalho abrange análise de dados, aplicação de algoritmos como KNN, Random Forest e SVM, otimização por Grid Search e interpretação dos resultados. Focado em eficiência e precisão, o objetivo é substituir a classificação manual, comum em cooperativas agrícolas, por uma abordagem automatizada e confiável.

## Prerequisites

- Python 3.12 or higher

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/farm-solutions/Cap3-MachineLearning-Scikit-learn

   ```

2. **Configure environment variables:**

   - Copy the `env-example` file from the `config` folder to `.env`:

     ```bash
     cp config/env-example .env
     ```

   - Edit the `.env` file to include your database credentials.
   - Export the environment variables:

     ```bash
     export $(cat .env)
     # windows users can use the the set-env.ps1 script
     \.scripts\set-env.ps1
     ```

3. **Install dependencies:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # For Windows
   source .venv/bin/activate  # For Linux/MacOS

   pip install -r config/requirements.txt
   ```

4. run jupyter notebook
To run the code [Notebook](/src/notebook.ipynb)


