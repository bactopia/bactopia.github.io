import type {ComponentType} from 'react';
import {MdTimer, MdLightbulb, MdStar, MdFavorite, MdBuild, MdBiotech} from 'react-icons/md';
import {GoArrowRight, GoVideo} from 'react-icons/go';
import {SiGooglescholar} from 'react-icons/si';

const ICON_MAP: Record<string, ComponentType<{size?: number; className?: string}>> = {
  'material-clock-fast': MdTimer,
  'material-bacteria': MdBiotech,
  'material-lightbulb-on': MdLightbulb,
  'material-star': MdStar,
  'material-heart': MdFavorite,
  'material-tools': MdBuild,
  'octicons-arrow-right-24': GoArrowRight,
  'octicons-video-24': GoVideo,
  'simple-googlescholar': SiGooglescholar,
};

interface IconProps {
  name: string;
  size?: number;
  className?: string;
}

export default function Icon({name, size = 24, className}: IconProps) {
  const IconComponent = ICON_MAP[name];
  if (!IconComponent) return null;
  return <IconComponent size={size} className={className} />;
}
