import ComponentTypes from '@theme-original/NavbarItem/ComponentTypes';
import GitHubNavbarItem from '@site/src/components/GitHubNavbarItem';
import SlackNavbarItem from '@site/src/components/SlackNavbarItem';

export default {
  ...ComponentTypes,
  'custom-slack': SlackNavbarItem,
  'custom-github': GitHubNavbarItem,
};
