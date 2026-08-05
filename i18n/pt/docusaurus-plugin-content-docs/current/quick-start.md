---
title: Inicio Rapido
description: >-
    Comece a usar Bactopia com alguns comandos, sem perguntas e sem olhar para trás!
sidebar_position: 1
---

## Instalação via Conda

Esta é a forma mais rápida de começar. Os comandos a seguir irão instalar Bactopia e executar um conjunto de dados de teste.

```bash
# Install Bactopia using Conda
conda create -y -n bactopia -c conda-forge -c bioconda bactopia

# Test Bactopia
# First launch will set up environments (e.g. Conda, Docker, or Singularity)
conda activate bactopia
bactopia -profile test,standard
```

:::note[A primeira execução pode demorar um pouco]
Na primeira vez que você executar Bactopia, ele irá construir os ambientes (Conda, Docker ou Singularity)
necessários para a análise. Dependendo da sua conexão com a internet, isso pode demorar um pouco.
Recomendo pegar um café ou dar uma caminhada. Esta construção é feita apenas uma vez, e as execuções
futuras serão muito mais rápidas.
:::

:::note[Use `-profile` para mudar o ambiente]
O perfil padrão do Bactopia é Conda. Se você quiser testar usando Docker ou
Singularity, pode usar a opção `-profile`. Por exemplo, para usar Docker você usaria
`-profile test,docker`, e `-profile test,singularity` para Singularity.
:::

## Executar a partir do Repositório GitHub

Alternativamente, se você já tem Nextflow instalado e não quer usar
Conda para instalar Bactopia, você pode executar Bactopia diretamente do repositório GitHub.

```bash
nextflow run bactopia/bactopia -profile test,standard
```

:::info[Comandos auxiliares não disponíveis]
A instalação via Conda do Bactopia inclui alguns comandos auxiliares que não estão disponíveis
ao executar diretamente com Nextflow. Esses comandos ajudam a preparar planilhas de amostras,
pesquisar bancos de dados públicos, pré-construir ambientes, entre outras ferramentas auxiliares.
:::
