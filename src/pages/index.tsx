import Layout from '@theme/Layout';
import {CardGrid, Card} from '../components/CardGrid';
import styles from './index.module.css';

export default function Home() {
  return (
    <Layout
      title="Home"
      description="An extensive workflow to process Nanopore and Illumina sequencing for bacterial genomes."
    >
      <main>
        <section className={styles.hero}>
          <img
            src="/img/bactopia-logo.png"
            alt="Bactopia"
            className={styles.heroLogo}
          />
          <p className={styles.tagline}>
            An extensive workflow to process Nanopore and Illumina sequencing
            for bacterial genomes.
          </p>
        </section>

        <section className={styles.section}>
          <CardGrid columns={2}>
            <Card
              icon="material-clock-fast"
              title="Set up in minutes"
              description="Install bactopia from Bioconda and start processing genomes in minutes"
              link="/docs/installation"
              linkText="Installation"
            />
            <Card
              icon="material-bacteria"
              title="Effortless bacterial genomics"
              description="Streamlined pipeline for efficient and complete analysis of bacterial genomes"
              link="/docs/beginners-guide"
              linkText="Beginner's Guide"
            />
            <Card
              icon="material-lightbulb-on"
              title="Seamlessly expand analyses"
              description="Rapidly extend studies with a variety of supplementary, ready-made, workflows"
              link="/docs/bactopia-tools/"
              linkText="Bactopia Tools"
            />
            <Card
              icon="material-star"
              title="Making an impact"
              description="A free and open-source tool that regularly contributes back to the community"
              link="/impact/"
              linkText="Impact and Outreach"
            />
          </CardGrid>
        </section>

        <section className={`${styles.section} ${styles.overview}`}>
          <h2 className={styles.sectionTitle}>Overview</h2>
          <p>
            Bactopia is a flexible pipeline for complete analysis of bacterial
            genomes. The goal of Bactopia is process your data with a broad set
            of tools, so that you can get to the fun part of analyses quicker!
          </p>
          <p>
            Bactopia was inspired by{' '}
            <a href="https://staphopia.github.io/">Staphopia</a>, a workflow
            targeted towards <em>Staphylococcus aureus</em> genomes. Using what
            we learned from Staphopia and user feedback, Bactopia was developed
            from scratch with usability, portability, and speed in mind from the
            start.
          </p>
          <p>
            Bactopia uses <a href="https://www.nextflow.io/">Nextflow</a> to
            manage the workflow, allowing for support of many types of
            environments (e.g. cluster or cloud). Bactopia allows for the usage
            of many public datasets as well as your own datasets to further
            enhance the analysis of your sequencing. Bactopia only uses software
            packages available from{' '}
            <a href="https://bioconda.github.io/">Bioconda</a> and{' '}
            <a href="https://conda-forge.org/">Conda-Forge</a> to make
            installation as simple as possible for <em>all</em> users.
          </p>
          <a href="/img/bactopia-workflow.png" target="_blank" rel="noopener">
            <img
              src="/img/bactopia-workflow.png"
              alt="Bactopia Workflow"
              className={styles.workflowImg}
            />
          </a>
        </section>

        <section className={styles.section}>
          <h2 className={styles.sectionTitle}>Funding</h2>
          <p>
            Support for this project came (in part) from an Emory Public Health
            Bioinformatics Fellowship funded by the{' '}
            <a href="https://dph.georgia.gov/EIP">
              CDC Emerging Infections Program
            </a>
            , the{' '}
            <a href="https://health.wyo.gov/publichealth/">
              Wyoming Public Health Division
            </a>
            , and the{' '}
            <a href="https://www.linkedin.com/company/center-for-applied-pathogen-epidemiology-and-outbreak-control/">
              Center for Applied Pathogen Epidemiology and Outbreak Control
              (CAPE)
            </a>
            .
          </p>
          <div className={styles.funding}>
            <a href="https://dph.georgia.gov/EIP">
              <img
                src="/img/gaeip-banner.png"
                alt="Georgia Emerging Infections Program"
                style={{width: '140px'}}
              />
            </a>
            <a href="https://health.wyo.gov/publichealth/">
              <img
                src="/img/wyphd-banner.jpg"
                alt="Wyoming Public Health Division"
                style={{width: '280px'}}
              />
            </a>
            <a href="https://www.linkedin.com/company/center-for-applied-pathogen-epidemiology-and-outbreak-control/">
              <img
                src="/img/cape-banner.png"
                alt="Center for Applied Pathogen Epidemiology and Outbreak Control"
                style={{width: '185px'}}
              />
            </a>
          </div>
        </section>

        <section className={styles.section}>
          <h2 className={styles.sectionTitle}>Citing Bactopia</h2>
          <p className={styles.citation}>
            Petit III RA, Read TD.{' '}
            <a href="https://doi.org/10.1128/mSystems.00190-20">
              Bactopia - a flexible pipeline for complete analysis of bacterial
              genomes.
            </a>{' '}
            <em>mSystems</em> 5 (2020)
          </p>
        </section>
      </main>
    </Layout>
  );
}
