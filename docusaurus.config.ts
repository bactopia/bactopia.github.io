import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Bactopia',
  tagline: 'An extensive workflow to process Nanopore and Illumina sequencing for bacterial genomes.',
  favicon: 'img/favicon.ico',

  url: 'https://bactopia.github.io',
  baseUrl: '/',

  organizationName: 'bactopia',
  projectName: 'bactopia.github.io',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  future: {
    v4: true,
  },

  markdown: {
    format: 'md',
    parseFrontMatter: async (params) => {
      const result = await params.defaultParseFrontMatter(params);
      if (result.frontMatter.tags === null || result.frontMatter.tags === undefined) {
        delete result.frontMatter.tags;
      }
      return result;
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
          exclude: [
            'custom/**',
            'assets/**',
            'blog/**',
            'data/**',
          ],
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
        gtag: {
          trackingID: 'G-QH76FN9N78',
          anonymizeIP: true,
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/bactopia-small-logo.png',
    navbar: {
      title: 'Bactopia',
      logo: {
        alt: 'Bactopia Logo',
        src: 'img/bactopia-small-logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'bactopia',
          position: 'left',
          label: 'Docs',
        },
        {
          href: 'https://github.com/bactopia/bactopia',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Quick Start',
              to: '/quick-start',
            },
            {
              label: 'Installation',
              to: '/installation',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/bactopia/bactopia',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/rpetit3',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub Docs Repo',
              href: 'https://github.com/bactopia/bactopia.github.io',
            },
          ],
        },
      ],
      copyright: `Copyright \u00A9 2019-${new Date().getFullYear()} Robert A. Petit III. All rights reserved.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'yaml'],
    },
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
