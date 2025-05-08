# DjangoSIGE [![Build Status](https://travis-ci.org/thiagopena/djangoSIGE.svg?branch=master)](https://travis-ci.org/thiagopena/djangoSIGE)

Sistema Integrado de Gestão Empresarial baseado em Django

Projeto independente open-source desenvolvido em Python 3 no Windows, testado no GNU/Linux e Windows.


## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.5+
- [django](http://www.djangoproject.com) == 3.1.7
- [geraldo](https://github.com/thiagopena/geraldo) - Geração de PDF para pedidos de venda/compra
- [PySIGNFe](https://github.com/thiagopena/PySIGNFe) (Opcional) - Necessário para a geração de NF-e, NFC-e, comunicação com SEFAZ, geração do DANFE, etc.
- [apache2](https://www.apache.org/) (Opcional)
- [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/) (Opcional)

## Instalação:
1. Clone o repositorio:
   ```bash
   python.exe -m venv venv
   ```
   
    1.1 Ative o ambiente virtual:
   ```bash
   venv/scripts/activate
   ```
   
   1.2 Atualizar o pip:
   ```bash
   python.exe -m pip install --upgrade pip
   ```
   
2. Instalar dependências:

```bash
pip install -r requirements.txt --only-binary=:all:

```

3. Gere um `.env` local

```bash
python contrib/env_gen.py
```


4. Sincronize a base de dados:

```bash
python manage.py migrate
```

5. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8001 no navegador):

```bash
python manage.py runserver 8001

```

## Implementações

- Cadastro de produtos, clientes, empresas, fornecedores e transportadoras
- Login/Logout
- Criação de perfil para cada usuário.
- Definição de permissões para usuários.
- Criação e geração de PDF para orçamentos e pedidos de compra/venda
- Módulo financeiro (Plano de Contas, Fluxo de Caixa e Lançamentos)
- Módulo para controle de estoque
- Módulo fiscal:
    - Geração e armazenamento de notas fiscais
    - Validação do XML de NF-e/NFC-es
    - Emissão, download, consulta e cancelamento de NF-e/NFC-es **(Testar em ambiente de homologação)**
    - Comunicação com SEFAZ (Consulta de cadastro, inutilização de notas, manifestação do destinatário)
- Interface simples e em português

