import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import Icon from './Icon';
import styles from './CardGrid.module.css';

interface CardGridProps {
  children: ReactNode;
  columns?: 2 | 3 | 4;
}

export function CardGrid({children, columns = 2}: CardGridProps) {
  const columnClass = styles[`columns${columns}`];
  return <div className={`${styles.grid} ${columnClass}`}>{children}</div>;
}

interface CardProps {
  icon?: string;
  title: string;
  description: string;
  link?: string;
  linkText?: string;
}

export function Card({icon, title, description, link, linkText = 'Learn more'}: CardProps) {
  return (
    <div className={styles.card}>
      {icon && (
        <div className={styles.cardIcon}>
          <Icon name={icon} size={40} />
        </div>
      )}
      <div className={styles.cardTitle}>{title}</div>
      <div className={styles.cardDescription}>{description}</div>
      {link && (
        <Link className={styles.cardLink} to={link}>
          {linkText} <Icon name="octicons-arrow-right-24" size={16} />
        </Link>
      )}
    </div>
  );
}
