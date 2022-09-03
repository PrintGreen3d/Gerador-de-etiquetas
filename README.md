
# Gerador de Etiquetas

Projeto para gerar etiquetas de identificação do carreteis de filamento com o codigo de barras para controle.

### 📋 Pré-requisitos

Foi desenvolvido em um Fedora 36 com python 3.10.6

```
* dynaconf==3.1.9
* reportlab==3.6.11
* svglib==1.4.1
* Python 3
* SQlite

```

### 🔧 Instalação


```
Dar exemplos
```

## 🛠️ Construído com

Ferramentas utilizadas para desenvolvimento do projeto:

* [VSCODE](https://code.visualstudio.com/) - IDE desenvolvimento
* [Dynaconf](https://www.dynaconf.com/) - Gerente de Dependência
* [Reportlab](https://docs.reportlab.com/) - Usado para geração das etiquetas
* [SQLite](https://www.sqlite.org/index.html) - Banco usado para armazenamento


## 📌 Melhorias

Proximas melhorias a serem realizadas:

* Montagem do relatorio (etiquetas)
* Definir o gabarito da etiqueta (atualmente folha a4)
* Imprimir a quantidade de etiquetas informada pelo usuario
* Paginação de paginas de etiquetas (conforme quantidade informada) - https://www.youtube.com/watch?v=b4HJpi3DyVs
* Verificação do preechimento dos campos - ✅
* Consistencias dos dados (Ex: Temp. é compativel com material?)