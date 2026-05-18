## Portuguese Translation Rules (Brazilian Portuguese)

Translation prompts adapted from the Nextflow Training project:
https://github.com/nextflow-io/training/blob/master/TRANSLATING.md

### Tone and Style

- Use **Brazilian Portuguese** spelling conventions (e.g., "arquivo" not "ficheiro").
- Use informal "voce" form consistently.
- Write in a clear, direct style appropriate for technical documentation.

### Key Term Translations

Use these translations consistently throughout:

| English | Portuguese |
|---------|-----------|
| workflow | fluxo de trabalho |
| pipeline | pipeline |
| assembly | montagem |
| reads | reads |
| contig | contig |
| scaffold | scaffold |
| annotation | anotacao |
| antimicrobial resistance | resistencia antimicrobiana |
| virulence | virulencia |
| serotype | sorotipo |
| sequence type | tipo de sequencia |
| quality control | controle de qualidade |
| trimming | trimagem |
| mapping | mapeamento |
| variant calling | chamada de variantes |
| phylogenetics | filogenetica |
| pan-genome | pan-genoma |
| reference genome | genoma de referencia |
| sample | amostra |
| input | entrada |
| output | saida |
| parameter | parametro |
| module | modulo |
| subworkflow | subworkflow |
| tool | ferramenta |
| installation | instalacao |
| quick start | inicio rapido |
| tutorial | tutorial |
| developer | desenvolvedor |
| citation | citacao |
| acknowledgement | agradecimento |
| usage | uso |

### Terms to keep in English

These terms should NEVER be translated, even in prose:

- Bactopia, Nextflow, nf-core, Conda, Bioconda, Docker, Singularity, Apptainer
- All bioinformatics tool names (e.g., Prokka, Bakta, ABRicate, MLST, Snippy)
- File formats: FASTQ, FASTA, GFF, VCF, BAM, SAM, TSV, CSV, JSON, YAML
- reads, contigs, scaffolds (when used as data type nouns)
- Software concepts: fork, pull request, branch, commit, merge

### Admonition titles

| English | Portuguese |
|---------|-----------|
| Note | Nota |
| Tip | Dica |
| Info | Informacao |
| Warning | Aviso |
| Danger | Perigo |
| Caution | Cuidado |

### Common pitfalls to avoid

1. Do NOT translate code syntax or parameter names.
2. Do NOT translate console output or command examples.
3. Do NOT use European Portuguese spelling.
4. Do NOT translate scientific citations -- keep them in English exactly as written.
5. Keep tool names in English even when they could be translated (e.g., do NOT translate
   "Assembler" to "Montador" when it is a tool name).
