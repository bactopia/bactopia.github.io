import type {LoadContext, Plugin} from '@docusaurus/types';
import path from 'path';
import fs from 'fs/promises';
import satori from 'satori';
import {Resvg} from '@resvg/resvg-js';

const CARD_WIDTH = 1200;
const CARD_HEIGHT = 630;
const TEAL = '#009688';

function extractMeta(html: string): {title: string; description: string} {
  const titleMatch = html.match(/<title[^>]*>([^<]*)<\/title>/);
  const descMatch = html.match(
    /name=description\s+content="([^"]*)"/,
  );
  const rawTitle = titleMatch?.[1] ?? '';
  const title = rawTitle.replace(/\s*\|.*$/, '').trim();
  const description = descMatch?.[1] ?? '';
  return {title, description};
}

function htmlPathToSlug(outDir: string, htmlPath: string): string {
  const relative = path.relative(outDir, htmlPath);
  const withoutExt = relative.replace(/\.html$/, '');
  const normalized =
    withoutExt.endsWith('/index') || withoutExt === 'index'
      ? withoutExt.replace(/\/?index$/, '')
      : withoutExt;
  const slug = normalized.replace(/\//g, '--');
  return slug || 'index';
}

async function findHtmlFiles(dir: string): Promise<string[]> {
  const results: string[] = [];
  const entries = await fs.readdir(dir, {withFileTypes: true});
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === 'assets' || entry.name === 'img') continue;
      results.push(...(await findHtmlFiles(fullPath)));
    } else if (entry.name.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results;
}

export default function socialCardsPlugin(context: LoadContext): Plugin {
  return {
    name: 'docusaurus-plugin-social-cards',

    async postBuild({outDir}) {
      const {siteConfig} = context;
      const siteUrl = siteConfig.url;
      const baseUrl = siteConfig.baseUrl;

      const fontBold = await fs.readFile(
        path.join(context.siteDir, 'static/fonts/Ubuntu-Bold.ttf'),
      );
      const fontRegular = await fs.readFile(
        path.join(context.siteDir, 'static/fonts/Ubuntu-Regular.ttf'),
      );

      const logoData = await fs.readFile(
        path.join(context.siteDir, 'static/img/bactopia-large-logo.png'),
      );
      const logoBase64 = `data:image/png;base64,${logoData.toString('base64')}`;

      const cardsDir = path.join(outDir, 'img', 'social-cards');
      await fs.mkdir(cardsDir, {recursive: true});

      const htmlFiles = await findHtmlFiles(outDir);
      let generated = 0;

      for (const htmlPath of htmlFiles) {
        const html = await fs.readFile(htmlPath, 'utf-8');
        const {title, description} = extractMeta(html);

        if (!title || title === '404') continue;

        const slug = htmlPathToSlug(outDir, htmlPath);
        const cardFilename = `${slug}.png`;
        const cardPath = path.join(cardsDir, cardFilename);
        const cardUrl = `${siteUrl}${baseUrl}img/social-cards/${cardFilename}`;

        const svg = await satori(
          {
            type: 'div',
            props: {
              style: {
                display: 'flex',
                flexDirection: 'column',
                width: CARD_WIDTH,
                height: CARD_HEIGHT,
                backgroundColor: TEAL,
                padding: '50px 60px',
                fontFamily: 'Ubuntu',
                color: 'white',
              },
              children: [
                {
                  type: 'div',
                  props: {
                    style: {
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'flex-start',
                    },
                    children: [
                      {
                        type: 'div',
                        props: {
                          style: {
                            fontSize: 28,
                            fontWeight: 700,
                          },
                          children: 'Bactopia',
                        },
                      },
                      {
                        type: 'img',
                        props: {
                          src: logoBase64,
                          width: 140,
                          height: 161,
                          style: {
                            marginTop: -10,
                          },
                        },
                      },
                    ],
                  },
                },
                {
                  type: 'div',
                  props: {
                    style: {
                      display: 'flex',
                      flex: 1,
                      alignItems: 'center',
                      fontSize: 56,
                      fontWeight: 700,
                      lineHeight: 1.2,
                      maxWidth: '85%',
                      overflow: 'hidden',
                    },
                    children: title,
                  },
                },
                {
                  type: 'div',
                  props: {
                    style: {
                      fontSize: 22,
                      lineHeight: 1.4,
                      opacity: 0.9,
                      maxWidth: '80%',
                      overflow: 'hidden',
                    },
                    children: description || siteConfig.tagline,
                  },
                },
              ],
            },
          },
          {
            width: CARD_WIDTH,
            height: CARD_HEIGHT,
            fonts: [
              {name: 'Ubuntu', data: fontBold, weight: 700, style: 'normal'},
              {name: 'Ubuntu', data: fontRegular, weight: 400, style: 'normal'},
            ],
          },
        );

        const resvg = new Resvg(svg, {
          fitTo: {mode: 'width', value: CARD_WIDTH},
        });
        const png = resvg.render().asPng();
        await fs.writeFile(cardPath, png);

        const updatedHtml = html
          .replace(
            /(property=og:image\s+content=)("[^"]*"|[^\s>]+)/,
            `$1${cardUrl}`,
          )
          .replace(
            /(name=twitter:image\s+content=)("[^"]*"|[^\s>]+)/,
            `$1${cardUrl}`,
          );

        if (updatedHtml !== html) {
          await fs.writeFile(htmlPath, updatedHtml);
        }

        generated++;
      }

      console.log(
        `[social-cards] Generated ${generated} social card images in ${cardsDir}`,
      );
    },
  };
}
