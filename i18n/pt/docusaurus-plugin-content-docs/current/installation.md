---
title: Installation
description: >-
    Aprenda como instalar o Bactopia e comece a usar o Bactopia para suas análises genômicas.
sidebar_position: 2
---

O Bactopia inclui centenas de ferramentas em seu fluxo de trabalho. Como você pode imaginar, instalar todas essas
ferramentas pode se tornar um processo bastante frustrante. Com isso em mente, desde o início o Bactopia foi
desenvolvido para incluir apenas programas disponíveis no [Bioconda](https://bioconda.github.io/)
e no [Conda-Forge](https://conda-forge.org/).

## *(Opcional)* Instalar o Conda via Miniforge

O Conda é um sistema de gerenciamento de pacotes e de ambientes de código aberto que funciona
no Windows, Mac OSX e Linux. Usando pacotes disponíveis no Conda, podemos simplificar o
processo de instalação das centenas de ferramentas que o Bactopia utiliza.

Se você não tem o Conda instalado, recomendo instalar o
[Miniforge](https://github.com/conda-forge/miniforge), pois ele é mantido pela comunidade Conda-Forge e não inclui o canal `defaults`. Você deve seguir as
[Instruções de Instalação do Miniforge](https://github.com/conda-forge/miniforge#unix-like-platforms-macos-linux--wsl)
para isso. O processo levará alguns minutos, mas ao concluir você estará pronto para instalar
o Bactopia.

## Instalação
Com o Conda configurado, você está pronto para criar um ambiente para o
Bactopia. Para isso, use o seguinte comando:

```bash
conda create -n bactopia -c conda-forge -c bioconda bactopia
```

Após alguns minutos você terá um novo ambiente conda adequadamente chamado *bactopia*.
Para ativar esse ambiente, use o seguinte comando:

```bash
conda activate bactopia
```

E voilà, você está pronto para começar a processar seus dados!

## Suporte para Windows e OSX

:::warning[Windows não é suportado, use o Subsistema Windows para Linux]
O Bactopia nunca suportará Windows nativamente devido às dependências. Para usar o Bactopia em uma
máquina Windows, você precisará configurar o Subsistema Windows para Linux (WSL). Isso permitirá
que você execute o Bactopia dentro do subsistema Linux. Tenho recursos limitados para testar
o Bactopia no WSL, mas se você tentar e encontrar algum problema, entre em contato!
:::

:::warning[OSX tem suporte limitado]
Desenvolvi o Bactopia principalmente para Linux, mas reconheço que ele pode ser usado no Mac OSX.
Atualmente o suporte para OSX será limitado por não ter recursos suficientes
disponíveis para testar o OSX de forma extensiva. Tenha isso em mente ao usar o Bactopia no
OSX. Ainda assim, tentarei ajudar se você encontrar algum problema!
:::

:::danger[Apple silicon (ARM) não é suportado]
O Bactopia não funcionará em Apple silicon ou outros processadores ARM. Isso se deve ao fato de muitas das
ferramentas usadas pelo Bactopia não possuírem uma versão compatível com ARM. Está planejado para o
futuro do Bioconda; até lá, a melhor opção é usar Docker para emular a arquitetura linux/amd64.
Isso pode ser feito usando a opção `-profile arm` ao executar o Bactopia.
:::

## Docker e Singularity

Você também pode usar o Bactopia com Docker ou Singularity, mas será o Nextflow que ficará
responsável por isso. Isso é feito usando a opção `-profile`. Por exemplo, para usar Docker você
usaria `-profile docker`, e `-profile singularity` para Singularity.

Ao usar esses perfis, o Nextflow utilizará Docker ou Singularity para cada processo que
for executado. Em outras palavras, o Nextflow usará `docker run` ou `singularity exec`
sem que você precise fazer mais nada.

:::tip[Prefira sempre contêineres em vez do Conda]
Embora eu seja o primeiro a admitir que adoro o Conda, ele não é perfeito. Com o tempo, ferramentas
podem ficar desatualizadas ou incompatíveis devido a dependências. Contêineres são uma ótima forma
de evitar esses problemas. Se você estiver usando o Bactopia e tiver Docker ou Singularity
disponíveis, recomendo usá-los em vez do Conda.
:::

## Executar a partir do Repositório GitHub

Alternativamente, se você já tem o Nextflow instalado e não deseja usar o
Conda para instalar o Bactopia, você pode executar o Bactopia diretamente do repositório GitHub.

```bash
nextflow run bactopia/bactopia
```

:::info[Comandos auxiliares não disponíveis]
A instalação do Bactopia via Conda inclui alguns comandos auxiliares que não estão disponíveis
ao executar diretamente com o Nextflow. Esses comandos ajudam a preparar planilhas de amostras,
pesquisar bancos de dados públicos, pré-construir ambientes, entre outras ferramentas auxiliares.
:::
