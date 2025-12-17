# 3rd Workshop on Test-Time Updates (TTU)

For the published page, please see https://ttu-iclr2026.github.io/.

## Development/updates

If you want to edit this site:

- Main page: Edit [./docs/source/index.rst](./docs/source/index.rst)
- Schedule: Edit [./docs/source/schedule.rst](./docs/source/schedule.rst)
    - Schedule itself is generated from the data in [./docs/source/schedule.csv](./docs/source/schedule.csv)
- Accepted papers: Edit [./docs/source/papers.rst](./docs/source/papers.rst)
    - Papers are listed in [./docs/source/papers.csv](./docs/source/papers.csv)
- Organizers: Edit [./docs/source/organizers.html](./docs/source/organizers.html)
    - Organizer photos are in [./docs/source/_static/organizers](./docs/source/_static/organizers)
- Speakers: Edit [./docs/source/speakers.rst](./docs/source/speakers.rst)
    - Speaker photos are in [./docs/source/_static/speakers](./docs/source/_static/speakers)

To build the site locally:

```bash
./build_docs.sh
```

Each change merged to `main` will be automatically deployed to the published site.
