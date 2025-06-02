# Alembic-Study

Este repositório é um estudo prático sobre migrações de banco de dados utilizando [Alembic](https://alembic.sqlalchemy.org/) e [SQLAlchemy](https://www.sqlalchemy.org/).
O objetivo é demonstrar como gerenciar versões de esquemas de banco de dados de forma segura e automatizada em projetos Python.

## 📁 Estrutura do Projeto

```
Alembic-Study/
├── alembic/             # Diretório padrão do Alembic com scripts de migração
├── migrations/          # Scripts de migração gerados
├── migrations.db        # Banco de dados SQLite utilizado para testes
├── models.py            # Definição dos modelos ORM com SQLAlchemy
├── alembic.ini          # Arquivo de configuração do Alembic
├── venv/                # Ambiente virtual Python (não incluído no controle de versão)
└── __pycache__/         # Arquivos compilados automaticamente (ignorados no controle de versão)
```

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- SQLAlchemy
- Alembic
- SQLite (para testes locais)

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/ricardofsilva7/Alembic-Study.git
   cd Alembic-Study
   ```

2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install sqlalchemy alembic
   ```

4. **Configure o Alembic:**

   Edite o arquivo `alembic.ini` para apontar para o banco de dados desejado. Por exemplo:

   ```ini
   sqlalchemy.url = sqlite:///migrations.db
   ```

5. **Crie uma nova migração:**

   ```bash
   alembic revision --autogenerate -m "Descrição da migração"
   ```

6. **Aplique a migração ao banco de dados:**

   ```bash
   alembic upgrade head
   ```

## 📚 Referências

- [Documentação do Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Documentação do SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
