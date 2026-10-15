# FishinGO — Do zero ao MVP em Python

**Apostila prática em 8 volumes | 1º período de Análise e Desenvolvimento de Sistemas**

> Objetivo: construir, compreender e conseguir explicar um MVP **somente no terminal**, com Python, demonstrando CRUD, lista, tupla, dicionário, funções, arquivos e tratamento de erros. Não existe banco de dados, interface gráfica, API, integração com IA ou assistente Mara. Não é um marketplace completo.

## Como estudar este material

1. Leia os volumes na ordem. **Digite os trechos de exemplo** para compreender o funcionamento.
2. No Volume 7, abra o arquivo completo `fishingo.py` enviado junto com esta apostila. Ele reúne os conceitos estudados e pode ser executado diretamente.
3. Execute os testes manuais do Volume 8 e **entenda cada função antes de apresentar**. Você deve adaptar nomes e mensagens junto ao seu grupo, se desejar.
4. Nenhuma biblioteca externa é exigida. O projeto usa apenas `json` e `pathlib`, incluídas no Python.

---

# Volume 1 — Interpretar o FishinGO

**Neste trabalho de Fundamentos de Programação, vamos implementar apenas os cadastros, sem simular funcionalidades complexas que não são necessárias para demonstrar a matéria.**

## 1.2. Recorte do MVP acadêmico

Três cadastros, cada um com CRUD completo:

| Entidade | Campos | Por que existe? |

| Pescador | ID, nome, contato | Representar quem oferta pescado |
| Peixaria | ID, nome, contato | Representar quem pode comprar |
| Lote de pescado | ID, ID do pescador, espécie, quantidade em kg, preço por kg, local de captura | Representar a produção ofertada |

O sistema permite cadastrar, listar, editar e excluir. Para cadastrar um lote, deve existir um pescador. Ao excluir um pescador que possui lotes, a operação é bloqueada para evitar lotes sem responsável.

**Não implementar:** pedidos, mapas, localização em tempo real, autenticação, login com Face ID, pagamentos, comparação de preços, selo de qualidade automatizado, IA Mara, áudio, aplicativo mobile, interface gráfica, banco SQL, cadastro de entregadores, serviço de entrega. Tudo isso aumentaria o escopo e não é necessário para os requisitos do slide.

## 1.3. Fluxo adaptado ao terminal

```text
INICIAR PROGRAMA
  |
  v
MENU PRINCIPAL
  |-- PESCADORES -> Criar / Listar / Editar / Excluir
  |-- PEIXARIAS  -> Criar / Listar / Editar / Excluir
  |-- LOTES      -> Criar / Listar / Editar / Excluir
  |                    |
  |                    +-> verificar pescador
  |                    +-> espécie
  |                    +-> quantidade e preço
  |                    +-> origem
  |                    +-> revisar e confirmar
  |
  +-- SAIR
```

### Correspondência com o Figma

- `Cadastro PESCADOR 1, 2, 3` → um cadastro de pescador simplificado no terminal.
- `Cadastro PEIXARIA 1, 2, 3` → um cadastro de peixaria simplificado.
- `Cadastrar Pescado`, `Espécie`, `Quantidade & Preço`, `Origem & Captura`, `Revisão & Publicação` → perguntas em sequência no terminal.
- `HOME PESCADOR`, `HOME PEIXARIA` → opções do menu, sem layout visual.
- `Pedidos` e `Mapas` → fora deste MVP.

---

# Volume 2 — Fundamentos: variáveis, entrada e saída

## 2.1. O que é uma variável?

É um nome associado a um valor. Use variáveis para guardar respostas do usuário.

```python
nome = "José"
contato = "81999999999"
quantidade = 20.0
preco = 15.50
print(nome, contato, quantidade, preco)
```

Aspas representam texto (tipo `str`). `20.0` e `15.50` são números decimais (`float`). O telefone é texto: não precisamos somar números de telefone, e ele pode conter zero no início.

## 2.2. Receber dados do terminal

```python
nome = input("Nome do pescador: ")
print("Pescador cadastrado:", nome)
```

`input()` devolve texto. Para obter números:

```python
quantidade = float(input("Quantidade em kg: "))
```

**Cuidado:** digitar `abc` gera `ValueError`. Corrigiremos isso no Volume 6. Não use `eval(input())`.

## 2.3. Decidir com `if`

```python
quantidade = 12.0
if quantidade > 0:
    print("Quantidade válida")
else:
    print("A quantidade deve ser positiva")
```

**Onde entra no FishinGO?** Para rejeitar quantidade igual a zero, preço negativo, nome vazio e ID inexistente.

## 2.4. Repetir com `while`

```python
while True:
    opcao = input("Digite 0 para sair: ")
    if opcao == "0":
        break
    print("Ainda no menu")
```

`while True` mantém o programa aberto; `break` encerra a repetição.

### Exercício do volume

Escreva um script que peça nome do pescador, espécie e quantidade, e imprima um resumo. Ainda não precisa guardar os dados.

---

# Volume 3 — Estruturas de dados: lista, tupla e dicionário

Essas **três estruturas aparecem de verdade** no MVP. Não basta importá-las ou citá-las: é necessário saber por que foram escolhidas.

## 3.1. Lista `[]`: coleção que pode crescer

```python
pescadores = []
pescadores.append({"id": 1, "nome": "José", "contato": "81999999999"})
pescadores.append({"id": 2, "nome": "Maria", "contato": "81888888888"})

for pescador in pescadores:
    print(pescador["nome"])
```

**Por quê?** Precisamos cadastrar vários pescadores, peixarias e lotes. Com `.append()` incluímos um cadastro; com `.remove()` excluímos.

## 3.2. Dicionário `{}`: um cadastro com campos nomeados

```python
pescador = {
    "id": 1,
    "nome": "José",
    "contato": "81999999999"
}
print(pescador["nome"])
pescador["contato"] = "81777777777"  # UPDATE
```

**Por quê?** `pescador["nome"]` é mais claro do que `pescador[1]`. Um dicionário representa um registro completo e permite alterar campos por chave.

## 3.3. Tupla `()`: conjunto fixo de opções

```python
ESPECIES = ("Tilápia", "Sardinha", "Atum", "Pescada", "Outros")
print(ESPECIES[0])
```

**Por quê?** A lista de espécies de exemplo é fixa durante a execução; não precisamos acrescentar ou remover espécies. Tuplas não permitem alterar elementos em suas posições.

## 3.4. Juntar as estruturas

```python
dados = {
    "pescadores": [],
    "peixarias": [],
    "lotes": []
}

novo = {"id": 1, "nome": "José", "contato": "81999999999"}
dados["pescadores"].append(novo)
```

Aqui, `dados` é um **dicionário** que contém **listas**; cada lista contém **dicionários de cadastros**. Essa é a estrutura central de armazenamento durante a execução.

### Exercício do volume

Adicione duas peixarias à lista `dados["peixarias"]` e percorra a lista para exibir seus nomes.

---

# Volume 4 — Funções: organizar sem repetir código

## 4.1. O que é uma função?

Uma função agrupa instruções, recebe valores (parâmetros) e opcionalmente devolve um resultado (`return`).

```python
def mostrar_saudacao(nome):
    return "Olá, " + nome

print(mostrar_saudacao("José"))
```

**Por quê?** No MVP, pescador e peixaria compartilham as mesmas operações. Podemos reutilizar funções em vez de copiar blocos inteiros.

## 4.2. Encontrar um cadastro pelo ID

```python
def procurar(registros, identificador):
    for registro in registros:
        if registro["id"] == identificador:
            return registro
    return None
```

- `registros`: lista que será percorrida.
- `identificador`: número do cadastro procurado.
- `for`: examina cada registro.
- `return registro`: devolve o cadastro encontrado.
- `return None`: indica que ele não existe.

Exemplo:

```python
pescadores = [{"id": 1, "nome": "José"}]
print(procurar(pescadores, 1))     # encontra
print(procurar(pescadores, 99))    # None
```

## 4.3. Gerar ID simples

```python
def proximo_id(registros):
    return max((registro["id"] for registro in registros), default=0) + 1
```

Quando a lista está vazia, `max(..., default=0)` resulta em 0 e o primeiro ID será 1. Quando existem IDs, devolve um valor acima do maior.

> Simplificação acadêmica: não serve como sistema de identificação multiusuário ou concorrente. Aqui só existe um programa local acessando o arquivo.

## 4.4. Entendendo as funções do projeto

| Função de `fishingo.py`         | Responsabilidade                          |
| ------------------------------- | ----------------------------------------- |
| `dados_iniciais()`              | Criar a estrutura vazia                   |
| `carregar()`                    | Ler dados salvos do JSON                  |
| `salvar(dados)`                 | Gravar alterações no JSON                 |
| `proximo_id(registros)`         | Gerar identificador                       |
| `texto_obrigatorio(mensagem)`   | Validar campos de texto                   |
| `numero_positivo(mensagem)`     | Validar quantidade e preço                |
| `procurar(registros, id)`       | Buscar registro                           |
| `escolher_id(registros, nome)`  | Ler ID digitado                           |
| `cadastrar_pessoa(dados, tipo)` | Criar pescador ou peixaria                |
| `listar(dados, tipo)`           | Ler todos os registros                    |
| `editar_pessoa(dados, tipo)`    | Atualizar dados da pessoa/estabelecimento |
| `excluir_pessoa(dados, tipo)`   | Remover cadastro com proteção de vínculo  |
| `escolher_especie()`            | Escolher item da tupla                    |
| `cadastrar_lote(dados)`         | Criar lote e revisar publicação           |
| `editar_lote(dados)`            | Atualizar lote                            |
| `excluir_lote(dados)`           | Excluir lote                              |
| `menu()`                        | Apresentar ações e chamar funções         |

### Observação para a apresentação

Duas funções bastam para satisfazer literalmente “uso de funções”, mas o código usa várias porque **cada uma tem uma responsabilidade**. Isso facilita testes, leitura e manutenção.

---

# Volume 5 — CRUD: criar, consultar, atualizar e excluir

CRUD significa **Create, Read, Update, Delete**. O enunciado da avaliação escreve “Create, Read, Update, Delete”, equivalentes a criar, ler, atualizar e excluir.

## 5.1. CREATE — novo pescador

Código ilustrativo, sem arquivo por enquanto:

```python
def criar_pescador(dados, nome, contato):
    registro = {
        "id": proximo_id(dados["pescadores"]),
        "nome": nome,
        "contato": contato
    }
    dados["pescadores"].append(registro)
```

No programa final, `cadastrar_pessoa()` faz isso tanto para pescador quanto para peixaria e chama `salvar()`.

## 5.2. READ — listar

```python
def listar_pescadores(dados):
    for pescador in dados["pescadores"]:
        print(pescador)
```

No programa final, `listar(dados, tipo)` atende às três entidades.

## 5.3. UPDATE — alterar um registro

```python
def alterar_contato(dados, identificador, novo_contato):
    pescador = procurar(dados["pescadores"], identificador)
    if pescador is not None:
        pescador["contato"] = novo_contato
```

No programa final, `editar_pessoa()` e `editar_lote()` chamam `salvar()` após alterações.

## 5.4. DELETE — remover

```python
def remover_pescador(dados, identificador):
    pescador = procurar(dados["pescadores"], identificador)
    if pescador is not None:
        dados["pescadores"].remove(pescador)
```

No programa final, `excluir_pessoa()` **não permite excluir pescador que ainda tenha lotes**, para manter os cadastros coerentes. Também pede confirmação para evitar exclusão acidental.

## 5.5. Como os cadastros se relacionam

```text
PESCADOR
  id=1, nome="José"
     |
     +---- LOTE id=1, pescador_id=1, espécie="Tilápia"
     +---- LOTE id=2, pescador_id=1, espécie="Sardinha"

PEIXARIA
  id=1, nome="Peixaria Azul"
```

`pescador_id` conecta o lote ao seu responsável. Não é uma chave estrangeira de banco de dados: é apenas um número que o código verifica antes de salvar. A peixaria fica cadastrada, mas **não precisa estar associada a pedidos**, porque pedidos estão fora do escopo.

## 5.6. Por que cadastrar lote?

Não é expansão arbitrária: é o fluxo central do Figma (`Espécie` → `Quantidade & Preço` → `Origem & Captura` → `Revisão & Publicação`). Também serve para aplicar os conteúdos de programação ensinados.

---

# Volume 6 — Arquivos e tratamento de erros

## 6.1. Por que usar arquivo?

Sem arquivo, o conteúdo da lista seria perdido ao fechar o programa. A disciplina exige manipulação de arquivos; portanto, salvamos em **`dados.json`**, um arquivo de texto local. Isso **não é um banco de dados**.

## 6.2. Como fica o arquivo?

Este é um **exemplo ilustrativo**, não um arquivo que você precisa digitar manualmente:

```json
{
  "pescadores": [{ "id": 1, "nome": "José", "contato": "81999999999" }],
  "peixarias": [{ "id": 1, "nome": "Peixaria Azul", "contato": "8133333333" }],
  "lotes": [
    {
      "id": 1,
      "pescador_id": 1,
      "especie": "Tilápia",
      "quantidade_kg": 20.0,
      "preco_kg": 15.5,
      "origem": "Recife"
    }
  ]
}
```

## 6.3. Como gravar dados

```python
import json

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)
```

- `"w"`: modo de escrita (substitui o conteúdo anterior).
- `encoding="utf-8"`: trata caracteres acentuados.
- `json.dump`: transforma dicionários e listas em texto JSON.
- `ensure_ascii=False`: preserva os caracteres legíveis.
- `indent=2`: organiza a formatação.

O código final usa `Path(__file__).with_name('dados.json')` para manter os dados na mesma pasta do programa, independentemente de onde o terminal foi aberto.

## 6.4. Como ler dados

```python
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
```

`json.load()` transforma o texto JSON de volta em listas e dicionários.

## 6.5. Tratamento de exceções com `try` / `except`

```python
try:
    preco = float(input("Preço: ").replace(",", "."))
except ValueError:
    print("Digite um número válido.")
```

O `try` tenta executar. O `except ValueError` trata o caso em que o texto não pode ser convertido em número. Evita que o programa encerre abruptamente por entrada incorreta.

No programa final:

- `texto_obrigatorio()`: impede nome ou local vazio.
- `numero_positivo()`: rejeita valor não numérico, zero, negativo e infinito.
- `escolher_especie()`: rejeita número fora da lista.
- `escolher_id()`: trata ID não inteiro.
- `carregar()`: trata arquivo ausente, JSON inválido e problemas de acesso.
- `salvar()`: trata falha de escrita.
- `menu()`: encerra de forma amigável ao receber Ctrl+C ou fim de entrada.

**Limite didático importante:** `salvar()` retorna se a gravação funcionou, mas o MVP não implementa transação nem recuperação de alterações em memória caso a escrita falhe. Isso é aceitável para um aplicativo local inicial e deve ser explicado sem prometer tolerância completa a falhas.

---

# Volume 7 — Montar e executar o programa final

## 7.1. Estrutura mínima

```text
fishingo_mvp/
├── fishingo.py       # programa que você executa
├── TUTORIAL_FISHINGO.md  # esta apostila
└── dados.json        # criado automaticamente ao salvar o primeiro cadastro
```

O arquivo `dados.json` do seu uso será criado automaticamente. **Não é necessário instalar pacotes** como `pip install ...`.

## 7.2. Preparar o ambiente

1. Instale uma versão atual do Python 3 (ex.: Python 3.10 ou superior).
2. Abra a pasta `fishingo_mvp` no VS Code ou em um terminal.
3. Confira a instalação:

```bash
python --version
```

No macOS ou Linux, o comando pode ser `python3 --version`.

## 7.3. Executar

```bash
python fishingo.py
```

Ou:

```bash
python3 fishingo.py
```

Aparecerá o menu:

```text
=== FishinGO — MVP Acadêmico ===
PESCADORES: 1 Criar | 2 Listar | 3 Editar | 4 Excluir
PEIXARIAS:  5 Criar | 6 Listar | 7 Editar | 8 Excluir
LOTES:      9 Criar | 10 Listar | 11 Editar | 12 Excluir
0 Sair
```

## 7.4. Como acompanhar o código sem se perder

Abra `fishingo.py` e leia de cima para baixo em blocos:

**Bloco A — Configuração e dados:** importações, `ARQUIVO`, `ESPECIES`, `dados_iniciais()`.

**Bloco B — Persistência:** `carregar()` e `salvar()`. Procure por `json.load` (leitura) e `json.dump` (escrita).

**Bloco C — Auxiliares:** `proximo_id()`, `texto_obrigatorio()`, `numero_positivo()`, `procurar()`, `escolher_id()`. São peças reutilizadas pelas funcionalidades.

**Bloco D — CRUD de pessoas:** `cadastrar_pessoa()`, `listar()`, `editar_pessoa()`, `excluir_pessoa()`. O parâmetro `tipo` seleciona a lista `pescadores` ou `peixarias`.

**Bloco E — CRUD de lotes:** `escolher_especie()`, `cadastrar_lote()`, `editar_lote()`, `excluir_lote()`. Esta parte adapta o fluxo sequencial do Figma.

**Bloco F — Navegação:** `menu()`, um `while` que recebe a opção e executa a função correspondente.

**Importante:** no programa final, a variável `acoes` é um dicionário de opções do menu para funções. A expressão `lambda` cria uma função pequena que adia a chamada até a escolha da opção. É apenas uma forma compacta de escrever o menu, não um recurso obrigatório da disciplina. Se o professor preferir um `if/elif`, você pode substituí-la:

```python
if opcao == "1":
    cadastrar_pessoa(dados, "pescadores")
elif opcao == "2":
    listar(dados, "pescadores")
# ... seguir para as demais opções
```

## 7.5. Guia de uso: simulação completa

1. Digite `1` e cadastre o pescador José, telefone `81999999999`.
2. Digite `5` e cadastre a Peixaria Azul, contato `8133333333`.
3. Digite `9` para cadastrar um lote. Informe ID do pescador `1`, espécie `1` (Tilápia), `20` kg, preço `15,50`, origem `Recife` e confirme com `s`.
4. Digite `10` e confira se o lote aparece.
5. Digite `11`, selecione o lote e altere seus dados.
6. Digite `12`, selecione o lote e confirme a exclusão.
7. Digite `4` para excluir o pescador, agora que ele não possui lotes.
8. Digite `0` para encerrar.
9. Abra novamente o programa e confirme que os registros restantes foram carregados do arquivo.

---

# Volume 8 — Testes, apresentação e critérios do professor

## 8.1. Checklist de testes manuais

- [ ] Cadastrar pescador e listar o cadastro.
- [ ] Alterar nome e contato de um pescador.
- [ ] Excluir um pescador sem lote.
- [ ] Cadastrar peixaria e listar o cadastro.
- [ ] Editar e excluir uma peixaria.
- [ ] Cadastrar lote associado a pescador existente.
- [ ] Conferir a escolha de espécie na tupla.
- [ ] Editar espécie, quantidade, preço e origem de um lote.
- [ ] Excluir lote.
- [ ] Tentar criar lote sem pescadores cadastrados.
- [ ] Tentar excluir pescador com lote e verificar o bloqueio.
- [ ] Digitar `abc` onde se espera número e verificar mensagem de erro.
- [ ] Digitar zero e valor negativo para quantidade/preço.
- [ ] Informar ID inexistente.
- [ ] Fechar e reabrir o programa, verificando persistência.
- [ ] Verificar que o JSON é legível e possui as três listas.

## 8.2. Relação direta com os critérios mostrados na avaliação

| Critério do slide | Onde foi aplicado                                                    | Como demonstrar                                              |
| ----------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ |
| **CRUD**          | Pescadores, peixarias, lotes                                         | Criar, listar, editar e excluir cada entidade                |
| **Lista**         | `dados["pescadores"]`, `dados["peixarias"]`, `dados["lotes"]`        | Mostrar `.append()`, percurso com `for` e `.remove()`        |
| **Tupla**         | `ESPECIES`                                                           | Mostrar que o cardápio de espécies é fixo                    |
| **Dicionário**    | `dados` e cada registro                                              | Explicar chaves como `"nome"`, `"quantidade_kg"`             |
| **Função**        | Funções com `def`                                                    | Demonstrar `procurar()` e `cadastrar_lote()`                 |
| **Arquivo**       | `dados.json`                                                         | Fechar e abrir o programa sem perder os dados                |
| **Exceção**       | `try/except` de conversão e arquivos                                 | Digitar `abc` no preço e mostrar a recuperação               |
| **Complexidade**  | Dois tipos de usuário + lotes vinculados + validações + persistência | Explicar relações e regras sem alegar que é sistema completo |

O slide mostra pontuações por critério (função 2, estruturas 2, CRUD 2, arquivo 2, exceção 1, complexidade 1). **A pontuação depende da avaliação do professor; a presença dos recursos não garante nota automática.**

## 8.3. Miniroteiro para apresentação individual

**1. Contextualização (30 segundos):** “FishinGO é um marketplace que pretende aproximar pescadores artesanais de peixarias. Nosso MVP acadêmico representa os cadastros necessários para essa proposta.”

**2. Escopo (20 segundos):** “Optamos por não implementar mapa, pedidos, interface visual, IA ou banco de dados, porque a disciplina solicita fundamentos de programação e persistência em arquivos.”

**3. Mostrar o código (1 minuto):** apresentar dicionário `dados`, listas de registros, tupla `ESPECIES`, função `procurar()` e `salvar()`.

**4. Demonstrar CRUD (1 a 2 minutos):** cadastrar pescador, peixaria e lote; listar, editar e excluir pelo menu.

**5. Mostrar tratamento de erros (30 segundos):** tentar preço negativo e uma entrada textual inválida.

**6. Persistência (30 segundos):** encerrar, abrir `dados.json`, executar novamente e listar cadastros.

## 8.4. Perguntas que o professor pode fazer

**Por que lista?** Para guardar uma quantidade variável de cadastros e percorrê-los.

**Por que dicionário?** Para representar registros com campos nomeados.

**Por que tupla?** Para um conjunto simples de espécies que não muda durante a execução.

**Por que funções?** Para modularizar, reutilizar e evitar duplicação de lógica.

**O que é CRUD?** Create, Read, Update, Delete: cadastro, consulta, edição e exclusão.

**Onde ocorre leitura e escrita de arquivo?** `json.load()` recupera os dados; `json.dump()` grava.

**Como trata um preço inválido?** `float()` dentro de `try/except ValueError`; o programa avisa e pede outro valor.

**O que impede cadastrar lote sem pescador?** `cadastrar_lote()` exige que a lista de pescadores não esteja vazia e verifica o ID com `procurar()`.

**É um sistema com banco de dados?** Não. É persistência em arquivo JSON local.

**Por que não implementaram pedidos?** O requisito da disciplina pode ser plenamente demonstrado com os cadastros básicos; pedidos introduziriam estados e regras comerciais que não são necessários ao MVP acadêmico.

**Como justificam a complexidade?** Existem três tipos de cadastro com CRUD, validação de entradas, relações entre dados e persistência, sem criar recursos extras.

## 8.5. Melhorias que NÃO precisam ser feitas neste trabalho

Não acrescente autenticação, login, senha, integração de áudio, API, mapa, sistema de compras, logística, interface gráfica ou banco de dados apenas para “deixar bonito”. Quanto mais simples, mais fácil demonstrar **domínio do código, clareza e participação individual**, que também são critérios explícitos no slide.

---

# Conclusão

A versão acadêmica do FishinGO não precisa copiar todas as telas do Figma. Ela traduz o **núcleo de cadastros e publicação de pescado** para comandos no terminal. O projeto atende aos conteúdos solicitados e mantém escopo compreensível para o primeiro período. Para dominar o sistema, pratique cada CRUD e tente explicar, sem consultar o texto, de onde o dado vem, como é validado, onde fica em memória e como é salvo no arquivo.
