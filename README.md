# Mohd Zaki

Academic website for Mohd Zaki. It is a Hugo site with no database and no API keys. The pages are Markdown. Publications, teaching, awards, conferences, news, and the CV are YAML in `data/`.

The visual reference is a text-first professor’s homepage. Colors come from the [Johns Hopkins palette](https://brand.jhu.edu/visual-identity/colors/). A season control in the header changes the accent. The background stays white and the text stays sable.

[pmichaillat/hugo-website](https://github.com/pmichaillat/hugo-website) is MIT-licensed and was reviewed as a structural reference. These templates are not a copy of that repository.

## Run it locally

Install [Hugo 0.168.0](https://github.com/gohugoio/hugo/releases/tag/v0.168.0) (the standard build is enough).

```bash
hugo server
```

Open the URL Hugo prints, usually http://localhost:1313/.

A production build:

```bash
hugo --minify --baseURL "https://example.org/"
```

Set `--baseURL` to the real site address. For a project site that is `https://USER.github.io/REPO/`. For a user site or a custom domain it is the site root, with a trailing slash.

## Edit the site

| What | Where |
| --- | --- |
| Name, biography, affiliation, email, links, photo, CV file | `data/profile.yaml` |
| Research directions | `data/research.yaml` and `content/research/` |
| Publications | `data/publications.yaml` |
| Awards | `data/awards.yaml` |
| Teaching | `data/teaching.yaml` |
| Conferences | `data/conferences.yaml` |
| News | `data/news.yaml` |
| Education, appointments, service, skills | matching files in `data/` |
| Software and datasets | `data/software.yaml` |
| Collaborators | `data/collaborators.yaml` |
| Research impact | `data/impact.yaml` |
| Season colors | `assets/css/main.css` |
| How many news items and talks the homepage shows | `hugo.toml` |

Leave a profile link blank to hide it. `photo` is a path under `static/`, such as `images/portrait.jpg`. Google Scholar, ORCID, and LinkedIn are blank until you add verified URLs.

The public CV PDF is `static/cv/mohd-zaki-cv.pdf`. Replace that file when the CV changes, or point `cv_pdf` at another file in `static/`. The copy at the repository root is the source PDF used to seed the site.

Do not invent degrees, awards, collaborators, citation counts, or repository URLs. Empty sections are intentional.

`scripts/seed_from_cv.py` rewrites the CV-backed YAML files. Run it only when you intend to replace those files. After that, edit the YAML directly.

### Publications

Each record in `data/publications.yaml` can include authors, title, venue, year, type (`journal`, `conference`, `preprint`, `chapter`, `other`), topics, DOI, publisher or preprint URL, PDF, code, dataset, BibTeX, `featured`, and `open_access`.

Topics are `materials-ai`, `explainable-ai`, `structural-resilience`, and `scientific-ml`. `featured: true` adds the paper to the homepage selection. Set `open_access: true` only for a version you can share.

To draft records from BibTeX:

```bash
python3 scripts/bibtex_to_yaml.py papers.bib
```

Read the YAML, fill topics and links, and merge the records you want into `data/publications.yaml`. The site build does not run this script, and it does not publish anything by itself.

### Research impact

`data/impact.yaml` is the curated list of work that cites, extends, applies, or checks a specific paper. The public pages show records with `verified: true` only. A citation is not enough. Write `relationship_summary` after reading the paper, and set `cited_work_id` to an `id` in `data/publications.yaml`.

`relationship_category` is one of:

- Methods Extended
- Applications
- Follow-up Research
- Independent Validation
- Dataset or Software Reuse

The file ships with one unverified sample so the filter can be checked. Delete it when you add real records. Do not mark the sample verified.

Later, a separate script or GitHub Action can pull candidate papers from OpenAlex, Semantic Scholar, or Crossref. Keep that job out of the site build. Save candidates with `verified: false`. Review, edit, or delete them by hand. Never publish a newly discovered paper as verified impact. Do not scrape Google Scholar. If a workflow needs a token, store it as a GitHub Actions secret. The website itself does not need one.

### Seasons

Winter (December–February) uses Heritage Blue `#002D72`. Spring (March–May) uses Forest Green `#275E3D`. Summer (June–August) uses Medium Blue `#0077D8`. Autumn (September–November) uses Maroon `#6A202B`.

With no saved choice, the month picks the season. The header control stores the choice in the browser. Printing uses Heritage Blue. Spirit Blue is not used for text on white.

### Research pages

`content/research/` is Markdown. Placeholders are marked and should be replaced with sourced text. Figures use the built-in figure shortcode:

```
{{< figure src="/images/example.png" alt="Description" caption="Caption" >}}
```

Inline math uses `\(` and `\)`. Display math uses `$$`. Math rendering loads KaTeX from a CDN on research pages only. The rest of the site does not need that CDN.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` builds the site with Hugo 0.168.0 and deploys to GitHub Pages. It works for a user site and a project site because the Pages base URL is passed into Hugo.

In the repository settings, set Pages to “GitHub Actions.” The first deployment needs the `github-pages` environment, which GitHub creates when the workflow runs.

For a custom domain, add the domain in the Pages settings, put it in `static/CNAME`, and keep passing the Pages base URL from the workflow (it will be that domain).

Internal links use Hugo’s `relURL`, so they follow the base URL.

## What is still open

- Google Scholar, ORCID, and LinkedIn URLs
- A profile photograph
- DOI, PDF, code, and dataset links the CV does not list
- Verified software, datasets, and collaborators
- Reviewed research-impact records
- Sourced text for the four research pages
- Mentoring, supervision, outreach, tutorials, and memberships
