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
    format: 'detect',
    mermaid: true,
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

  themes: ['@docusaurus/theme-mermaid'],

  plugins: [
    'docusaurus-plugin-image-zoom',
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'impact',
        path: 'impact',
        routeBasePath: 'impact-and-outreach',
        sidebarPath: './sidebars-impact.ts',
        editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'workflows',
        path: 'workflows',
        routeBasePath: 'workflows',
        sidebarPath: './sidebars-workflows.ts',
        editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'subworkflows',
        path: 'subworkflows',
        routeBasePath: 'subworkflows',
        sidebarPath: './sidebars-subworkflows.ts',
        editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'modules',
        path: 'modules',
        routeBasePath: 'modules',
        sidebarPath: './sidebars-modules.ts',
        editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
      },
    ],
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: 'docs',
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
          exclude: [
            'custom/**',
            'assets/**',
            'blog/**',
            'data/**',
            'impact-and-outreach/**',
          ],
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
        },
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
          label: 'Bactopia',
        },
        {
          type: 'docSidebar',
          sidebarId: 'workflows',
          docsPluginId: 'workflows',
          position: 'left',
          label: 'Workflows',
        },
        {
          type: 'docSidebar',
          sidebarId: 'subworkflows',
          docsPluginId: 'subworkflows',
          position: 'left',
          label: 'Subworkflows',
        },
        {
          type: 'docSidebar',
          sidebarId: 'modules',
          docsPluginId: 'modules',
          position: 'left',
          label: 'Modules',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          type: 'docSidebar',
          sidebarId: 'impact',
          docsPluginId: 'impact',
          position: 'left',
          label: 'Impact & Outreach',
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
              to: '/docs/quick-start',
            },
            {
              label: 'Installation',
              to: '/docs/installation',
            },
            {
              label: 'CLI Reference',
              to: '/docs/cli/',
            },
          ],
        },
        {
          title: 'Pipelines',
          items: [
            {
              label: 'Workflows',
              to: '/workflows/',
            },
            {
              label: 'Subworkflows',
              to: '/subworkflows/',
            },
            {
              label: 'Modules',
              to: '/modules/',
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
            {
              label: 'Impact & Outreach',
              to: '/impact-and-outreach/',
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
    zoom: {
      selector: '.markdown :not(em) > img',
      background: {
        light: 'rgba(255, 255, 255, 0.9)',
        dark: 'rgba(50, 50, 50, 0.9)',
      },
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
