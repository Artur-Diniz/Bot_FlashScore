# Documentacao do arquivo `Obter_Estatisticas.py`

## Visao geral

O arquivo `Obter_Estatisticas.py` e responsavel por abrir a pagina de uma partida no Flashscore, coletar estatisticas da partida com Selenium, montar os objetos de dominio usados pelo projeto e salvar o resultado no banco de dados.

Ele atua como uma etapa central do fluxo de raspagem de dados, porque:

- inicia o navegador com configuracoes voltadas para automacao;
- acessa a URL de uma partida;
- coleta informacoes gerais da partida;
- coleta estatisticas do time da casa e do time visitante;
- evita processamento duplicado consultando o banco antes de salvar;
- trata alguns casos especiais, como partidas decididas nos penaltis e amistosos;
- persiste os dados processados por meio da camada `DTB`.

## Dependencias principais

O arquivo depende de:

- `selenium`: navegacao, espera de elementos e interacao com a pagina;
- `psutil`: usado para registrar informacoes de memoria em mensagens de erro;
- `random` e `time.sleep`: usados para inserir espera aleatoria e reduzir comportamento muito rigido;
- `metodos.RecolherEstatisticas`: classe auxiliar que centraliza parte da coleta dos dados da interface;
- `models.Partidas`: modelo com os dados gerais da partida;
- `models.EstatisticaPartidas.Estatisticas`: modelo com as estatisticas de cada time;
- `DTB.processarJogo.ProcessarJogo`: salva os dados no banco;
- `DTB.processarJogo.GetPartidabyNamesAndDate`: consulta se a partida ja foi processada.

## Funcoes do arquivo

### `Obter_Estatisticas(url: str, tipoPartida: str)`

Funcao principal do arquivo.

#### Objetivo

Receber a URL de uma partida e o tipo da partida, acessar a pagina correspondente, extrair os dados necessarios e retornar o identificador da partida salva no banco quando a operacao for concluida.

#### Parametros

- `url`: endereco da partida no Flashscore.
- `tipoPartida`: classificacao usada no projeto para identificar o tipo do jogo.

#### Retorno esperado

O comportamento observado no codigo e:

- retorna o `id` da partida quando ela ja existe no banco;
- retorna o `id` apos salvar e reler a partida;
- retorna vazio (`None`) em amistosos interclubes;
- pode terminar sem retorno explicito em caso de falha.

#### Fluxo resumido

1. Inicializa uma tentativa de coleta com no maximo 2 execucoes.
2. Configura o Chrome com opcoes de estabilidade e automacao.
3. Abre a URL da partida.
4. Aceita o banner de cookies.
5. Fecha um possivel popup de onboarding.
6. Navega ate a area de estatisticas.
7. Instancia objetos de partida e estatisticas.
8. Preenche os dados basicos da partida e dos dois times.
9. Ajusta gols sofridos com base nos gols do adversario.
10. Consulta se a partida ja existe no banco.
11. Trata o caso de partidas decididas por penaltis.
12. Ignora amistosos interclubes.
13. Percorre as linhas de estatisticas para tempo total e primeiro tempo.
14. Valida se estatisticas essenciais foram preenchidas.
15. Salva a partida e as estatisticas no banco.
16. Busca novamente a partida salva e retorna seu identificador.
17. Em caso de erro, registra backlog apos a segunda tentativa.

#### Etapas em mais detalhes

##### 1. Configuracao do navegador

O codigo cria um objeto `Options` do Chrome e aplica argumentos como:

- `--disable-gpu`
- `--disable-software-rasterizer`
- `--disable-dev-shm-usage`
- `--no-sandbox`
- `--disable-blink-features=AutomationControlled`
- `--start-maximized`
- `--disable-infobars`
- `--disable-extensions`

Essas configuracoes buscam dar mais estabilidade ao Selenium e reduzir sinais comuns de automacao.

##### 2. Criacao do coletor auxiliar

Depois de abrir o navegador, o codigo instancia:

```python
bot = RecolherEstatisticas(driver)
```

Esse objeto concentra operacoes como clique em seletores CSS, leitura de informacoes da partida e leitura das estatisticas por linha.

##### 3. Coleta dos dados principais

A funcao usa os seguintes metodos auxiliares:

- `bot.recolher_Info_Partida(driver, tipoPartida)`
- `bot.recolher_Estatistica_Time_Base(driver, True)`
- `bot.recolher_Estatistica_Time_Base(driver, False)`

Com isso, ela popula:

- um objeto `Partidas`, com os metadados do jogo;
- um objeto `Estatisticas` para o time da casa;
- um objeto `Estatisticas` para o time visitante.

##### 4. Prevencao de duplicidade

Antes de continuar, o codigo consulta:

```python
GetPartidabyNamesAndDate(casa.Nome, fora.Nome, partida.data)
```

Se a partida ja existir, o navegador e fechado e a funcao retorna o `id` existente.

##### 5. Ajuste para decisoes por penaltis

O arquivo possui uma regra importante: quando a partida foi decidida nos penaltis, o Flashscore pode exibir um gol adicional para o classificado. O codigo tenta detectar essa situacao e subtrai 1 gol do vencedor para manter apenas o placar considerado valido para analise estatistica no tempo regulamentar.

##### 6. Ignorar amistosos

Se `partida.Campeonato == "AMISTOSO INTERCLUBES"`, a funcao encerra sem salvar. Isso indica que esse tipo de jogo foi considerado irrelevante para o objetivo analitico do projeto.

##### 7. Leitura das estatisticas detalhadas

O codigo busca as linhas de estatistica da pagina e percorre dois ciclos:

- um para estatisticas gerais;
- um para estatisticas de primeiro tempo.

Durante esse processo, chama:

```python
bot.Partida(driver, casa, True, ft, row)
bot.Partida(driver, fora, False, ft, row)
```

O parametro `ft` controla o contexto da coleta, diferenciando tempo total e primeiro tempo.

##### 8. Validacao minima

Ao final da leitura, o codigo valida se alguns campos criticos foram preenchidos:

- `Posse_de_bola`
- `Passes`

Se esses dados continuarem zerados para algum dos times, a funcao entende que a coleta falhou ou que houve uma variacao nova no layout do site.

##### 9. Persistencia

Quando a coleta termina com sucesso:

```python
ProcessarJogo(partida, casa, fora)
```

Em seguida, o codigo consulta novamente a partida no banco e retorna seu identificador.

### `InstanciarPartidaZerada(estatisticas: Estatisticas)`

Funcao auxiliar responsavel por inicializar com zero uma longa lista de atributos do objeto `Estatisticas`.

#### Objetivo

Evitar que campos numericos fiquem nulos antes da coleta. Isso protege a integracao com a API, o banco e qualquer rotina que assuma valores inteiros.

#### O que ela faz

Preenche com `0` os campos:

- estatisticas gerais;
- estatisticas de primeiro tempo, identificadas pelo sufixo `_HT`.

#### Retorno

Retorna o proprio objeto `estatisticas` apos a inicializacao.

## Estrutura dos objetos usados

### `Partidas`

Representa os dados gerais da partida, como:

- nomes dos times;
- data;
- campeonato;
- tipo da partida;
- URL da partida.

### `Estatisticas`

Representa os dados estatisticos de um time, incluindo:

- gols marcados;
- gols sofridos;
- posse de bola;
- finalizacoes;
- escanteios;
- faltas;
- cartoes;
- passes;
- cruzamentos;
- interceptacoes;
- e as respectivas versoes do primeiro tempo.

## Regras de negocio importantes

O arquivo contem algumas regras de negocio que merecem destaque:

- nao processar novamente partidas ja existentes;
- desconsiderar amistosos interclubes;
- corrigir placar em jogos resolvidos nos penaltis;
- registrar falhas em backlog apenas apos a segunda tentativa;
- considerar que estatisticas essenciais zeradas podem significar mudanca de layout ou ausencia de dados.

## Riscos e fragilidades do arquivo

Alguns pontos merecem atencao na manutencao:

- os seletores CSS estao fortemente acoplados ao HTML atual do Flashscore;
- ha varios `except:` genericos, o que dificulta diagnostico;
- a funcao mistura navegacao, regra de negocio, validacao e persistencia em um unico bloco grande;
- o retorno da funcao nao e totalmente padronizado;
- o nome das variaveis e mensagens tem pequenas inconsistencias de grafia;
- o controle de tentativa pode ficar dificil de acompanhar em futuras manutencoes.

## Sugestoes de melhoria

Se o objetivo for evoluir esse arquivo, as melhorias mais valiosas seriam:

- adicionar docstrings mais completas nas funcoes;
- trocar `except:` generico por excecoes mais especificas;
- separar o fluxo em funcoes menores, como:
  - abrir pagina;
  - coletar cabecalho da partida;
  - coletar estatisticas;
  - validar dados;
  - salvar no banco;
- padronizar os retornos da funcao principal;
- centralizar os seletores CSS em constantes;
- adicionar logs estruturados em vez de `print`;
- corrigir problemas de codificacao de caracteres no arquivo.

## Exemplo de uso

O proprio arquivo traz exemplos comentados no final:

```python
# Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/flamengo-WjxY29qB/remo-2i0B6Zul/?mid=baSfzIsI", "Teste")
# Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/Yg2idzak/#/resumo-de-jogo/resumo-de-jogo", "Teste")
```

## Resumo final

`Obter_Estatisticas.py` e um modulo de raspagem e processamento de estatisticas de futebol. Ele abre uma partida no Flashscore, coleta informacoes da interface, aplica algumas regras de negocio do projeto e grava o resultado no banco. E um arquivo importante para o funcionamento da automacao, mas tambem e um ponto sensivel do sistema por depender diretamente da estrutura da pagina e por concentrar varias responsabilidades em um unico fluxo.
