---
title: Melhorias ao OSS
description: >-
  Descubra os princípios de design por trás das inúmeras contribuições do Bactopia para a
  comunidade de bioinformática
sidebar_position: 4
---

# Melhorias ao Software de Código Aberto

Manter software de código aberto é um desafio difícil que frequentemente exige tempo e esforço
substanciais, geralmente sem o benefício de reconhecimento ou apoio. A área de bioinformática
não é exceção, pois depende fortemente de ferramentas mantidas por indivíduos com pouco ou
nenhum suporte. O Bactopia não é diferente.

Reconhecendo esses desafios, projetei o Bactopia com o objetivo explícito de retribuir à
comunidade. Para cumprir esse objetivo, incorporei vários requisitos de design fundamentais:

1. As ferramentas devem ser de código aberto e gratuitas para uso.
2. As ferramentas devem estar disponíveis no conda.
3. As Bactopia Tools devem estar disponíveis no [nf-core/modules](https://github.com/nf-core/modules).

:::tip[O Bactopia forneceu mais de 181 contribuições para a comunidade de bioinformática]
- 11 ferramentas independentes, cada uma disponível no Bioconda
- 30 novas receitas Conda, 46
  receitas atualizadas, e [mais de 2.000 pull requests do Bioconda revisados](https://github.com/bioconda/bioconda-recipes/pulls?q=is%3Apr+involves%3Arpetit3+is%3Aclosed).
- 68 contribuições para nf-core/modules
- 26 contribuições para outras ferramentas

Essas contribuições são para a comunidade em geral e não exigem que você use o Bactopia para aproveitá-las.
:::

## Ferramentas Independentes

Às vezes, ferramentas são desenvolvidas para aprimorar as capacidades do Bactopia, como o
[Dragonflye](https://github.com/rpetit3/dragonflye), que foi desenvolvido para adicionar
suporte ao Nanopore. Essas ferramentas são projetadas para funcionar como ferramentas
independentes. Abaixo estão 11 dessas ferramentas, originalmente criadas para o Bactopia,
que você também pode usar independentemente do Bactopia.

| Ferramenta | Descrição |
|------|-------------|
| [assembly-scan](https://github.com/rpetit3/assembly-scan) | Gera estatísticas básicas para uma montagem |
| [dragonflye](https://github.com/rpetit3/dragonflye) | Monta genomas de isolados bacterianos a partir de reads Nanopore |
| [fastq-dl](https://github.com/rpetit3/fastq-dl) | Baixa arquivos FASTQ dos repositórios SRA ou ENA. |
| [fastq-scan](https://github.com/rpetit3/fastq-scan) | Exibe estatísticas resumidas de FASTQ no formato JSON |
| [GOBLIN](https://github.com/rpetit3/goblin) | Gera proteínas confiáveis para complementar a anotação bacteriana |
| [pasty](https://github.com/rpetit3/pasty) | Uma ferramenta para sorogrupamento in silico de isolados de Pseudomonas aeruginosa |
| [pbptyper](https://github.com/rpetit3/pbptyper) | Tipador in silico de Proteína Ligante de Penicilina para Streptococcus pneumoniae |
| [pmga](https://github.com/rpetit3/pmga) | Um fork do PMGA para todas as espécies de Neisseria e Haemophilus influenzae |
| [shovill-se](https://github.com/rpetit3/shovill) | Um fork do Shovill que inclui suporte para reads de extremidade única |
| [staphopia-sccmec](https://github.com/rpetit3/vcf-annotator) | Uma versão independente do método de tipagem SCCmec do Staphopia |
| [vcf-annotator](https://github.com/staphopia/staphopia-sccmec) | Adiciona anotações biológicas a variantes em um arquivo VCF fornecido |

## Contribuições ao Bioconda

O Bactopia exige que as ferramentas sejam instaláveis com Conda para simplificar o processo
de instalação para os usuários. Esse requisito levou a um envolvimento mais profundo com a
comunidade Bioconda, não planejado, mas bem-vindo. O Bioconda é mais do que `conda install`;
é um recurso valioso que torna as ferramentas de bioinformática mais acessíveis à comunidade.
Toda vez que uma ferramenta é adicionada ao Bioconda, um contêiner Docker é criado pelo
[Biocontainers](https://biocontainers.pro/), e uma imagem Singularity é criada pelo
[Galaxy Project](https://galaxyproject.org/). Em essência, uma única receita contribui
significativamente para a comunidade em geral.

O Bactopia resultou em 30 novas receitas, 46 receitas atualizadas, e
[mais de 2.000 pull requests foram revisados](https://github.com/bioconda/bioconda-recipes/pulls?q=is%3Apr+involves%3Arpetit3+is%3Aclosed).

### Novas Receitas

O Bactopia levou à adição de 30 novas receitas ao
[Bioconda](https://bioconda.github.io/) e ao [conda-forge](https://conda-forge.org/).
Essas novas receitas permitem que os usuários comecem rapidamente a usar essas ferramentas
em suas próprias análises, e incluem:

| Ferramenta | Descrição | Pull Request  |
|------|-------------|---------------|
| [Aspera Connect](https://www.ibm.com/aspera/connect/) | cliente de transferência de alto desempenho | [anaconda/rpetit3](https://anaconda.org/rpetit3/aspera-connect) |
| [assembly-scan](https://github.com/rpetit3/assembly-scan) | Gera estatísticas básicas para uma montagem | [bioconda/bioconda-recipes#11425](https://github.com/bioconda/bioconda-recipes/pull/11425) |
| [bactopia](https://github.com/bactopia/bactopia) | Um pipeline flexível para análise completa de genomas bacterianos | [bioconda/bioconda-recipes#17434](https://github.com/bioconda/bioconda-recipes/pull/17434) |
| [Dragonflye](https://github.com/rpetit3/dragonflye) | Monta genomas de isolados bacterianos a partir de reads Nanopore | [bioconda/bioconda-recipes#29696](https://github.com/bioconda/bioconda-recipes/pull/29696) |
| [ena-dl](https://github.com/rpetit3/ena-dl) | Baixa arquivos FASTQ do ENA | [bioconda/bioconda-recipes#17354](https://github.com/bioconda/bioconda-recipes/pull/17354) |
| [EToKi](https://github.com/zheminzhou/EToKi) | todos os métodos relacionados ao Enterobase | [bioconda/bioconda-recipes#37069](https://github.com/bioconda/bioconda-recipes/pull/37069) |
| [executor](https://github.com/xolox/python-executor) | wrapper Python para subprocessos, amigável ao programador | [conda-forge/staged-recipes#9457](https://github.com/conda-forge/staged-recipes/pull/9457) |
| [fastq-dl](https://github.com/rpetit3/fastq-dl) | Baixa arquivos FASTQ dos repositórios SRA ou ENA. | [bioconda/bioconda-recipes#18252](https://github.com/bioconda/bioconda-recipes/pull/18252) |
| [fastq-scan](https://github.com/rpetit3/fastq-scan) | Exibe estatísticas resumidas de FASTQ no formato JSON | [bioconda/bioconda-recipes#11415](https://github.com/bioconda/bioconda-recipes/pull/11415) |
| [GenoTyphi](https://github.com/katholt/genotyphi) | atribui genótipos a genomas de *Salmonella* Typhi | [bioconda/bioconda-recipes#25674](https://github.com/bioconda/bioconda-recipes/pull/25674) |
| [GOBLIN](https://github.com/rpetit3/goblin) | Gera proteínas confiáveis para complementar a anotação bacteriana | [bioconda/bioconda-recipes#38922](https://github.com/bioconda/bioconda-recipes/pull/38922) |
| [illumina-cleanup](https://github.com/rpetit3/illumina-cleanup) | Um pipeline simples para pré-processamento de arquivos FASTQ Illumina | [bioconda/bioconda-recipes#11481](https://github.com/bioconda/bioconda-recipes/pull/11481) |
| [ISMapper](https://github.com/jhawkey/IS_mapper) | software de mapeamento de sequências de inserção | [bioconda/bioconda-recipes#14180](https://github.com/bioconda/bioconda-recipes/pull/14180) |
| [mashpit](https://github.com/tongzhouxu/mashpit) | Plataforma de vigilância baseada em sketch | [bioconda/bioconda-recipes#35199](https://github.com/bioconda/bioconda-recipes/pull/35199) |
| [NextPolish](https://github.com/Nextomics/NextPolish) | Polimento rápido e preciso de genomas gerados por reads longas | [bioconda/bioconda-recipes#36582](https://github.com/bioconda/bioconda-recipes/pull/36582) |
| [ParallelTask](https://github.com/moold/ParallelTask) | Um motor de tarefas paralelas simples e leve | [conda-forge/staged-recipes#19616](https://github.com/conda-forge/staged-recipes/pull/19616) |
| [ParallelTask](https://github.com/moold/ParallelTask) | Um motor de tarefas paralelas simples e leve | [conda-forge/staged-recipes#19616](https://github.com/conda-forge/staged-recipes/pull/19616) |
| [pasty](https://github.com/rpetit3/pasty) | Uma ferramenta para sorogrupamento in silico de isolados de Pseudomonas aeruginosa | [bioconda/bioconda-recipes#35930](https://github.com/bioconda/bioconda-recipes/pull/35930) |
| [pbptyper](https://github.com/rpetit3/pbptyper) | Tipador in silico de Proteína Ligante de Penicilina para Streptococcus pneumoniae | [bioconda/bioconda-recipes#36222](https://github.com/bioconda/bioconda-recipes/pull/36222) |
| [pHierCC](https://github.com/zheminzhou/pHierCC) | Agrupamento hierárquico de cgMLST | [bioconda/bioconda-recipes#37070](https://github.com/bioconda/bioconda-recipes/pull/37070) |
| [pmga](https://github.com/CDCgov/BMGAP) | Versão de linha de comando do PMGA (PubMLST Genome Annotator) | [bioconda/bioconda-recipes/#32801](https://github.com/bioconda/bioconda-recipes/pull/32801) |
| [property-manager](https://github.com/xolox/python-property-manager) | variantes de propriedades úteis para programação em Python | [conda-forge/staged-recipes#9442](https://github.com/conda-forge/staged-recipes/pull/9442) |
| [RFPlasmid](https://github.com/aldertzomer/RFPlasmid) | previsão de contigs de plasmídeos a partir de montagens | [bioconda/bioconda-recipes#25849](https://github.com/bioconda/bioconda-recipes/pull/25849) |
| [SerotypeFinder](https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/) | Identifica o sorotipo em isolados de E. coli total ou parcialmente sequenciados | [bioconda/bioconda-recipes#29718](https://github.com/bioconda/bioconda-recipes/pull/29718) |
| [shovill-se](https://github.com/rpetit3/shovill) | Um fork do Shovill que inclui suporte para reads de extremidade única | [bioconda/bioconda-recipes#26040](https://github.com/bioconda/bioconda-recipes/pull/26040) |
| [spaTyper](https://github.com/HCGB-IGTP/spaTyper) | método computacional para encontrar tipos *spa* | [bioconda/bioconda-recipes#26044](https://github.com/bioconda/bioconda-recipes/pull/26044) |
| [sra-human-scrubber](https://github.com/ncbi/sra-human-scrubber) | Identifica e remove reads humanas de arquivos FASTQ | [bioconda/bioconda-recipes#29926](https://github.com/bioconda/bioconda-recipes/pull/29926) |
| [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec) | Uma versão independente do método de tipagem SCCmec do Staphopia | [bioconda/bioconda-recipes#28214](https://github.com/bioconda/bioconda-recipes/pull/28214) |
| [tbl2asn-forever](https://github.com/rpetit3/tbl2asn-forever) | use o tbl2asn para sempre fingindo que ainda é 2019 | [bioconda/bioconda-recipes#20073](https://github.com/bioconda/bioconda-recipes/pull/20073) |
| [vcf-annotator](https://github.com/rpetit3/assembly-scan) | Adiciona anotações biológicas a variantes em um arquivo VCF fornecido | [bioconda/bioconda-recipes#13417](https://github.com/bioconda/bioconda-recipes/pull/13417) |

:::note[Cada receita recebe um contêiner Docker e Singularity]
Muitas vezes esquecido, é importante reiterar: toda receita adicionada ao Bioconda tem um
contêiner Docker criado pelo [Biocontainers](https://biocontainers.pro/), e um contêiner
Singularity criado pelo [Galaxy Project](https://galaxyproject.org/). Esses contêineres
permitem análises reproduzíveis com controle de versão.
:::

### Melhorias e Correções

Um problema comum com as receitas do Bioconda é que a ferramenta funciona bem em um ambiente
Conda, mas falha quando contêinerizada por diversos motivos. Quando esses problemas ocorrem
com uma ferramenta usada pelo Bactopia, um esforço é feito para melhorar ou corrigir a receita
do Bioconda. Abaixo está uma lista de correções e melhorias em algumas receitas do Bioconda:

| Ferramenta | Descrição | Pull Request  |
|------|-------------|---------------|
| [abriTAMR](https://github.com/MDU-PHL/abritamr) | fix amrfinderplus pinning in abritamr | [bioconda/bioconda-recipes#46714](https://github.com/bioconda/bioconda-recipes/pull/46714) |
| [Gubbins](https://github.com/nickjcroucher/gubbins) | adjust python pinning in gubbins | [bioconda/bioconda-recipes#46713](https://github.com/bioconda/bioconda-recipes/pull/46713) |
| [SISTR](https://github.com/phac-nml/sistr_cmd) | fix issue with sistr container | [bioconda/bioconda-recipes#46712](https://github.com/bioconda/bioconda-recipes/pull/46712) |
| [RGI](https://github.com/arpcard/rgi) | Update rgi pinning for pyrodigal | [bioconda/bioconda-recipes#46669](https://github.com/bioconda/bioconda-recipes/pull/46669) |
| [Snippy](https://github.com/tseemann/snippy) | pin tabix version in snippy | [bioconda/bioconda-recipes#46458](https://github.com/bioconda/bioconda-recipes/pull/46458) |
| [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) | Patch ncbi-genome-download recipe | [bioconda/bioconda-recipes#41640](https://github.com/bioconda/bioconda-recipes/pull/41640) |
| [GTDB-Tk](https://github.com/Ecogenomics/GTDBTk) | Update GTDB-tk recipe | [bioconda/bioconda-recipes#40333](https://github.com/bioconda/bioconda-recipes/pull/40333) |
| [mlst](https://github.com/tseemann/mlst) | update midas pinnings to match docs | [bioconda/bioconda-recipes#38826](https://github.com/bioconda/bioconda-recipes/pull/38826) |
| [MIDAS](https://github.com/snayfach/MIDAS) | update midas pinnings to match docs | [bioconda/bioconda-recipes#38566](https://github.com/bioconda/bioconda-recipes/pull/38566) |
| [smoove](https://github.com/brentp/smoove) | rebuild smoove container | [bioconda/bioconda-recipes#37394](https://github.com/bioconda/bioconda-recipes/pull/37394) |
| [fasta3](https://github.com/wrpearson/fasta36) | update fasta3 to latest version | [bioconda/bioconda-recipes#37306](https://github.com/bioconda/bioconda-recipes/pull/37306) |
| [pggb](https://github.com/pangenome/pggb) | Update pinnings in pggb | [bioconda/bioconda-recipes#35734](https://github.com/bioconda/bioconda-recipes/pull/35734) |
| [Nullarbor](https://github.com/tseemann/nullarbor) | Rebuild nullarbor container | [bioconda/bioconda-recipes#35687](https://github.com/bioconda/bioconda-recipes/pull/35687) |
| [GenoTyphi](https://github.com/katholt/genotyphi) | Update genotyphi recipe for mykrobe based analysis | [bioconda/bioconda-recipes#35388](https://github.com/bioconda/bioconda-recipes/pull/35388) |
| [Seroba](https://github.com/sanger-pathogens/seroba) | Add database to Seroba recipe | [bioconda/bioconda-recipes#35378](https://github.com/bioconda/bioconda-recipes/pull/35378) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | Update ariba dependencies for latest pymummer | [bioconda/bioconda-recipes#35383](https://github.com/bioconda/bioconda-recipes/pull/35383) |
| [pymummer](https://github.com/sanger-pathogens/pymummer) | patch pymummer recipe to use system/user TMP | [bioconda/bioconda-recipes#35379](https://github.com/bioconda/bioconda-recipes/pull/35379) |
| [PlasmidFinder](https://bitbucket.org/genomicepidemiology/plasmidfinder) | Update PlasmidFinder for better container support | [bioconda/bioconda-recipes#35314](https://github.com/bioconda/bioconda-recipes/pull/35314) |
| [GTDB-Tk](https://github.com/Ecogenomics/GTDBTk) | Allow GTDB-Tk database download with container | [bioconda/bioconda-recipes#35174](https://github.com/bioconda/bioconda-recipes/pull/35174) |
| [ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper) | update shigatyper recipe for better container support | [bioconda/bioconda-recipes#35161](https://github.com/bioconda/bioconda-recipes/pull/35161) |
| [FastANI](https://github.com/ParBLiSS/FastANI) | Remove fastani from build fail list | [bioconda/bioconda-recipes#33556](https://github.com/bioconda/bioconda-recipes/pull/33556) |
| [FastANI](https://github.com/ParBLiSS/FastANI) | update FastANI recipe | [bioconda/bioconda-recipes#33433](https://github.com/bioconda/bioconda-recipes/pull/33433) |
| [Prokka](https://github.com/tseemann/prokka) | Update Prokka bioperl pinning | [bioconda/bioconda-recipes#33411](https://github.com/bioconda/bioconda-recipes/pull/33411) |
| [SsuisSero](https://github.com/jimmyliu1326/SsuisSero) | update SsuisSero dependency | [bioconda/bioconda-recipes#33268](https://github.com/bioconda/bioconda-recipes/pull/33268) |
| [RGI](https://github.com/arpcard/rgi) | Improve RGI docker container | [bioconda/bioconda-recipes#33249](https://github.com/bioconda/bioconda-recipes/pull/33249) |
| [legsta](https://github.com/tseemann/legsta) | Improve dockerbuild for Legsta | [bioconda/bioconda-recipes#33246](https://github.com/bioconda/bioconda-recipes/pull/33246) |
| [fastq-scan](https://github.com/rpetit3/fastq-scan) | Update fastq-scan recipe to include jq | [bioconda/bioconda-recipes#32650](https://github.com/bioconda/bioconda-recipes/pull/32650) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | Patch ariba recipe with minor bug fixes | [bioconda/bioconda-recipes#32258](https://github.com/bioconda/bioconda-recipes/pull/32258) |
| [PIRATE](https://github.com/SionBayliss/PIRATE) | Update PIRATE recipe to include post-analysis scripts | [bioconda/bioconda-recipes#31629](https://github.com/bioconda/bioconda-recipes/pull/31629) |
| [ngmaster](https://github.com/MDU-PHL/ngmaster) | rebuild ngmaster to get docker container | [bioconda/bioconda-recipes#31376](https://github.com/bioconda/bioconda-recipes/pull/31376) |
| [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE) | add missing dependency for agrvate | [bioconda/bioconda-recipes#31035](https://github.com/bioconda/bioconda-recipes/pull/31035) |
| [spaTyper](https://github.com/HCGB-IGTP/spaTyper) | Patch spatyper for entrypoint support | [bioconda/bioconda-recipes#30824](https://github.com/bioconda/bioconda-recipes/pull/30824) |
| [spaTyper](https://github.com/HCGB-IGTP/spaTyper) | Patch spatyper for better container support | [bioconda/bioconda-recipes#30622](https://github.com/bioconda/bioconda-recipes/pull/30622) |
| [Kleborate](https://github.com/katholt/Kleborate) | Update kleborate recipe to build DB | [bioconda/bioconda-recipes#30582](https://github.com/bioconda/bioconda-recipes/pull/30582) |
| [cyvcf2](https://github.com/brentp/cyvcf2) | Loosen htslib version requirement for cyvcf2 | [bioconda/bioconda-recipes#30044](https://github.com/bioconda/bioconda-recipes/pull/30044) |
| [Kleborate](https://github.com/katholt/Kleborate) | Patch Kleborate's method for discovering Kaptive | [bioconda/bioconda-recipes#29623](https://github.com/bioconda/bioconda-recipes/pull/29623) |
| [spaTyper](https://github.com/HCGB-IGTP/spaTyper) | update spatyper - drop blake_sha256 requirement | [bioconda/bioconda-recipes#27321](https://github.com/bioconda/bioconda-recipes/pull/27321) |
| [ISMapper](https://github.com/jhawkey/IS_mapper/) | ISMapper - Fix BioPython pinning | [bioconda/bioconda-recipes#26599](https://github.com/bioconda/bioconda-recipes/pull/26599) |
| [CheckM](https://ecogenomics.github.io/CheckM/) | checkm-genome - fix broken pinning by older pysam version | [bioconda/bioconda-recipes#25856](https://github.com/bioconda/bioconda-recipes/pull/25856) |
| [ISMapper](https://github.com/jhawkey/IS_mapper/) | Update ISMapper - Pin BioPython version | [bioconda/bioconda-recipes#24314](https://github.com/bioconda/bioconda-recipes/pull/24314) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | Patches for third party links used by Ariba | [bioconda/bioconda-recipes#24010](https://github.com/bioconda/bioconda-recipes/pull/24010) |
| [Seroba](https://github.com/sanger-pathogens/seroba) | Add pysam pinning for Seroba | [bioconda/bioconda-recipes#17568](https://github.com/bioconda/bioconda-recipes/pull/17568) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | Update pysam pinning for Ariba | [bioconda/bioconda-recipes#17448](https://github.com/bioconda/bioconda-recipes/pull/17448) |
| [tbl2asn](https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2) | Previous version of tbl2asn has expired, updated to 25.7 | [bioconda/bioconda-recipes#16131](https://github.com/bioconda/bioconda-recipes/pull/16131) |
| [ISMapper](https://github.com/jhawkey/IS_mapper/) | Rebuild ismapper for GCC7 migration | [bioconda/bioconda-recipes#14276](https://github.com/bioconda/bioconda-recipes/pull/14276) |
| [MentaLiST](https://github.com/WGS-TB/MentaLiST) | MentaLiST v0.2.4 patch for Julia | [bioconda/bioconda-recipes#13137](https://github.com/bioconda/bioconda-recipes/pull/13137) |

## Contribuições ao nf-core/modules

Quando o Bactopia fez a transição para o Nextflow DSL2, isso abriu as portas para a adoção
de módulos do [nf-core/modules](https://github.com/nf-core/modules). Esses módulos permitem
que os usuários os integrem facilmente em seus próprios pipelines Nextflow DSL2. Para apoiar
essa integração, decidi exigir que cada Bactopia Tool tivesse um módulo correspondente
disponível no nf-core/modules. Se tal módulo não estiver disponível, ele será adicionado.

Ao adotar essa prática, foram feitas 68 contribuições ao
nf-core/modules na forma de novos módulos, atualizações de módulos e ajustes de testes.

| Ferramenta | Descrição | Pull Request  |
|------|-------------|---------------|
| [BTyper3](https://github.com/lmc297/BTyper3) | add module for btyper3 | [nf-core/modules#3817](https://github.com/nf-core/modules/pull/3817) |
| [abriTAMR](https://github.com/MDU-PHL/abritamr) | add module for abritamr_run | [nf-core/modules#3725](https://github.com/nf-core/modules/pull/3725) |
| [PneumoCaT](https://github.com/ukhsa-collaboration/PneumoCaT) | add module for pneumocat | [nf-core/modules#3592](https://github.com/nf-core/modules/pull/3592) |
| [STECFinder](https://github.com/LanLab/STECFinder) | add module for stecfinder | [nf-core/modules#2702](https://github.com/nf-core/modules/pull/2702) |
| [MIDAS](https://github.com/snayfach/MIDAS) | add module for midas/run | [nf-core/modules#2696](https://github.com/nf-core/modules/pull/2696) |
| [SRA Human Scrubber](https://github.com/ncbi/sra-human-scrubber) | add modules for sra-human-scrubber | [nf-core/modules#2694](https://github.com/nf-core/modules/pull/2694) |
| [ShigEiFinder](https://github.com/LanLab/ShigEiFinder) | add shigeifinder module | [nf-core/modules#2523](https://github.com/nf-core/modules/pull/2523) |
| [nf-core/modules](https://github.com/nf-core/modules) | fix a few tests after restructure | [nf-core/modules#2234](https://github.com/nf-core/modules/pull/2252) |
| [Biohansel](https://github.com/phac-nml/biohansel) | add biohansel module | [nf-core/modules#2234](https://github.com/nf-core/modules/pull/2234) |
| [pbptyper](https://github.com/rpetit3/pbptyper) | add pbptyper module | [nf-core/modules#2005](https://github.com/nf-core/modules/pull/2005) |
| [pasty](https://github.com/rpetit3/pasty) | add module for pasty | [nf-core/modules#2003](https://github.com/nf-core/modules/pull/2003) |
| [snippy-core](https://github.com/tseemann/snippy) | add snippy/core module | [nf-core/modules#1855](https://github.com/nf-core/modules/pull/1855) |
| [Mykrobe](https://github.com/Mykrobe-tools/mykrobe) | add module for mykrobe/predict | [nf-core/modules#1818](https://github.com/nf-core/modules/pull/1818) |
| [GenoTyphi](https://github.com/katholt/genotyphi) | add module for genotyphi/parse | [nf-core/modules#1818](https://github.com/nf-core/modules/pull/1818) |
| [Seroba](https://sanger-pathogens.github.io/seroba/) | add module for seroba | [nf-core/modules#1816](https://github.com/nf-core/modules/pull/1816) |
| [PlasmidFinder](https://bitbucket.org/genomicepidemiology/plasmidfinder) | add plasmidfinder module | [nf-core/modules#1773](https://github.com/nf-core/modules/pull/1773) |
| [mcroni](https://github.com/liampshaw/mcroni) | add mcroni module | [nf-core/modules#1750](https://github.com/nf-core/modules/pull/1750) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | add ariba module | [nf-core/modules#1731](https://github.com/nf-core/modules/pull/1731) |
| [snippy](https://github.com/tseemann/snippy) | add snippy module | [nf-core/modules#1643](https://github.com/nf-core/modules/pull/1643) |
| [ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper) | add shigatyper module | [nf-core/modules#1548](https://github.com/nf-core/modules/pull/1548) |
| [panaroo](https://github.com/gtonkinhill/panaroo) | add module for panaroo, fix pirate tests | [nf-core/modules#1444](https://github.com/nf-core/modules/pull/1444) |
| [Dragonflye](https://github.com/rpetit3/dragonflye) | Update dragonflye to latest version | [nf-core/modules#1442](https://github.com/nf-core/modules/pull/1442) |
| [Bakta](https://github.com/oschwengers/bakta) | update bakta to latest version (v1.4.0) | [nf-core/modules#1428](https://github.com/nf-core/modules/pull/1428) |
| [Roary](https://github.com/sanger-pathogens/Roary) | Update test.yml for Roary module | [nf-core/modules#1419](https://github.com/nf-core/modules/pull/1419) |
| [HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero) | add hpsuisero module | [nf-core/modules#1331](https://github.com/nf-core/modules/pull/1331) |
| [SsuisSero](https://github.com/jimmyliu1326/SsuisSero) | add ssuisero module | [nf-core/modules#1329](https://github.com/nf-core/modules/pull/1329) |
| [SISTR](https://github.com/phac-nml/sistr_cmd) | add sistr module | [nf-core/modules#1322](https://github.com/nf-core/modules/pull/1322) |
| [RGI](https://github.com/arpcard/rgi) | add rgi module | [nf-core/modules#1321](https://github.com/nf-core/modules/pull/1321) |
| [legsta](https://github.com/tseemann/legsta) | add legsta module | [nf-core/modules#1319](https://github.com/nf-core/modules/pull/1319) |
| [AMRFinder+](https://github.com/ncbi/amr) | add amrfindplus module | [nf-core/modules#1284](https://github.com/nf-core/modules/pull/1284) |
| [abricate](https://github.com/tseemann/abricate) | add abricate module | [nf-core/modules#1280](https://github.com/nf-core/modules/pull/1280) |
| [mobsuite/recon](https://github.com/phac-nml/mob-suite) | add mobsuite/recon module | [nf-core/modules#1270](https://github.com/nf-core/modules/pull/1270) |
| [mash/dist](https://github.com/marbl/Mash) | add mash/dist module | [nf-core/modules#1193](https://github.com/nf-core/modules/pull/1193) |
| [Kleborate](https://github.com/katholt/Kleborate) | Fix kleborate inputs | [nf-core/modules#1172](https://github.com/nf-core/modules/pull/1172) |
| [nf-core/modules](https://github.com/nf-core/modules) | fix test data path for ClonalFrameML,roary,pirate | [nf-core/modules#1085](https://github.com/nf-core/modules/pull/1085) |
| [Bakta](https://github.com/oschwengers/bakta) | add bakta module | [nf-core/modules#1085](https://github.com/nf-core/modules/pull/1085) |
| [nf-core/modules](https://github.com/nf-core/modules) | use underscores in anchors and references | [nf-core/modules#1080](https://github.com/nf-core/modules/pull/1080) |
| [Scoary](https://github.com/AdmiralenOla/Scoary) | add scoary module | [nf-core/modules#1034](https://github.com/nf-core/modules/pull/1034) |
| [emmtyper](https://github.com/MDU-PHL/emmtyper) | add emmtyper module | [nf-core/modules#1028](https://github.com/nf-core/modules/pull/1028) |
| [LisSero](https://github.com/MDU-PHL/LisSero) | add lissero module | [nf-core/modules#1026](https://github.com/nf-core/modules/pull/1026) |
| [ngmaster](https://github.com/MDU-PHL/ngmaster) | add ngmaster module | [nf-core/modules#1024](https://github.com/nf-core/modules/pull/1024) |
| [meningotype](https://github.com/MDU-PHL/meningotype) | add meningotype module | [nf-core/modules#1022](https://github.com/nf-core/modules/pull/1022) |
| [SeqSero2](https://github.com/denglab/SeqSero2) | add seqsero2 module | [nf-core/modules#1016](https://github.com/nf-core/modules/pull/1016) |
| [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) | add ncbi-genome-download module | [nf-core/modules#980](https://github.com/nf-core/modules/pull/980) |
| [ClonalFrameML](https://github.com/xavierdidelot/ClonalFrameML) | add clonalframeml module | [nf-core/modules#974](https://github.com/nf-core/modules/pull/974) |
| [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE) | Update agrvate version | [nf-core/modules#970](https://github.com/nf-core/modules/pull/970) |
| [ECTyper](https://github.com/phac-nml/ecoli_serotyping) | add ectyper module | [nf-core/modules#948](https://github.com/nf-core/modules/pull/948) |
| [TBProfiler](https://github.com/jodyphelan/TBProfiler) | add tbprofiler module | [nf-core/modules#947](https://github.com/nf-core/modules/pull/947) |
| [spaTyper](https://github.com/HCGB-IGTP/spaTyper) | Update spatyper module (cleanup debug)  | [nf-core/modules#938](https://github.com/nf-core/modules/pull/938) |
| [hicap](https://github.com/scwatts/hicap) | [fix] hicap module allow optional outputs | [nf-core/modules#937](https://github.com/nf-core/modules/pull/937) |
| [fastq-scan](https://github.com/rpetit3/fastq-scan) | add fastq-scan module | [nf-core/modules#935](https://github.com/nf-core/modules/pull/935) |
| [csvtk](https://github.com/shenwei356/csvtk) | patch output extension in csvtk/concat | [nf-core/modules#797](https://github.com/nf-core/modules/pull/797) |
| [csvtk](https://github.com/shenwei356/csvtk) | add csvtk/concat module | [nf-core/modules#785](https://github.com/nf-core/modules/pull/785) |
| [spaTyper](https://github.com/HCGB-IGTP/spaTyper) | add spatyper module | [nf-core/modules#784](https://github.com/nf-core/modules/pull/784) |
| [PIRATE](https://github.com/SionBayliss/PIRATE) | add pirate module | [nf-core/modules#777](https://github.com/nf-core/modules/pull/777) |
| [Roary](https://github.com/sanger-pathogens/Roary) | add roary module | [nf-core/modules#776](https://github.com/nf-core/modules/pull/776) |
| [ISMapper](https://github.com/jhawkey/IS_mapper/) | add ismapper module | [nf-core/modules#773](https://github.com/nf-core/modules/pull/773) |
| [hicap](https://github.com/scwatts/hicap) | add hicap module | [nf-core/modules#772](https://github.com/nf-core/modules/pull/772) |
| [mashtree](https://github.com/lskatz/mashtree) | add mashtree module | [nf-core/modules#767](https://github.com/nf-core/modules/pull/767) |
| [nf-core/modules](https://github.com/nf-core/modules) | update tests for 12 modules for new config | [nf-core/modules#758](https://github.com/nf-core/modules/pull/758) |
| [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE) | Update agrvate to v1.0.1 | [nf-core/modules#728](https://github.com/nf-core/modules/pull/728) |
| [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec) | add staphopia-sccmec module | [nf-core/modules#702](https://github.com/nf-core/modules/pull/702) |
| [Dragonflye](https://github.com/rpetit3/dragonflye) | add module for dragonflye | [nf-core/modules#633](https://github.com/nf-core/modules/pull/633) |
| [nf-core/modules](https://github.com/nf-core/modules) | update tests for 21 modules for new config | [nf-core/modules#384](https://github.com/nf-core/modules/pull/384) |
| [Prokka](https://github.com/tseemann/prokka) | Update Prokka modules - add process label | [nf-core/modules#350](https://github.com/nf-core/modules/pull/350) |
| [nf-core/modules](https://github.com/nf-core/modules) | README - Fix link describing process labels | [nf-core/modules#349](https://github.com/nf-core/modules/pull/349) |
| [Shovill](https://github.com/tseemann/shovill) | Update shovill module | [nf-core/modules#337](https://github.com/nf-core/modules/pull/337) |
| [Prokka](https://github.com/tseemann/prokka) | add prokka module | [nf-core/modules#298](https://github.com/nf-core/modules/pull/298) |

## Outras Contribuições

Além do Bioconda e do nf-core/modules, o Bactopia fez 26 contribuições a outras ferramentas, incluindo:

| Ferramenta | Descrição | Pull Request  |
|------|-------------|---------------|
| [MOB-suite](https://github.com/phac-nml/mob-suite) | fix hostrange() missing 1 required positional argument: 'database_directory' | [phac-nml/mob-suite#149](https://github.com/phac-nml/mob-suite/pull/149) |
| [bioconda-utils](https://github.com/bioconda/bioconda-utils) | chore: update change visibility action | [bioconda/bioconda-utils#873](https://github.com/bioconda/bioconda-utils/pull/873) |
| [Prokka](https://github.com/tseemann/prokka) | Convert Travis CI to Github Actions | [tseemann/prokka#662](https://github.com/tseemann/prokka/pull/662) |
| [bioconda-utils](https://github.com/bioconda/bioconda-utils) | chore: add CI to changevisibility of private containers | [bioconda/bioconda-utils#835](https://github.com/bioconda/bioconda-utils/pull/835) |
| [bioconda-containers](https://github.com/bioconda/bioconda-containers) | Patch - small fix on merge command and quay toggle visibility | [bioconda/bioconda-containers#54](https://github.com/bioconda/bioconda-containers/pull/54) |
| [Shigatyper](https://github.com/CFSAN-Biostatistics/shigatyper) | Incorporate patches from Bioconda | [CFSAN-Biostatistics/shigatyper#14](https://github.com/CFSAN-Biostatistics/shigatyper/pull/14) |
| [EToKi](https://github.com/lskatz/EToKi) | let tempfile determine where to put temp files | [lskatz/EToKi#2](https://github.com/lskatz/EToKi/pull/2) |
| [EToKi](https://github.com/lskatz/EToKi) | Allow multiple path parameters on the configure step | [lskatz/EToKi#1](https://github.com/lskatz/EToKi/pull/1) |
| [Seroba](https://github.com/sanger-pathogens/seroba) | let tempfile determine temp dir location | [sanger-pathogens/seroba#68](https://github.com/sanger-pathogens/seroba/pull/68) |
| [pymummer](https://github.com/sanger-pathogens/pymummer) | allow the user to specify temp dir or use the system default | [sanger-pathogens/pymummer#36](https://github.com/sanger-pathogens/pymummer/pull/36) |
| [ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper) | Fix install process | [CFSAN-Biostatistics/shigatyper#10](https://github.com/CFSAN-Biostatistics/shigatyper/pull/10) |
| [legsta](https://github.com/tseemann/legsta) | use grep -q to play nice with bioconda docker build | [tseemann/legsta#17](https://github.com/tseemann/legsta/pull/17) |
| [ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper) | Add single-end and ONT support, add GitHub Actions, update readme | [CFSAN-Biostatistics/shigatyper#9](https://github.com/CFSAN-Biostatistics/shigatyper/pull/9) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | Ignore comments column and drop Bio.Alphabet | [sanger-pathogens/ariba#319](https://github.com/sanger-pathogens/ariba/pull/319) |
| [BioContainers](https://github.com/BioContainers/multi-package-containers) | Add ClonalFrameML and maskrc-svg multipackage | [BioContainers/multi-package-containers#1923"](https://github.com/BioContainers/multi-package-containers/pull/1923) |
| [Kleborate](https://github.com/katholt/Kleborate) | Add --kaptive_path to specify path to kaptive data | [katholt/Kleborate#59](https://github.com/katholt/Kleborate/pull/59) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | fix SPAdes version capture | [sanger-pathogens/ariba#315](https://github.com/sanger-pathogens/ariba/pull/315) |
| [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE) | Fix for dots in sample names | [VishnuRaghuram94/AgrVATE#9](https://github.com/VishnuRaghuram94/AgrVATE/pull/9) |
| [PIRATE](https://github.com/SionBayliss/PIRATE) | Add minimum feature length option | [SionBayliss/PIRATE#53](https://github.com/SionBayliss/PIRATE/pull/53) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | Fix for changes in PubMLST url | [sanger-pathogens/ariba#305](https://github.com/sanger-pathogens/ariba/pull/305) |
| [Ariba](https://github.com/sanger-pathogens/ariba) | Solution 1: for fixing CARD download | [sanger-pathogens/ariba#302](https://github.com/sanger-pathogens/ariba/pull/302) |
| [bowtie2](https://github.com/BenLangmead/bowtie2) | Rename VERSION to BOWTIE2_VERSION | [BenLangmead/bowtie2#302](https://github.com/BenLangmead/bowtie2/pull/302) |
| [phyloFlash](https://github.com/HRGV/phyloFlash) | Improved single end support | [HRGV/phyloFlash#102](https://github.com/HRGV/phyloFlash/pull/102) |
| [ISMapper](https://github.com/jhawkey/IS_mapper) | set min_range and max_range args to be a float | [jhawkey/IS_mapper#38](https://github.com/jhawkey/IS_mapper/pull/38) |
| [maskrc-svg](https://github.com/kwongj/maskrc-svg) | Add requirements.txt for python modules | [kwongj/maskrc-svg#2](https://github.com/kwongj/maskrc-svg/pull/2) |
| [Shovill](https://github.com/tseemann/shovill) | Added shovill-se for processing single-end reads | [tseemann/shovill#105](https://github.com/tseemann/shovill/pull/105) |
