# Commitizen Deno Provider

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org)
[![PyPI Package latest release](https://img.shields.io/pypi/v/commitizen-deno-provider.svg?style=flat-square)](https://pypi.org/project/commitizen-deno-provider/)
[![PyPI Package download count (per month)](https://img.shields.io/pypi/dm/commitizen-deno-provider?style=flat-square)](https://pypi.org/project/commitizen-deno-provider/)
[![Supported versions](https://img.shields.io/pypi/pyversions/commitizen-deno-provider.svg?style=flat-square)](https://pypi.org/project/commitizen-deno-provider/)

A Plugin for commitizen to provide versionning within Deno projects. Update the version in the deno.json and jsr.json files.

## Installation

```bash
pip install commitizen-deno-provider
```

## Usage

```yml
---
commitizen:
  major_version_zero: true
  name: cz_conventional_commits
  tag_format: $version
  update_changelog_on_bump: true
  version_provider: deno-provider
  version_scheme: semver
```
