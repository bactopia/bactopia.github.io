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

  headTags: [
    {
      tagName: 'link',
      attributes: {
        rel: 'alternate',
        type: 'text/plain',
        href: '/llms.txt',
        title: 'LLM-readable site index',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'alternate',
        type: 'application/json',
        href: '/catalog.json',
        title: 'Machine-readable documentation catalog',
      },
    },
  ],

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

  themes: [
    '@docusaurus/theme-mermaid',
    [
      '@easyops-cn/docusaurus-search-local',
      {
        hashed: true,
        indexBlog: true,
        indexDocs: true,
        docsRouteBasePath: ['/', 'bactopia-tools', 'bactopia-pipelines', 'developers', 'impact-and-outreach'],
        docsDir: ['docs', 'bactopia-tools', 'bactopia-pipelines', 'developers', 'impact'],
        highlightSearchTermsOnTargetPage: true,
      },
    ],
  ],

  clientModules: ['./src/gtag-noop.js'],

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
        id: 'bactopia-tools',
        path: 'bactopia-tools',
        routeBasePath: 'bactopia-tools',
        sidebarPath: './sidebars-bactopia-tools.ts',
        editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'bactopia-pipelines',
        path: 'bactopia-pipelines',
        routeBasePath: 'bactopia-pipelines',
        sidebarPath: './sidebars-bactopia-pipelines.ts',
        editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'developers',
        path: 'developers',
        routeBasePath: 'developers',
        sidebarPath: './sidebars-developers.ts',
        editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
        async sidebarItemsGenerator({defaultSidebarItemsGenerator, ...args}: any) {
          const items = await defaultSidebarItemsGenerator(args);
          return items.filter((item: any) => !(item.type === 'doc' && item.id?.endsWith('/index')));
        },
      },
    ],
  ],

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
            'impact-and-outreach/**',
          ],
          lastVersion: 'current',
          versions: {
            current: {
              label: 'dev',
              path: '',
              badge: false,
            },
          },
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/bactopia/bactopia.github.io/edit/master/',
          blogTitle: 'Bactopia Blog',
          blogDescription: 'News, tutorials, and updates from the Bactopia project.',
          blogSidebarCount: 'ALL',
          feedOptions: {
            type: ['rss', 'atom'],
            title: 'Bactopia Blog',
            description: 'News, tutorials, and updates from the Bactopia project.',
            copyright: `Copyright ${new Date().getFullYear()} Robert A. Petit III`,
          },
        },
        theme: {
          customCss: './src/css/custom.css',
        },
        ...(process.env.NODE_ENV === 'production' && {
          gtag: {
            trackingID: 'G-QH76FN9N78',
            anonymizeIP: true,
          },
        }),
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/bactopia-small-logo.png',
    navbar: {
      style: 'primary',
      title: '',
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
          sidebarId: 'bactopia-tools',
          docsPluginId: 'bactopia-tools',
          position: 'left',
          label: 'Bactopia Tools',
        },
        {
          type: 'docSidebar',
          sidebarId: 'bactopia-pipelines',
          docsPluginId: 'bactopia-pipelines',
          position: 'left',
          label: 'Bactopia Pipelines',
        },
        {
          type: 'docSidebar',
          sidebarId: 'developers',
          docsPluginId: 'developers',
          position: 'left',
          label: 'Developers',
        },
        {
          type: 'docSidebar',
          sidebarId: 'impact',
          docsPluginId: 'impact',
          position: 'left',
          label: 'Impact & Outreach',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          type: 'docsVersionDropdown',
          position: 'right',
          dropdownItemsAfter: [
            {type: 'html', value: '<hr style="margin: 0.3rem 0">'},
            {href: 'pathname:///v3.1.0/', label: 'v3.1.0', target: '_self'},
            {href: 'pathname:///v3.0.1/', label: 'v3.0.1', target: '_self'},
            {href: 'pathname:///v3.0.0/', label: 'v3.0.0', target: '_self'},
            {href: 'pathname:///v2.2.0/', label: 'v2.2.0', target: '_self'},
            {href: 'pathname:///v2.1.1/', label: 'v2.1.1', target: '_self'},
            {href: 'pathname:///v2.1.0/', label: 'v2.1.0', target: '_self'},
          ],
        },
        {
          type: 'search',
          position: 'right',
        },
        {
          type: 'custom-slack',
          position: 'right',
        },
        {
          type: 'custom-github',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Bactopia',
          items: [
            {
              label: 'Quick Start',
              to: '/quick-start',
            },
            {
              label: 'Installation',
              to: '/installation',
            },
            {
              label: 'CLI Reference',
              to: '/developers/cli/',
            },
          ],
        },
        {
          title: 'More Resources',
          items: [
            {
              label: 'Bactopia Tools',
              to: '/bactopia-tools/',
            },
            {
              label: 'Bactopia Pipelines',
              to: '/bactopia-pipelines/',
            },
            {
              label: 'Developers',
              to: '/developers/',
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
              label: 'Bluesky',
              href: 'https://bsky.app/profile/bactopia.io',
            },
            {
              label: 'Slack',
              href: 'pathname:///slack/',
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
