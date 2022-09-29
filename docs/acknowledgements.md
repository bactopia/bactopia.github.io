---
title: Acknowledgements
description: >- 
    A full list of the 140 datasets and software packages used by
    Bactopia, along with links and citations.
---
# Acknowledgements

Bactopia is truly a case of *"standing upon the shoulders of giants"*. Bactopia
currently includes more than 140 datasets and software packages. Nearly 
every component uses, from the workflow, datasets, software packages, even the 
framework for this site, was created by others and made freely available to the public.

I would like to personally extend my many thanks and gratitude to the authors
of these software packages and public datasets. If you've made it this far, I 
owe you a beer 🍻 (or coffee ☕!) if we ever encounter one another in person. 
Really, thank you very much!

!!! info "Please Cite Datasets and Tools"
    If you have used Bactopia in your work, please be sure to cite any datasets
    or software you may have used.

## Influences

### nf-core
[nf-core](https://nf-co.re/) is group of great individuals volunteering 
their time to create a set of curated Nextflow analysis pipelines. The [nf-core Team](https://nf-co.re/about)
is putting together some amazing practices that I think really strengthen the 
Nextflow community as a whole!

Since the beginning I have always had the idea of Bactopia one day being 
apart of nf-core. Unfortunately, I think Bactopia is a much to big at this point to fit the nf-core mold, but that's OK! 
There are still many nf-core practices I've been able to adapt into Bactopia.

1. Arguement parsing based on nf-core library
2. All Bactopia Tools are adapted from nf-core/modules
3. Testing implemented to follow nf-core/modules

By implementing these practices, Bactopia I believe is much better pipeline to use. For this I'm very 
grateful to the nf-core community! Thank you!

Ewels P, Peltzer A, Fillinger S, Patel H, Alneberg J, Wilm A, Garcia MU, Di Tommaso P, Nahnsen S [The nf-core framework for community-curated bioinformatics pipelines.](https://dx.doi.org/10.1038/s41587-020-0439-x) _Nat Biotechnol._ (2020)


## Public Datasets
Below is a list of 19 public datasets that could have potentially 
been included during the *[Build Datasets](datasets.md)* step.

### Ariba Reference Datasets
These datasets are available using Ariba's `getref` function. You can learn 
more about this function at [Ariba's Wiki](https://github.com/sanger-pathogens/ariba/wiki/Task:-getref).

1. __[ARG-ANNOT](http://en.mediterranee-infection.com/article.php?laref=283%26titre=arg-annot)__   
Gupta SK, Padmanabhan BR, Diene SM, Lopez-Rojas R, Kempf M, Landraud L, Rolain J-M [ARG-ANNOT, a new bioinformatic tool to discover antibiotic resistance genes in bacterial genomes.](https://doi.org/10.1128/aac.01310-13) _Antimicrob. Agents Chemother_ 58, 212–220 (2014)
  
2. __[CARD](https://card.mcmaster.ca/)__   
Alcock BP, Raphenya AR, Lau TTY, Tsang KK, Bouchard M, Edalatmand A, Huynh W, Nguyen A-L V, Cheng AA, Liu S, Min SY, Miroshnichenko A, Tran H-K, Werfalli RE, Nasir JA, Oloni M, Speicher DJ, Florescu A, Singh B, Faltyn M, Hernandez-Koutoucheva A, Sharma AN, Bordeleau E, Pawlowski AC, Zubyk HL, Dooley D, Griffiths E, Maguire F, Winsor GL, Beiko RG, Brinkman FSL, Hsiao WWL, Domselaar GV, McArthur AG [CARD 2020: antibiotic resistome surveillance with the comprehensive antibiotic resistance database.](https://doi.org/10.1093/nar/gkz935) _Nucleic acids research_ 48.D1, D517-D525 (2020)
  
3. __[EcOH](https://dx.doi.org/10.1099%2Fmgen.0.000064)__   
Ingle DJ, Valcanis M, Kuzevski A, Tauschek M, Inouye M, Stinear T, Levine MM, Robins-Browne RM, Holt KE [In silico serotyping of E. coli from short read data identifies limited novel O-loci but extensive diversity of O:H serotype combinations within and between pathogenic lineages.](https://doi.org/10.1099/mgen.0.000064) _Microbial Genomics_, 2(7), e000064. (2016)
  
4. __[MEGARes](https://megares.meglab.org/)__   
Lakin SM, Dean C, Noyes NR, Dettenwanger A, Ross AS, Doster E, Rovira P, Abdo Z, Jones KL, Ruiz J, Belk KE, Morley PS, Boucher C [MEGARes: an antimicrobial resistance database for high throughput sequencing.](https://doi.org/10.1093/nar/gkw1009) _Nucleic Acids Res._ 45, D574–D580 (2017)
  
5. __[MEGARes 2.0](https://megares.meglab.org/)__   
Doster E, Lakin SM, Dean CJ, Wolfe C, Young JG, Boucher C, Belk KE, Noyes NR, Morley PS [MEGARes 2.0: a database for classification of antimicrobial drug, biocide and metal resistance determinants in metagenomic sequence data.](https://doi.org/10.1093/nar/gkz1010) _Nucleic Acids Research_, 48(D1), D561–D569. (2020)
  
6. __[NCBI Reference Gene Catalog](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA313047)__   
Feldgarden M, Brover V, Haft DH, Prasad AB, Slotta DJ, Tolstoy I, Tyson GH, Zhao S, Hsu C-H, McDermott PF, Tadesse DA, Morales C, Simmons M, Tillman G, Wasilenko J, Folster JP, Klimke W [Validating the NCBI AMRFinder Tool and Resistance Gene Database Using Antimicrobial Resistance Genotype-Phenotype Correlations in a Collection of NARMS Isolates](https://doi.org/10.1128/AAC.00483-19). _Antimicrob. Agents Chemother._ (2019)
  
7. __[PlasmidFinder](https://cge.cbs.dtu.dk/services/PlasmidFinder/)__   
Carattoli A, Zankari E, García-Fernández A, Larsen MV, Lund O, Villa L, Aarestrup FM, Hasman H [In silico detection and typing of plasmids using PlasmidFinder and plasmid multilocus sequence typing.](https://doi.org/10.1128/aac.02412-14) _Antimicrob. Agents Chemother._ 58, 3895–3903 (2014)
  
8. __[ResFinder](https://cge.cbs.dtu.dk//services/ResFinder/)__   
Zankari E, Hasman H, Cosentino S, Vestergaard M, Rasmussen S, Lund O, Aarestrup FM, Larsen MV [Identification of acquired antimicrobial resistance genes.](https://doi.org/10.1093/jac/dks261) _J. Antimicrob. Chemother._ 67, 2640–2644 (2012)
  
9. __[SRST2](https://github.com/katholt/srst2)__   
Inouye M, Dashnow H, Raven L-A, Schultz MB, Pope BJ, Tomita T, Zobel J, Holt KE [SRST2: Rapid genomic surveillance for public health and hospital microbiology labs.](https://doi.org/10.1186/s13073-014-0090-6) _Genome Med._ 6, 90 (2014)
  
10. __[VFDB](http://www.mgc.ac.cn/VFs/)__   
Chen L, Zheng D, Liu B, Yang J, Jin Q [VFDB 2016: hierarchical and refined dataset for big data analysis--10 years on.](https://doi.org/10.1093/nar/gkv1239) _Nucleic Acids Res._ 44, D694–7 (2016)
  
11. __[VirulenceFinder](https://cge.cbs.dtu.dk/services/VirulenceFinder/)__   
Joensen KG, Scheutz F, Lund O, Hasman H, Kaas RS, Nielsen EM, Aarestrup FM [Real-time whole-genome sequencing for routine typing, surveillance, and outbreak detection of verotoxigenic _Escherichia coli_.](https://doi.org/10.1128/jcm.03617-13) _J. Clin. Microbiol._ 52, 1501–1510 (2014)
  


### Minmer Datasets
1. __[Mash Refseq (release 88) Sketch](https://mash.readthedocs.io/en/latest/data.html)__   
Ondov BD, Starrett GJ, Sappington A, Kostic A, Koren S, Buck CB, Phillippy AM [Mash Screen: high-throughput sequence containment estimation for genome discovery](https://doi.org/10.1186/s13059-019-1841-x) _Genome Biol_ 20, 232 (2019)
  
2. __[Sourmash Genbank LCA Signature](https://sourmash.readthedocs.io/en/latest/databases.html)__   
Brown CT, Irber L [sourmash: a library for MinHash sketching of DNA](http://dx.doi.org/10.21105/joss.00027). _JOSS_ 1, 27 (2016)
  


### Everything Else

1. __[eggNOG 5.0 Database](http://eggnog.embl.de/)__   
Huerta-Cepas J, Szklarczyk D, Heller D, Hernández-Plaza A, Forslund SK, Cook H, Mende DR, Letunic I, Rattei T, Jensen LJ, von Mering C, Bork P [eggNOG 5.0: a hierarchical, functionally and phylogenetically annotated orthology resource based on 5090 organisms and 2502 viruses.](https://doi.org/10.1093/nar/gky1085) _Nucleic Acids Res._ 47, D309–D314 (2019)
  
2. __[Genome Taxonomy Database](https://gtdb.ecogenomic.org/)__   
Parks DH, Chuvochina M, Rinke C, Mussig AJ, Chaumeil P-A, Hugenholtz P [GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically consistent, rank normalized and complete genome-based taxonomy](https://doi.org/10.1093/nar/gkab776) _Nucleic Acids Research_ gkab776 (2021)
  
3. __[MOB-suite Database](https://github.com/phac-nml/mob-suite)__   
Robertson J, Bessonov K, Schonfeld J, Nash JHE. [Universal whole-sequence-based plasmid typing and its utility to prediction of host range and epidemiological surveillance.](https://doi.org/10.1099/mgen.0.000435) _Microbial Genomics_, 6(10)(2020)
  
4. __[NCBI RefSeq Database](https://www.ncbi.nlm.nih.gov/refseq/)__   
O'Leary NA, Wright MW, Brister JR, Ciufo S, Haddad D, McVeigh R, Rajput B, Robbertse B, Smith-White B, Ako-Adjei D, Astashyn A, Badretdin A, Bao Y, Blinkova O0, Brover V, Chetvernin V, Choi J, Cox E, Ermolaeva O, Farrell CM, Goldfarb T, Gupta T, Haft D, Hatcher E, Hlavina W, Joardar VS, Kodali VK, Li W, Maglott D, Masterson P, McGarvey KM, Murphy MR, O'Neill K, Pujar S, Rangwala SH, Rausch D, Riddick LD, Schoch C, Shkeda A, Storz SS, Sun H, Thibaud-Nissen F, Tolstoy I, Tully RE, Vatsan AR, Wallin C, Webb D, Wu W, Landrum MJ, Kimchi A, Tatusova T, DiCuccio M, Kitts P, Murphy TD, Pruitt KD [Reference sequence (RefSeq) database at NCBI: current status, taxonomic expansion, and functional annotation.](https://doi.org/10.1093/nar/gkv1189) _Nucleic Acids Res._ 44, D733–45 (2016)
  
5. __[PubMLST.org](https://pubmlst.org/)__   
Jolley KA, Bray JE, Maiden MCJ [Open-access bacterial population genomics: BIGSdb software, the PubMLST.org website and their applications.](http://dx.doi.org/10.12688/wellcomeopenres.14826.1) _Wellcome Open Res_ 3, 124 (2018)
  
6. __[SILVA rRNA Database](https://www.arb-silva.de/)__   
Quast C, Pruesse E, Yilmaz P, Gerken J, Schweer T, Yarza P, Peplies J, Glöckner FO [The SILVA ribosomal RNA gene database project: improved data processing and web-based tools.](https://doi.org/10.1093/nar/gks1219) _Nucleic Acids Res._ 41, D590–6 (2013)
  


## Software Included In Bactopia
Below are 121 of software packages used (directly and indirectly) by 
Bactopia. A link to the software page as well as the citation (if available) 
have been included.

1. __[Abricate](https://github.com/tseemann/abricate)__  
Mass screening of contigs for antimicrobial and virulence genes  
Seemann T [Abricate: mass screening of contigs for antimicrobial and virulence genes](https://github.com/tseemann/abricate) (GitHub)
  
2. __[AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE)__  
Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.  
Raghuram V. [AgrVATE: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.](https://github.com/VishnuRaghuram94/AgrVATE) (GitHub)
  
3. __[AMRFinderPlus](https://github.com/ncbi/amr)__  
Find acquired antimicrobial resistance genes and some point mutations in protein or assembled nucleotide sequences.  
Feldgarden M, Brover V, Haft DH, Prasad AB, Slotta DJ, Tolstoy I, Tyson GH, Zhao S, Hsu C-H, McDermott PF, Tadesse DA, Morales C, Simmons M, Tillman G, Wasilenko J, Folster JP, Klimke W [Validating the NCBI AMRFinder Tool and Resistance Gene Database Using Antimicrobial Resistance Genotype-Phenotype Correlations in a Collection of NARMS Isolates](https://doi.org/10.1128/AAC.00483-19). _Antimicrob. Agents Chemother._ (2019)
  
4. __[any2fasta](https://github.com/tseemann/any2fasta)__  
Convert various sequence formats to FASTA  
Seemann T [any2fasta: Convert various sequence formats to FASTA](https://github.com/tseemann/any2fasta) (GitHub)
  
5. __[Aragorn](http://130.235.244.92/ARAGORN/Downloads/)__  
Finds transfer RNA features (tRNA)  
Laslett D, Canback B [ARAGORN, a program to detect tRNA genes and tmRNA genes in nucleotide sequences.](https://doi.org/10.1093/nar/gkh152) _Nucleic Acids Res_. 32(1):11-6 (2004)
  
6. __[Ariba](https://github.com/sanger-pathogens/ariba)__  
Antimicrobial Resistance Identification By Assembly  
Hunt M, Mather AE, Sánchez-Busó L, Page AJ, Parkhill J, Keane JA, Harris SR [ARIBA: rapid antimicrobial resistance genotyping directly from sequencing reads](http://dx.doi.org/10.1099/mgen.0.000131). _Microb Genom_ 3, e000131 (2017)
  
7. __[ART](https://www.niehs.nih.gov/research/resources/software/biostatistics/art/index.cfm)__  
A set of simulation tools to generate synthetic next-generation sequencing reads  
Huang W, Li L, Myers JR, Marth GT [ART: a next-generation sequencing read simulator.](http://dx.doi.org/10.1093/bioinformatics/btr708) _Bioinformatics_ 28, 593–594 (2012)
  
8. __[assembly-scan](https://github.com/rpetit3/assembly-scan)__  
Generate basic stats for an assembly.  
Petit III RA [assembly-scan: generate basic stats for an assembly](https://github.com/rpetit3/assembly-scan) (GitHub)
  
9. __[Bakta](https://github.com/oschwengers/bakta)__  
Rapid & standardized annotation of bacterial genomes & plasmids  
Schwengers O, Jelonek L, Dieckmann MA, Beyvers S, Blom J, Goesmann A [Bakta - rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.](https://doi.org/10.1099/mgen.0.000685) _Microbial Genomics_ 7(11) (2021)
  
10. __[Barrnap](https://github.com/tseemann/barrnap)__  
Bacterial ribosomal RNA predictor  
Seemann T [Barrnap: Bacterial ribosomal RNA predictor](https://github.com/tseemann/barrnap) (GitHub)
  
11. __[BBTools](https://jgi.doe.gov/data-and-tools/bbtools/)__  
BBTools is a suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data.  
Bushnell B [BBMap short read aligner, and other bioinformatic tools.](http://sourceforge.net/projects/bbmap/) (Link)
  
12. __[BCFtools](https://github.com/samtools/bcftools)__  
Utilities for variant calling and manipulating VCFs and BCFs.  
Danecek P, Bonfield JK, Liddle J, Marshall J, Ohan V, Pollard MO, Whitwham A, Keane T, McCarthy SA, Davies RM, Li H [Twelve years of SAMtools and BCFtools](https://doi.org/10.1093/gigascience/giab008) _GigaScience_ Volume 10, Issue 2 (2021)
  
13. __[Bedtools](https://github.com/arq5x/bedtools2)__  
A powerful toolset for genome arithmetic.  
Quinlan AR, Hall IM [BEDTools: a flexible suite of utilities for comparing genomic features](http://dx.doi.org/10.1093/bioinformatics/btq033). _Bioinformatics_ 26, 841–842 (2010)
  
14. __[BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi)__  
Basic Local Alignment Search Tool  
Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, Madden TL [BLAST+: architecture and applications](http://dx.doi.org/10.1186/1471-2105-10-421). _BMC Bioinformatics_ 10, 421 (2009)
  
15. __[Bowtie2](https://github.com/BenLangmead/bowtie2)__  
A fast and sensitive gapped read aligner  
Langmead B, Salzberg SL [Fast gapped-read alignment with Bowtie 2.](http://dx.doi.org/10.1038/nmeth.1923) _Nat. Methods._ 9, 357–359 (2012)
  
16. __[BUSCO](https://gitlab.com/ezlab/busco)__  
Assessing genome assembly and annotation completeness with Benchmarking Universal Single-Copy Orthologs (BUSCO)  
Manni M, Berkeley MR, Seppey M, Simão FA, Zdobnov EM [BUSCO Update: Novel and Streamlined Workflows along with Broader and Deeper Phylogenetic Coverage for Scoring of Eukaryotic, Prokaryotic, and Viral Genomes.](https://doi.org/10.1093/molbev/msab199) _Molecular Biology and Evolution_ 38(10), 4647–4654. (2021)
  
17. __[BWA](https://github.com/lh3/bwa/)__  
Burrow-Wheeler Aligner for short-read alignment  
Li H [Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM](http://arxiv.org/abs/1303.3997). _arXiv_ [q-bio.GN] (2013)
  
18. __[CD-HIT](https://github.com/weizhongli/cdhit)__  
Accelerated for clustering the next-generation sequencing data  
Li W, Godzik A [Cd-hit: a fast program for clustering and comparing large sets of protein or nucleotide sequences](http://dx.doi.org/10.1093/bioinformatics/btl158). _Bioinformatics_ 22, 1658–1659 (2006)
  
19. __[CD-HIT-EST](https://github.com/weizhongli/cdhit)__  
Accelerated for clustering the next-generation sequencing data  
Fu L, Niu B, Zhu Z, Wu S, Li W [CD-HIT: accelerated for clustering the next-generation sequencing data](http://dx.doi.org/10.1093/bioinformatics/bts565). _Bioinformatics_ 28, 3150–3152 (2012)
  
20. __[CheckM](https://github.com/Ecogenomics/CheckM)__  
Assess the quality of microbial genomes recovered from isolates, single cells, and metagenomes  
Parks DH, Imelfort M, Skennerton CT, Hugenholtz P, Tyson GW [CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes.](http://dx.doi.org/10.1101/gr.186072.114) _Genome Res_ 25, 1043–1055 (2015)
  
21. __[ClonalFramML](https://github.com/xavierdidelot/ClonalFrameML)__  
Efficient Inference of Recombination in Whole Bacterial Genomes  
Didelot X, Wilson DJ [ClonalFrameML: Efficient Inference of Recombination in Whole Bacterial Genomes.](https://doi.org/10.1371/journal.pcbi.1004041) _PLoS Comput Biol_ 11(2) e1004041 (2015)
  
22. __[DIAMOND](https://github.com/bbuchfink/diamond)__  
Accelerated BLAST compatible local sequence aligner.  
Buchfink B, Xie C, Huson DH [Fast and sensitive protein alignment using DIAMOND.](http://dx.doi.org/10.1038/nmeth.3176) _Nat. Methods._ 12, 59–60 (2015)
  
23. __[ECTyper](https://github.com/phac-nml/ecoli_serotyping)__  
In-silico prediction of _Escherichia coli_ serotype  
Laing C, Bessonov K, Sung S, La Rose C [ECTyper - In silico prediction of _Escherichia coli_ serotype](https://github.com/phac-nml/ecoli_serotyping) (GitHub)  
24. __[eggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper)__  
Fast genome-wide functional annotation through orthology assignment  
Huerta-Cepas J, Forslund K, Coelho LP, Szklarczyk D, Jensen LJ, von Mering C, Bork P [Fast Genome-Wide Functional Annotation through Orthology Assignment by eggNOG-Mapper.](http://dx.doi.org/10.1093/molbev/msx148) _Mol. Biol. Evol._ 34, 2115–2122 (2017)
  
25. __[emmtyper](https://github.com/MDU-PHL/emmtyper)__  
emm Automatic Isolate Labeller  
Tan A, Seemann T, Lacey D, Davies M, Mcintyre L, Frost H, Williamson D, Gonçalves da Silva A [emmtyper - emm Automatic Isolate Labeller](https://github.com/MDU-PHL/emmtyper) (GitHub)
  
26. __[FastANI](https://github.com/ParBLiSS/FastANI)__  
Fast Whole-Genome Similarity (ANI) Estimation  
Jain C, Rodriguez-R LM, Phillippy AM, Konstantinidis KT, Aluru S [High throughput ANI analysis of 90K prokaryotic genomes reveals clear species boundaries.](http://dx.doi.org/10.1038/s41467-018-07641-9) _Nat. Commun._ 9, 5114 (2018)
  
27. __[FastQC](https://github.com/s-andrews/FastQC)__  
A quality control analysis tool for high throughput sequencing data.  
Andrews S [FastQC: a quality control tool for high throughput sequence data.](http://www.bioinformatics.babraham.ac.uk/projects/fastqc) (WebLink)
  
28. __[fastq-dl](https://github.com/rpetit3/fastq-dl)__  
Download FASTQ files from SRA or ENA repositories.  
Petit III RA [fastq-dl: Download FASTQ files from SRA or ENA repositories.](https://github.com/rpetit3/fastq-dl) (GitHub)
  
29. __[fastq-scan](https://github.com/rpetit3/fastq-scan)__  
Output FASTQ summary statistics in JSON format  
Petit III RA [fastq-scan: generate summary statistics of input FASTQ sequences.](https://github.com/rpetit3/fastq-scan) (GitHub)
  
30. __[FastTree](http://www.microbesonline.org/fasttree)__  
Approximately-maximum-likelihood phylogenetic trees  
Price MN, Dehal PS, Arkin AP [FastTree 2 – Approximately Maximum-Likelihood Trees for Large Alignments.](https://dx.doi.org/10.1371%2Fjournal.pone.0009490) _PLoS One_ 5, e9490 (2010)
  
31. __[FLASH](https://ccb.jhu.edu/software/FLASH/)__  
A fast and accurate tool to merge paired-end reads.  
Magoč T, Salzberg SL [FLASH: fast length adjustment of short reads to improve genome assemblies.](https://doi.org/10.1093/bioinformatics/btr507) _Bioinformatics_ 27.21 2957-2963 (2011)
  
32. __[Flye](https://github.com/fenderglass/Flye)__  
De novo assembler for single molecule sequencing reads using repeat graphs  
Kolmogorov M, Yuan J, Lin Y, Pevzner P [Assembly of Long Error-Prone Reads Using Repeat Graphs](https://doi.org/10.1038/s41587-019-0072-8) _Nature Biotechnology_ (2019)
  
33. __[freebayes](https://github.com/ekg/freebayes)__  
Bayesian haplotype-based genetic polymorphism discovery and genotyping  
Garrison E, Marth G [Haplotype-based variant detection from short-read sequencing.](https://arxiv.org/abs/1207.3907) arXiv preprint arXiv:1207.3907 [q-bio.GN] (2012)
  
34. __[GAMMA](https://github.com/rastanton/GAMMA)__  
Gene Allele Mutation Microbial Assessment  
Stanton RA, Vlachos N, Halpin AL [GAMMA: a tool for the rapid identification, classification, and annotation of translated gene matches from sequencing data.](https://doi.org/10.1093/bioinformatics/btab607) _Bioinformatics_ (2021)
  
35. __[GenoTyphi](https://github.com/katholt/genotyphi)__  
Assign genotypes to Salmonella Typhi genomes based on Mykrobe results  
Wong VK, Baker S, Connor TR, Pickard D, Page AJ, Dave J, Murphy N, Holliman R, Sefton A, Millar M, Dyson ZA, Dougan G, Holt KE, & International Typhoid Consortium. [An extended genotyping framework for Salmonella enterica serovar Typhi, the cause of human typhoid](https://doi.org/10.1038/ncomms12827) _Nature Communications_ 7, 12827. (2016)
  
36. __[GNU Parallel](https://www.gnu.org/software/parallel/)__  
A shell tool for executing jobs in parallel  
Tange O [GNU Parallel](https://doi.org/10.5281/zenodo.1146014) (2018)
  
37. __[GTDB-Tk](https://github.com/Ecogenomics/GTDBTk)__  
A toolkit for assigning objective taxonomic classifications to bacterial and archaeal genomes  
Chaumeil PA, Mussig AJ, Hugenholtz P, Parks DH [GTDB-Tk: a toolkit to classify genomes with the Genome Taxonomy Database.](https://doi.org/10.1093/bioinformatics/btz848) _Bioinformatics_ (2019)
  
38. __[Gubbins](https://github.com/nickjcroucher/gubbins)__  
Rapid phylogenetic analysis of large samples of recombinant bacterial whole genome sequences  
Croucher NJ, Page AJ, Connor TR, Delaney AJ, Keane JA, Bentley SD, Parkhill J, Harris SR [Rapid phylogenetic analysis of large samples of recombinant bacterial whole genome sequences using Gubbins.](https://doi.org/10.1093/nar/gku1196) _Nucleic Acids Research_ 43(3), e15. (2015)
  
39. __[hicap](https://github.com/scwatts/hicap)__  
in silico typing of the _H. influenzae_ cap locus  
Watts SC, Holt KE [hicap: in silico serotyping of the Haemophilus influenzae capsule locus.](https://doi.org/10.1128/JCM.00190-19) _Journal of Clinical Microbiology_ JCM.00190-19 (2019)
  
40. __[HMMER](http://hmmer.org/)__  
Biosequence analysis using profile hidden Markov models  
Eddy SR [Accelerated Profile HMM Searches.](https://doi.org/10.1371/journal.pcbi.1002195) _PLoS Comput. Biol._ 7, e1002195 (2011)
  
41. __[HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero)__  
Rapid _Haemophilus parasuis_ serotyping  
Lui J [HpsuisSero: Rapid _Haemophilus parasuis_ serotyping](https://github.com/jimmyliu1326/HpsuisSero) (GitHub)
  
42. __[Infernal](http://eddylab.org/infernal/)__  
Searches DNA sequence databases for RNA structure and sequence similarities  
Nawrocki EP, Eddy SR [Infernal 1.1: 100-fold faster RNA homology searches.](https://doi.org/10.1093/bioinformatics/btt509) _Bioinformatics_ 29(22), 2933-2935 (2013)
  
43. __[IQ-TREE](https://github.com/Cibiv/IQ-TREE)__  
Efficient phylogenomic software by maximum likelihood  
Nguyen L-T, Schmidt HA, von Haeseler A, Minh BQ [IQ-TREE: A fast and effective stochastic algorithm for estimating maximum likelihood phylogenies.](https://doi.org/10.1093/molbev/msu300) _Mol. Biol. Evol._ 32:268-274 (2015)
  
44. __[ModelFinder](https://github.com/Cibiv/IQ-TREE)__  
Used for automatic model selection  
Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS [ModelFinder - Fast model selection for accurate phylogenetic estimates.](https://doi.org/10.1038/nmeth.4285) _Nat. Methods_ 14:587-589 (2017)
  
45. __[UFBoot2](https://github.com/Cibiv/IQ-TREE)__  
Used to conduct ultrafast bootstrapping  
Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS [UFBoot2: Improving the ultrafast bootstrap approximation.](https://doi.org/10.1093/molbev/msx281) _Mol. Biol. Evol._ 35:518–522 (2018)
  
46. __[ISMapper](https://github.com/jhawkey/IS_mapper)__  
IS mapping software  
Hawkey J, Hamidian M, Wick RR, Edwards DJ, Billman-Jacobe H, Hall RM, Holt KE [ISMapper: identifying transposase insertion sites in bacterial genomes from short read sequence data](http://dx.doi.org/10.1186/s12864-015-1860-2). _BMC Genomics_ 16, 667 (2015)
  
47. __[Kaptive](https://github.com/katholt/Kaptive)__  
Surface polysaccharide loci for _Klebsiella pneumoniae_ species complex and _Acinetobacter baumannii_ genomes  
Wyres KL, Wick RR, Gorrie C, Jenney A, Follador R, Thomson NR, Holt KE [Identification of Klebsiella capsule synthesis loci from whole genome data.](https://doi.org/10.1099/mgen.0.000102) _Microbial genomics_ 2(12) (2016)
  
48. __[Kleborate](https://github.com/katholt/Kleborate)__  
Genotyping tool for _Klebsiella pneumoniae_ and its related species complex  
Lam MMC, Wick RR, Watts, SC, Cerdeira LT, Wyres KL, Holt KE [A genomic surveillance framework and genotyping tool for Klebsiella pneumoniae and its related species complex.](https://doi.org/10.1038/s41467-021-24448-3) _Nat Commun_ 12, 4188 (2021)
  
49. __[KMC](https://github.com/refresh-bio/KMC)__  
Fast and frugal disk based k-mer counter  
Deorowicz S, Kokot M, Grabowski Sz, Debudaj-Grabysz A [KMC 2: Fast and resource-frugal k-mer counting](https://doi.org/10.1093/bioinformatics/btv022) _Bioinformatics_ 31(10):1569–1576 (2015)
  
50. __[Kraken2](https://github.com/DerrickWood/kraken2)__  
The second version of the Kraken taxonomic sequence classification system  
Wood DE, Lu J, Langmead B [Improved metagenomic analysis with Kraken 2.](https://doi.org/10.1186/s13059-019-1891-0) *Genome Biology*, 20(1), 257. (2019)
  
51. __[legsta](https://github.com/tseemann/legsta)__  
In silico Legionella pneumophila Sequence Based Typing  
Seemann T [legsta: In silico Legionella pneumophila Sequence Based Typing](https://github.com/tseemann/legsta) (GitHub)
  
52. __[Lighter](https://github.com/mourisl/Lighter)__  
Fast and memory-efficient sequencing error corrector  
Song L, Florea L, Langmead B [Lighter: Fast and Memory-efficient Sequencing Error Correction without Counting](https://doi.org/10.1186/s13059-014-0509-9). _Genome Biol._ 15(11):509 (2014)
  
53. __[LisSero](https://github.com/MDU-PHL/LisSero)__  
_In silico_ serotype prediction for _Listeria monocytogenes_  
Kwong J, Zhang J, Seeman T, Horan, K, Gonçalves da Silva A [LisSero - _In silico_ serotype prediction for _Listeria monocytogenes_](https://github.com/MDU-PHL/LisSero) (GitHub)
  
54. __[MAFFT](https://mafft.cbrc.jp/alignment/software/)__  
Multiple alignment program for amino acid or nucleotide sequences  
Katoh K, Standley DM [MAFFT multiple sequence alignment software version 7: improvements in performance and usability.](https://doi.org/10.1093/molbev/mst010) _Mol. Biol. Evol._ 30, 772–780 (2013)
  
55. __[Mash](https://github.com/marbl/Mash)__  
Fast genome and metagenome distance estimation using MinHash  
Ondov BD, Treangen TJ, Melsted P, Mallonee AB, Bergman NH, Koren S, Phillippy AM [Mash: fast genome and metagenome distance estimation using MinHash](http://dx.doi.org/10.1186/s13059-016-0997-x). _Genome Biol_ 17, 132 (2016)
  
56. __[Mash](https://github.com/marbl/Mash)__  
High-throughput sequence containment estimation  
Ondov BD, Starrett GJ, Sappington A, Kostic A, Koren S, Buck CB, Phillippy AM [Mash Screen: high-throughput sequence containment estimation for genome discovery](https://doi.org/10.1186/s13059-019-1841-x) _Genome Biol_ 20, 232 (2019)
  
57. __[Mashtree](https://github.com/lskatz/mashtree)__  
Create a tree using Mash distances  
Katz LS, Griswold T, Morrison S, Caravas J, Zhang S, den Bakker HC, Deng X, Carleton HA [Mashtree: a rapid comparison of whole genome sequence files.](https://doi.org/10.21105/joss.01762) _Journal of Open Source Software_, 4(44), 1762 (2019)
  
58. __[maskrc-svg](https://github.com/kwongj/maskrc-svg)__  
Masks recombination as detected by ClonalFrameML or Gubbins  
Kwong J [maskrc-svg - Masks recombination as detected by ClonalFrameML or Gubbins and draws an SVG.](https://github.com/kwongj/maskrc-svg) (GitHub)  
59. __[McCortex](https://github.com/mcveanlab/mccortex)__  
De novo genome assembly and multisample variant calling  
Turner I, Garimella KV, Iqbal Z, McVean G [Integrating long-range connectivity information into de Bruijn graphs.](http://dx.doi.org/10.1093/bioinformatics/bty157) _Bioinformatics_ 34, 2556–2565 (2018)
  
60. __[mcroni](https://github.com/liampshaw/mcroni)__  
Scripts for finding and processing promoter variants upstream of mcr-1  
Shaw L [mcroni: Scripts for finding and processing promoter variants upstream of mcr-1](https://github.com/liampshaw/mcroni) (GitHub)
  
61. __[Medaka](None)__  
Sequence correction provided by ONT Research  
ONT Research [Medaka: Sequence correction provided by ONT Research](https://github.com/nanoporetech/medaka) (GitHub)
  
62. __[meningotype](https://github.com/MDU-PHL/meningotype)__  
In silico serotyping, finetyping and Bexsero antigen sequence typing of _Neisseria meningitidis_  
Kwong JC, Gonçalves da Silva A, Stinear TP, Howden BP, & Seemann T [meningotype: in silico typing for _Neisseria meningitidis_.](https://github.com/MDU-PHL/meningotype) (GitHub)
  
63. __[MEGAHIT](https://github.com/voutcn/megahit)__  
Ultra-fast and memory-efficient (meta-)genome assembler  
Li D, Liu C-M, Luo R, Sadakane K, Lam T-W [MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph.](https://doi.org/10.1093/bioinformatics/btv033) _Bioinformatics_ 31.10 1674-1676 (2015)
  
64. __[mlst](https://github.com/tseemann/mlst)__  
Scan contig files against PubMLST typing schemes  
Seemann T [mlst: scan contig files against PubMLST typing schemes](https://github.com/tseemann/mlst) (GitHub)
  
65. __[MinCED](https://github.com/ctSkennerton/minced)__  
Mining CRISPRs in Environmental Datasets  
Skennerton C [MinCED: Mining CRISPRs in Environmental Datasets](https://github.com/ctSkennerton/minced) (GitHub)
  
66. __[Miniasm](https://github.com/lh3/miniasm)__  
Ultrafast de novo assembly for long noisy reads (though having no consensus step)  
Li H [Miniasm: Ultrafast de novo assembly for long noisy reads](https://github.com/lh3/miniasm) (GitHub)
  
67. __[Minimap2](https://github.com/lh3/minimap2)__  
A versatile pairwise aligner for genomic and spliced nucleotide sequences  
Li H [Minimap2: pairwise alignment for nucleotide sequences.](https://doi.org/10.1093/bioinformatics/bty191) _Bioinformatics_ 34:3094-3100 (2018)
  
68. __[MOB-suite](https://github.com/phac-nml/mob-suite)__  
Software tools for clustering, reconstruction and typing of plasmids from draft assemblies  
Robertson J, Nash JHE [MOB-suite: software tools for clustering, reconstruction and typing of plasmids from draft assemblies.](https://doi.org/10.1099/mgen.0.000206) _Microbial Genomics_ 4(8). (2018)
  
69. __[Mykrobe](https://github.com/Mykrobe-tools/mykrobe)__  
Antibiotic resistance prediction in minutes  
Hunt M, Bradley P, Lapierre SG, Heys S, Thomsit M, Hall MB, Malone KM, Wintringer P, Walker TM, Cirillo DM, Comas I, Farhat MR, Fowler P, Gardy J, Ismail N, Kohl TA, Mathys V, Merker M, Niemann S, Omar SV, Sintchenko V, Smith G, Supply P, Tahseen S, Wilcox M, Arandjelovic I, Peto TEA, Crook, DW, Iqbal Z [Antibiotic resistance prediction for Mycobacterium tuberculosis from genome sequence data with Mykrobe](https://doi.org/10.12688/wellcomeopenres.15603.1) _Wellcome Open Research_ 4, 191. (2019)
  
70. __[NanoPlot](https://github.com/wdecoster/NanoPlot)__  
Plotting scripts for long read sequencing data  
De Coster W, D’Hert S, Schultz DT, Cruts M, Van Broeckhoven C [NanoPack: visualizing and processing long-read sequencing data](https://doi.org/10.1093/bioinformatics/bty149) _Bioinformatics_ Volume 34, Issue 15 (2018) 
  
71. __[Nanoq](https://github.com/esteinig/nanoq)__  
Minimal but speedy quality control for nanopore reads in Rust  
Steinig E [Nanoq: Minimal but speedy quality control for nanopore reads in Rust](https://github.com/esteinig/nanoq) (GitHub)
  
72. __[ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)__  
Scripts to download genomes from the NCBI FTP servers  
Blin K [ncbi-genome-download: Scripts to download genomes from the NCBI FTP servers](https://github.com/kblin/ncbi-genome-download) (GitHub)
  
73. __[Nextflow](https://github.com/nextflow-io/nextflow)__  
A DSL for data-driven computational pipelines.  
Di Tommaso P, Chatzou M, Floden EW, Barja PP, Palumbo E, Notredame C [Nextflow enables reproducible computational workflows.](https://www.nature.com/articles/nbt.3820.pdf?origin=ppub) _Nat. Biotechnol._ 35, 316–319 (2017)
  
74. __[ngmaster](https://github.com/MDU-PHL/ngmaster)__  
_In silico_ multi-antigen sequence typing for _Neisseria gonorrhoeae_ (NG-MAST)  
Kwong J, Gonçalves da Silva A, Schultz M, Seeman T [ngmaster - _In silico_ multi-antigen sequence typing for _Neisseria gonorrhoeae_ (NG-MAST)](https://github.com/MDU-PHL/ngmaster) (GitHub)
  
75. __[nhmmer](http://hmmer.org/)__  
DNA homology search with profile HMMs.  
Wheeler TJ, Eddy SR [nhmmer: DNA homology search with profile HMMs.](https://doi.org/10.1093/bioinformatics/btt403) _Bioinformatics_ 29, 2487–2489 (2013)
  
76. __[Panaroo](https://github.com/gtonkinhill/panaroo)__  
An updated pipeline for pangenome investigation  
Tonkin-Hill G, MacAlasdair N, Ruis C, Weimann A, Horesh G, Lees JA, Gladstone RA, Lo S, Beaudoin C, Floto RA, Frost SDW, Corander J, Bentley SD, Parkhill J [Producing polished prokaryotic pangenomes with the Panaroo pipeline.](https://doi.org/10.1186/s13059-020-02090-4) _Genome Biology_ 21(1), 180. (2020)
  
77. __[phyloFlash](https://github.com/HRGV/phyloFlash)__  
A pipeline to rapidly reconstruct the SSU rRNAs and explore phylogenetic composition of an illumina (meta)genomic dataset.  
Gruber-Vodicka HR, Seah BKB, Pruesse E [phyloFlash: Rapid Small-Subunit rRNA Profiling and Targeted Assembly from Metagenomes](https://doi.org/10.1128/mSystems.00920-20) _mSystems_ 5 (2020)
  
78. __[Pigz](https://zlib.net/pigz/)__  
A parallel implementation of gzip for modern multi-processor, multi-core machines.  
Adler M. [pigz: A parallel implementation of gzip for modern multi-processor, multi-core machines.](https://zlib.net/pigz/) _Jet Propulsion Laboratory_ (2015)
  
79. __[Pilon](https://github.com/broadinstitute/pilon/)__  
An automated genome assembly improvement and variant detection tool  
Walker BJ, Abeel T,  Shea T, Priest M, Abouelliel A, Sakthikumar S, Cuomo CA, Zeng Q, Wortman J, Young SK, Earl AM [Pilon: an integrated tool for comprehensive microbial variant detection and genome assembly improvement.](https://doi.org/10.1371/journal.pone.0112963) _PloS one_ 9.11 e112963 (2014)
  
80. __[PIRATE](http://github.com/SionBayliss/PIRATE)__  
A toolbox for pangenome analysis and threshold evaluation.  
Bayliss SC, Thorpe HA, Coyle NM, Sheppard SK, Feil EJ [PIRATE: A fast and scalable pangenomics toolbox for clustering diverged orthologues in bacteria.](https://doi.org/10.1093/gigascience/giz119) _Gigascience_ 8 (2019)
  
81. __[PlasmidFinder](https://bitbucket.org/genomicepidemiology/plasmidfinder)__  
Identifies plasmids in total or partial sequenced isolates of bacteria  
Carattoli A, Zankari E, García-Fernández A, Voldby Larsen M, Lund O, Villa L, Møller Aarestrup F, Hasman H [In silico detection and typing of plasmids using PlasmidFinder and plasmid multilocus sequence typing.](https://doi.org/10.1128/AAC.02412-14) _Antimicrobial Agents and Chemotherapy_ 58(7), 3895–3903. (2014)
  
82. __[Porechop](https://github.com/rrwick/Porechop)__  
adapter trimmer for Oxford Nanopore reads  
Wick RR, Judd LM, Gorrie CL, Holt KE. [Completing bacterial genome assemblies with multiplex MinION sequencing.](https://doi.org/10.1099/mgen.0.000132) _Microb Genom._ 3(10):e000132 (2017)
  
83. __[pplacer](https://github.com/matsen/pplacer)__  
Phylogenetic placement and downstream analysis  
Matsen FA, Kodner RB, Armbrust EV [pplacer: linear time maximum-likelihood and Bayesian phylogenetic placement of sequences onto a fixed reference tree.](https://doi.org/10.1186/1471-2105-11-538) _BMC Bioinformatics_ 11, 538 (2010)
  
84. __[Prodigal](https://github.com/hyattpd/Prodigal)__  
Fast, reliable protein-coding gene prediction for prokaryotic genomes.  
Hyatt D, Chen G-L, LoCascio PF, Land ML, Larimer FW, Hauser LJ [Prodigal: prokaryotic gene recognition and translation initiation site identification.](https://doi.org/10.1186/1471-2105-11-119) _BMC Bioinformatics_ 11.1 119 (2010)
  
85. __[Prokka](https://github.com/tseemann/prokka)__  
Rapid prokaryotic genome annotation  
Seemann T [Prokka: rapid prokaryotic genome annotation](http://dx.doi.org/10.1093/bioinformatics/btu153) _Bioinformatics_ 30, 2068–2069 (2014)
  
86. __[QUAST](http://quast.sourceforge.net/)__  
Quality Assessment Tool for Genome  
Gurevich A, Saveliev V, Vyahhi N, Tesler G [QUAST: quality assessment tool for genome assemblies.](http://dx.doi.org/10.1093/bioinformatics/btt086) _Bioinformatics_ 29, 1072–1075 (2013)
  
87. __[Racon](https://github.com/lbcb-sci/racon)__  
Ultrafast consensus module for raw de novo genome assembly of long uncorrected reads  
Vaser R, Sović I, Nagarajan N, Šikić M [Fast and accurate de novo genome assembly from long uncorrected reads.](http://dx.doi.org/10.1101/gr.214270.116) _Genome Res_ 27, 737–746 (2017)
  
88. __[Rasusa](https://github.com/mbhall88/rasusa)__  
Randomly subsample sequencing reads to a specified coverage  
Hall MB [Rasusa: Randomly subsample sequencing reads to a specified coverage.](https://doi.org/10.5281/zenodo.3731394) (2019).
  
89. __[Raven](https://github.com/lbcb-sci/raven)__  
De novo genome assembler for long uncorrected reads  
Vaser R, Šikić M [Time- and memory-efficient genome assembly with Raven.](https://doi.org/10.1038/s43588-021-00073-4) _Nat Comput Sci_ 1, 332–336 (2021)
  
90. __[Resistance Gene Identifier (RGI)](https://github.com/arpcard/rgi)__  
Software to predict resistomes from protein or nucleotide data, based on homology and SNP models.  
Alcock BP, Raphenya AR, Lau TTY, Tsang KK, Bouchard M, Edalatmand A, Huynh W, Nguyen A-L V, Cheng AA, Liu S, Min SY, Miroshnichenko A, Tran H-K, Werfalli RE, Nasir JA, Oloni M, Speicher DJ, Florescu A, Singh B, Faltyn M, Hernandez-Koutoucheva A, Sharma AN, Bordeleau E, Pawlowski AC, Zubyk HL, Dooley D, Griffiths E, Maguire F, Winsor GL, Beiko RG, Brinkman FSL, Hsiao WWL, Domselaar GV, McArthur AG [CARD 2020: antibiotic resistome surveillance with the comprehensive antibiotic resistance database.](https://doi.org/10.1093/nar/gkz935) _Nucleic acids research_ 48.D1, D517-D525 (2020)
  
91. __[RNAmmer](http://www.cbs.dtu.dk/services/RNAmmer/)__  
Consistent and rapid annotation of ribosomal RNA genes  
Lagesen K, Hallin P, Rødland EA, Stærfeldt H-H, Rognes T, Ussery DW [RNAmmer: consistent annotation of rRNA genes in genomic sequences.](https://dx.doi.org/10.1093%2Fnar%2Fgkm160) _Nucleic Acids Res_ 35.9: 3100-3108 (2007)
  
92. __[Roary](https://github.com/sanger-pathogens/Roary)__  
Rapid large-scale prokaryote pan genome analysis  
Page AJ, Cummins CA, Hunt M, Wong VK, Reuter S, Holden MTG, Fookes M, Falush D, Keane JA, Parkhill J [Roary: rapid large-scale prokaryote pan genome analysis.](https://doi.org/10.1093/bioinformatics/btv421) _Bioinformatics_ 31, 3691–3693 (2015)
  
93. __[samclip](https://github.com/tseemann/samclip)__  
Filter SAM file for soft and hard clipped alignments  
Seemann T [Samclip: Filter SAM file for soft and hard clipped alignments](https://github.com/tseemann/samclip) (GitHub)
  
94. __[Samtools](https://github.com/samtools/samtools)__  
Tools for manipulating next-generation sequencing data  
Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R [The Sequence Alignment/Map format and SAMtools](http://dx.doi.org/10.1093/bioinformatics/btp352). _Bioinformatics_ 25, 2078–2079 (2009)
  
95. __[Scoary](https://github.com/AdmiralenOla/Scoary)__  
Pan-genome wide association studies  
Brynildsrud O, Bohlin J, Scheffer L, Eldholm V [Rapid scoring of genes in microbial pan-genome-wide association studies with Scoary.](https://doi.org/10.1186/s13059-016-1108-8) _Genome Biol._ 17:238 (2016)
  
96. __[SeqSero2](https://github.com/denglab/SeqSero2)__  
Salmonella serotype prediction from genome sequencing data  
Zhang S, Den-Bakker HC, Li S, Dinsmore BA, Lane C, Lauer AC, Fields PI, Deng X. [SeqSero2: rapid and improved Salmonella serotype determination using whole genome sequencing data.](https://doi.org/10.1128/AEM.01746-19) _Appl Environ Microbiology_ 85(23):e01746-19 (2019)
  
97. __[Seqtk](https://github.com/lh3/seqtk)__  
A fast and lightweight tool for processing sequences in the FASTA or FASTQ format.  
Li H [Toolkit for processing sequences in FASTA/Q formats](https://github.com/lh3/seqtk) (GitHub)
  
98. __[Seroba](https://github.com/sanger-pathogens/seroba)__  
k-mer based pipeline to identify the serotype of _Streptococcus pneumoniae_ from Illumina NGS reads  
Epping L, van Tonder AJ, Gladstone RA, The Global Pneumococcal Sequencing Consortium, Bentley SD, Page AJ, Keane JA [SeroBA: rapid high-throughput serotyping of Streptococcus pneumoniae from whole genome sequence data.](https://doi.org/10.1099/mgen.0.000186) _Microbial Genomics_, 4(7) (2018)
  
99. __[ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper)__  
Shigella serotype from Illumina or Oxford Nanopore reads  
Wu Y, Lau HK, Lee T, Lau DK, Payne J [In Silico Serotyping Based on Whole-Genome Sequencing Improves the Accuracy of Shigella Identification.](https://doi.org/10.1128/AEM.00165-19) *Applied and Environmental Microbiology*, 85(7). (2019)
  
100. __[Shovill](https://github.com/tseemann/shovill)__  
Faster assembly of Illumina reads  
Seemann T [Shovill: De novo assembly pipeline for Illumina paired reads](https://github.com/tseemann/shovill) (GitHub)
  
101. __[SignalP](http://www.cbs.dtu.dk/services/SignalP-4.0/)__  
SISTR (Salmonella In Silico Typing Resource) command-line tool  
Petersen TN, Brunak S, von Heijne G, Nielsen H [SignalP 4.0: discriminating signal peptides from transmembrane regions.](https://doi.org/10.1038/nmeth.1701) _Nature methods_ 8.10: 785 (2011)
  
102. __[SISTR](https://github.com/phac-nml/sistr_cmd)__  
Finds signal peptide features in CDS  
Yoshida CE, Kruczkiewicz P, Laing CR, Lingohr EJ, Gannon VPJ, Nash JHE, Taboada EN [The Salmonella In Silico Typing Resource (SISTR): An Open Web-Accessible Tool for Rapidly Typing and Subtyping Draft Salmonella Genome Assemblies.](https://doi.org/10.1371/journal.pone.0147101) _PloS One_, 11(1), e0147101. (2016)
  
103. __[SKESA](https://github.com/ncbi/SKESA)__  
Strategic Kmer Extension for Scrupulous Assemblies  
Souvorov A, Agarwala R, Lipman DJ [SKESA: strategic k-mer extension for scrupulous assemblies.](https://doi.org/10.1186/s13059-018-1540-z) _Genome Biology_ 19:153 (2018)
  
104. __[Snippy](https://github.com/tseemann/snippy)__  
Rapid haploid variant calling and core genome alignment  
Seemann T [Snippy: fast bacterial variant calling from NGS reads](https://github.com/tseemann/snippy) (GitHub)
  
105. __[SnpEff](http://snpeff.sourceforge.net/)__  
Genomic variant annotations and functional effect prediction toolbox.  
Cingolani P, Platts A, Wang LL, Coon M, Nguyen T, Wang L, Land SJ, Lu X, Douglas M [A program for annotating and predicting the effects of single nucleotide polymorphisms, SnpEff: SNPs in the genome of Drosophila melanogaster strain w1118; iso-2; iso-3.](https://doi.org/10.4161/fly.19695) _Fly_ 6(2), 80-92 (2012)
  
106. __[snp-dists](https://github.com/tseemann/snp-dists)__  
Pairwise SNP distance matrix from a FASTA sequence alignment  
Seemann T [snp-dists - Pairwise SNP distance matrix from a FASTA sequence alignment.](https://github.com/tseemann/snp-dists) (GitHub)
  
107. __[SNP-sites](https://github.com/sanger-pathogens/snp-sites)__  
Rapidly extracts SNPs from a multi-FASTA alignment.  
Page AJ, Taylor B, Delaney AJ, Soares J, Seemann T, Keane JA, Harris SR [SNP-sites: rapid efficient extraction of SNPs from multi-FASTA alignments.](https://dx.doi.org/10.1099%2Fmgen.0.000056) _Microbial Genomics_ 2.4 (2016)
  
108. __[Sourmash](https://github.com/dib-lab/sourmash)__  
Compute and compare MinHash signatures for DNA data sets.  
Brown CT, Irber L [sourmash: a library for MinHash sketching of DNA](http://dx.doi.org/10.21105/joss.00027). _JOSS_ 1, 27 (2016)
  
109. __[SPAdes](https://github.com/ablab/spades)__  
An assembly toolkit containing various assembly pipelines.  
Bankevich A, Nurk S, Antipov D, Gurevich AA, Dvorkin M, Kulikov AS, Lesin VM, Nikolenko SI, Pham S, Prjibelski AD, Pyshkin AV, Sirotkin AV, Vyahhi N, Tesler G, Alekseyev MA, Pevzner PA [SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing.](https://doi.org/10.1089/cmb.2012.0021) _Journal of computational biology_ 19.5 455-477 (2012)
  
110. __[spaTyper](https://github.com/HCGB-IGTP/spaTyper)__  
Computational method for finding spa types.  
Sanchez-Herrero JF, and Sullivan M [spaTyper: Staphylococcal protein A (spa) characterization pipeline](http://doi.org/10.5281/zenodo.4063625). Zenodo. (2020)
  
111. __[spaTyper Database](https://cge.cbs.dtu.dk/services/spatyper/)__  
Database used by spaTyper  
Harmsen D, Claus H, Witte W, Rothgänger J, Claus H, Turnwald D, and Vogel U [Typing of methicillin-resistant _Staphylococcus aureus_ in a university hospital setting using a novel software for spa-repeat determination and database management.](https://doi.org/10.1128/jcm.41.12.5442-5448.2003) _J. Clin. Microbiol._ 41:5442-5448 (2003)
  
112. __[SsuisSero](https://github.com/jimmyliu1326/SsuisSero)__  
Rapid _Streptococcus suis_ serotyping  
Lui J [SsuisSero: Rapid _Streptococcus suis_ serotyping](https://github.com/jimmyliu1326/SsuisSero) (GitHub)
  
113. __[staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec)__  
A standalone version of Staphopia's SCCmec typing method.  
Petit III RA, Read TD [_Staphylococcus aureus_ viewed from the perspective of 40,000+ genomes.](http://dx.doi.org/10.7717/peerj.5261) _PeerJ_ 6, e5261 (2018)
  
114. __[TBProfiler](https://github.com/jodyphelan/TBProfiler)__  
Profiling tool for _Mycobacterium tuberculosis_ to detect resistance and strain type  
Phelan JE, O’Sullivan DM, Machado D, Ramos J, Oppong YEA, Campino S, O’Grady J, McNerney R, Hibberd ML, Viveiros M, Huggett JF, Clark TG [Integrating informatics tools and portable sequencing technology for rapid detection of resistance to anti-tuberculous drugs.](https://doi.org/10.1186/s13073-019-0650-x) _Genome Med_ 11, 41 (2019)
  
115. __[Trimmomatic](http://www.usadellab.org/cms/index.php?page=trimmomatic)__  
A flexible read trimming tool for Illumina NGS data  
Bolger AM, Lohse M, Usadel B [Trimmomatic: a flexible trimmer for Illumina sequence data.](https://doi.org/10.1093/bioinformatics/btu170) _Bioinformatics_ 30.15 2114-2120 (2014)
  
116. __[Unicycler](https://github.com/rrwick/Unicycler)__  
Hybrid assembly pipeline for bacterial genomes  
Wick RR, Judd LM, Gorrie CL, Holt KE [Unicycler: Resolving bacterial genome assemblies from short and long sequencing reads.](http://dx.doi.org/10.1371/journal.pcbi.1005595) _PLoS Comput. Biol._ 13, e1005595 (2017)
  
117. __[VCF-Annotator](https://github.com/rpetit3/vcf-annotator)__  
Add biological annotations to variants in a VCF file.  
Petit III RA [VCF-Annotator: Add biological annotations to variants in a VCF file.](https://github.com/rpetit3/vcf-annotator) (GitHub)
  
118. __[Vcflib](https://github.com/vcflib/vcflib)__  
a simple C++ library for parsing and manipulating VCF files  
Garrison E [Vcflib: A C++ library for parsing and manipulating VCF files](https://github.com/vcflib/vcflib) (GitHub)
  
119. __[Velvet](https://github.com/dzerbino/velvet)__  
Short read de novo assembler using de Bruijn graphs  
Zerbino DR, Birney E [Velvet: algorithms for de novo short read assembly using de Bruijn graphs.](http://www.genome.org/cgi/doi/10.1101/gr.074492.107) _Genome research_ 18.5 821-829 (2008)
  
120. __[VSEARCH](https://github.com/torognes/vsearch)__  
Versatile open-source tool for metagenomics  
Rognes T, Flouri T, Nichols B, Quince C, Mahé F [VSEARCH: a versatile open source tool for metagenomics.](https://doi.org/10.7717/peerj.2584) _PeerJ_ 4, e2584 (2016)
  
121. __[vt](https://github.com/atks/vt)__  
A tool set for short variant discovery in genetic sequence data.  
Tan A, Abecasis GR, Kang HM [Unified representation of genetic variants.](https://doi.org/10.1093/bioinformatics/btv112) _Bioinformatics_ 31(13), 2202-2204 (2015)
  
