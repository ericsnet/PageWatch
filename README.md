# PageWatch

**[English](./README.md) · [Español](./README.es.md)**

PageWatch is a project in its planning stage that aims to monitor web pages over time and detect meaningful changes in their content.

## Planned features

- **Scheduled checks:** revisit pages at a configurable interval.
- **Version comparison:** identify differences between previous and current content.
- **Change history:** keep a record of detected updates.
- **Noise filters:** ignore irrelevant changes, such as dynamic page elements.
- **Section monitoring:** track a specific part of a page where feasible.
- **Notifications:** alert users when changes match their configured criteria.

These are planned goals, not implemented features.

## Planned technology

- **Python** for fetching, checking, and comparing page content.
- **SQLite** for storing monitored pages, snapshots, and change events.
- **Web interface** for managing monitored pages and reviewing history.

Automated checks will require the monitoring process to be running on a computer or server. The final architecture has not yet been decided.

## Status

**Early planning.** This repository currently contains documentation and a license only. No executable code is included yet.

## Initial roadmap

1. Define how pages are registered and how check intervals are configured.
2. Design storage for page content and change history.
3. Implement page fetching and content normalization.
4. Compare versions and filter irrelevant changes.
5. Add section monitoring and notifications.
6. Build a web interface for managing monitored pages.

## Responsible use

PageWatch is intended for public web pages. Future use must respect website terms, access restrictions, applicable policies, and reasonable request rates.

## License

PageWatch is publicly viewable on GitHub but is **not open-source software**. All rights are reserved. Public access does not grant permission to copy, modify, redistribute, or otherwise use this project's contents except as permitted by applicable law or with prior written permission. See [LICENSE](./LICENSE).
