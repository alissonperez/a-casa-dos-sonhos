# Spotippos dream

Resolução do teste https://github.com/VivaReal/code-challenge/blob/master/backend.md

Pacotes necessários
---------------------

Utilizando **python 3.4**.

Utilizando banco **sqlite3**.

Setup
------

Baixe o projeto e configure o virtualenv. Em seguida, rode o camando a seguir para configurar o banco (criar, aplicar migrações e preenche-lo com dados para teste):

```
$ make setup_db
```

Para subir a **api** com um servidor local, rode:

```
$ make serve
```

Acesse http://localhost:8000/ para navegar pela api (acessando via Browser é possível navegar pela API).

Testes
--------

Para rodar os testes:

```
$ make test
```

Observações
-------------

- Optei por utilizar Django, mesmo sendo uma api simples, devido à agilidade no desenvolvimento. Com Django também há uma estrutura pronta para uma evolução organizada do projeto além de já prover todas as ferramentas necessárias para desenvolvimento de uma API Rest com Django Rest Framework.
- Utilizei *keys* mais genéricas no resultado do endpoint de listagem/busca de propriedades, dessa forma poderíamos ter um padrão comum para outros endpoints de listagem com paginação da API.
- Adicionalmente, fiz um endpoint para listar as províncias.

Melhorias
----------

- Ocultar os ids dos itens do banco utilizando libs como **hashids-python**.
- Cachear de alguma forma a busca das provincias para cada item da listagem de Propriedades não busque novamente no banco.