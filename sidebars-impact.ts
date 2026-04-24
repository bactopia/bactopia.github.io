import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  impact: [
    {
      type: 'category',
      label: 'Impact & Outreach',
      link: {type: 'doc', id: 'index'},
      items: [
        'acknowledgements',
        'citations',
        'enhancements',
        'presentations',
      ],
    },
  ],
};

export default sidebars;
