Sistema Integrado de Gestão Empresarial baseado em Django


## Instalação:
1. Clone o repositorio:
   ```bash
   git clone https://github.com/Luan-c-r/ERP_DjangoSiGE.git
   ```
   
   1.1 Crie um ambiente virtual:
   ```bash
   python.exe -m venv venv
   ```
   
   1.2 Ative o ambiente virtual:
   ```bash
   venv/scripts/activate
   ```
   
   1.3 Atualizar o pip:
   ```bash
   python.exe -m pip install --upgrade pip
   ```
   
3. Instalar dependências:

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

## Creditos
thiagopena : https://github.com/thiagopena/djangoSIGE
