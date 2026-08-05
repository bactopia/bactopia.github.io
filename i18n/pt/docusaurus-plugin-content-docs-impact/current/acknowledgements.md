---
title: Acknowledgements
description: >-
  A comprehensive list of datasets and software packages utilized in Bactopia,
  complete with links and citations.
sidebar_position: 2
---

# Agradecimentos

Bactopia é verdadeiramente um caso de *"estar sobre os ombros de gigantes"*. Bactopia
atualmente integra mais de 159 datasets e pacotes de software. Praticamente
cada componente utilizado no Bactopia, desde o fluxo de trabalho até os datasets, os
pacotes de software e até mesmo o framework deste site, foi criado por outras pessoas
e disponibilizado gratuitamente ao público.

Gostaria de expressar pessoalmente minha enorme gratidão aos autores
desses pacotes de software e datasets públicos. Se você chegou até aqui, eu
devo a você uma cerveja (ou um café!) se nos encontrarmos pessoalmente.
Sério, muito obrigado!

:::info[Por favor, cite os datasets e ferramentas]
Se você utilizou o Bactopia em seu trabalho, certifique-se de citar os datasets
ou softwares que possa ter usado.
:::

## Influências

### nf-core

[nf-core](https://nf-co.re/) é um ótimo grupo de pessoas que voluntariam seu tempo para
criar um conjunto de pipelines de análise Nextflow curados. A [equipe do nf-core](https://nf-co.re/about)
desenvolveu práticas incríveis que acredito fortalecer muito a comunidade Nextflow
como um todo!

Frequentemente me perguntam: _O Bactopia algum dia vai fazer parte do nf-core?_

A resposta é: _Não, mas..._

O Bactopia foi adaptado do Staphopia, que precede o início do nf-core. À medida que tanto o nf-core
quanto o Bactopia cresceram, ficou claro que adicionar o Bactopia ao nf-core seria uma tarefa
difícil. A última oportunidade para isso provavelmente foi quando o Bactopia foi convertido para DSL2, mas
as Bactopia Tools provavelmente nunca se encaixariam no molde do nf-core.

_No entanto_, sempre que possível, tentei implementar as práticas do nf-core no Bactopia.
Alguns exemplos incluem:

1. Análise de argumentos baseada na biblioteca do nf-core
2. Todas as Bactopia Tools são adaptadas de módulos do nf-core
3. Testes implementados seguindo o padrão do nf-core/modules

Ao implementar essas práticas, acredito que o Bactopia se tornou um pipeline muito melhor. Por
isso sou muito grato à comunidade nf-core! Obrigado!

Ewels P, Peltzer A, Fillinger S, Patel H, Alneberg J, Wilm A, Garcia MU, Di Tommaso P, Nahnsen S [The nf-core framework for community-curated bioinformatics pipelines.](https://dx.doi.org/10.1038/s41587-020-0439-x) _Nat Biotechnol._ (2020)

## Tradução

As ferramentas e prompts de tradução utilizados para traduzir a documentação do Bactopia
foram adaptados do sistema de tradução do projeto
[Nextflow Training](https://github.com/nextflow-io/training)
([TRANSLATING.md](https://github.com/nextflow-io/training/blob/master/TRANSLATING.md)).
Todas as traduções são geradas e mantidas por IA usando
[Claude](https://www.anthropic.com/claude) da Anthropic. Obrigado à equipe do
Nextflow por disponibilizar abertamente sua infraestrutura de tradução!

## Datasets Públicos

Abaixo está uma lista de 17 datasets públicos que potencialmente
podem ter sido utilizados através do Bactopia ou das Bactopia Tools.

### Datasets de Referência do Ariba

Esses datasets estão disponíveis usando a função `getref` do Ariba. Você pode aprender
mais sobre essa função na [Wiki do Ariba](https://github.com/sanger-pathogens/ariba/wiki/Task:-getref).

1: **[ARG-ANNOT](http://en.mediterranee-infection.com/article.php?laref=283%26titre=arg-annot)**<br/>
Gupta SK, Padmanabhan BR, Diene SM, Lopez-Rojas R, Kempf M, Landraud L, Rolain J-M [ARG-ANNOT, a new bioinformatic tool to discover antibiotic resistance genes in bacterial genomes.](https://doi.org/10.1128/aac.01310-13) _Antimicrob. Agents Chemother_ 58, 212-220 (2014)

2: **[CARD](https://card.mcmaster.ca/)**<br/>
Alcock BP, Raphenya AR, Lau TTY, Tsang KK, Bouchard M, Edalatmand A, Huynh W, Nguyen A-L V, Cheng AA, Liu S, Min SY, Miroshnichenko A, Tran H-K, Werfalli RE, Nasir JA, Oloni M, Speicher DJ, Florescu A, Singh B, Faltyn M, Hernandez-Koutoucheva A, Sharma AN, Bordeleau E, Pawlowski AC, Zubyk HL, Dooley D, Griffiths E, Maguire F, Winsor GL, Beiko RG, Brinkman FSL, Hsiao WWL, Domselaar GV, McArthur AG [CARD 2020: antibiotic resistome surveillance with the comprehensive antibiotic resistance database.](https://doi.org/10.1093/nar/gkz935) _Nucleic acids research_ 48.D1, D517-D525 (2020)

3: **[EcOH](https://dx.doi.org/10.1099%2Fmgen.0.000064)**<br/>
Ingle DJ, Valcanis M, Kuzevski A, Tauschek M, Inouye M, Stinear T, Levine MM, Robins-Browne RM, Holt KE [In silico serotyping of E. coli from short read data identifies limited novel O-loci but extensive diversity of O:H serotype combinations within and between pathogenic lineages.](https://doi.org/10.1099/mgen.0.000064) _Microbial Genomics_, 2(7), e000064. (2016)

4: **[MEGARes](https://megares.meglab.org/)**<br/>
Lakin SM, Dean C, Noyes NR, Dettenwanger A, Ross AS, Doster E, Rovira P, Abdo Z, Jones KL, Ruiz J, Belk KE, Morley PS, Boucher C [MEGARes: an resistencia antimicrobiana database for high throughput sequencing.](https://doi.org/10.1093/nar/gkw1009) _Nucleic Acids Res._ 45, D574-D580 (2017)

5: **[MEGARes 2.0](https://megares.meglab.org/)**<br/>
Doster E, Lakin SM, Dean CJ, Wolfe C, Young JG, Boucher C, Belk KE, Noyes NR, Morley PS [MEGARes 2.0: a database for classification of antimicrobial drug, biocide and metal resistance determinants in metagenomic sequence data.](https://doi.org/10.1093/nar/gkz1010) _Nucleic Acids Research_, 48(D1), D561-D569. (2020)

6: **[NCBI Reference Gene Catalog](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA313047)**<br/>
Feldgarden M, Brover V, Haft DH, Prasad AB, Slotta DJ, Tolstoy I, Tyson GH, Zhao S, Hsu C-H, McDermott PF, Tadesse DA, Morales C, Simmons M, Tillman G, Wasilenko J, Folster JP, Klimke W [Validating the NCBI AMRFinder Tool and Resistance Gene Database Using resistencia antimicrobiana Genotype-Phenotype Correlations in a Collection of NARMS Isolates](https://doi.org/10.1128/AAC.00483-19). _Antimicrob. Agents Chemother._ (2019)

7: **[ResFinder](https://cge.food.dtu.dk//services/ResFinder/)**<br/>
Zankari E, Hasman H, Cosentino S, Vestergaard M, Rasmussen S, Lund O, Aarestrup FM, Larsen MV [Identification of acquired resistencia antimicrobiana genes.](https://doi.org/10.1093/jac/dks261) _J. Antimicrob. Chemother._ 67, 2640-2644 (2012)

8: **[SRST2](https://github.com/katholt/srst2)**<br/>
Inouye M, Dashnow H, Raven L-A, Schultz MB, Pope BJ, Tomita T, Zobel J, Holt KE [SRST2: Rapid genomic surveillance for public health and hospital microbiology labs.](https://doi.org/10.1186/s13073-014-0090-6) _Genome Med._ 6, 90 (2014)

9: **[VFDB](http://www.mgc.ac.cn/VFs/)**<br/>
Chen L, Zheng D, Liu B, Yang J, Jin Q [VFDB 2016: hierarchical and refined dataset for big data analysis--10 years on.](https://doi.org/10.1093/nar/gkv1239) _Nucleic Acids Res._ 44, D694-7 (2016)

10: **[VirulenceFinder](https://cge.food.dtu.dk/services/VirulenceFinder/)**<br/>
Joensen KG, Scheutz F, Lund O, Hasman H, Kaas RS, Nielsen EM, Aarestrup FM [Real-time whole-genome sequencing for routine typing, surveillance, and outbreak detection of verotoxigenic _Escherichia coli_.](https://doi.org/10.1128/jcm.03617-13) _J. Clin. Microbiol._ 52, 1501-1510 (2014)

### Datasets Minmer

1: **[Mash Refseq (release 88) Sketch](https://mash.readthedocs.io/en/latest/data.html)**<br/>
Ondov BD, Starrett GJ, Sappington A, Kostic A, Koren S, Buck CB, Phillippy AM [Mash Screen: high-throughput sequence containment estimation for genome discovery](https://doi.org/10.1186/s13059-019-1841-x) _Genome Biol_ 20, 232 (2019)

2: **[Sourmash Genbank LCA Signature](https://sourmash.readthedocs.io/en/latest/databases.html)**<br/>
Brown CT, Irber L [sourmash: a library for MinHash sketching of DNA](http://dx.doi.org/10.21105/joss.00027). _JOSS_ 1, 27 (2016)

### Outros Datasets

1: **[eggNOG 5.0 Database](http://eggnog.embl.de/)**<br/>
Huerta-Cepas J, Szklarczyk D, Heller D, Hernández-Plaza A, Forslund SK, Cook H, Mende DR, Letunic I, Rattei T, Jensen LJ, von Mering C, Bork P [eggNOG 5.0: a hierarchical, functionally and phylogenetically annotated orthology resource based on 5090 organisms and 2502 viruses.](https://doi.org/10.1093/nar/gky1085) _Nucleic Acids Res._ 47, D309-D314 (2019)

2: **[Genome Taxonomy Database](https://gtdb.ecogenomic.org/)**<br/>
Parks DH, Chuvochina M, Rinke C, Mussig AJ, Chaumeil P-A, Hugenholtz P [GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically consistent, rank normalized and complete genome-based taxonomy](https://doi.org/10.1093/nar/gkab776) _Nucleic Acids Research_ gkab776 (2021)

3: **[MOB-suite Database](https://github.com/phac-nml/mob-suite)**<br/>
Robertson J, Bessonov K, Schonfeld J, Nash JHE. [Universal whole-sequence-based plasmid typing and its utility to prediction of host range and epidemiological surveillance.](https://doi.org/10.1099/mgen.0.000435) _Microbial Genomics_, 6(10)(2020)

4: **[NCBI RefSeq Database](https://www.ncbi.nlm.nih.gov/refseq/)**<br/>
O'Leary NA, Wright MW, Brister JR, Ciufo S, Haddad D, McVeigh R, Rajput B, Robbertse B, Smith-White B, Ako-Adjei D, Astashyn A, Badretdin A, Bao Y, Blinkova O0, Brover V, Chetvernin V, Choi J, Cox E, Ermolaeva O, Farrell CM, Goldfarb T, Gupta T, Haft D, Hatcher E, Hlavina W, Joardar VS, Kodali VK, Li W, Maglott D, Masterson P, McGarvey KM, Murphy MR, O'Neill K, Pujar S, Rangwala SH, Rausch D, Riddick LD, Schoch C, Shkeda A, Storz SS, Sun H, Thibaud-Nissen F, Tolstoy I, Tully RE, Vatsan AR, Wallin C, Webb D, Wu W, Landrum MJ, Kimchi A, Tatusova T, DiCuccio M, Kitts P, Murphy TD, Pruitt KD [Reference sequence (RefSeq) database at NCBI: current status, taxonomic expansion, and functional annotation.](https://doi.org/10.1093/nar/gkv1189) _Nucleic Acids Res._ 44, D733-45 (2016)

5: **[PubMLST.org](https://pubmlst.org/)**<br/>
Jolley KA, Bray JE, Maiden MCJ [Open-access bacterial population genomics: BIGSdb software, the PubMLST.org website and their applications.](http://dx.doi.org/10.12688/wellcomeopenres.14826.1) _Wellcome Open Res_ 3, 124 (2018)


## Softwares Incluídos no Bactopia

Abaixo estão 141 pacotes de software utilizados (direta e indiretamente) pelo
Bactopia. Um link para a página do software, bem como a citação (quando disponível),
foram incluídos.

1: **[PlasmidFinder](https://bitbucket.org/genomicepidemiology/plasmidfinder)**<br/>
Identifica plasmídeos em isolados bacterianos sequenciados total ou parcialmente<br/>
Carattoli A, Zankari E, García-Fernández A, Voldby Larsen M, Lund O, Villa L, Møller Aarestrup F, Hasman H [In silico detection and typing of plasmids using PlasmidFinder and plasmid multilocus sequence typing.](https://doi.org/10.1128/AAC.02412-14) _Antimicrobial Agents and Chemotherapy_ 58(7), 3895-3903. (2014)

2: **[Abricate](https://github.com/tseemann/abricate)**<br/>
Triagem em massa de contigs para genes de resistência antimicrobiana e virulência<br/>
Seemann T [Abricate: mass screening of contigs for antimicrobial and virulence genes](https://github.com/tseemann/abricate) (GitHub)

3: **[abriTAMR](https://github.com/MDU-PHL/abritamr)**<br/>
Um pipeline para executar o AMRfinderPlus e consolidar os resultados em classes funcionais<br/>
Sherry NL, Horan KA, Ballard SA, Gonҫalves da Silva A, Gorrie CL, Schultz MB, Stevens K, Valcanis M, Sait ML, Stinear TP, Howden BP, and Seemann T [An ISO-certified genomics workflow for identification and surveillance of resistencia antimicrobiana.](https://doi.org/10.1038/s41467-022-35713-4) _Nature Communications_, 14(1), 60. (2023)

4: **[AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE)**<br/>
Identificação rápida do tipo do locus agr de _Staphylococcus aureus_ e variantes do operon agr.<br/>
Raghuram V. [AgrVATE: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.](https://github.com/VishnuRaghuram94/AgrVATE) (GitHub)

5: **[AMRFinderPlus](https://github.com/ncbi/amr)**<br/>
Encontra genes de resistência antimicrobiana adquiridos e algumas mutações pontuais em sequências de proteínas ou nucleotídeos montados.<br/>
Feldgarden M, Brover V, Haft DH, Prasad AB, Slotta DJ, Tolstoy I, Tyson GH, Zhao S, Hsu C-H, McDermott PF, Tadesse DA, Morales C, Simmons M, Tillman G, Wasilenko J, Folster JP, Klimke W [Validating the NCBI AMRFinder Tool and Resistance Gene Database Using resistencia antimicrobiana Genotype-Phenotype Correlations in a Collection of NARMS Isolates](https://doi.org/10.1128/AAC.00483-19). _Antimicrob. Agents Chemother._ (2019)

6: **[any2fasta](https://github.com/tseemann/any2fasta)**<br/>
Converte vários formatos de sequência para FASTA<br/>
Seemann T [any2fasta: Convert various sequence formats to FASTA](https://github.com/tseemann/any2fasta) (GitHub)

7: **[Aragorn](http://130.235.244.92/ARAGORN/Downloads/)**<br/>
Encontra características de RNA de transferência (tRNA)<br/>
Laslett D, Canback B [ARAGORN, a program to detect tRNA genes and tmRNA genes in nucleotide sequences.](https://doi.org/10.1093/nar/gkh152) _Nucleic Acids Res_. 32(1):11-6 (2004)

8: **[Ariba](https://github.com/sanger-pathogens/ariba)**<br/>
Identificação de Resistência Antimicrobiana por Montagem<br/>
Hunt M, Mather AE, Sánchez-Busó L, Page AJ, Parkhill J, Keane JA, Harris SR [ARIBA: rapid resistencia antimicrobiana genotyping directly from sequencing reads](http://dx.doi.org/10.1099/mgen.0.000131). _Microb Genom_ 3, e000131 (2017)

9: **[ART](https://www.niehs.nih.gov/research/resources/software/biostatistics/art/index.cfm)**<br/>
Um conjunto de ferramentas de simulação para gerar reads sintéticos de sequenciamento de próxima geração<br/>
Huang W, Li L, Myers JR, Marth GT [ART: a next-generation sequencing read simulator.](http://dx.doi.org/10.1093/bioinformatics/btr708) _Bioinformatics_ 28, 593-594 (2012)

10: **[assembly-scan](https://github.com/rpetit3/assembly-scan)**<br/>
Gera estatísticas básicas para uma montagem.<br/>
Petit III RA [assembly-scan: generate basic stats for an assembly](https://github.com/rpetit3/assembly-scan) (GitHub)

11: **[Bakta](https://github.com/oschwengers/bakta)**<br/>
Anotação rápida e padronizada de genomas bacterianos e plasmídeos<br/>
Schwengers O, Jelonek L, Dieckmann MA, Beyvers S, Blom J, Goesmann A [Bakta - rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.](https://doi.org/10.1099/mgen.0.000685) _Microbial Genomics_ 7(11) (2021)

12: **[Barrnap](https://github.com/tseemann/barrnap)**<br/>
Preditor de RNA ribossomal bacteriano<br/>
Seemann T [Barrnap: Bacterial ribosomal RNA predictor](https://github.com/tseemann/barrnap) (GitHub)

13: **[BBTools](https://jgi.doe.gov/data-and-tools/bbtools/)**<br/>
BBTools é um conjunto de ferramentas bioinformáticas rápidas e multithreaded projetadas para análise de dados de sequências de DNA e RNA.<br/>
Bushnell B [BBMap short read aligner, and other bioinformatic tools.](http://sourceforge.net/projects/bbmap/) (Link)

14: **[BCFtools](https://github.com/samtools/bcftools)**<br/>
Utilitários para chamada de variantes e manipulação de arquivos VCF e BCF.<br/>
Danecek P, Bonfield JK, Liddle J, Marshall J, Ohan V, Pollard MO, Whitwham A, Keane T, McCarthy SA, Davies RM, Li H [Twelve years of SAMtools and BCFtools](https://doi.org/10.1093/gigascience/giab008) _GigaScience_ Volume 10, Issue 2 (2021)

15: **[Bedtools](https://github.com/arq5x/bedtools2)**<br/>
Um poderoso conjunto de ferramentas para aritmética genômica.<br/>
Quinlan AR, Hall IM [BEDTools: a flexible suite of utilities for comparing genomic features](http://dx.doi.org/10.1093/bioinformatics/btq033). _Bioinformatics_ 26, 841-842 (2010)

16: **[BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi)**<br/>
Ferramenta de Busca por Alinhamento Local Básico<br/>
Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, Madden TL [BLAST+: architecture and applications](http://dx.doi.org/10.1186/1471-2105-10-421). _BMC Bioinformatics_ 10, 421 (2009)

17: **[Bowtie2](https://github.com/BenLangmead/bowtie2)**<br/>
Um alinhador de reads com gaps rápido e sensível<br/>
Langmead B, Salzberg SL [Fast gapped-read alignment with Bowtie 2.](http://dx.doi.org/10.1038/nmeth.1923) _Nat. Methods._ 9, 357-359 (2012)

18: **[Bracken](https://github.com/jenniferlu717/Bracken)**<br/>
Bracken é um método estatístico de alta precisão que calcula a abundância de espécies em sequências de DNA de amostras metagenômicas<br/>
Lu J, Breitwieser FP, Thielen P, and Salzberg SL [Bracken: estimating species abundance in metagenomics data.](https://doi.org/10.7717/peerj-cs.104) _PeerJ Computer Science_, 3, e104. (2017)

19: **[BTyper3](https://github.com/lmc297/BTyper3)**<br/>
Classificação taxonômica in silico de genomas do grupo _Bacillus cereus_ usando dados de sequenciamento de genoma completo<br/>
Carroll LM, Cheng RA, Kovac J [No Assembly Required: Using BTyper3 to Assess the Congruency of a Proposed Taxonomic Framework for the Bacillus cereus Group With Historical Typing Methods.](https://doi.org/10.3389/fmicb.2020.580691) _Frontiers in Microbiology_, 11, 580691. (2020)

20: **[BUSCO](https://gitlab.com/ezlab/busco)**<br/>
Avaliação da completude de montagens e anotações genômicas com Benchmarking Universal Single-Copy Orthologs (BUSCO)<br/>
Manni M, Berkeley MR, Seppey M, Simão FA, Zdobnov EM [BUSCO Update: Novel and Streamlined Workflows along with Broader and Deeper Phylogenetic Coverage for Scoring of Eukaryotic, Prokaryotic, and Viral Genomes.](https://doi.org/10.1093/molbev/msab199) _Molecular Biology and Evolution_ 38(10), 4647-4654. (2021)

21: **[BWA](https://github.com/lh3/bwa/)**<br/>
Alinhador Burrow-Wheeler para alinhamento de reads curtos<br/>
Li H [Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM](http://arxiv.org/abs/1303.3997). _arXiv_ [q-bio.GN] (2013)

22: **[CD-HIT](https://github.com/weizhongli/cdhit)**<br/>
Acelerado para agrupamento de dados de sequenciamento de próxima geração<br/>
Li W, Godzik A [Cd-hit: a fast program for clustering and comparing large sets of protein or nucleotide sequences](http://dx.doi.org/10.1093/bioinformatics/btl158). _Bioinformatics_ 22, 1658-1659 (2006)

23: **[CheckM](https://github.com/Ecogenomics/CheckM)**<br/>
Avalia a qualidade de genomas microbianos recuperados de isolados, células únicas e metagenomas<br/>
Parks DH, Imelfort M, Skennerton CT, Hugenholtz P, Tyson GW [CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes.](http://dx.doi.org/10.1101/gr.186072.114) _Genome Res_ 25, 1043-1055 (2015)

24: **[CheckM2](https://github.com/chklovski/CheckM2)**<br/>
Avaliação rápida da qualidade de bins genômicos usando aprendizado de máquina<br/>
Chklovksi A [Rapid assessment of genome bin quality using machine learning](https://github.com/chklovski/CheckM2) (GitHub)

25: **[ClermontTyping](https://github.com/happykhan/ClermonTyping)**<br/>
Método in silico fácil de usar e preciso para filotipagem de cepas do gênero _Escherichia_<br/>
Beghain J, Bridier-Nahmias A, Le Nagard H, Denamur E, Clermont O. [ClermonTyping: an easy-to-use and accurate in silico method for Escherichia genus strain phylotyping.](https://doi.org/10.1099/mgen.0.000192) Microbial Genomics, 4(7), e000192. (2018)

26: **[ClonalFramML](https://github.com/xavierdidelot/ClonalFrameML)**<br/>
Inferência eficiente de recombinação em genomas bacterianos completos<br/>
Didelot X, Wilson DJ [ClonalFrameML: Efficient Inference of Recombination in Whole Bacterial Genomes.](https://doi.org/10.1371/journal.pcbi.1004041) _PLoS Comput Biol_ 11(2) e1004041 (2015)

27: **[csvtk](https://bioinf.shenwei.me/csvtk/)**<br/>
Um toolkit CSV/TSV multiplataforma, eficiente e prático em Golang<br/>
Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)

28: **[deacon](https://github.com/bede/deacon)**<br/>
Filtragem de sequências de DNA acelerada por SIMD usando comparação baseada em minimizadores<br/>
Bede N. [deacon: SIMD-accelerated filtering of DNA sequences using minimizer-based comparison.](https://github.com/bede/deacon) (GitHub)

29: **[DefenseFinder](https://github.com/mdmparis/defense-finder)**<br/>
Busca sistemática de todos os sistemas anti-fago conhecidos.<br/>
Tesson F, Hervé A, Mordret E, Touchon M, d'Humières C, Cury J, Bernheim A [Systematic and quantitative view of the antiviral arsenal of prokaryotes.](https://doi.org/10.1038/s41467-022-30269-9) Nature Communications, 13(1), 2561. (2022)

30: **[DIAMOND](https://github.com/bbuchfink/diamond)**<br/>
Alinhador de sequências local compatível com BLAST e acelerado.<br/>
Buchfink B, Xie C, Huson DH [Fast and sensitive protein alignment using DIAMOND.](http://dx.doi.org/10.1038/nmeth.3176) _Nat. Methods._ 12, 59-60 (2015)

31: **[Dragonflye](https://github.com/rpetit3/dragonflye)**<br/>
Monta genomas de isolados bacterianos a partir de reads Nanopore.<br/>
Petit III RA [Dragonflye: Assemble bacterial isolate genomes from Nanopore reads.](https://github.com/rpetit3/dragonflye) (GitHub)

32: **[ECTyper](https://github.com/phac-nml/ecoli_serotyping)**<br/>
Predição in silico do sorotipo de _Escherichia coli_<br/>
Laing C, Bessonov K, Sung S, La Rose C [ECTyper - In silico prediction of _Escherichia coli_ serotype](https://github.com/phac-nml/ecoli_serotyping) (GitHub)

33: **[eggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper)**<br/>
Anotação funcional rápida em escala genômica por atribuição de ortologia<br/>
Huerta-Cepas J, Forslund K, Coelho LP, Szklarczyk D, Jensen LJ, von Mering C, Bork P [Fast Genome-Wide Functional Annotation through Orthology Assignment by eggNOG-Mapper.](http://dx.doi.org/10.1093/molbev/msx148) _Mol. Biol. Evol._ 34, 2115-2122 (2017)

34: **[emmtyper](https://github.com/MDU-PHL/emmtyper)**<br/>
Rotulador Automático de Isolados emm<br/>
Tan A, Seemann T, Lacey D, Davies M, Mcintyre L, Frost H, Williamson D, Gonçalves da Silva A [emmtyper - emm Automatic Isolate Labeller](https://github.com/MDU-PHL/emmtyper) (GitHub)

35: **[FastANI](https://github.com/ParBLiSS/FastANI)**<br/>
Estimativa rápida de similaridade de genoma completo (ANI)<br/>
Jain C, Rodriguez-R LM, Phillippy AM, Konstantinidis KT, Aluru S [High throughput ANI analysis of 90K prokaryotic genomes reveals clear species boundaries.](http://dx.doi.org/10.1038/s41467-018-07641-9) _Nat. Commun._ 9, 5114 (2018)

36: **[FastQC](https://github.com/s-andrews/FastQC)**<br/>
Uma ferramenta de análise de controle de qualidade para dados de sequenciamento de alto rendimento.<br/>
Andrews S [FastQC: a controle de qualidade tool for high throughput sequence data.](http://www.bioinformatics.babraham.ac.uk/projects/fastqc) (WebLink)

37: **[fastq-dl](https://github.com/rpetit3/fastq-dl)**<br/>
Baixa arquivos FASTQ dos repositórios SRA ou ENA.<br/>
Petit III RA [fastq-dl: Download FASTQ files from SRA or ENA repositories.](https://github.com/rpetit3/fastq-dl) (GitHub)

38: **[fastq-scan](https://github.com/rpetit3/fastq-scan)**<br/>
Gera estatísticas resumidas de FASTQ no formato JSON<br/>
Petit III RA [fastq-scan: generate summary statistics of input FASTQ sequences.](https://github.com/rpetit3/fastq-scan) (GitHub)

39: **[fastp](https://github.com/OpenGene/fastp)**<br/>
Uma ferramenta projetada para fornecer pré-processamento rápido e completo para arquivos FastQ<br/>
Chen S, Zhou Y, Chen Y, and Gu J [fastp: an ultra-fast all-in-one FASTQ preprocessor.](https://doi.org/10.1093/bioinformatics/bty560) _Bioinformatics_, 34(17), i884-i890. (2018)

40: **[FLASH](https://ccb.jhu.edu/software/FLASH/)**<br/>
Uma ferramenta rápida e precisa para mesclar reads paired-end.<br/>
Magoč T, Salzberg SL [FLASH: fast length adjustment of short reads to improve genome assemblies.](https://doi.org/10.1093/bioinformatics/btr507) _Bioinformatics_ 27.21 2957-2963 (2011)

41: **[Flye](https://github.com/fenderglass/Flye)**<br/>
Montador de novo para reads de sequenciamento de moléculas únicas usando grafos de repetição<br/>
Kolmogorov M, Yuan J, Lin Y, Pevzner P [Assembly of Long Error-Prone Reads Using Repeat Graphs](https://doi.org/10.1038/s41587-019-0072-8) _Nature Biotechnology_ (2019)

42: **[freebayes](https://github.com/ekg/freebayes)**<br/>
Descoberta de polimorfismos genéticos e genotipagem baseada em haplótipos bayesianos<br/>
Garrison E, Marth G [Haplotype-based variant detection from short-read sequencing.](https://arxiv.org/abs/1207.3907) arXiv preprint arXiv:1207.3907 [q-bio.GN] (2012)

43: **[GAMMA](https://github.com/rastanton/GAMMA)**<br/>
Avaliação Microbiana de Mutações em Alelos Gênicos<br/>
Stanton RA, Vlachos N, Halpin AL [GAMMA: a tool for the rapid identification, classification, and annotation of translated gene matches from sequencing data.](https://doi.org/10.1093/bioinformatics/btab607) _Bioinformatics_ (2021)

44: **[GenoTyphi](https://github.com/katholt/genotyphi)**<br/>
Atribui genótipos a genomas de _Salmonella_ Typhi com base em resultados do Mykrobe<br/>
Wong VK, Baker S, Connor TR, Pickard D, Page AJ, Dave J, Murphy N, Holliman R, Sefton A, Millar M, Dyson ZA, Dougan G, Holt KE, & International Typhoid Consortium. [An extended genotyping framework for Salmonella enterica serovar Typhi, the cause of human typhoid](https://doi.org/10.1038/ncomms12827) _Nature Communications_ 7, 12827. (2016)

45: **[GigaTyper](https://github.com/rpetit3/gigatyper)**<br/>
Executa todos os esquemas MLST disponíveis para uma espécie contra uma montagem<br/>
Petit III RA, Fearing T, Groves E [GigaTyper: Why choose one scheme when you can flex them all?](https://github.com/rpetit3/gigatyper) (GitHub)

46: **[GTDB-Tk](https://github.com/Ecogenomics/GTDBTk)**<br/>
Um toolkit para atribuir classificações taxonômicas objetivas a genomas bacterianos e arqueais<br/>
Chaumeil PA, Mussig AJ, Hugenholtz P, Parks DH [GTDB-Tk: a toolkit to classify genomes with the Genome Taxonomy Database.](https://doi.org/10.1093/bioinformatics/btz848) _Bioinformatics_ (2019)

47: **[Gubbins](https://github.com/nickjcroucher/gubbins)**<br/>
Análise filogenética rápida de grandes amostras de sequências de genoma bacteriano completo recombinante<br/>
Croucher NJ, Page AJ, Connor TR, Delaney AJ, Keane JA, Bentley SD, Parkhill J, Harris SR [Rapid phylogenetic analysis of large samples of recombinant bacterial whole genome sequences using Gubbins.](https://doi.org/10.1093/nar/gku1196) _Nucleic Acids Research_ 43(3), e15. (2015)

48: **[hicap](https://github.com/scwatts/hicap)**<br/>
Tipagem in silico do locus cap de _H. influenzae_<br/>
Watts SC, Holt KE [hicap: in silico serotyping of the Haemophilus influenzae capsule locus.](https://doi.org/10.1128/JCM.00190-19) _Journal of Clinical Microbiology_ JCM.00190-19 (2019)

49: **[HMMER](http://hmmer.org/)**<br/>
Análise de biosequências usando modelos ocultos de Markov de perfil<br/>
Eddy SR [Accelerated Profile HMM Searches.](https://doi.org/10.1371/journal.pcbi.1002195) _PLoS Comput. Biol._ 7, e1002195 (2011)

50: **[HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero)**<br/>
Sorotipagem rápida de _Haemophilus parasuis_<br/>
Lui J [HpsuisSero: Rapid _Haemophilus parasuis_ serotyping](https://github.com/jimmyliu1326/HpsuisSero) (GitHub)

51: **[Infernal](http://eddylab.org/infernal/)**<br/>
Busca em bancos de dados de sequências de DNA por similaridades de estrutura e sequência de RNA<br/>
Nawrocki EP, Eddy SR [Infernal 1.1: 100-fold faster RNA homology searches.](https://doi.org/10.1093/bioinformatics/btt509) _Bioinformatics_ 29(22), 2933-2935 (2013)

52: **[IQ-TREE](https://github.com/Cibiv/IQ-TREE)**<br/>
Software filogenômico eficiente por máxima verossimilhança<br/>
Nguyen L-T, Schmidt HA, von Haeseler A, Minh BQ [IQ-TREE: A fast and effective stochastic algorithm for estimating maximum likelihood phylogenies.](https://doi.org/10.1093/molbev/msu300) _Mol. Biol. Evol._ 32:268-274 (2015)

53: **[ModelFinder](https://github.com/Cibiv/IQ-TREE)**<br/>
Usado para seleção automática de modelos<br/>
Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS [ModelFinder - Fast model selection for accurate phylogenetic estimates.](https://doi.org/10.1038/nmeth.4285) _Nat. Methods_ 14:587-589 (2017)

54: **[UFBoot2](https://github.com/Cibiv/IQ-TREE)**<br/>
Usado para realizar bootstrap ultrarrápido<br/>
Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS [UFBoot2: Improving the ultrafast bootstrap approximation.](https://doi.org/10.1093/molbev/msx281) _Mol. Biol. Evol._ 35:518-522 (2018)

55: **[ISMapper](https://github.com/jhawkey/IS_mapper)**<br/>
Software para mapeamento de IS<br/>
Hawkey J, Hamidian M, Wick RR, Edwards DJ, Billman-Jacobe H, Hall RM, Holt KE [ISMapper: identifying transposase insertion sites in bacterial genomes from short read sequence data](http://dx.doi.org/10.1186/s12864-015-1860-2). _BMC Genomics_ 16, 667 (2015)

56: **[Kaptive](https://github.com/katholt/Kaptive)**<br/>
Loci de polissacarídeos de superfície para o complexo de espécies _Klebsiella pneumoniae_ e genomas de _Acinetobacter baumannii_<br/>
Wyres KL, Wick RR, Gorrie C, Jenney A, Follador R, Thomson NR, Holt KE [Identification of Klebsiella capsule synthesis loci from whole genome data.](https://doi.org/10.1099/mgen.0.000102) _Microbial genomics_ 2(12) (2016)

57: **[Kleborate](https://github.com/katholt/Kleborate)**<br/>
Ferramenta de genotipagem para _Klebsiella pneumoniae_ e seu complexo de espécies relacionadas<br/>
Lam MMC, Wick RR, Watts, SC, Cerdeira LT, Wyres KL, Holt KE [A genomic surveillance framework and genotyping tool for Klebsiella pneumoniae and its related species complex.](https://doi.org/10.1038/s41467-021-24448-3) _Nat Commun_ 12, 4188 (2021)

58: **[Kraken2](https://github.com/DerrickWood/kraken2)**<br/>
A segunda versão do sistema de classificação de sequências taxonômicas Kraken<br/>
Wood DE, Lu J, Langmead B [Improved metagenomic analysis with Kraken 2.](https://doi.org/10.1186/s13059-019-1891-0) *Genome Biology*, 20(1), 257. (2019)

59: **[Krona](https://github.com/marbl/Krona)**<br/>
Explore metagenomas e muito mais de forma interativa em um navegador web<br/>
Ondov BD, Bergman NH, and Phillippy AM [Interactive metagenomic visualization in a Web browser.](https://doi.org/10.1186/1471-2105-12-385) _BMC Bioinformatics_, 12, 385. (2011)

60: **[legsta](https://github.com/tseemann/legsta)**<br/>
Tipagem in silico baseada em sequências de _Legionella pneumophila_<br/>
Seemann T [legsta: In silico Legionella pneumophila Sequence Based Typing](https://github.com/tseemann/legsta) (GitHub)

61: **[Lighter](https://github.com/mourisl/Lighter)**<br/>
Corretor de erros de sequenciamento rápido e eficiente em memória<br/>
Song L, Florea L, Langmead B [Lighter: Fast and Memory-efficient Sequencing Error Correction without Counting](https://doi.org/10.1186/s13059-014-0509-9). _Genome Biol._ 15(11):509 (2014)

62: **[LisSero](https://github.com/MDU-PHL/LisSero)**<br/>
Predição de sorotipo _in silico_ para _Listeria monocytogenes_<br/>
Kwong J, Zhang J, Seeman T, Horan, K, Gonçalves da Silva A [LisSero - _In silico_ serotype prediction for _Listeria monocytogenes_](https://github.com/MDU-PHL/LisSero) (GitHub)

63: **[MAFFT](https://mafft.cbrc.jp/alignment/software/)**<br/>
Programa de alinhamento múltiplo para sequências de aminoácidos ou nucleotídeos<br/>
Katoh K, Standley DM [MAFFT multiple sequence alignment software version 7: improvements in performance and usability.](https://doi.org/10.1093/molbev/mst010) _Mol. Biol. Evol._ 30, 772-780 (2013)

64: **[Mash](https://github.com/marbl/Mash)**<br/>
Estimativa rápida de distância entre genomas e metagenomas usando MinHash<br/>
Ondov BD, Treangen TJ, Melsted P, Mallonee AB, Bergman NH, Koren S, Phillippy AM [Mash: fast genome and metagenome distance estimation using MinHash](http://dx.doi.org/10.1186/s13059-016-0997-x). _Genome Biol_ 17, 132 (2016)

65: **[Mash Screen](https://github.com/marbl/Mash)**<br/>
Estimativa de contenção de sequências de alto rendimento<br/>
Ondov BD, Starrett GJ, Sappington A, Kostic A, Koren S, Buck CB, Phillippy AM [Mash Screen: high-throughput sequence containment estimation for genome discovery](https://doi.org/10.1186/s13059-019-1841-x) _Genome Biol_ 20, 232 (2019)

66: **[Mashtree](https://github.com/lskatz/mashtree)**<br/>
Cria uma árvore usando distâncias Mash<br/>
Katz LS, Griswold T, Morrison S, Caravas J, Zhang S, den Bakker HC, Deng X, Carleton HA [Mashtree: a rapid comparison of whole genome sequence files.](https://doi.org/10.21105/joss.01762) _Journal of Open Source Software_, 4(44), 1762 (2019)

67: **[maskrc-svg](https://github.com/kwongj/maskrc-svg)**<br/>
Mascara recombinação detectada pelo ClonalFrameML ou Gubbins<br/>
Kwong J [maskrc-svg - Masks recombination as detected by ClonalFrameML or Gubbins and draws an SVG.](https://github.com/kwongj/maskrc-svg) (GitHub)

68: **[McCortex](https://github.com/mcveanlab/mccortex)**<br/>
Montagem de genoma de novo e chamada de variantes em múltiplas amostras<br/>
Turner I, Garimella KV, Iqbal Z, McVean G [Integrating long-range connectivity information into de Bruijn graphs.](http://dx.doi.org/10.1093/bioinformatics/bty157) _Bioinformatics_ 34, 2556-2565 (2018)

69: **[mcroni](https://github.com/liampshaw/mcroni)**<br/>
Scripts para encontrar e processar variantes de promotor upstream de mcr-1<br/>
Shaw L [mcroni: Scripts for finding and processing promoter variants upstream of mcr-1](https://github.com/liampshaw/mcroni) (GitHub)

70: **[Medaka](https://github.com/nanoporetech/medaka)**<br/>
Correção de sequências fornecida pela ONT Research<br/>
ONT Research [Medaka: Sequence correction provided by ONT Research](https://github.com/nanoporetech/medaka) (GitHub)

71: **[meningotype](https://github.com/MDU-PHL/meningotype)**<br/>
Sorotipagem in silico, finetyping e tipagem de sequências de antígenos Bexsero de _Neisseria meningitidis_<br/>
Kwong JC, Gonçalves da Silva A, Stinear TP, Howden BP, & Seemann T [meningotype: in silico typing for _Neisseria meningitidis_.](https://github.com/MDU-PHL/meningotype) (GitHub)

72: **[MEGAHIT](https://github.com/voutcn/megahit)**<br/>
Montador de (meta-)genoma ultrarrápido e eficiente em memória<br/>
Li D, Liu C-M, Luo R, Sadakane K, Lam T-W [MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph.](https://doi.org/10.1093/bioinformatics/btv033) _Bioinformatics_ 31.10 1674-1676 (2015)

73: **[mlst](https://github.com/tseemann/mlst)**<br/>
Verifica arquivos de contigs contra esquemas de tipagem PubMLST<br/>
Seemann T [mlst: scan contig files against PubMLST typing schemes](https://github.com/tseemann/mlst) (GitHub)

74: **[MIDAS](https://github.com/snayfach/MIDAS)**<br/>
Um pipeline integrado para estimar variação genômica em nível de cepa a partir de dados metagenômicos<br/>
Nayfach S, Rodriguez-Mueller B, Garud N, and Pollard KS [An integrated metagenomics pipeline for strain profiling reveals novel patterns of bacterial transmission and biogeography.](https://doi.org/10.1101/gr.201863.115) _Genome Research_, 26(11), 1612-1625. (2016)

75: **[MinCED](https://github.com/ctSkennerton/minced)**<br/>
Mineração de CRISPRs em Datasets Ambientais<br/>
Skennerton C [MinCED: Mining CRISPRs in Environmental Datasets](https://github.com/ctSkennerton/minced) (GitHub)

76: **[Miniasm](https://github.com/lh3/miniasm)**<br/>
Montagem de novo ultrarrápida para reads longos e ruidosos (sem etapa de consenso)<br/>
Li H [Miniasm: Ultrafast de novo assembly for long noisy reads](https://github.com/lh3/miniasm) (GitHub)

77: **[Minimap2](https://github.com/lh3/minimap2)**<br/>
Um alinhador par a par versátil para sequências nucleotídicas genômicas e spliced<br/>
Li H [Minimap2: pairwise alignment for nucleotide sequences.](https://doi.org/10.1093/bioinformatics/bty191) _Bioinformatics_ 34:3094-3100 (2018)

78: **[MOB-suite](https://github.com/phac-nml/mob-suite)**<br/>
Ferramentas de software para agrupamento, reconstrução e tipagem de plasmídeos a partir de montagens rascunho<br/>
Robertson J, Nash JHE [MOB-suite: software tools for clustering, reconstruction and typing of plasmids from draft assemblies.](https://doi.org/10.1099/mgen.0.000206) _Microbial Genomics_ 4(8). (2018)

79: **[Mykrobe](https://github.com/Mykrobe-tools/mykrobe)**<br/>
Predição de resistência a antibióticos em minutos<br/>
Hunt M, Bradley P, Lapierre SG, Heys S, Thomsit M, Hall MB, Malone KM, Wintringer P, Walker TM, Cirillo DM, Comas I, Farhat MR, Fowler P, Gardy J, Ismail N, Kohl TA, Mathys V, Merker M, Niemann S, Omar SV, Sintchenko V, Smith G, Supply P, Tahseen S, Wilcox M, Arandjelovic I, Peto TEA, Crook, DW, Iqbal Z [Antibiotic resistance prediction for Mycobacterium tuberculosis from genome sequence data with Mykrobe](https://doi.org/10.12688/wellcomeopenres.15603.1) _Wellcome Open Research_ 4, 191. (2019)

80: **[NanoPlot](https://github.com/wdecoster/NanoPlot)**<br/>
Scripts de visualização para dados de sequenciamento de reads longos<br/>
De Coster W, D'Hert S, Schultz DT, Cruts M, Van Broeckhoven C [NanoPack: visualizing and processing long-read sequencing data](https://doi.org/10.1093/bioinformatics/bty149) _Bioinformatics_ Volume 34, Issue 15 (2018)

81: **[Nanoq](https://github.com/esteinig/nanoq)**<br/>
Controle de qualidade mínimo e ágil para reads de nanopore em Rust<br/>
Steinig E [Nanoq: Minimal but speedy controle de qualidade for nanopore reads in Rust](https://github.com/esteinig/nanoq) (GitHub)

82: **[ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)**<br/>
Scripts para baixar genomas dos servidores FTP do NCBI<br/>
Blin K [ncbi-genome-download: Scripts to download genomes from the NCBI FTP servers](https://github.com/kblin/ncbi-genome-download) (GitHub)

83: **[Nextflow](https://github.com/nextflow-io/nextflow)**<br/>
Uma DSL para pipelines computacionais orientados a dados.<br/>
Di Tommaso P, Chatzou M, Floden EW, Barja PP, Palumbo E, Notredame C [Nextflow enables reproducible computational workflows.](https://www.nature.com/articles/nbt.3820.pdf?origin=ppub) _Nat. Biotechnol._ 35, 316-319 (2017)

84: **[nf-test](https://www.nf-test.com/)**<br/>
Um framework de testes simples para pipelines Nextflow<br/>
Forer L, Schönherr S [Improving the reliability, quality, and maintainability of bioinformatics pipelines with nf-test.](https://doi.org/10.1093/gigascience/giaf130) _GigaScience_ 14, giaf130 (2025)

85: **[ngmaster](https://github.com/MDU-PHL/ngmaster)**<br/>
Tipagem de sequências de múltiplos antígenos _in silico_ para _Neisseria gonorrhoeae_ (NG-MAST)<br/>
Kwong J, Gonçalves da Silva A, Schultz M, Seeman T [ngmaster - _In silico_ multi-antigen sequence typing for _Neisseria gonorrhoeae_ (NG-MAST)](https://github.com/MDU-PHL/ngmaster) (GitHub)

86: **[nhmmer](http://hmmer.org/)**<br/>
Busca de homologia de DNA com HMMs de perfil.<br/>
Wheeler TJ, Eddy SR [nhmmer: DNA homology search with profile HMMs.](https://doi.org/10.1093/bioinformatics/btt403) _Bioinformatics_ 29, 2487-2489 (2013)

87: **[Panaroo](https://github.com/gtonkinhill/panaroo)**<br/>
Um pipeline atualizado para investigação de pan-genoma<br/>
Tonkin-Hill G, MacAlasdair N, Ruis C, Weimann A, Horesh G, Lees JA, Gladstone RA, Lo S, Beaudoin C, Floto RA, Frost SDW, Corander J, Bentley SD, Parkhill J [Producing polished prokaryotic pangenomes with the Panaroo pipeline.](https://doi.org/10.1186/s13059-020-02090-4) _Genome Biology_ 21(1), 180. (2020)

88: **[pasty](https://github.com/rpetit3/pasty)**<br/>
Sorogrupamento in silico de isolados de _Pseudomonas aeruginosa_<br/>
Petit III RA [pasty: in silico serogrouping of _Pseudomonas aeruginosa_ isolates](https://github.com/rpetit3/pasty) (GitHub)

89: **[pbptyper](https://github.com/rpetit3/pbptyper)**<br/>
Tipador de Proteína de Ligação à Penicilina (PBP) para montagens de _Streptococcus pneumoniae_<br/>
Petit III RA [pbptyper: In silico Penicillin Binding Protein (PBP) typer for _Streptococcus pneumoniae_ assemblies](https://github.com/rpetit3/pbptyper) (GitHub)

90: **[PhiSpy](https://github.com/linsalrob/PhiSpy)**<br/>
Predição de profagos em genomas bacterianos<br/>
Akhter S, Aziz RK, and Edwards RA [PhiSpy: a novel algorithm for finding prophages in bacterial genomes that combines similarity- and composition-based strategies.](https://doi.org/10.1093/nar/gks406) _Nucleic Acids Research_, 40(16), e126. (2012)

91: **[Pigz](https://zlib.net/pigz/)**<br/>
Uma implementação paralela do gzip para máquinas modernas com múltiplos processadores e núcleos.<br/>
Adler M. [pigz: A parallel implementation of gzip for modern multi-processor, multi-core machines.](https://zlib.net/pigz/) _Jet Propulsion Laboratory_ (2015)

92: **[Pilon](https://github.com/broadinstitute/pilon/)**<br/>
Uma ferramenta automatizada para melhoria de montagem genômica e detecção de variantes<br/>
Walker BJ, Abeel T,  Shea T, Priest M, Abouelliel A, Sakthikumar S, Cuomo CA, Zeng Q, Wortman J, Young SK, Earl AM [Pilon: an integrated tool for comprehensive microbial variant detection and genome assembly improvement.](https://doi.org/10.1371/journal.pone.0112963) _PloS one_ 9.11 e112963 (2014)

93: **[PIRATE](http://github.com/SionBayliss/PIRATE)**<br/>
Uma caixa de ferramentas para análise de pan-genoma e avaliação de limiares.<br/>
Bayliss SC, Thorpe HA, Coyle NM, Sheppard SK, Feil EJ [PIRATE: A fast and scalable pangenomics toolbox for clustering diverged orthologues in bacteria.](https://doi.org/10.1093/gigascience/giz119) _Gigascience_ 8 (2019)

94: **[PneumoCaT](https://github.com/ukhsa-collaboration/PneumoCaT)**<br/>
Ferramenta de Tipagem Capsular Pneumocócica para dados de NGS<br/>
Kapatai G, Sheppard CL, Al-Shahib A, Litt DJ, Underwood AP, Harrison TG, and Fry NK [Whole genome sequencing of Streptococcus pneumoniae: development, evaluation and verification of targets for serogroup and serotype prediction using an automated pipeline.](https://doi.org/10.7717/peerj.2477) PeerJ, 4, e2477. (2016)

95: **[Porechop](https://github.com/rrwick/Porechop)**<br/>
Trimmagem de adaptadores para reads Oxford Nanopore<br/>
Wick RR, Judd LM, Gorrie CL, Holt KE. [Completing bacterial genome assemblies with multiplex MinION sequencing.](https://doi.org/10.1099/mgen.0.000132) _Microb Genom._ 3(10):e000132 (2017)

96: **[pplacer](https://github.com/matsen/pplacer)**<br/>
Posicionamento filogenético e análise downstream<br/>
Matsen FA, Kodner RB, Armbrust EV [pplacer: linear time maximum-likelihood and Bayesian phylogenetic placement of sequences onto a fixed reference tree.](https://doi.org/10.1186/1471-2105-11-538) _BMC Bioinformatics_ 11, 538 (2010)

97: **[Prodigal](https://github.com/hyattpd/Prodigal)**<br/>
Predição rápida e confiável de genes codificadores de proteínas para genomas procarióticos.<br/>
Hyatt D, Chen G-L, LoCascio PF, Land ML, Larimer FW, Hauser LJ [Prodigal: prokaryotic gene recognition and translation initiation site identification.](https://doi.org/10.1186/1471-2105-11-119) _BMC Bioinformatics_ 11.1 119 (2010)

98: **[Prokka](https://github.com/tseemann/prokka)**<br/>
Anotação rápida de genomas procarióticos<br/>
Seemann T [Prokka: rapid prokaryotic genome annotation](http://dx.doi.org/10.1093/bioinformatics/btu153) _Bioinformatics_ 30, 2068-2069 (2014)

99: **[QUAST](http://quast.sourceforge.net/)**<br/>
Ferramenta de Avaliação de Qualidade para Genomas<br/>
Gurevich A, Saveliev V, Vyahhi N, Tesler G [QUAST: quality assessment tool for genome assemblies.](http://dx.doi.org/10.1093/bioinformatics/btt086) _Bioinformatics_ 29, 1072-1075 (2013)

100: **[Racon](https://github.com/lbcb-sci/racon)**<br/>
Módulo de consenso ultrarrápido para montagem de genoma de novo bruto a partir de reads longos não corrigidos<br/>
Vaser R, Sović I, Nagarajan N, Šikić M [Fast and accurate de novo genome assembly from long uncorrected reads.](http://dx.doi.org/10.1101/gr.214270.116) _Genome Res_ 27, 737-746 (2017)

101: **[Rasusa](https://github.com/mbhall88/rasusa)**<br/>
Subamostragem aleatória de reads de sequenciamento para uma cobertura especificada<br/>
Hall MB [Rasusa: Randomly subsample sequencing reads to a specified coverage.](https://doi.org/10.5281/zenodo.3731394) (2019).

102: **[Raven](https://github.com/lbcb-sci/raven)**<br/>
Montador de genoma de novo para reads longos não corrigidos<br/>
Vaser R, Šikić M [Time- and memory-efficient genome assembly with Raven.](https://doi.org/10.1038/s43588-021-00073-4) _Nat Comput Sci_ 1, 332-336 (2021)

103: **[Resistance Gene Identifier (RGI)](https://github.com/arpcard/rgi)**<br/>
Software para predizer resistomas a partir de dados de proteínas ou nucleotídeos, com base em modelos de homologia e SNP.<br/>
Alcock BP, Raphenya AR, Lau TTY, Tsang KK, Bouchard M, Edalatmand A, Huynh W, Nguyen A-L V, Cheng AA, Liu S, Min SY, Miroshnichenko A, Tran H-K, Werfalli RE, Nasir JA, Oloni M, Speicher DJ, Florescu A, Singh B, Faltyn M, Hernandez-Koutoucheva A, Sharma AN, Bordeleau E, Pawlowski AC, Zubyk HL, Dooley D, Griffiths E, Maguire F, Winsor GL, Beiko RG, Brinkman FSL, Hsiao WWL, Domselaar GV, McArthur AG [CARD 2020: antibiotic resistome surveillance with the comprehensive antibiotic resistance database.](https://doi.org/10.1093/nar/gkz935) _Nucleic acids research_ 48.D1, D517-D525 (2020)

104: **[RNAmmer](http://www.cbs.dtu.dk/services/RNAmmer/)**<br/>
Anotação consistente e rápida de genes de RNA ribossomal<br/>
Lagesen K, Hallin P, Rødland EA, Stærfeldt H-H, Rognes T, Ussery DW [RNAmmer: consistent annotation of rRNA genes in genomic sequences.](https://dx.doi.org/10.1093%2Fnar%2Fgkm160) _Nucleic Acids Res_ 35.9: 3100-3108 (2007)

105: **[Roary](https://github.com/sanger-pathogens/Roary)**<br/>
Análise rápida e em grande escala de pan-genoma procariótico<br/>
Page AJ, Cummins CA, Hunt M, Wong VK, Reuter S, Holden MTG, Fookes M, Falush D, Keane JA, Parkhill J [Roary: rapid large-scale prokaryote pan genome analysis.](https://doi.org/10.1093/bioinformatics/btv421) _Bioinformatics_ 31, 3691-3693 (2015)

106: **[samclip](https://github.com/tseemann/samclip)**<br/>
Filtra arquivos SAM para alinhamentos com clipping suave e rígido<br/>
Seemann T [Samclip: Filter SAM file for soft and hard clipped alignments](https://github.com/tseemann/samclip) (GitHub)

107: **[Samtools](https://github.com/samtools/samtools)**<br/>
Ferramentas para manipulação de dados de sequenciamento de próxima geração<br/>
Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R [The Sequence Alignment/Map format and SAMtools](http://dx.doi.org/10.1093/bioinformatics/btp352). _Bioinformatics_ 25, 2078-2079 (2009)

108: **[sccmec](https://github.com/rpetit3/sccmec)**<br/>
Uma ferramenta para tipagem de cassetes SCCmec em montagens.<br/>
Petit III RA, Read TD [sccmec: A tool for typing SCCmec cassettes in assemblies](https://github.com/rpetit3/sccmec) (GitHub)

109: **[Scoary](https://github.com/AdmiralenOla/Scoary)**<br/>
Estudos de associação em escala de pan-genoma<br/>
Brynildsrud O, Bohlin J, Scheffer L, Eldholm V [Rapid scoring of genes in microbial pan-genoma-wide association studies with Scoary.](https://doi.org/10.1186/s13059-016-1108-8) _Genome Biol._ 17:238 (2016)

110: **[SeqSero2](https://github.com/denglab/SeqSero2)**<br/>
Predição do sorotipo de Salmonella a partir de dados de sequenciamento de genoma<br/>
Zhang S, Den-Bakker HC, Li S, Dinsmore BA, Lane C, Lauer AC, Fields PI, Deng X. [SeqSero2: rapid and improved Salmonella serotype determination using whole genome sequencing data.](https://doi.org/10.1128/AEM.01746-19) _Appl Environ Microbiology_ 85(23):e01746-19 (2019)

111: **[Seqtk](https://github.com/lh3/seqtk)**<br/>
Uma ferramenta rápida e leve para processar sequências no formato FASTA ou FASTQ.<br/>
Li H [Toolkit for processing sequences in FASTA/Q formats](https://github.com/lh3/seqtk) (GitHub)

112: **[Seroba](https://github.com/sanger-pathogens/seroba)**<br/>
Pipeline baseado em k-mer para identificar o sorotipo de _Streptococcus pneumoniae_ a partir de reads de NGS Illumina<br/>
Epping L, van Tonder AJ, Gladstone RA, The Global Pneumococcal Sequencing Consortium, Bentley SD, Page AJ, Keane JA [SeroBA: rapid high-throughput serotyping of Streptococcus pneumoniae from whole genome sequence data.](https://doi.org/10.1099/mgen.0.000186) _Microbial Genomics_, 4(7) (2018)

113: **[shigapass](https://github.com/imanyass/ShigaPass)**<br/>
Uma ferramenta in silico para predizer sorotipos de Shigella<br/>
Yassine I, Hansen EE, Lefèvre S, Ruckly C, Carle I, Lejay-Collin M, Fabre L, Rafei R, Pardos de la Gandara M, Daboussi F, Shahin A, Weill FX [ShigaPass: an in silico tool predicting Shigella serotypes from whole-genome sequencing assemblies.](https://doi.org/10.1099%2Fmgen.0.000961) _Microb Genomics_ 9(3) (2023)

114: **[ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper)**<br/>
Sorotipo de Shigella a partir de reads Illumina ou Oxford Nanopore<br/>
Wu Y, Lau HK, Lee T, Lau DK, Payne J [In Silico Serotyping Based on Whole-Genome Sequencing Improves the Accuracy of Shigella Identification.](https://doi.org/10.1128/AEM.00165-19) *Applied and Environmental Microbiology*, 85(7). (2019)

115: **[ShigEiFinder](https://github.com/LanLab/ShigEiFinder)**<br/>
Ferramenta de sorotipagem de Shigella e EIEC informada por cluster a partir de reads Illumina e montagens<br/>
Zhang X, Payne M, Nguyen T, Kaur S, Lan R [Cluster-specific gene markers enhance Shigella and enteroinvasive Escherichia coli in silico serotyping.](https://doi.org/10.1099/mgen.0.000704) Microbial Genomics, 7(12). (2021)

116: **[Shovill](https://github.com/tseemann/shovill)**<br/>
Montagem mais rápida de reads Illumina<br/>
Seemann T [Shovill: De novo assembly pipeline for Illumina paired reads](https://github.com/tseemann/shovill) (GitHub)

117: **[Shovill-SE](https://github.com/rpetit3/shovill)**<br/>
Um fork do Shovill que inclui suporte para reads single-end.<br/>
Petit III RA [Shovill-SE: A fork of Shovill that includes support for single end reads.](https://github.com/rpetit3/shovill) (GitHub)

118: **[SignalP](http://www.cbs.dtu.dk/services/SignalP-4.0/)**<br/>
Encontra características de peptídeo sinal em CDS<br/>
Petersen TN, Brunak S, von Heijne G, Nielsen H [SignalP 4.0: discriminating signal peptides from transmembrane regions.](https://doi.org/10.1038/nmeth.1701) _Nature methods_ 8.10: 785 (2011)

119: **[SISTR](https://github.com/phac-nml/sistr_cmd)**<br/>
Ferramenta de linha de comando SISTR (Salmonella In Silico Typing Resource)<br/>
Yoshida CE, Kruczkiewicz P, Laing CR, Lingohr EJ, Gannon VPJ, Nash JHE, Taboada EN [The Salmonella In Silico Typing Resource (SISTR): An Open Web-Accessible Tool for Rapidly Typing and Subtyping Draft Salmonella Genome Assemblies.](https://doi.org/10.1371/journal.pone.0147101) _PloS One_, 11(1), e0147101. (2016)

120: **[sizemeup](https://github.com/rpetit3/sizemeup)**<br/>
Uma ferramenta simples para recuperar o tamanho do genoma de um determinado nome de espécie ou ID taxonômico<br/>
Petit III RA [sizemeup: A simple tool to retrieve the genome size for a given species name or tax ID](https://github.com/rpetit3/sizemeup) (GitHub)

121: **[SKESA](https://github.com/ncbi/SKESA)**<br/>
Extensão Estratégica de Kmer para Montagens Escrupulosas<br/>
Souvorov A, Agarwala R, Lipman DJ [SKESA: strategic k-mer extension for scrupulous assemblies.](https://doi.org/10.1186/s13059-018-1540-z) _Genome Biology_ 19:153 (2018)

122: **[Snippy](https://github.com/tseemann/snippy)**<br/>
Chamada rápida de variantes haploides e alinhamento do genoma central<br/>
Seemann T [Snippy: fast bacterial chamada de variantes from NGS reads](https://github.com/tseemann/snippy) (GitHub)

123: **[SnpEff](http://snpeff.sourceforge.net/)**<br/>
Caixa de ferramentas para anotação de variantes genômicas e predição de efeito funcional.<br/>
Cingolani P, Platts A, Wang LL, Coon M, Nguyen T, Wang L, Land SJ, Lu X, Douglas M [A program for annotating and predicting the effects of single nucleotide polymorphisms, SnpEff: SNPs in the genome of Drosophila melanogaster strain w1118; iso-2; iso-3.](https://doi.org/10.4161/fly.19695) _Fly_ 6(2), 80-92 (2012)

124: **[snp-dists](https://github.com/tseemann/snp-dists)**<br/>
Matriz de distância de SNP par a par a partir de um alinhamento de sequências FASTA<br/>
Seemann T [snp-dists - Pairwise SNP distance matrix from a FASTA sequence alignment.](https://github.com/tseemann/snp-dists) (GitHub)

125: **[Sourmash](https://github.com/dib-lab/sourmash)**<br/>
Calcula e compara assinaturas MinHash para conjuntos de dados de DNA.<br/>
Brown CT, Irber L [sourmash: a library for MinHash sketching of DNA](http://dx.doi.org/10.21105/joss.00027). _JOSS_ 1, 27 (2016)

126: **[SPAdes](https://github.com/ablab/spades)**<br/>
Um toolkit de montagem contendo vários pipelines de montagem.<br/>
Bankevich A, Nurk S, Antipov D, Gurevich AA, Dvorkin M, Kulikov AS, Lesin VM, Nikolenko SI, Pham S, Prjibelski AD, Pyshkin AV, Sirotkin AV, Vyahhi N, Tesler G, Alekseyev MA, Pevzner PA [SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing.](https://doi.org/10.1089/cmb.2012.0021) _Journal of computational biology_ 19.5 455-477 (2012)

127: **[spaTyper](https://github.com/HCGB-IGTP/spaTyper)**<br/>
Método computacional para encontrar tipos spa.<br/>
Sanchez-Herrero JF, and Sullivan M [spaTyper: Staphylococcal protein A (spa) characterization pipeline](http://doi.org/10.5281/zenodo.4063625). Zenodo. (2020)

128: **[spaTyper Database](https://cge.food.dtu.dk/services/spatyper/)**<br/>
Banco de dados usado pelo spaTyper<br/>
Harmsen D, Claus H, Witte W, Rothgänger J, Claus H, Turnwald D, and Vogel U [Typing of methicillin-resistant _Staphylococcus aureus_ in a university hospital setting using a novel software for spa-repeat determination and database management.](https://doi.org/10.1128/jcm.41.12.5442-5448.2003) _J. Clin. Microbiol._ 41:5442-5448 (2003)

129: **[SRA Human Scrubber](https://github.com/ncbi/sra-human-scrubber)**<br/>
Uma ferramenta SRA que recebe como entrada um arquivo fastq local de uma amostra de infecção clínica, identifica e remove qualquer read humano significativo, e gera o arquivo fastq editado (limpo) que pode ser usado com segurança para submissão ao SRA<br/>
Katz KS, Shutov O, Lapoint R, Kimelman M, Brister JR, and O'Sullivan C [STAT: a fast, scalable, MinHash-based k-mer tool to assess Sequence Read Archive next-generation sequence submissions.](https://doi.org/10.1186/s13059-021-02490-0) _Genome Biology_, 22(1), 270 (2021)

130: **[SsuisSero](https://github.com/jimmyliu1326/SsuisSero)**<br/>
Sorotipagem rápida de _Streptococcus suis_<br/>
Lui J [SsuisSero: Rapid _Streptococcus suis_ serotyping](https://github.com/jimmyliu1326/SsuisSero) (GitHub)

131: **[StaphSCAN](https://github.com/riccabolla/StaphSCAN)**<br/>
Análise de vigilância baseada em genoma de _Staphylococcus aureus_<br/>
Bollini R [StaphSCAN (v0.3.0).](https://github.com/riccabolla/StaphSCAN) Zenodo (2026)

132: **[staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec)**<br/>
Uma versão standalone do método de tipagem SCCmec do Staphopia.<br/>
Petit III RA, Read TD [_Staphylococcus aureus_ viewed from the perspective of 40,000+ genomes.](http://dx.doi.org/10.7717/peerj.5261) _PeerJ_ 6, e5261 (2018)

133: **[STECFinder](https://github.com/LanLab/STECFinder)**<br/>
Agrupamento e sorotipagem de _E. coli_ produtora de toxina Shiga (STEC) usando marcadores genômicos específicos de cluster<br/>
Zhang X, Payne M, Kaur S, and Lan R [Improved Genomic Identification, Clustering, and Serotyping of Shiga Toxin-Producing Escherichia coli Using Cluster/Serotype-Specific Gene Markers.](https://doi.org/10.3389/fcimb.2021.772574) _Frontiers in Cellular and Infection Microbiology_, 11, 772574. (2021)

134: **[Sylph](https://github.com/bluenote-1/sylph)**<br/>
Perfilamento taxonômico ultrarrápido e estimativa de contenção para dados metagenômicos<br/>
Shaw J, and Yu YW [Rapid species-level metagenome profiling and containment estimation with sylph.](https://doi.org/10.1038/s41587-024-02412-y) _Nature Biotechnology_ (2024)

135: **[TBProfiler](https://github.com/jodyphelan/TBProfiler)**<br/>
Ferramenta de perfilamento de _Mycobacterium tuberculosis_ para detectar resistência e tipo de cepa<br/>
Phelan JE, O'Sullivan DM, Machado D, Ramos J, Oppong YEA, Campino S, O'Grady J, McNerney R, Hibberd ML, Viveiros M, Huggett JF, Clark TG [Integrating informatics tools and portable sequencing technology for rapid detection of resistance to anti-tuberculous drugs.](https://doi.org/10.1186/s13073-019-0650-x) _Genome Med_ 11, 41 (2019)

136: **[Traitar](https://github.com/nick-youngblut/traitar3/)**<br/>
Predição de características fenotípicas a partir de genomas microbianos<br/>
Weimann A, Mooren K, Frank J, Pope PB, Gronow S, So AP [From genomes to phenotypes: Traitar, the microbial trait analyzer.](https://doi.org/10.1128/mSystems.00101-16) _mSystems_ 1(6), e00101-16 (2016)

137: **[Unicycler](https://github.com/rrwick/Unicycler)**<br/>
Pipeline de montagem híbrida para genomas bacterianos<br/>
Wick RR, Judd LM, Gorrie CL, Holt KE [Unicycler: Resolving bacterial genome assemblies from short and long sequencing reads.](http://dx.doi.org/10.1371/journal.pcbi.1005595) _PLoS Comput. Biol._ 13, e1005595 (2017)

138: **[VCF-Annotator](https://github.com/rpetit3/vcf-annotator)**<br/>
Adiciona anotações biológicas a variantes em um arquivo VCF.<br/>
Petit III RA [VCF-Annotator: Add biological annotations to variants in a VCF file.](https://github.com/rpetit3/vcf-annotator) (GitHub)

139: **[Vcflib](https://github.com/vcflib/vcflib)**<br/>
Uma biblioteca C++ simples para análise e manipulação de arquivos VCF<br/>
Garrison E [Vcflib: A C++ library for parsing and manipulating VCF files](https://github.com/vcflib/vcflib) (GitHub)

140: **[Velvet](https://github.com/dzerbino/velvet)**<br/>
Montador de novo para reads curtos usando grafos de de Bruijn<br/>
Zerbino DR, Birney E [Velvet: algorithms for de novo short read assembly using de Bruijn graphs.](http://www.genome.org/cgi/doi/10.1101/gr.074492.107) _Genome research_ 18.5 821-829 (2008)

141: **[vt](https://github.com/atks/vt)**<br/>
Um conjunto de ferramentas para descoberta de variantes curtas em dados de sequências genéticas.<br/>
Tan A, Abecasis GR, Kang HM [Unified representation of genetic variants.](https://doi.org/10.1093/bioinformatics/btv112) _Bioinformatics_ 31(13), 2202-2204 (2015)


## Citação do Bactopia

Se você usar o Bactopia em sua análise, por favor cite o seguinte.

Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
