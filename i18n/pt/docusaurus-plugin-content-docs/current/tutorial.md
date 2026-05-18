---
title: Tutorial
description: >-
    Um tutorial para começar a usar o Bactopia com genomas publicamente disponíveis.
sidebar_position: 4
---
Neste tutorial, vamos percorrer o processamento de amostras de *S. aureus* associadas a
infecções pulmonares por fibrose cística. Essas amostras são da publicação abaixo e estão
disponíveis no acesso BioProject [PRJNA480016](https://www.ebi.ac.uk/ena/data/view/PRJNA480016).

* *Bernardy, Eryn E., et al. ["Whole-Genome Sequences of Staphylococcus aureus Isolates from Cystic Fibrosis Lung Infections."](https://doi.org/10.1128/MRA.01564-18) Microbiol Resour Announc 8.3 (2019): e01564-18.*

O objetivo do tutorial é:

* [ ] Verificar se o Bactopia está funcionando
* [ ] Usar o Bactopia para processar:
    * [ ] Uma única amostra do SRA/ENA
    * [ ] Múltiplas amostras do SRA/ENA
    * [ ] Uma única amostra local
    * [ ] Múltiplas amostras locais
    * [ ] Agregar resultados de múltiplas amostras
* [ ] Usar as Bactopia Tools para:
    * [ ] Executar análises específicas de *S. aureus*
    * [ ] Gerar uma árvore usando [Mashtree](/bactopia-tools/mashtree)

Ao concluir este tutorial, você estará pronto para processar seus próprios dados usando o Bactopia!

:::warning[O Bactopia Deve Estar Instalado]
Este tutorial pressupõe que você já instalou o Bactopia. Se ainda não instalou, veja como
fazer em [Instalação](./installation).
:::

:::warning[Entre em contato se tiver problemas com este tutorial]
Faço o possível para garantir que tudo funcione como esperado, mas entendo que nem sempre é
o caso. Se encontrar algum problema neste tutorial, por favor me avise enviando uma
[GitHub Issue](https://github.com/bactopia/bactopia/issues/new/choose).
Juntos, certamente conseguiremos descobrir o que está acontecendo.
:::

OK! Vamos começar o tutorial!

## Selecionando um Profile

Como o Bactopia é escrito em Nextflow, ele pode ser executado em muitos ambientes diferentes.
Para os propósitos deste tutorial, usaremos o profile padrão, que utilizará ambientes Conda
para executar as ferramentas. No entanto, se você estiver em um sistema com Singularity ou Docker,
esses são recomendados em vez dos ambientes Conda.

Se quiser usar Docker, basta adicionar `-profile docker` aos comandos abaixo.
Da mesma forma, se quiser usar Singularity, adicione `-profile singularity`.

<details>
<summary>Profiles podem ser estendidos para outros sistemas (por exemplo, HPC e nuvem)</summary>

O Nextflow tem suporte integrado para vários sistemas. Se você estiver interessado em usar o Bactopia
em um sistema diferente da sua máquina local, consulte os
[Nextflow Executors](https://www.nextflow.io/docs/latest/executor.html). Configurar um
profile personalizado para este tutorial está fora do seu escopo, mas se estiver interessado em fazer
isso, sinta-se à vontade para entrar em contato.

</details>

## Verificando se o Bactopia Está Funcionando

Antes de começarmos, usaremos o profile `test` integrado para verificar se o Bactopia está funcionando
para você. Este profile `test` baixará um genoma bacteriano muito pequeno (~350kb de tamanho),
o que permitirá que você teste o Bactopia rapidamente.

Para executar o teste, basta rodar o seguinte comando:

```bash
bactopia -profile test,standard
```

No exemplo acima, `standard` é um profile que faz uso de ambientes Conda.

<details>
<summary>Exemplos de comandos para usar Docker ou Singularity</summary>

Se você estiver usando Docker, execute o seguinte comando:
```bash
bactopia -profile test,docker
```

Se você estiver usando Singularity, execute o seguinte comando:
```bash
bactopia -profile test,singularity
```

</details>

:::note[A primeira execução pode demorar um pouco]
Na primeira vez que você executar o Bactopia, ele criará os ambientes (Conda, Docker ou Singularity)
necessários para a análise. Dependendo da sua conexão com a internet, isso pode demorar um pouco.
Recomendo pegar um café ou dar uma caminhada. Esta é uma construção única; execuções futuras
serão muito mais rápidas.
:::

Após a conclusão, você verá um texto semelhante ao seguinte:

```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[67/254aed] GATHER:GATHER_MODULE (SRR2838702)            [100%] 1 of 1 ✔
[48/e17b5c] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[90/a4499c] QC:QC_MODULE (SRR2838702)                    [100%] 1 of 1 ✔
[13/caba51] ASSEMBLER:ASSEMBLER_MODULE (SRR2838702)      [100%] 1 of 1 ✔
[8a/3b2e31] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[6b/d0dfa7] SKETCHER:SKETCHER_MODULE (SRR2838702)        [100%] 1 of 1 ✔
[e0/b1d5b9] PROKKA:PROKKA_MODULE (SRR2838702)            [100%] 1 of 1 ✔
[2c/900d9e] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRR2838702) [100%] 1 of 1 ✔
[12/c2fcd1] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[82/800c26] MLST:MLST_MODULE (SRR2838702)                [100%] 1 of 1 ✔
[9c/5206fe] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 10:55:13
Duration    : 3m 29s
CPU hours   : 0.2
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none -profile test,docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : test,docker
Completed At     : 2026-04-29T10:55:13.036123110-06:00
Duration         : 3m 29s
Resumed          : false
Success          : true
Merged Results   : bactopia/bactopia-runs/bactopia-20260429-105142


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia bactopia --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia bactopia --wf pangenome
bactopia -profile docker --bactopia bactopia --wf merlin
bactopia -profile docker --bactopia bactopia --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
What cheese can never be yours? Nacho cheese!
```

Se você ver um texto semelhante, está pronto para continuar!

* [x] Verificar se o Bactopia está funcionando

## Amostras no SRA/ENA

OK! Estamos prontos para começar a processar alguns genomas bacterianos usando o Bactopia. Nesta seção,
processaremos genomas publicamente disponíveis no Sequence Read Archive (SRA) e no
European Nucleotide Archive (ENA).

### Uma Única Amostra

Vamos começar baixando uma única amostra do [Sequence Read Archive](https://www.ncbi.nlm.nih.gov/sra)
(SRA) e processando-a pelo Bactopia. Para fazer isso, você pode usar o comando `bactopia` com
o parâmetro `--accession`, como no seguinte comando:

```bash
bactopia \
    --accession SRX4563634 \
    --coverage 100 \
    --genome_size 2800000 \
    --max_cpus 2 \
    --outdir ena-single-sample
```

Após pressionar Enter, relaxe e acompanhe as atualizações em tempo real do Nextflow para
a análise de SRX4563634! Esta análise terá um **tempo de conclusão aproximado de ~15-30 minutos**,
dependendo do número de cpus disponíveis e dos tempos de download do ENA. Enquanto isso acontece,
podemos revisar alguns dos parâmetros usados no comando.

Aqui estão os parâmetros usados no comando:

| Parâmetro | Descrição |
| --------- | ----------- |
| `--accession` | O acesso de Experimento do SRA para baixar e processar. |
| `--coverage` | A cobertura estimada para limitar os FASTQs. |
| `--genome_size` | O tamanho estimado do genoma. |
| `--max_cpus` | O número máximo de cpus a utilizar. |
| `--outdir` | O diretório para armazenar os resultados. |

Em resumo, informamos ao Bactopia para baixar os FASTQs associados ao acesso de Experimento
SRX4563634 (`--accession SRX4563634`), limitar o arquivo FASTQ limpo a uma cobertura estimada de 100x
(`--coverage 100`) com base no tamanho do genoma de 2.800.000bp (`--genome_size 2800000`), usar apenas
2 cpus por processo (`--max_cpus 2`) e, finalmente, gravar as saídas no diretório `ena-single-sample`
(`--outdir ena-single-sample`).

__*Algum tempo depois...*__

Após algum tempo (_15 minutos no meu caso_), você terá resultados disponíveis em
`ena-single-sample/SRX4563634/`. Cada um desses arquivos de saída está documentado em detalhes
na seção __*Workflow Steps*__ da documentação, começando com a
etapa Gather.

<details>
<summary>Informações de log esperadas</summary>

O Nextflow produzirá informações de log explicando o que está acontecendo durante a
análise. Aqui está um exemplo do texto de log que você deve ver:
```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[ee/03bca9] GATHER:GATHER_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[1c/00a83a] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[5f/e313c3] QC:QC_MODULE (SRX4563634)                    [100%] 1 of 1 ✔
[f0/76d7d3] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)      [100%] 1 of 1 ✔
[e0/ed8bf7] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[05/bc5789] SKETCHER:SKETCHER_MODULE (SRX4563634)        [100%] 1 of 1 ✔
[b8/5c3c0b] PROKKA:PROKKA_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[71/1c2646] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634) [100%] 1 of 1 ✔
[f1/d82589] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[76/d9b39f] MLST:MLST_MODULE (SRX4563634)                [100%] 1 of 1 ✔
[b1/3c8b94] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:05:37
Duration    : 8m 55s
CPU hours   : 0.3
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --accession SRX4563634 --coverage 100 --genome_size 2800000 --max_cpus 2 --outdir ena-single-sample -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:05:37.643590738-06:00
Duration         : 8m 55s
Resumed          : false
Success          : true
Merged Results   : ena-single-sample/bactopia-runs/bactopia-20260429-105641


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia ena-single-sample --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia ena-single-sample --wf pangenome
bactopia -profile docker --bactopia ena-single-sample --wf merlin
bactopia -profile docker --bactopia ena-single-sample --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
When does a joke become a 'dad' joke? When it becomes apparent!
```

</details>

<details>
<summary>Estrutura de diretório de saída esperada</summary>

Após a conclusão da execução do Bactopia, você deverá ter uma estrutura de diretório semelhante
à seguinte:
```bash
tree ena-single-sample/
ena-single-sample/
├── bactopia-runs
│   └── bactopia-20260429-105641
│       ├── merged-results
│       │   ├── amrfinderplus.tsv
│       │   ├── assembly-scan.tsv
│       │   ├── logs
│       │   │   ├── amrfinderplus-concat
│       │   │   │   ├── nf.command.begin
│       │   │   │   ├── nf.command.err
│       │   │   │   ├── nf.command.log
│       │   │   │   ├── nf.command.out
│       │   │   │   ├── nf.command.run
│       │   │   │   ├── nf.command.sh
│       │   │   │   ├── nf.command.trace
│       │   │   │   └── versions.yml
│       │   │   ├── assembly-scan-concat
│       │   │   │   ├── nf.command.begin
│       │   │   │   ├── nf.command.err
│       │   │   │   ├── nf.command.log
│       │   │   │   ├── nf.command.out
│       │   │   │   ├── nf.command.run
│       │   │   │   ├── nf.command.sh
│       │   │   │   ├── nf.command.trace
│       │   │   │   └── versions.yml
│       │   │   ├── meta-concat
│       │   │   │   ├── nf.command.begin
│       │   │   │   ├── nf.command.err
│       │   │   │   ├── nf.command.log
│       │   │   │   ├── nf.command.out
│       │   │   │   ├── nf.command.run
│       │   │   │   ├── nf.command.sh
│       │   │   │   ├── nf.command.trace
│       │   │   │   └── versions.yml
│       │   │   └── mlst-concat
│       │   │       ├── nf.command.begin
│       │   │       ├── nf.command.err
│       │   │       ├── nf.command.log
│       │   │       ├── nf.command.out
│       │   │       ├── nf.command.run
│       │   │       ├── nf.command.sh
│       │   │       ├── nf.command.trace
│       │   │       └── versions.yml
│       │   ├── meta.tsv
│       │   └── mlst.tsv
│       └── nf-reports
│           ├── bactopia-dag.dot
│           ├── bactopia-report.html
│           ├── bactopia-timeline.html
│           └── bactopia-trace.txt
└── SRX4563634
    ├── main
    │   ├── annotator
    │   │   └── prokka
    │   │       ├── logs
    │   │       │   ├── nf.command.begin
    │   │       │   ├── nf.command.err
    │   │       │   ├── nf.command.log
    │   │       │   ├── nf.command.out
    │   │       │   ├── nf.command.run
    │   │       │   ├── nf.command.sh
    │   │       │   ├── nf.command.trace
    │   │       │   ├── SRX4563634.err
    │   │       │   ├── SRX4563634.log
    │   │       │   └── versions.yml
    │   │       ├── SRX4563634-blastdb.tar.gz
    │   │       ├── SRX4563634.faa.gz
    │   │       ├── SRX4563634.ffn.gz
    │   │       ├── SRX4563634.fna.gz
    │   │       ├── SRX4563634.fsa.gz
    │   │       ├── SRX4563634.gbk.gz
    │   │       ├── SRX4563634.gff.gz
    │   │       ├── SRX4563634.sqn.gz
    │   │       ├── SRX4563634.tbl.gz
    │   │       ├── SRX4563634.tsv
    │   │       └── SRX4563634.txt
    │   ├── assembler
    │   │   ├── logs
    │   │   │   ├── nf.command.begin
    │   │   │   ├── nf.command.err
    │   │   │   ├── nf.command.log
    │   │   │   ├── nf.command.out
    │   │   │   ├── nf.command.run
    │   │   │   ├── nf.command.sh
    │   │   │   ├── nf.command.trace
    │   │   │   ├── shovill.log
    │   │   │   └── versions.yml
    │   │   ├── SRX4563634.fna.gz
    │   │   ├── SRX4563634.tsv
    │   │   └── supplemental
    │   │       ├── flash.hist
    │   │       ├── flash.histogram
    │   │       ├── illumina.txt
    │   │       └── shovill.corrections
    │   ├── gather
    │   │   ├── logs
    │   │   │   ├── nf.command.begin
    │   │   │   ├── nf.command.err
    │   │   │   ├── nf.command.log
    │   │   │   ├── nf.command.out
    │   │   │   ├── nf.command.run
    │   │   │   ├── nf.command.sh
    │   │   │   ├── nf.command.trace
    │   │   │   └── versions.yml
    │   │   └── SRX4563634-meta.tsv
    │   ├── qc
    │   │   ├── logs
    │   │   │   ├── nf.command.begin
    │   │   │   ├── nf.command.err
    │   │   │   ├── nf.command.log
    │   │   │   ├── nf.command.out
    │   │   │   ├── nf.command.run
    │   │   │   ├── nf.command.sh
    │   │   │   ├── nf.command.trace
    │   │   │   ├── SRX4563634-fastp.log
    │   │   │   └── versions.yml
    │   │   ├── SRX4563634_R1.fastq.gz
    │   │   ├── SRX4563634_R2.fastq.gz
    │   │   └── supplemental
    │   │       ├── SRX4563634.fastp.html
    │   │       ├── SRX4563634.fastp.json
    │   │       ├── SRX4563634_R1-final_fastqc.html
    │   │       ├── SRX4563634_R1-final_fastqc.zip
    │   │       ├── SRX4563634_R1-final.json
    │   │       ├── SRX4563634_R1-original_fastqc.html
    │   │       ├── SRX4563634_R1-original_fastqc.zip
    │   │       ├── SRX4563634_R1-original.json
    │   │       ├── SRX4563634_R2-final_fastqc.html
    │   │       ├── SRX4563634_R2-final_fastqc.zip
    │   │       ├── SRX4563634_R2-final.json
    │   │       ├── SRX4563634_R2-original_fastqc.html
    │   │       ├── SRX4563634_R2-original_fastqc.zip
    │   │       └── SRX4563634_R2-original.json
    │   └── sketcher
    │       ├── logs
    │       │   ├── nf.command.begin
    │       │   ├── nf.command.err
    │       │   ├── nf.command.log
    │       │   ├── nf.command.out
    │       │   ├── nf.command.run
    │       │   ├── nf.command.sh
    │       │   ├── nf.command.trace
    │       │   └── versions.yml
    │       ├── SRX4563634-k21.msh
    │       ├── SRX4563634-k31.msh
    │       ├── SRX4563634-mash-refseq88-k21.txt
    │       ├── SRX4563634.sig
    │       └── SRX4563634-sourmash-gtdb-rs207-k31.txt
    └── tools
        ├── amrfinderplus
        │   ├── logs
        │   │   ├── nf.command.begin
        │   │   ├── nf.command.err
        │   │   ├── nf.command.log
        │   │   ├── nf.command.out
        │   │   ├── nf.command.run
        │   │   ├── nf.command.sh
        │   │   ├── nf.command.trace
        │   │   └── versions.yml
        │   └── SRX4563634.tsv
        └── mlst
            ├── logs
            │   ├── nf.command.begin
            │   ├── nf.command.err
            │   ├── nf.command.log
            │   ├── nf.command.out
            │   ├── nf.command.run
            │   ├── nf.command.sh
            │   ├── nf.command.trace
            │   └── versions.yml
            └── SRX4563634.tsv

30 directories, 141 files
```

</details>

* [x] Usar o Bactopia para processar:
    * [x] Uma única amostra do SRA/ENA

### Múltiplas Amostras

Processar uma amostra é ótimo, mas [PRJNA480016](https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA480016),
o estudo que estamos usando para este tutorial, tem 66 amostras. Não se preocupe, não vamos processar
todas as 66 amostras, mas você pode imaginar que quase todo estudo terá mais de uma amostra. O Bactopia
permite que você processe quantas amostras quiser, e é bem fácil de fazer.

Para este tutorial, vamos processar 5 amostras do [PRJNA480016](https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA480016).
Para isso, faremos uso do comando `bactopia search`. Este comando permite que você pesquise
amostras no SRA/ENA e gere uma lista de acessos para processamento com o Bactopia.

:::tip[Confira o Guia do Iniciante para mais informações sobre `bactopia search`]
Por enquanto, vamos usar o `bactopia search` sem muitos detalhes sobre como funciona.
Você pode usar o `bactopia search` para algumas coisas interessantes; para saber mais sobre ele, confira
[Guia do Iniciante -> Accessions](./beginners-guide#accessions).
:::

Vamos experimentar o `bactopia search`:

```bash
bactopia search \
    --query PRJNA480016 \
    --limit 5 \
    --use-ncbi-genome-size
```

Este comando produzirá 4 arquivos:

| Nome do arquivo           | Descrição                                                                      |
|---------------------------|--------------------------------------------------------------------------------|
| `bactopia-metadata.txt`   | Um arquivo delimitado por tabulação com todos os resultados da consulta         |
| `bactopia-accessions.txt` | Uma lista de acessos de Experimento a serem processados                        |
| `bactopia-filtered.txt`   | Uma lista de acessos de Experimento que foram filtrados, caso contrário vazio  |
| `bactopia-search.txt`     | Um resumo da solicitação concluída                                             |

Para este tutorial, `bactopia-accessions.txt` é o arquivo de que precisamos. Ele contém cinco acessos de
Experimento, um por linha. Semelhante a isto:

```bash
accession       runtype species genome_size
SRX4563690      illumina        Staphylococcus aureus   2800000
SRX4563681      illumina        Staphylococcus aureus   2800000
SRX4563689      illumina        Staphylococcus aureus   2800000
SRX4563687      illumina        Staphylococcus aureus   2800000
SRX4563682      illumina        Staphylococcus aureus   2800000
```

__*Nota: você pode ter 5 acessos diferentes do projeto PRJNA480016.*__

Antes de usar este arquivo, vamos explicar o que ele contém.

| Coluna | Descrição |
| ------ | ----------- |
| `accession`   | O acesso de Experimento a ser baixado                                           |
| `runtype`     | Informa ao Bactopia como processar os dados (por exemplo, Illumina ou Nanopore) |
| `species`     | A espécie associada ao acesso de Experimento                                    |
| `genome_size` | O tamanho esperado do genoma da espécie obtido do NCBI                          |


Agora vem a parte divertida! Não precisamos executar o Bactopia 5 vezes para cada acesso;
em vez disso, podemos passar o `bactopia-accession.txt` para o Bactopia usando o parâmetro `--accessions`.
Vamos experimentar:

```bash
bactopia \
    --accessions bactopia-accessions.txt \
    --coverage 100 \
    --outdir ena-multiple-samples \
    --max_cpus 2
```

Em vez de `--accession`, agora estamos usando `--accessions`, que diz ao Bactopia para ler o
arquivo fornecido, no nosso caso `bactopia-accessions.txt`, e baixar cada acesso de Experimento
do SRA/ENA e então processá-los todos de uma vez.

:::tip[Faça uma pausa, isso vai demorar um pouco]
Neste ponto, você pode querer dar uma caminhada ou se preparar um café! Esta etapa tem
um **tempo de conclusão aproximado de ~15-120 minutos**. Novamente, o tempo total dependerá
do seu sistema e da sua conexão com a internet.
:::

Após a conclusão, os resultados de todas as cinco amostras serão encontrados no
diretório `ena-multiple-samples`. Cada amostra terá sua própria pasta de resultados.

<details>
<summary>Informações de log esperadas</summary>

O Nextflow produzirá informações de log explicando o que está acontecendo durante a
análise. Aqui está um exemplo do texto de log que você deve ver:
```bash
executor >  local (39)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[e6/6018f9] GATHER:GATHER_MODULE (SRX4563688)            [100%] 5 of 5 ✔
[53/b1868a] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[0e/05679c] QC:QC_MODULE (SRX4563688)                    [100%] 5 of 5 ✔
[d7/aaf093] ASSEMBLER:ASSEMBLER_MODULE (SRX4563688)      [100%] 5 of 5 ✔
[d2/04970a] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[46/6ef407] SKETCHER:SKETCHER_MODULE (SRX4563688)        [100%] 5 of 5 ✔
[50/4e3e72] PROKKA:PROKKA_MODULE (SRX4563688)            [100%] 5 of 5 ✔
[62/d43d72] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563688) [100%] 5 of 5 ✔
[76/a4e627] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[f2/1d3aa4] MLST:MLST_MODULE (SRX4563688)                [100%] 5 of 5 ✔
[80/19f956] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:21:01
Duration    : 10m 59s
CPU hours   : 3.9
Succeeded   : 39

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --accessions bactopia-accessions.txt --coverage 100 --outdir ena-multiple-samples --max_cpus 4 -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:21:01.214462971-06:00
Duration         : 11m
Resumed          : false
Success          : true
Merged Results   : ena-multiple-samples/bactopia-runs/bactopia-20260429-111000


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia ena-multiple-samples --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia ena-multiple-samples --wf pangenome
bactopia -profile docker --bactopia ena-multiple-samples --wf merlin
bactopia -profile docker --bactopia ena-multiple-samples --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
What kind of music do planets listen to? Neptunes!
```

</details>

* [x] Usar o Bactopia para processar:
    * [x] Uma única amostra do SRA/ENA
    * [x] Múltiplas amostras do SRA/ENA

Parabéns! Neste ponto, você deve ter conseguido usar o Bactopia para processar múltiplos
genomas publicamente disponíveis no SRA/ENA. Agora vamos seguir para o processamento de algumas amostras locais!

## Amostras Locais

Para este tutorial, pensei em ter um conjunto de dados para você baixar, mas já baixamos
algumas amostras! Em vez disso, vamos reutilizar algumas das amostras que baixamos do SRA/ENA.

Primeiro, vamos criar um diretório para colocar os FASTQs:

```bash
mkdir fastqs
```

Agora vamos mover alguns FASTQs da nossa amostra SRX4563634 para esta pasta.

```bash
cp ./ena-single-sample/SRX4563634/main/qc/SRX4563634*.fastq.gz fastqs
```

Por fim, vamos também criar uma versão single-end do SRX4563634.

```bash
cat fastqs/SRX4563634_R1.fastq.gz fastqs/SRX4563634_R2.fastq.gz > fastqs/SRX4563634-SE.fastq.gz
```

Isso nos dará três FASTQs locais para trabalhar:

```bash
ls fastqs/
SRX4563634-SE.fastq.gz  SRX4563634_R1.fastq.gz  SRX4563634_R2.fastq.gz
```

Com tudo pronto, vamos começar a processar algumas amostras locais!

* [ ] Usar o Bactopia para processar:
    * [ ] Uma única amostra local
    * [ ] Múltiplas amostras locais

### Uma Única Amostra

Primeiro, vamos processar uma única amostra. Isso será muito semelhante à amostra única do
SRA/ENA acima, com algumas pequenas modificações. Para processar uma única amostra, você pode usar os
parâmetros `--r1`/`--r2` (paired-end), `--se` (single-end) e `--sample`.

:::tip[Saiba mais no Guia do Iniciante]
Para saber mais sobre esses parâmetros, consulte a seção
[Guia do Iniciante -> Amostra Única](./beginners-guide#single-sample). Cada um desses
parâmetros está descrito em detalhes.
:::

#### Paired-End

Para reads paired-end, você vai querer usar `--R1`, `--R2` e `--sample`. Para este exemplo de paired-end,
usaremos SRX4563634 novamente, que copiamos para a pasta `fastqs`.

```bash
bactopia \
    --r1 fastqs/SRX4563634_R1.fastq.gz \
    --r2 fastqs/SRX4563634_R2.fastq.gz \
    --sample SRX4563634 \
    --coverage 100 \
    --genome_size 2800000 \
    --outdir local-single-sample \
    --max_cpus 2
```

No comando acima, usamos os parâmetros `--r1` e `--r2` para informar ao Bactopia que os reads de
entrada devem ser processados como reads paired-end Illumina. O parâmetro `--sample` é usado para
nomear os arquivos de saída. Como antes, também fornecemos os parâmetros `--coverage`, `--genome_size`
e `--max_cpus`.

Agora você provavelmente está pegando o jeito. Assim como na amostra única do SRA/ENA,
podemos esperar que isso leve **aproximadamente ~15-30 minutos para concluir**, então considere
fazer uma pausa.

Após a conclusão, os resultados podem ser encontrados em `local-single-sample/`.

<details>
<summary>Informações de log esperadas</summary>

O Nextflow produzirá informações de log explicando o que está acontecendo durante a
análise. Aqui está um exemplo do texto de log que você deve ver:

```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[f2/02a83e] GATHER:GATHER_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[67/4c51ca] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[8c/d85d58] QC:QC_MODULE (SRX4563634)                    [100%] 1 of 1 ✔
[6a/c11313] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)      [100%] 1 of 1 ✔
[b7/a83b77] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[16/ba5aef] SKETCHER:SKETCHER_MODULE (SRX4563634)        [100%] 1 of 1 ✔
[ae/c0cc9f] PROKKA:PROKKA_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[4d/40bbaf] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634) [100%] 1 of 1 ✔
[1a/d416b4] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[35/d75a90] MLST:MLST_MODULE (SRX4563634)                [100%] 1 of 1 ✔
[c2/98573c] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:44:07
Duration    : 7m
CPU hours   : 0.6
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --r1 fastqs/SRX4563634_R1.fastq.gz --r2 fastqs/SRX4563634_R2.fastq.gz --sample SRX4563634 --coverage 100 --genome_size 2800000 --outdir local-single-sample --max_cpus 4 -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:44:07.351753090-06:00
Duration         : 7m 1s
Resumed          : false
Success          : true
Merged Results   : local-single-sample/bactopia-runs/bactopia-20260429-113705


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia local-single-sample --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia local-single-sample --wf pangenome
bactopia -profile docker --bactopia local-single-sample --wf merlin
bactopia -profile docker --bactopia local-single-sample --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
What do you call a cow with no legs? Ground beef!
```

</details>

#### Single-End

Agora, você pode estar se perguntando _"single-end"_? Embora nas execuções modernas do Illumina
raramente encontremos reads single-end, eles existem. Há muitas amostras Illumina single-end
disponíveis no SRA/ENA. Por isso, o suporte a single-end foi incorporado ao Bactopia.

É uma mudança simples: para analisar reads single-end, em vez de `--r1` e `--r2`, usaremos
`--se`. Vamos experimentar usando o arquivo `SRX4563634-SE.fastq.gz` que criamos anteriormente:

```bash
bactopia \
    --se fastqs/SRX4563634-SE.fastq.gz \
    --sample SRX4563634-SE \
    --coverage 100 \
    --genome_size 2800000 \
    --outdir local-single-sample \
    --max_cpus 2
```

Com o comando acima, SRX4563634-SE será processado como uma amostra single-end. Para o
processamento single-end, algumas análises exclusivas de paired-end (por exemplo, correção de erros)
serão ignoradas. Na maior parte, porém, os reads paired-end e single-end passam pelas mesmas análises.

Está na hora de mais uma pausa! Esta execução levará **aproximadamente ~15-30 minutos para concluir**.

Após a conclusão, seus resultados single-end estarão disponíveis em `local-single-sample`.

<details>
<summary>Informações de log esperadas</summary>

O Nextflow produzirá informações de log explicando o que está acontecendo durante a
análise. Aqui está um exemplo do texto de log que você deve ver:

```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                        [100%] 1 of 1, stored: 1 ✔
[3f/ac6144] GATHER:GATHER_MODULE (SRX4563634-SE)            [100%] 1 of 1 ✔
[b9/4aceb0] GATHER:CSVTK_CONCAT (meta)                      [100%] 1 of 1 ✔
[53/b4c1fd] QC:QC_MODULE (SRX4563634-SE)                    [100%] 1 of 1 ✔
[7b/81dffd] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634-SE)      [100%] 1 of 1 ✔
[17/25f551] ASSEMBLER:CSVTK_CONCAT (assembly-scan)          [100%] 1 of 1 ✔
[cb/1b89ef] SKETCHER:SKETCHER_MODULE (SRX4563634-SE)        [100%] 1 of 1 ✔
[27/f7c3e5] PROKKA:PROKKA_MODULE (SRX4563634-SE)            [100%] 1 of 1 ✔
[a2/9ffd0c] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634-SE) [100%] 1 of 1 ✔
[d5/257b5e] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)      [100%] 1 of 1 ✔
[d6/3402fe] MLST:MLST_MODULE (SRX4563634-SE)                [100%] 1 of 1 ✔
[bb/760752] MLST:CSVTK_CONCAT (mlst)                        [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:55:49
Duration    : 7m 47s
CPU hours   : 0.3
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --se fastqs/SRX4563634-SE.fastq.gz --sample SRX4563634-SE --coverage 100 --genome_size 2800000 --outdir local-single-sample --max_cpus 2 -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:55:49.702989944-06:00
Duration         : 7m 47s
Resumed          : false
Success          : true
Merged Results   : local-single-sample/bactopia-runs/bactopia-20260429-114801


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia local-single-sample --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia local-single-sample --wf pangenome
bactopia -profile docker --bactopia local-single-sample --wf merlin
bactopia -profile docker --bactopia local-single-sample --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
Where do lizards go after their tails fall off? The retail store!
```

</details>

Se você chegou até aqui, está quase concluindo!

* [x] Usar o Bactopia para processar:
    * [x] Uma única amostra local

### Múltiplas Amostras (FOFN)

Vamos lá! Vamos pegar todas essas amostras que temos e processá-las de uma vez! Para fazer isso,
o Bactopia permite que você forneça um arquivo de texto descrevendo as amostras de entrada. Este
arquivo de nomes de arquivo (FOFN), contém nomes de amostras e a localização dos FASTQs associados.

Como você já deve ter adivinhado, não é necessário criar esses FOFNs manualmente, o Bactopia pode fazer isso.
Nesta seção, exploraremos como usar o comando `bactopia prepare` para gerar o
FOFN necessário para processar múltiplas amostras.

:::tip[Saiba mais no Guia do Iniciante]
Para saber mais sobre esses parâmetros, consulte a seção
[Guia do Iniciante -> Amostras Locais](./beginners-guide#local-samples). Cada um desses
parâmetros está descrito em detalhes.
:::

Vamos reutilizar mais arquivos FASTQ. Antes de prosseguir, vamos mover mais FASTQs para nossa
pasta `fastqs`. Para isso, usaremos os FASTQs de `ena-multiple-samples`. Vamos copiá-los:

```bash
find ena-multiple-samples/ -name *.fastq.gz | \
    xargs -I {} cp {} fastqs/
```

Agora devemos ter FASTQs de 7 amostras em nossa pasta `fastqs`. Com eles, vamos gerar
um FOFN usando `bactopia prepare`:

```bash
bactopia prepare --path fastqs/
sample  runtype genome_size     species r1      r2      se      ont     assembly
SRX4563634      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R2.fastq.gz
SRX4563634-SE   single-end      0       UNKNOWN_SPECIES                 /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634-SE.fastq.gz
SRX4563678      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R2.fastq.gz
SRX4563680      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R2.fastq.gz
SRX4563684      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R2.fastq.gz
SRX4563686      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R2.fastq.gz
SRX4563688      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R2.fastq.gz
```

Este comando tentará criar um FOFN para você. Para este tutorial, os nomes dos arquivos FASTQ são bastante diretos
e devem produzir um FOFN correto (ou pelo menos deveria!... espero!). Se não for o caso para você,
existem maneiras de [ajustar o `bactopia prepare`](./beginners-guide#bactopia-prepare).

Espere! Esquecemos algo: na saída acima, temos `0` para `genome_size` e
`UNKNOWN_SPECIES` para `species`. Podemos corrigir isso usando as opções `--species` e `--genome-size`.
Vamos tentar novamente:

```bash
bactopia prepare \
    --path fastqs/ \
    --species "Staphylococcus aureus" \
    --genome-size 2800000
sample  runtype genome_size     species r1      r2      se      ont     assembly
SRX4563634      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R2.fastq.gz
SRX4563634-SE   single-end      2800000 Staphylococcus aureus                   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634-SE.fastq.gz
SRX4563678      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R2.fastq.gz
SRX4563680      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R2.fastq.gz
SRX4563684      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R2.fastq.gz
SRX4563686      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R2.fastq.gz
SRX4563688      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R2.fastq.gz
```

Muito melhor! Ao adicionar o tamanho do genoma, o Bactopia agora pode reduzir a cobertura total ao
valor fornecido por `--coverage`.

No entanto, precisamos gravar isso em um arquivo para usá-lo. Vamos fazer isso agora:

```bash
bactopia prepare \
    --path fastqs/ \
    --species "Staphylococcus aureus" \
    --genome-size 2800000 \
    > samples.txt
```

Pronto! Agora temos tudo o que precisamos para processar todas essas amostras usando o Bactopia. Agora,
vamos processar essas amostras usando o FOFN que acabamos de criar.

```bash
bactopia \
    --samples samples.txt \
    --coverage 100 \
    --max_cpus 2 \
    --outdir local-multiple-samples
```

Em vez de usar `--r1`, `--r2`, `--se` ou `--sample`, estamos usando `--samples`.
O parâmetro `--samples` espera um FOFN gerado pelo `bactopia prepare`, que ele então
usará para configurar a análise de cada amostra incluída.

Sim! Você adivinhou, hora de mais uma pausa! Esta etapa levará **aproximadamente ~15-120 minutos para concluir**.
Até já!

__*Algum tempo depois...*__

Após a conclusão, os resultados de cada amostra (dentro de sua própria pasta) serão encontrados no diretório `local-multiple-samples`.

:::tip[Usar `--samples` é mais eficiente em CPU, tornando-o mais rápido]
O real benefício de usar o método FOFN para processar múltiplas amostras é que o sistema de fila do Nextflow
fará melhor uso das cpus. Processar múltiplas amostras uma de cada vez
(via `--r1`/`--r2` ou `--se`) levará a mais instâncias de jobs aguardando que outros jobs
terminem, período durante o qual as cpus não estão sendo usadas.
:::

<details>
<summary>Informações de log esperadas</summary>

O Nextflow produzirá informações de log explicando o que está acontecendo durante a
análise. Aqui está um exemplo do texto de log que você deve ver:

```bash
executor >  local (53)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[2e/454798] GATHER:GATHER_MODULE (SRX4563634)            [100%] 7 of 7 ✔
[0f/47679f] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[6b/941117] QC:QC_MODULE (SRX4563680)                    [100%] 7 of 7 ✔
[42/913683] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)      [100%] 7 of 7 ✔
[e2/048276] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[5b/b2ac99] SKETCHER:SKETCHER_MODULE (SRX4563634)        [100%] 7 of 7 ✔
[c8/64642a] PROKKA:PROKKA_MODULE (SRX4563634)            [100%] 7 of 7 ✔
[8c/577268] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634) [100%] 7 of 7 ✔
[2c/0dfff6] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[7d/2da0da] MLST:MLST_MODULE (SRX4563634)                [100%] 7 of 7 ✔
[1b/4f229b] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 12:24:25
Duration    : 9m 48s
CPU hours   : 2.5
Succeeded   : 53

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --samples samples.txt --coverage 100 --max_cpus 2 --outdir local-multiple-samples -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T12:24:25.163874442-06:00
Duration         : 9m 48s
Resumed          : false
Success          : true
Merged Results   : local-multiple-samples/bactopia-runs/bactopia-20260429-121435


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia local-multiple-samples --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia local-multiple-samples --wf pangenome
bactopia -profile docker --bactopia local-multiple-samples --wf merlin
bactopia -profile docker --bactopia local-multiple-samples --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
Learn more about Bactopia at https://bactopia.io/
```

</details>

* [x] Usar o Bactopia para processar:
    * [x] Uma única amostra local
    * [x] Múltiplas amostras locais

### Resumo do Bactopia

Agora que processamos várias amostras, pode ser útil obter uma visão geral rápida das suas
amostras. Por exemplo, quais passaram, quais foram os tipos de sequência, como foi a montagem,
etc... Também seria útil reunir tudo isso em um único arquivo. É aqui que o
comando `bactopia summary` entra. Este comando gerará um arquivo delimitado por tabulação com
resultados de cada uma das etapas do Bactopia.

Vamos experimentar e depois vamos percorrer alguns dos detalhes. Para isso, usaremos o
diretório `local-multiple-samples`.

```bash
bactopia summary \
    --bactopia-path local-multiple-samples/
2026-04-29 12:45:12 INFO     2026-04-29 12:45:12:root:INFO - Found 7 samples in local-multiple-samples/ to process                                                    summary.py:341
                    INFO     2026-04-29 12:45:12:root:INFO - Writing report: ./bactopia-report.tsv                                                                    summary.py:432
                    INFO     2026-04-29 12:45:12:root:INFO - Writing exclusion report: ./bactopia-exclude.tsv                                                         summary.py:436
                    INFO     2026-04-29 12:45:12:root:INFO - Writing summary report: ./bactopia-summary.txt
```

Após a conclusão, isso produzirá três arquivos:

| Arquivo                | Descrição |
| ---------------------- | ----------- |
| `bactopia-report.tsv`  | Um arquivo delimitado por tabulação com mais de 70 colunas de resultados das etapas do Bactopia. |
| `bactopia-exclude.tsv` | Um arquivo delimitado por tabulação com amostras que **_provavelmente_** devem ser excluídas de análises posteriores. |
| `bactopia-summary.txt` | Um resumo simples de classificações de qualidade e contagens de exclusão. |

<details>
<summary>Exemplo: `bactopia-report.tsv` _(Aviso! É muito largo!)_</summary>

Abaixo está um exemplo do arquivo `bactopia-report.tsv`. Como você pode ver, há muitas
colunas! Essas colunas incluem muitas informações e funcionam muito bem com Excel ou R.

```tsv
sample  rank    reason  genome_size     species runtype original_runtype        mlst_scheme     mlst_st assembler_total_contig  assembler_total_contig_length   assembler_max_conti _length assembler_mean_contig_length    assembler_median_contig_length  assembler_min_contig_length     assembler_n50_contig_length     assembler_l50_contig_count      assembler_n m_contig_non_acgtn      assembler_contig_percent_a      assembler_contig_percent_c      assembler_contig_percent_g      assembler_contig_percent_t      assembler_contig_percent_n  ssembler_contig_non_acgtn       assembler_contigs_greater_1m    assembler_contigs_greater_100k  assembler_contigs_greater_10k   assembler_contigs_greater_1k    assembler_percent_c ntigs_greater_1m        assembler_percent_contigs_greater_100k  assembler_percent_contigs_greater_10k   assembler_percent_contigs_greater_1k    is_paired       is_compressed   ann tator_total_CDS annotator_total_rRNA    annotator_total_tRNA    qc_original_total_bp    qc_original_coverage    qc_original_read_total  qc_original_read_min    qc_original_read_me n       qc_original_read_std    qc_original_read_median qc_original_read_max    qc_original_read_25th   qc_original_read_75th   qc_original_qual_min    qc_original_qual_mean   qc_ riginal_qual_std        qc_original_qual_max    qc_original_qual_median qc_original_qual_25th   qc_original_qual_75th   qc_final_is_paired      qc_final_total_bp       qc_final_co erage   qc_final_read_total     qc_final_read_min       qc_final_read_mean      qc_final_read_std       qc_final_read_median    qc_final_read_max       qc_final_read_25th      qc_ inal_read_75th  qc_final_qual_min       qc_final_qual_mean      qc_final_qual_std       qc_final_qual_max       qc_final_qual_median    qc_final_qual_25th      qc_final_qual_75th
SRX4563680      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      24      2785142 552034  116047  47976   854     401 93      3       0       33.91   16.13   16.50   33.46   0.00    0.00    0       8       17      22      0.00    33.33   70.83   91.67   true    true    2579    3       59      280 00113   100.0   1156364 22.5000 242.1385        70.4918 282     301     188     301     19      32.4292 4.0463  37      33      29.5000 36      True    280000113       100.0   115 364     22.5000 242.1385        70.4918 282     301     188     301     19      32.4292 4.0463  37      33      29.5000 36
SRX4563684      silver  Low coverage (85.07x, expect >= 100x)   2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      67      2899294 524852  43273   394
        521     160269  5       0       34.51   15.32   17.49   32.67   0.00    0.00    0       9       28      58      0.00    13.43   41.79   86.57   true    true    2725    3   8       238189696       85.0677 985930  27.5000 241.5890        69.2295 274     301     188     301     19      32.4652 4.0385  37      33      30      36      True    238189696   5.0677  985930  27.5000 241.5890        69.2295 274     301     188     301     19      32.4652 4.0385  37      33      30      36
SRX4563686      silver  Low coverage (90.43x, expect >= 100x)   2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      24      2782895 606699  115953  517 1       1071    289301  4       0       33.60   16.43   16.35   33.63   0.00    0.00    0       8       17      24      0.00    33.33   70.83   100.00  true    true    2568    4   8       253197833       90.42779999999999       1063712 25      238.0325        71.9346 268.5000        301     181     301     19      32.5022 4.0360  37      33.5000 30      36  rue     253197833       90.42779999999999       1063712 25      238.0325        71.9346 268.5000        301     181     301     19      32.5022 4.0360  37      33.5000 30      36
SRX4563634      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      26      2875932 838470  110612  23259   855     346 58      3       0       35.00   15.02   17.62   32.36   0.00    0.00    0       8       16      24      0.00    30.77   61.54   92.31   true    true    2682    5       59      280 00172   100.0001        1135318 25      246.6270        67.9079 293     301     197     301     19      32.2062 4.0878  37      33      29.5000 36      True    280000172       100 0001    1135318 25      246.6270        67.9079 293     301     197     301     19      32.2062 4.0878  37      33      29.5000 36
SRX4563678      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      30      2708907 356005  90296   68738   570     201 73      6       0       34.64   15.50   17.26   32.60   0.00    0.00    0       11      21      29      0.00    36.67   70.00   96.67   true    true    2469    6       55      280 00172   100.0   1196990 20      233.9205        73.6150 258.5000        301     175     301     18.5000 33.2099 3.7695  37      34      31      36.5000 True    280000172       100 0       1196990 20      233.9205        73.6150 258.5000        301     175     301     18.5000 33.2099 3.7695  37      34      31      36.5000
SRX4563634-SE   bronze  Single-end reads        2800000 Staphylococcus aureus   single-end      single-end      SCHEME  ST      42      2866760 804138  68256   21805   506     150 23      5       0       34.79   15.27   17.36   32.58   0.00    0.00    0       10      28      37      0.00    23.81   66.67   88.10   false   true    2665    5       59      280 00172   100.0   1135318 25      246.627 67.9105 294     301     197     301     19      32.2063 4.12132 37      33      30      36      False   280000172       100.0   1135318 25  46.627  67.9105 294     301     197     301     19      32.2063 4.12132 37      33      30      36
SRX4563688      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      21      2778300 606249  132300  52250   790     389 17      3       0       33.64   16.33   16.47   33.56   0.00    0.00    0       9       14      19      0.00    42.86   66.67   90.48   true    true    2576    5       58      280 00312   100.0002        1195526 24.5000 234.2070        71.1001 254.5000        301     178     301     18.5000 34.2879 3.3316  37      35.5000 33      37      True    280000312   00.0002 1195526 24.5000 234.2070        71.1001 254.5000        301     178     301     18.5000 34.2879 3.3316  37      35.5000 33      37
```

</details>

<details>
<summary>Exemplo: `bactopia-summary.txt`</summary>

Abaixo está um exemplo do arquivo `bactopia-summary.txt`. Este arquivo é um resumo simples
de contagens.
```bash
Bactopia Summary Report

Total Samples: 7

Passed: 7
    Gold: 4
    Silver: 2
    Bronze: 1

Excluded: 0
    Failed Cutoff: 0

    QC Failure: 0


Reports:
    Full Report (txt): ./bactopia-report.tsv
    Exclusion: ./bactopia-exclude.tsv
    Summary: ./bactopia-summary.txt

Rank Cutoffs:
    Gold:
        Coverage >= 100x
        Quality >= Q30
        Read Length >= 95bp
        Total Contigs < 100
    Silver:
        Coverage >= 50x
        Quality >= Q20
        Read Length >= 75bp
        Total Contigs < 200
    Bronze:
        Coverage >= 20x
        Quality >= Q12
        Read Length >= 49bp
        Total Contigs < 500

Assembly Length Exclusions:
    Minimum: None
    Maximum: None
```

</details>

Você pode estar se perguntando o que determina se uma amostra passa ou falha, e o que são
Gold, Silver e Bronze. Para ser honesto, as Olimpíadas podem ter estado acontecendo quando
escolhemos Gold, Silver e Bronze, mas esses termos funcionam muito bem. Aqui está o
resumo de cada um:

| Classificação | Cobertura | Qualidade | Comprimento de Read | Total de Contigs |
| ---- | -------- | ------- | ----------- | ------------- |
| Gold   | >= 100x | >= Q30  | >= 95bp     | < 100         |
| Silver | >= 50x  | >= Q20  | >= 75bp     | < 200         |
| Bronze | >= 20x  | >= Q12  | >= 49bp     | < 500         |
| Fail   | < 20x   | < Q12   | < 49bp      | >= 500        |

<details>
<summary>Esses limites podem ser alterados</summary>

Esses limites podem funcionar para a maioria, mas é importante ajustá-los às suas
necessidades específicas. Por exemplo, 100x de cobertura pode ser muito alto para o seu estudo, ou talvez
você queira excluir amostras com mais de 100 contigs. Esses limites podem ser alterados
usando os seguintes parâmetros:

| Parâmetro | Padrão | Descrição |
| --------- | ------- | ----------- |
| `--gold-coverage` | 100 | Quantidade mínima de cobertura necessária para o status Gold |
| `--gold-quality` | 30 | Pontuação mínima de qualidade média por read necessária para o status Gold |
| `--gold-read-length` | 95 | Comprimento médio mínimo de read necessário para o status Gold |
| `--gold-contigs` | 100 | Contagem máxima de contigs necessária para o status Gold |
| `--silver-coverage` | 50 | Quantidade mínima de cobertura necessária para o status Silver |
| `--silver-quality` | 20 | Pontuação mínima de qualidade média por read necessária para o status Silver |
| `--silver-read-length` | 75 | Comprimento médio mínimo de read necessário para o status Silver |
| `--silver-contigs` | 200 | Contagem máxima de contigs necessária para o status Silver |
| `--min-coverage` | 20 | Quantidade mínima de cobertura necessária para passar |
| `--min-quality` | 12 | Pontuação mínima de qualidade média por read necessária para passar |
| `--min-read-length` | 49 | Comprimento médio mínimo de read necessário para passar |
| `--max-contigs` | 500 | Contagem máxima de contigs necessária para passar |
| `--min-assembled-size` | 0 | Tamanho mínimo do genoma montado |
| `--max-assembled-size` | 0 | Tamanho máximo do genoma montado |

</details>

Esta foi uma introdução rápida ao comando `bactopia summary`. Com o tempo, este
comando deverá evoluir para um resumo mais robusto das suas amostras.

* [x] Usar o Bactopia para processar:
    * [x] Agregar resultados de múltiplas amostras

### Conclusão

Parabéns! Você conseguiu processar muitas amostras agora com o Bactopia! Até agora, neste
tutorial, abordamos como processar amostras locais e do SRA/ENA. Também abordamos o
`bactopia search` e o `bactopia prepare` para preparar arquivos para o processamento de múltiplas amostras.
Por fim, abordamos o comando `bactopia summary` para obter uma visão geral rápida das suas amostras.

* [x] Usar o Bactopia para processar:
    * [x] Uma única amostra do SRA/ENA
    * [x] Múltiplas amostras do SRA/ENA
    * [x] Uma única amostra local
    * [x] Múltiplas amostras locais
    * [x] Agregar resultados de múltiplas amostras

__*MAS!*__ Ainda não terminamos! Vamos dar uma olhada em como podemos processar ainda mais essas
amostras usando as [Bactopia Tools](/bactopia-tools/). Esses são fluxos de trabalho adicionais
pré-configurados que fazem uso das saídas existentes do Bactopia para se aprofundar ainda mais nos seus estudos.

## Bactopia Tools

Você pode estar se perguntando, _O que são essas "Bactopia Tools"?_ (Ou _Isso nunca vai acabar?!?_)

As Bactopia Tools são poderosos fluxos de trabalho pré-configurados que fazem uso das saídas existentes do Bactopia.
Elas permitem que você amplie rapidamente suas análises além do que o Bactopia oferece por padrão.
Por exemplo, precisa construir uma árvore filogenética? Ou quer chamar SNPs contra uma referência?
Ou talvez apenas fazer um BLAST de alguns genes contra todas as suas amostras? Existem Bactopia Tools para cada
um desses casos, e muito mais.

Essas Bactopia Tools permitem que você __Faça Mais Ciência__ fornecendo uma estrutura para ampliar rapidamente
suas análises.

Nesta seção, exploraremos como você pode usar algumas delas. Vamos começar!

### Análises Específicas de Espécie

Todas as amostras que processamos até agora são da mesma espécie, _Staphylococcus aureus_.
Existe uma Bactopia Tool chamada [staphtyper](/bactopia-tools/staphtyper) que pode ser usada para
executar algumas ferramentas específicas para a análise de _S. aureus_. Vamos executar nossa primeira Bactopia Tool usando as
amostras em `local-multiple-samples`:

```bash
bactopia \
    --wf staphtyper \
    --bactopia local-multiple-samples/
```

Antes de prosseguirmos, o que está acontecendo aqui? Estamos usando o parâmetro `--wf` para dizer ao Bactopia
para executar o fluxo de trabalho `staphtyper`. O parâmetro `--bactopia` é usado para dizer ao Bactopia onde
as saídas de uma execução anterior do Bactopia estão localizadas.

Com essas informações, o Bactopia verificará se um fluxo de trabalho `staphtyper` existe e então
verificará o diretório `local-multiple-samples` para as entradas necessárias. Se tudo
estiver correto, o Bactopia executará o fluxo de trabalho `staphtyper`.

Aqui estão as informações de log que você deve ver:

```bash
executor >  local (24)
[ae/f98c1e] STAPHTYPER:AGRVATE:AGRVATE_MODULE (SRX4563688)      [100%] 7 of 7 ✔
[26/28fe35] STAPHTYPER:AGRVATE:CSVTK_CONCAT (agrvate)           [100%] 1 of 1 ✔
[20/752007] STAPHTYPER:SPATYPER:SPATYPER_MODULE (SRX4563680)    [100%] 7 of 7 ✔
[43/9bba69] STAPHTYPER:SPATYPER:CSVTK_CONCAT (spatyper)         [100%] 1 of 1 ✔
[ea/518783] STAPHTYPER:SCCMEC:SCCMEC_MODULE (SRX4563680)        [100%] 7 of 7 ✔
[51/655b71] STAPHTYPER:SCCMEC:CSVTK_CONCAT (sccmec)             [100%] 1 of 1 ✔
WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Tool Execution Summary
-------------------------------
Workflow         : staphtyper
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/workflows/bactopia-tools/staphtyper/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --wf staphtyper --bactopia local-multiple-samples/ -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T12:48:22.408539959-06:00
Duration         : 15.6s
Resumed          : false
Success          : true
Merged Results   : local-multiple-samples//bactopia-runs/staphtyper-20260429-124805


Message of the Day
-------------------------------
When is a door not a door? When it's ajar!
```

Bem legal (_e rápido!_), não é? Simplesmente adicionando `--wf` e `--bactopia`, conseguimos executar rapidamente
três ferramentas diferentes de _S. aureus_ nas nossas amostras. Além disso, as saídas de cada uma dessas
análises foram combinadas em um único arquivo para fácil visualização.

:::tip[Visite a documentação do `staphtyper` para saber mais]
Para saber mais sobre o `staphtyper` e as saídas que ele produz, consulte a
[documentação do staphtyper](/bactopia-tools/staphtyper). Vale ressaltar que
**todas** as Bactopia Tools terão uma página de documentação semelhante.
:::

* [x] Usar as Bactopia Tools para:
    * [x] Executar análises específicas de *S. aureus*
    * [ ] Gerar uma árvore usando [Mashtree](/bactopia-tools/mashtree)

### Construindo uma Árvore

Agora que executamos algumas análises específicas de _S. aureus_, vamos tentar algo um pouco diferente.
Vamos construir uma árvore usando [Mashtree](/bactopia-tools/mashtree), que constrói a árvore usando
distâncias Mash.

Para este tutorial, estamos usando o Mashtree porque é rápido e, se você chegou até aqui,
provavelmente quer terminar logo!

Vamos concluir isso usando as amostras de `local-multiple-samples`, mas primeiro, vamos excluir
a amostra single-end `SRX4563634-SE` da análise, para demonstrar o uso de `--exclude`.

:::tip[Incluindo e excluindo amostras da análise das Bactopia Tools]
Cada Bactopia Tool tem os seguintes dois parâmetros disponíveis:

| Parâmetro | Descrição |
| --------- | ----------- |
| `--include` | Uma lista de amostras (uma amostra por linha) para _**incluir**_ na análise.   |
| `--exclude` | Uma lista de amostras (uma amostra por linha) para _**excluir**_ da análise. |

Este é um recurso útil para incluir ou excluir amostras de uma análise de Bactopia Tool por
uma razão específica. Por exemplo, imagine que o `bactopia summary` identificou uma amostra que
falhou nas verificações de qualidade e deve ser excluída da análise. Você pode passar o `bactopia-exclude.tsv`
gerado para `--exclude` para garantir que essas amostras com falha não sejam incluídas na análise.

Da mesma forma, suponha que você queira executar uma Bactopia Tool apenas em amostras específicas,
por exemplo, construindo uma árvore de um surto. Você pode passar esta lista de amostras para `--include` para
executar a Bactopia Tool somente nessas amostras.
:::

Primeiro, vamos criar um arquivo com a amostra que queremos excluir:

```bash
echo "SRX4563634-SE" > exclude.txt
```

Agora, executaremos o `mashtree` usando o diretório `local-multiple-samples`, mas excluindo `SRX4563634-SE`,
usando `--exclude` e o `exclude.txt` que acabamos de criar:

```bash
bactopia \
    --wf mashtree \
    --bactopia local-multiple-samples/ \
    --exclude exclude.txt
```

Não mudou muito; simplesmente alterando `staphtyper` para `mashtree`, conseguimos construir rapidamente
uma árvore usando distâncias Mash. Aqui estão as informações de log que você deve ver; observe
onde diz que 1 foi excluída e 6 foram incluídas:

```bash
Validating parameters for Bactopia Tools...
Validation complete.
Excluding 1 samples from the analysis
Found 6 samples to process

If this looks wrong, now's your chance to back out (CTRL+C 3 times).
Sleeping for 5 seconds...

--------------------------------------------------------------------
executor >  local (1)
[95/dbe13d] MASHTREE:MASHTREE_MODULE (mashtree) [100%] 1 of 1 ✔
WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Tool Execution Summary
-------------------------------
Workflow         : mashtree
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/workflows/bactopia-tools/mashtree/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --wf mashtree --bactopia local-multiple-samples/ --exclude exclude.txt -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T12:49:37.337015453-06:00
Duration         : 8.4s
Resumed          : false
Success          : true
Merged Results   : local-multiple-samples//bactopia-runs/mashtree-20260429-124927


Message of the Day
-------------------------------
What do you call a sleeping bull? A bulldozer!
```

:::tip[Visite a documentação do `mashtree` para saber mais]
Para saber mais sobre o `mashtree` e as saídas que ele produz, consulte a
[documentação do mashtree](/bactopia-tools/mashtree). Novamente, cada Bactopia
Tool terá uma página de documentação semelhante.
:::

### Conclusão

Você conseguiu! Espero que com dois exemplos simples, você tenha adquirido uma apreciação de como
as Bactopia Tools podem ajudar a tornar as coisas mais fáceis para você.

* [x] Usar as Bactopia Tools para:
    * [x] Executar análises específicas de *S. aureus*
    * [x] Gerar uma árvore usando [Mashtree](/bactopia-tools/mashtree)

Neste ponto, você provavelmente terminou! Vamos concluir!

## O que vem a seguir?

Este tutorial cobriu muito! Vamos recapitular o que fizemos:

* [x] Verificar se o Bactopia está funcionando
* [x] Usar o Bactopia para processar:
    * [x] Uma única amostra do SRA/ENA
    * [x] Múltiplas amostras do SRA/ENA
    * [x] Uma única amostra local
    * [x] Múltiplas amostras locais
    * [x] Agregar resultados de múltiplas amostras
* [x] Usar as Bactopia Tools para:
    * [x] Executar análises específicas de *S. aureus*
    * [x] Gerar uma árvore usando [Mashtree](/bactopia-tools/mashtree)

Esperamos que você tenha conseguido (eba! 🎉) e queira usar o Bactopia nos seus próprios dados!

Tenha em mente que este tutorial não abordou como processar reads do Oxford Nanopore ou
montagens. Há muito mais que podemos cobrir; se houver algo que você gostaria de ver,
ou quaisquer problemas que você possa ter encontrado, por favor me avise enviando uma
[GitHub Issue](https://github.com/bactopia/bactopia/issues).
