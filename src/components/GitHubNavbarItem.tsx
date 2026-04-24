import React, {useEffect, useState} from 'react';

interface GitHubStats {
  stars: number | null;
  forks: number | null;
  version: string | null;
}

const CACHE_KEY = 'bactopia-github-stats';
const CACHE_TTL = 1000 * 60 * 30;

function getCached(): GitHubStats | null {
  try {
    const raw = localStorage.getItem(CACHE_KEY);
    if (!raw) return null;
    const {data, ts} = JSON.parse(raw);
    if (Date.now() - ts > CACHE_TTL) return null;
    return data;
  } catch {
    return null;
  }
}

function setCache(data: GitHubStats) {
  try {
    localStorage.setItem(CACHE_KEY, JSON.stringify({data, ts: Date.now()}));
  } catch {}
}

function formatCount(n: number): string {
  if (n >= 1000) return (n / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
  return String(n);
}

export default function GitHubNavbarItem() {
  const [stats, setStats] = useState<GitHubStats>({stars: null, forks: null, version: null});

  useEffect(() => {
    const cached = getCached();
    if (cached) {
      setStats(cached);
      return;
    }

    const controller = new AbortController();

    Promise.all([
      fetch('https://api.github.com/repos/bactopia/bactopia', {signal: controller.signal})
        .then(r => r.json()),
      fetch('https://api.github.com/repos/bactopia/bactopia/releases/latest', {signal: controller.signal})
        .then(r => r.json()),
    ])
      .then(([repo, release]) => {
        const data: GitHubStats = {
          stars: repo.stargazers_count ?? null,
          forks: repo.forks_count ?? null,
          version: release.tag_name ?? null,
        };
        setStats(data);
        setCache(data);
      })
      .catch(() => {});

    return () => controller.abort();
  }, []);

  return (
    <a
      href="https://github.com/bactopia/bactopia"
      target="_blank"
      rel="noopener noreferrer"
      className="github-navbar-item"
    >
      <svg
        className="github-navbar-item__icon"
        viewBox="0 0 16 16"
        aria-hidden="true"
      >
        <path
          fillRule="evenodd"
          d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38
             0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13
             -.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87
             2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95
             0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21
             2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04
             2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82
             2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0
             1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016
             8c0-4.42-3.58-8-8-8z"
          fill="currentColor"
        />
      </svg>
      <span className="github-navbar-item__right">
        <span className="github-navbar-item__text">GitHub</span>
        {(stats.version || stats.stars !== null || stats.forks !== null) && (
          <span className="github-navbar-item__stats">
            {stats.version && (
              <span className="github-navbar-item__stat">{stats.version}</span>
            )}
            {stats.stars !== null && (
              <span className="github-navbar-item__stat">
                <svg viewBox="0 0 16 16" width="11" height="11" aria-hidden="true">
                  <path
                    fillRule="evenodd"
                    d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0
                       01.416 1.279l-3.046 2.97.719 4.192a.75.75 0
                       01-1.088.791L8 12.347l-3.766 1.98a.75.75 0
                       01-1.088-.79l.72-4.194L.818 6.374a.75.75 0
                       01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"
                    fill="currentColor"
                  />
                </svg>
                {formatCount(stats.stars)}
              </span>
            )}
            {stats.forks !== null && (
              <span className="github-navbar-item__stat">
                <svg viewBox="0 0 16 16" width="11" height="11" aria-hidden="true">
                  <path
                    fillRule="evenodd"
                    d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0
                       2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75
                       8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25
                       2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5
                       0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0
                       015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0
                       .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75
                       0 000 1.5z"
                    fill="currentColor"
                  />
                </svg>
                {formatCount(stats.forks)}
              </span>
            )}
          </span>
        )}
      </span>
    </a>
  );
}
