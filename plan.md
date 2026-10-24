# Build a Minimalist Academic Research Website for Mohd Zaki

Act as a senior frontend developer, academic website designer, and scientific publishing specialist. Build a complete, polished, production-ready personal academic website for **Mohd Zaki**, designed for deployment on GitHub Pages.

Do not just provide suggestions or a mockup. Inspect the current repository, implement the website, create the required pages and components, test the build, and document how to maintain and deploy it.

## 1. Design inspiration and philosophy

My primary design reference is:
https://www.cse.iitd.ac.in/~mausam/

I like its information-rich, traditional academic homepage, with a concise biography, research interests, news, publications, and links to detailed academic pages.

I want a modernized version of this approach:
- Minimalist, scholarly, professional, and content-first.
- Inspired by the information hierarchy of a traditional professor's homepage.
- Modern typography, carefully balanced whitespace, restrained colors, and excellent readability.
- No oversized hero sections, unnecessary animations, excessive cards, gradient backgrounds, or startup-style marketing design.
- The homepage should communicate research expertise and academic contributions immediately.
- Optimize for researchers, professors, faculty search committees, collaborators, students, and scientific communities.

Use this existing project as the preferred starting point if the repository is empty or a suitable Hugo setup can be created from it:
https://github.com/pmichaillat/hugo-website

Review its current structure and license before adapting it. If the repository already contains a functioning website, inspect it first and preserve useful existing work.

## 2. Technology stack and deployment

Preferred stack:
- Hugo static site generator.
- Markdown for page content.
- YAML or TOML for configuration and structured content.
- Custom HTML templates and CSS for design.
- Vanilla JavaScript only when necessary.
- GitHub Pages for free static hosting.
- GitHub Actions for automated builds and deployment.

Requirements:
- No paid services or mandatory third-party APIs.
- No backend server or database requirement.
- Fast loading, responsive design, accessibility, and search-engine optimization.
- Support a custom domain in the future.
- Work with both a project site and a user site on GitHub Pages.
- Use relative URL handling and Hugo's baseURL configuration correctly.
- Do not commit API keys, access tokens, credentials, or other secrets.
- Pin or appropriately manage dependencies.
- Provide a working GitHub Actions workflow and clear setup instructions.

If a different framework is already established in the repository and changing it would destroy useful work, explain the trade-off and preserve the existing framework where appropriate.

## 3. Main navigation

Use exactly these six primary navigation tabs:

1. Home
2. Publications
3. Research
4. Collaborators
5. Teaching
6. CV

The navigation must be consistent across all pages, responsive on mobile, keyboard accessible, and visually understated.

Do not add Research Impact as a seventh primary tab. Instead, make it a prominent section on the homepage and a dedicated page accessible through an in-page link.

The homepage should also link to Software and Datasets, News, and Research Impact without overcrowding the primary navigation.

## 4. Personal profile and research context

Build the information architecture around the following research profile.

Name: Mohd Zaki

Research areas:
- Artificial intelligence for materials science.
- Materials informatics and scientific language models.
- Explainable machine learning for inorganic glasses.
- Cementitious materials and supplementary cementitious materials.
- AI-assisted materials discovery and scientific knowledge extraction.
- Structural engineering and earthquake resilience.
- Machine learning for seismic response and fragility assessment.
- Corrosion, structural damage assessment, and uncertainty quantification.
- Scientific machine learning, reproducible research, and open-source research software.

Relevant academic and professional experience includes research at Johns Hopkins University and IIT Delhi.

Relevant research contributions include work on materials science language models, scientific AI for glass and cementitious materials, and machine learning for structural engineering.

IMPORTANT: Treat these details as initial context, not as permission to invent a complete biography. Do not fabricate degrees, job titles, institutional affiliations, awards, dates, publication titles, collaborator names, citation counts, or other achievements.

Put editable personal information in a centralized configuration or profile data file. Use clearly marked placeholders for details that need verification.

The site must be fully functional even before all profile information is supplied.

## 5. Homepage design

Create a text-forward homepage inspired by the reference website, with the following sections in this order.

### A. Profile introduction

Include:
- Name.
- Professional title or concise research description.
- A short biography of approximately 100–150 words.
- Current affiliation, only when verified.
- Links to Google Scholar, ORCID, GitHub, LinkedIn, and email.
- Optional profile photograph, controlled through configuration.

Keep the introduction compact. Do not create a full-screen hero section.

Suggested research descriptor:

"Artificial Intelligence for Materials Science and Structural Engineering"

Suggested introductory text:

"My research develops artificial intelligence and data-driven methods to understand, discover, and design engineering materials and resilient structures. My interests span scientific language models, materials informatics, explainable machine learning, structural response prediction, earthquake engineering, and uncertainty quantification. I am particularly interested in connecting scientific knowledge, experimental data, computational models, and AI to accelerate engineering discovery."

Keep this text editable.

### B. Research interests

Present four principal research directions as concise text-led entries:

1. Materials AI and Scientific Language Models
2. Explainable AI and Materials Informatics
3. Structural Resilience and Earthquake Engineering
4. Scientific Machine Learning and Uncertainty Quantification

Each entry should link to a dedicated research page.

Avoid excessive visual cards. Use typography, subtle separators, and restrained visual hierarchy.

### C. News and updates

Create a compact chronological news section.

Each entry should support:
- Date.
- Short headline.
- Brief description.
- Optional external link.

Store entries in structured files. Sort newest first. Display a configurable number of recent items and provide a link to the complete archive.

Do not generate fake news entries. Include a small number of clearly identified sample records only if necessary for demonstrating the layout.

### D. Selected publications

Display a curated selection of important papers, grouped or labeled by year.

Each entry should support:
- Authors.
- Publication title.
- Journal or conference.
- Publication year.
- DOI link.
- Publisher or preprint link.
- PDF link, when legally shareable.
- Code and dataset links, when available.
- BibTeX download or copy action.
- Optional badges such as "Open Access" or "Featured."

Make publication titles prominent and metadata compact.

Add a link to the complete Publications page.

### E. Research impact

Add a dedicated, prominent homepage section titled:

"Research Building on My Work"

Subtitle:
"Selected studies that cite, extend, apply, or independently evaluate my research."

This section is a major differentiating feature of my website.

Display selected citing papers with:
- Paper title.
- Authors.
- Journal or conference.
- Year.
- Link to the paper.
- The original publication of mine that it cites.
- A concise, manually curated explanation of how it relates to my research.
- A category describing the relationship.

Support these categories:
- Methods Extended
- Applications
- Follow-up Research
- Independent Validation
- Dataset or Software Reuse

Clearly distinguish ordinary citation from genuine methodological or scientific extension.

Do not claim that a paper builds on my work solely because it cites it. Each interpretive statement must be manually reviewed.

The data model should support a field indicating verification status, and the public site should show only verified, approved entries.

Provide a link to a dedicated Research Impact page containing the full curated collection.

### F. Software and datasets

Include a compact section for important research software, datasets, and scientific resources.

Each item should support:
- Name.
- Short description.
- GitHub repository.
- Documentation.
- Paper or DOI.
- Dataset link.
- Relevant research area.

Only display verified links and actual projects. Do not invent repository names or project URLs.

### G. Additional academic links

At the bottom of the homepage, provide links to:
- Complete publications.
- Research projects.
- Collaborators.
- Teaching and mentoring.
- CV.
- Research Impact.
- Contact and academic profiles.

## 6. Publications page

Build a dedicated publications page that can accommodate a large bibliography.

Requirements:
- Group papers by year, newest first.
- Search by title, author, keyword, or venue.
- Filter by research topic and publication type.
- Include journal articles, conference papers, preprints, book chapters, and other scholarly outputs where applicable.
- Support featured publications.
- Support DOI, publisher, PDF, code, dataset, and BibTeX links.
- Make the layout readable on mobile.
- Provide a clear empty state when a filter returns no results.

Create a reusable publication component.

Use a structured content format that is easy to maintain and supports importing records from BibTeX.

If practical, implement a build-time BibTeX import or conversion script rather than requiring manual duplication of publication metadata.

Do not fabricate any publication records. Include an example record only in a clearly identified demo or fixture file, not in the live production bibliography.

## 7. Research page

Create a research landing page and individual pages for research themes.

Each research page should support:
- Research motivation and problem statement.
- Key research questions.
- Methods and technical contributions.
- Selected publications.
- Relevant software and datasets.
- Collaborators.
- Figures, diagrams, or research illustrations when available.
- Links to related research directions.

Initially create pages for the four research directions specified above.

Write concise placeholder text where more detail is needed, and clearly mark it for replacement. Do not invent experimental results, performance metrics, or scientific conclusions.

Support Markdown, mathematical notation through KaTeX or an equivalent lightweight solution, figures with captions, and citation links.

## 8. Collaborators page

Create a dedicated Collaborators page for academic and research collaborations.

Support:
- Researcher name.
- Verified institutional affiliation.
- Research area.
- Personal or institutional webpage.
- Relevant shared projects or publications.
- Optional profile photograph.

Organize collaborators by research theme, project, or institution.

Do not invent names, relationships, or affiliations.

Make it easy to add a collaborator by creating a new structured content file.

Avoid implying that a person is a formal collaborator unless that relationship has been verified.

## 9. Teaching page

Create a Teaching page with support for:
- Courses taught.
- Course descriptions.
- Lecture notes and slides.
- Tutorials and workshops.
- Student mentoring.
- Research supervision and student projects.
- Educational outreach.

Include fields for institution, date or academic year, role, and resources.

Keep teaching, mentorship, and outreach distinguishable.

Do not invent course titles, teaching dates, or student identities.

## 10. CV page

Create a professional academic CV page.

Requirements:
- Education.
- Academic and research appointments.
- Research interests.
- Selected honors and awards.
- Publications summary.
- Teaching and mentoring.
- Professional service.
- Invited talks and presentations.
- Software and datasets.
- Professional memberships, where applicable.

Use structured data wherever reasonable.

Provide a downloadable PDF link controlled by configuration. If the PDF is not available, hide the download link or display a clear placeholder in development mode.

Do not automatically generate a CV PDF unless a reliable, maintainable process is implemented and documented.

## 11. Research Impact data architecture and page

Implement the Research Impact page as a first-class content section even though it is not a primary navigation tab.

Use a structured schema similar to:

- title
- authors
- year
- venue
- paper_url
- doi
- cited_work_id
- relationship_category
- relationship_summary
- evidence_note
- verified
- featured
- research_topics

Store records in YAML, JSON, or another format consistent with the chosen framework.

The page should:
- Show only records with verified=true.
- Allow filtering by relationship category and research topic.
- Support searching by title, author, and keyword.
- Link each citing paper to the original work it cites.
- Display the manually reviewed relationship summary.
- Distinguish curated research influence from automatically retrieved citation metadata.
- Avoid unsupported claims of causal influence.

Create an empty-state message for when no verified records exist.

### Citation discovery and automation

Design the data architecture so that candidate citations can be imported later from OpenAlex, Semantic Scholar, Crossref, or other appropriate scholarly metadata sources.

Do not require an external API for the static website to render.

If implementing a scheduled discovery workflow:
- Keep it separate from the normal site build.
- Respect API terms, rate limits, and attribution requirements.
- Store API credentials in GitHub Actions secrets only if genuinely needed.
- Save discovered records as unverified candidates.
- Never publish newly discovered papers automatically as verified research impact.
- Do not scrape Google Scholar.
- Document how a researcher reviews, approves, edits, and rejects candidate records.

If a robust automated discovery workflow would add unnecessary complexity, implement the static data schema and page first, then document the extension point.

## 12. Visual design system

Use a refined academic visual language.

Color palette:
- White or near-white background.
- Dark charcoal text.
- Muted gray secondary text.
- One restrained accent color, such as deep navy or dark academic green.
- Subtle border colors and understated hover states.

Typography:
- Use a highly readable body font.
- Use a refined heading font or a consistent system-font stack.
- Maintain comfortable line lengths.
- Make publication metadata smaller than titles but still accessible.
- Use consistent heading hierarchy.

Layout:
- Centered content with a readable maximum width.
- Consistent spacing.
- Compact, unobtrusive navigation.
- Clear visual distinction between titles, metadata, body text, and links.
- Minimal borders and shadows.
- No unnecessary animations.
- Avoid a card-based grid for every section.

Responsive behavior:
- Desktop: horizontal primary navigation and a well-balanced reading column.
- Mobile: accessible compact navigation, readable typography, and no horizontal overflow.

Accessibility:
- Semantic HTML.
- Keyboard navigation.
- Visible focus states.
- Adequate color contrast.
- Descriptive image alt text.
- Reduced-motion support.
- Accessible search and filtering controls.

## 13. SEO and scholarly discoverability

Implement:
- Unique page titles and meta descriptions.
- Canonical URLs.
- Sitemap.
- robots.txt.
- Open Graph metadata.
- Structured data where appropriate.
- Person schema for the researcher.
- ScholarlyArticle schema for publication pages where accurate.
- Correct DOI and external-link handling.
- Clean URLs.
- Social sharing metadata.

Make it straightforward to add ORCID, Google Scholar, GitHub, and institutional profile links.

Do not insert fabricated structured data or citation counts.

## 14. Project organization and maintainability

Use a clean, understandable repository structure.

Separate:
- Configuration.
- Layout templates.
- Reusable components or partials.
- Stylesheets.
- JavaScript.
- Publications.
- Research projects.
- Collaborators.
- Teaching content.
- News.
- Research Impact records.
- CV data.
- Images and other assets.

Create a centralized profile configuration file for:
- Name.
- Research description.
- Biography.
- Current verified affiliation.
- Email.
- Academic profile links.
- Social links.
- Profile photograph.
- CV file.
- Site URL.

Provide clear comments and documentation explaining where to edit every important item.

Avoid duplicating the same publication or profile information across multiple files.

## 15. Quality assurance and delivery

After implementation:

1. Run the static-site build and resolve all errors.
2. Check internal links and asset paths.
3. Verify that all main pages render correctly.
4. Test publication search and filters.
5. Test Research Impact search and filters.
6. Verify that unverified research-impact records are not publicly displayed.
7. Check responsive layouts and accessibility basics.
8. Confirm GitHub Pages baseURL and deployment configuration.
9. Verify that the website works without external API credentials.
10. Provide a concise README covering local development, content editing, publication import, research-impact curation, and GitHub Pages deployment.

Create the actual files and implement the website, not merely a specification.

If a decision is not specified, choose the simplest maintainable option consistent with a minimal academic website.

At the end, report:
- What was implemented.
- The repository structure.
- Any assumptions or placeholders.
- Commands to run the website locally.
- How to deploy it to GitHub Pages.
- Any remaining tasks requiring my personal information or verified academic records.

**Final design objective:** The finished site should feel like a thoughtful, modern academic professor's homepage inspired by Mausam's IIT Delhi website, with the minimalist visual restraint of a well-designed research portfolio. Research contributions, publications, collaborations, and demonstrable scientific impact must take precedence over decorative design.