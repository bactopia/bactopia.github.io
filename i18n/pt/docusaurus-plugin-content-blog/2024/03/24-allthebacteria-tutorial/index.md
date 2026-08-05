---
title: Usando Bactopia com Montagens do AllTheBacteria
authors: [rpetit3]
tags: [community, tutorial]
date: 2024-03-24
slug: allthebacteria-tutorial
description: Aprenda como usar Bactopia para analisar quase 2.000.000 de montagens bacterianas do projeto AllTheBacteria.
---

[AllTheBacteria](https://github.com/iqbal-lab-org/AllTheBacteria) (ATB) é uma coleção
de quase 2.000.000 de montagens bacterianas. Neste post você aprenderá como usar Bactopia para
analisar essas montagens de forma integrada com as [Bactopia Tools](/bactopia-tools) disponíveis.

<!-- truncate -->

## AllTheBacteria

O [Grupo de Zamin Iqbal](https://www.ebi.ac.uk/research/iqbal/), que nos trouxe as [661 mil montagens bacterianas](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001421),
foi ainda mais longe com o [AllTheBacteria](https://www.biorxiv.org/content/10.1101/2024.03.08.584059v1).
Como alguém que já foi encarregado de montar "todos os genomas de _Staphylococcus aureus_" (_embora fossem apenas
cerca de 700 amostras em 2010!_), isso é realmente um feito impressionante e um recurso valioso para a comunidade!
Com as montagens mais recentes, a coleção agora conta com quase 2.000.000 de montagens bacterianas!

Semelhante aos métodos anteriores, a versão mais recente do AllTheBacteria usa [Shovill](https://github.com/tseemann/shovill)
para montagem. Além disso, cada montagem tem métricas básicas calculadas, passa por estimativa de abundância taxonômica
e tem sketches disponibilizados. Para mais detalhes sobre este projeto,
consulte:

- Preprint: _[AllTheBacteria - all bacterial genomes assembled, available and searchable](https://www.biorxiv.org/content/10.1101/2024.03.08.584059v1)_
- GitHub: [AllTheBacteria](https://github.com/iqbal-lab-org/AllTheBacteria)

Desde que Zamin revelou as atualizações mais recentes do AllTheBacteria, fiquei me perguntando: _Como os usuários do Bactopia
poderiam aproveitar essas montagens? Especialmente, por meio das [Bactopia Tools](/bactopia-tools) disponíveis?_

## Por que Bactopia Tools?

O que há de realmente interessante nas Bactopia Tools é que elas tornam muito fácil executar [60 análises adicionais](/bactopia-tools)
nos seus genomas. É tão simples quanto adicionar `--wf <tool>` ao seu comando Bactopia, e então o Bactopia
cuidará do resto por você, incluindo a seleção de containers e trilhas de auditoria.

Obviamente, sou um pouco tendencioso aqui, mas utilizar as Bactopia Tools nessa situação
agilizaria bastante uma série de análises downstream das montagens do AllTheBacteria. Acredito que isso
permitiria que pesquisadores chegassem rapidamente à ciência por trás dessas montagens.

Para ter uma ideia, atualmente existem 38 Bactopia Tools que utilizam montagens como entradas.
Em outras palavras, cada uma dessas ferramentas seria fácil de executar nas 2.000.000 montagens do AllTheBacteria.

<details>
<summary>Expanda para ver a lista de Bactopia Tools</summary>

:::tip[Dica]

Cada uma das ferramentas listadas abaixo aceita uma única montagem como entrada.

| Ferramenta | Descrição |
|------------|-----------|
| [bakta](/bactopia-tools/bakta) | Anotação rápida de genomas bacterianos e plasmídeos |
| [fastani](/bactopia-tools/fastani) | Cálculo rápido sem alinhamento da Identidade Nucleotídica Média (ANI) de genomas completos |
| [gtdb](/bactopia-tools/gtdb) | Identificação de genes marcadores e atribuição de classificações taxonômicas |
| [mashtree](/bactopia-tools/mashtree) | Criação de árvores usando distâncias Mash |
| [abricate](/bactopia-tools/abricate) | Triagem em massa de contigs para genes de resistência antimicrobiana e virulência |
| [abritamr](/bactopia-tools/abritamr) | Ferramenta acreditada pela NATA para identificação de genes de resistência antimicrobiana |
| [agrvate](/bactopia-tools/agrvate) | Identificação rápida do tipo do locus agr e variantes do operon agr de Staphylococcus aureus |
| [amrfinderplus](/bactopia-tools/amrfinderplus) | Identificação de resistência antimicrobiana em genes ou proteínas |
| [btyper3](/bactopia-tools/btyper3) | Classificação taxonômica de isolados do grupo Bacillus cereus |
| [busco](/bactopia-tools/busco) | Completude da montagem baseada em expectativas evolutivas |
| [checkm](/bactopia-tools/checkm) | Avaliação da qualidade da montagem de amostras microbianas |
| [ectyper](/bactopia-tools/ectyper) | Predição in silico do sorotipo de Escherichia coli |
| [emmtyper](/bactopia-tools/emmtyper) | Tipagem emm de montagens de Streptococcus pyogenes |
| [gamma](/bactopia-tools/gamma) | Identificação, classificação e anotação de correspondências de genes traduzidos |
| [hicap](/bactopia-tools/hicap) | Identificação do sorotipo e estrutura do locus cap em montagens de Haemophilus influenzae |
| [hpsuissero](/bactopia-tools/hpsuissero) | Sorotipagem rápida de Haemophilus parasuis a partir de montagens |
| [kleborate](/bactopia-tools/kleborate) | Triagem de MLST, subespécies e outros genes de interesse relacionados a Klebsiella |
| [legsta](/bactopia-tools/legsta) | Tipagem de montagens de Legionella pneumophila |
| [lissero](/bactopia-tools/lissero) | Predição de tipagem de sorogrupo para Listeria monocytogenes |
| [mashdist](/bactopia-tools/mashdist) | Cálculo de distâncias Mash entre sequências |
| [mcroni](/bactopia-tools/mcroni) | Variação de sequência em genes de resistência à colistina mobilizada (mcr-1) |
| [meningotype](/bactopia-tools/meningotype) | Sorotipagem de Neisseria meningitidis |
| [mlst](/bactopia-tools/mlst) | Varredura de arquivos de contigs contra esquemas de tipagem PubMLST |
| [mobsuite](/bactopia-tools/mobsuite) | Reconstrução e anotação de plasmídeos em montagens bacterianas |
| [pasty](/bactopia-tools/pasty) | Sorogrupagem de isolados de Pseudomonas aeruginosa |
| [pbptyper](/bactopia-tools/pbptyper) | Tipador de Proteínas de Ligação à Penicilina (PBP) para Streptococcus pneumoniae |
| [phispy](/bactopia-tools/phispy) | Predição de profagos em genomas bacterianos |
| [plasmidfinder](/bactopia-tools/plasmidfinder) | Identificação de plasmídeos a partir de montagens |
| [prokka](/bactopia-tools/prokka) | Anotação de genomas completos de genomas pequenos (bacterianos, arqueais, virais) |
| [quast](/bactopia-tools/quast) | Avaliação da qualidade de contigs montados |
| [rgi](/bactopia-tools/rgi) | Predição de resistência a antibióticos a partir de montagens |
| [seqsero2](/bactopia-tools/seqsero2) | Predição de sorotipo de Salmonella a partir de reads ou montagens |
| [shigeifinder](/bactopia-tools/shigeifinder) | Sorotipagem de Shigella e EIEC a partir de montagens |
| [sistr](/bactopia-tools/sistr) | Predição de sorovar de montagens de Salmonella |
| [spatyper](/bactopia-tools/spatyper) | Método computacional para encontrar tipos spa em Staphylococcus aureus |
| [stecfinder](/bactopia-tools/stecfinder) | Sorotipagem de genomas de Escherichia coli produtores de toxina Shigella |
| [ssuissero](/bactopia-tools/ssuissero) | Sorotipagem rápida de Streptococcus suis a partir de montagens |

:::

</details>

:::danger[Bactopia Tools requerem amostras processadas com Bactopia]

Uma das principais características das Bactopia Tools é que elas utilizam as saídas do Bactopia para
identificar e iniciar a análise rapidamente. As montagens do AllTheBacteria não foram processadas pelo Bactopia,
portanto não são compatíveis com as Bactopia Tools. Mas não se preocupe, com um pouco de trabalho podemos
tornar isso possível!

:::

## `bactopia atb-formatter`

O Bactopia já permite montagens como entradas, mas eu não queria que os usuários precisassem passar pelo
pipeline completo do Bactopia para usar as Bactopia Tools. Em vez disso, queria criar uma forma rápida e fácil
para que os usuários fossem diretamente ao uso das Bactopia Tools. Para isso, criei um novo comando Bactopia
chamado [atb-formatter](https://github.com/bactopia/bactopia-py?tab=readme-ov-file#all-the-bacteria-atb)
(_AllTheBacteria Formatter_). Com o `atb-formatter`, a estrutura de diretórios de saída necessária do Bactopia
será criada a partir de um diretório de montagens do _AllTheBacteria_.

:::tip[Montagens do AllTheBacteria podem ser usadas com Bactopia Tools!]

:::

Isso é legal e tudo mais, mas vamos demonstrar na prática o uso do `atb-formatter` em algumas
montagens de _Legionella pneumophila_ do AllTheBacteria.

## Exemplo de Uso para _Legionella pneumophila_

Para demonstrar o uso do `bactopia atb-formatter`, utilizarei montagens de
_Legionella pneumophila_ do AllTheBacteria e executarei o [legsta](https://github.com/tseemann/legsta),
uma ferramenta de tipagem para montagens de _L. pneumophila_, escrita por [Torsten Seeman](https://www.doherty.edu.au/people/associate-professor-torsten-seemann).
Mais especificamente, executarei o legsta a partir da [Bactopia Tool](/bactopia-tools/legsta) disponível.

### Preparando o Ambiente

Antes de começar, você precisará ter o Bactopia instalado. Se ainda não fez isso,
consulte as [instruções de instalação](/installation).

Você também vai querer garantir que está usando pelo menos a versão 3.0.1 do Bactopia, pois esta é
a primeira versão que inclui o comando `atb-formatter`.

```bash
bactopia --version
bactopia 3.0.1
```

### Baixando as Montagens

Primeiro, vou baixar as montagens de _L. pneumophila_ do AllTheBacteria e depois extraí-las
em uma pasta chamada `legionella-assemblies`. Simples assim!

```bash
mkdir atb-legionella
cd atb-legionella

# Download the assemblies
wget https://ftp.ebi.ac.uk/pub/databases/AllTheBacteria/Releases/0.1/assembly/legionella_pneumophila__01.asm.tar.xz
wget https://ftp.ebi.ac.uk/pub/databases/AllTheBacteria/Releases/0.1/assembly/legionella_pneumophila__02.asm.tar.xz

# Extract the assemblies
mkdir legionella-assemblies
tar -C legionella-assemblies -xJf legionella_pneumophila__01.asm.tar.xz
tar -C legionella-assemblies -xJf legionella_pneumophila__02.asm.tar.xz
```

No momento em que este texto foi escrito, havia 5.393 montagens de _L. pneumophila_ disponíveis no
AllTheBacteria. Embora não seja _Salmonella enterica_ com suas centenas de milhares de montagens,
é um número ótimo para demonstrar o uso do `bactopia atb-formatter`.

### Criando a Estrutura de Diretórios do Bactopia

Com as montagens extraídas, agora preciso criar a estrutura de diretórios necessária do Bactopia para
usar as Bactopia Tools. Para isso, utilizei o `bactopia atb-formatter`, que cria uma pasta de amostra
para cada montagem correspondente ao número de acesso BioSample.

```bash
# Create the Bactopia directory structure
bactopia atb-formatter --path legionella-assemblies --recursive
```

<details>
<summary>Algumas notas sobre o <code>bactopia atb-formatter</code></summary>

:::info[Informacao]

Observe o uso de `--recursive` aqui, que percorrerá o diretório `legionella-assemblies`
para encontrar todas as montagens contidas. Neste ponto, a estrutura de diretórios do `bactopia`
foi criada para 5.393 montagens e está pronta para uso com as Bactopia Tools.

Além disso, por padrão as montagens não são copiadas para a estrutura de diretórios do Bactopia, mas
em vez disso são criados links simbólicos. Isso é para economizar espaço em disco, mas se você quiser
copiar as montagens, pode usar o parâmetro `--publish-mode` para alterar esse comportamento.

:::

</details>

Após executar o comando acima, você deverá ver algo semelhante ao seguinte:

```bash
2024-03-22 14:30:07:root:INFO - Setting up Bactopia directory structure (use --verbose to see more details)
2024-03-22 14:30:08:root:INFO - Bactopia directory structure created at bactopia
2024-03-22 14:30:08:root:INFO - Total assemblies processed: 5393
```

### Usando Bactopia para executar o Legsta

Ótimo! Agora temos todas as montagens vinculadas via link simbólico em uma estrutura de diretórios do Bactopia. É
hora de deixar as Bactopia Tools brilharem! Para isso, executarei a
[Bactopia Tool legsta](/bactopia-tools/legsta) e demonstrarei
como é simples tipar 5.393 montagens.

Com uma simples adição de `--wf legsta` e apontando para o diretório Bactopia, o `legsta` será
executado em todas as 5.393 montagens! É realmente assim tão simples!

```bash
# Run legsta
bactopia --wf legsta -profile singularity
```

:::tip[Por favor, use Docker ou Singularity para essas análises]

Sou um grande apoiador do Conda, mas para reprodutibilidade, é recomendado usar Docker ou
Singularity com as Bactopia Tools. Os ambientes Conda podem mudar dependendo de quando são
instalados, enquanto os containers serão sempre os mesmos.

:::

Após algum tempo, a ferramenta `legsta` será concluída para todas as 5.393 montagens, e você deverá ver
algo semelhante ao seguinte:

```bash
[5d/d04297] process > BACTOPIATOOLS:LEGSTA:LEGSTA_MODULE (SAMN29911258) [100%] 5393 of 5393 ✔
[71/c63bf7] process > BACTOPIATOOLS:LEGSTA:CSVTK_CONCAT (legsta)        [100%] 1 of 1 ✔
[16/833262] process > BACTOPIATOOLS:CUSTOM_DUMPSOFTWAREVERSIONS (1)     [100%] 1 of 1 ✔

    Bactopia Tools: `legsta Execution Summary
    ---------------------------
    Bactopia Version : 3.0.1
    Nextflow Version : 23.10.1
    Command Line     : nextflow run /home/rpetit3/bactopia/main.nf --wf legsta \
                                    --bactopia bactopia/ -profile singularity
    Resumed          : false
    Completed At     : 2024-03-22T15:09:54.959834620-06:00
    Duration         : 32m 51s
    Success          : true
    Exit Code        : 0
    Error Report     : -
    Launch Dir       : /home/rpetit3/test-legsta
```

Isso levou cerca de 30 minutos no meu laptop, mas foi incrivelmente simples executar o `legsta` em
todas as 5.393 montagens de _L. pneumophila_.

### Resultados da Tipagem

Aqui vem a parte divertida: os resultados de tipagem para todas as 5.393 montagens de _L. pneumophila_! Outro ponto
positivo das Bactopia Tools é que, na maioria dos casos, elas mesclam todos os resultados ao final,
deixando você com apenas um único arquivo para revisar.

Para compartilhar os resultados desta análise, fiz o upload dos resultados no Google Drive e os disponibilizei
neste link: <a href="https://docs.google.com/spreadsheets/d/1NjkXEstWq5PMP0CLmO392HTjC8UuW-JPQIXpqsZ30nU/edit?usp=sharing" target="_blank">Bactopia - Legsta Results from AllTheBacteria</a>

A partir desta planilha do Google, você pode fazer uma cópia ou exportar os resultados como arquivo CSV.

## Conclusão

Neste post, demonstrei como em apenas alguns passos você pode usar as Bactopia Tools para
começar a analisar de forma rápida e integrada as 2.000.000 montagens bacterianas do AllTheBacteria.
Se você está planejando fazer suas próprias análises downstream nessas montagens, espero que este post
tenha te convencido de que o Bactopia pode tornar esse processo muito mais fácil.

Se você tiver alguma dúvida ou ideia para novas Bactopia Tools, sinta-se à vontade para
entrar em contato comigo!

**Também! Este é o primeiro post do blog do Bactopia!**
