# System Shutdown Protocol

An offline, family-facing handbook authored in Markdown and built with [Hugo](https://gohugo.io/).

## Build

Hugo extended v0.152 or later is recommended.

```sh
hugo --minify
```

The offline site is written to `dist/`. Open `dist/index.html` directly in a browser; no web server or internet connection is required.

For local authoring with automatic refresh:

```sh
hugo server --disableFastRender
```

Then open the address printed by Hugo. The development server is only for editing—the final `dist/` folder remains fully offline.

## Edit content

Family-facing pages live in [`content/`](content/). Page order is controlled by the `weight` field in each file’s front matter.

Site configuration, including the review date, is in [`hugo.toml`](hugo.toml). Styling is in [`static/css/site.css`](static/css/site.css).

Before distributing a build:

1. Replace every `[placeholder]` with real information or remove it.
2. Set `params.lastReviewed` in `hugo.toml`.
3. Run `hugo --minify`.
4. Open `dist/index.html` on another device with networking disabled.
5. Copy the **entire** `dist/` directory, not only `index.html`.

## Security

The generated HTML is not encrypted. Do not put passwords, recovery codes, private keys, security-question answers, or unnecessary complete account numbers in this repository.

Use the handbook to point family members to a separate protected inventory and credential-recovery process. Review repository history before making it public or sharing it.
