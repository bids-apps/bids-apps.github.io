---
layout: post
title: Developer FAQ
---

## Versioning

### When is a new image deposited to Docker Hub?

Even though Docker image is being build on the CI server each time you push a
commit to the repository it is not automatically being pushed to Docker Hub.
Only if you tag a commit, push the tag to GitHub, and the tests you configured
pass a new image will be deposited in Docker Hub.

### How to tag a new release?

```bash
git tag v0.0.1
git push
```

### How should I version my BIDS App?

Since most BIDS Apps are just thin wrappers around existing pipelines it would
be most sensible to use the same version as the software they are wrapping. For
example in case of HCP Pipelines this would be `v3.17.0`.

### I want to release a new version of a BIDS App, but the pipeline version is the same?

This cna happen when only the runscript or the Dockerfile changed?

According to semantic versioning we should use the `+` signed followed by the
build number. Unfortunately Docker Hub does not support semantic versioning. The
best option is to use the `-` sign followed by the build number. For example
`v3.17.0-3`.

### Where should I describe changes between versions?

After tagging a new release it is important to provide a list of changes on the
GitHub Releases page. It accepts markdown syntax and allows you to explain in
detail what has changed. Here's an
[example](https://github.com/BIDS-Apps/example/releases).

### How can I check a version of a container I have available locally?

Inside each BIDS App there is a /version file with the version number. This file
is automatically populated with tag used to trigger the build on the CI server.

### How can I download a particular version of a BIDS App?

All versions of BIDS Apps are archived on Docker Hub. To access a particular
version you should refer to a specific Docker Hub tag. For example:

```bash
docker pull bids/example:v0.0.5
```
