# Contributing to BIDS Apps

- [Contributing to BIDS Apps](#contributing-to-bids-apps)
  - [Repository map](#repository-map)
  - [:technologist: You can contribute to BIDS-Apps by:](#technologist-you-can-contribute-to-bids-apps-by)
  - [Report a valid issue :heavy_check_mark:](#report-a-valid-issue-heavy_check_mark)
  - [Labels :label:](#labels-label)
  - [Making a change with a pull request :zap:](#making-a-change-with-a-pull-request-zap)
    - [Fork the project, clone your fork, and add the BIDS Apps remote:](#fork-the-project-clone-your-fork-and-add-the-bids-apps-remote)
    - [Get the latest changes from upstream:](#get-the-latest-changes-from-upstream)
    - [Create a new branch from the main master branch to contain your changes:](#create-a-new-branch-from-the-main-master-branch-to-contain-your-changes)
    - [Add and Commit your changes](#add-and-commit-your-changes)
  - [Build the website locally](#build-the-website-locally)
    - [Open a Pull Request with a clear title and description against the master branch.](#open-a-pull-request-with-a-clear-title-and-description-against-the-master-branch)
  - [Example Pull Request](#example-pull-request)
  - [Recognizing Contributions 🗒️](#recognizing-contributions-️)
  - [Get in touch with us :mailbox_with_mail:](#get-in-touch-with-us-mailbox_with_mail)
  - [A Special Note :high_brightness:](#a-special-note-high_brightness)

Welcome to the BIDS Apps repository! :rocket:

We're excited that you're here and equally thrilled to know that you want to
contribute. :superhero:

BIDS-Apps are a collection of containerized neuroimaging workflows and pipelines
that accept datasets organized according to the Brain Imaging Data Structure
(BIDS). To learn more please visit our
[Homepage](http://bids-apps.neuroimaging.io)

These guidelines are designed especially to make the whole process as easy and
smooth as possible. Still, if something is unclear or not mentioned please don't
hesitate to ask. [Email us](ffein@stanford.edu) or let us know by opening an
[issue!](https://github.com/bids-apps/bids-apps.github.io/issues)

Before you start you'll need to set up a free [GitHub](https://github.com/)
account and sign in. Here are some
[instructions](https://help.github.com/en/github/getting-started-with-github/signing-up-for-github).

Not Familiar with Git? Invest a few minutes on this
[Git Tutorial](https://git-scm.com/docs/gittutorial) :octocat:

## Repository map

To help you find what is where.

```bash
.
├── _includes  # defines layout for typical page sections
├── _layouts   # defines layout for typical page
├── _posts     # not currently used
├── css
├── fonts
├── js
├── images
├── _config.yml # the 'control room' for the website
├── index.html  # landing page
├── about.md      # page see navigation section in _config.yml
├── apps.md       # page see navigation section in _config.yml
├── dev_faq.md    # page see navigation section in _config.yml
├── tutorial.md   # page see navigation section in _config.yml
├── CNAME
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── feed.xml
├── Gemfile
├── sitemap.xml
├── categories.md
└── tags.md
```

To add a page:

1. add a markdown document in the root directory with this YML frontmatter (see
   the [tutorials](./tutorial.md) for an example.)

```yml
---
layout: post
title: your title goes here
---
```

1. List it in the `navigation` section of the [\_config.yml](./_config.yml)
   file.

## :technologist: You can contribute to BIDS-Apps by:

- Reporting a valid
  [issue](https://github.com/bids-apps/bids-apps.github.io/issues)
- Helping us in closing an existing
  [issue](https://github.com/bids-apps/bids-apps.github.io/issues)
- Opening a
  [Pull Request](https://github.com/bids-apps/bids-apps.github.io/pulls)
- Want to discuss something else: [Email us](ffein@stanford.edu)

## Report a valid issue :heavy_check_mark:

BIDS-Apps uses
[GitHub's issue tracker](https://github.com/bids-apps/bids-apps.github.io/issues).
All bugs and enhancements should be listed so that we don't lose track of them,
can prioritize and assign them to the relevant developer or maintainer.

Consider the following recommended best practice for writing issues, which are
(Recommended but not limited to):

1. More detailed description rather than one-liners
2. Screenshots
3. Providing example files and error logs
4. How to reproduce it
5. Details of your local system or environment that you're using

## Labels :label:

Labels let us identify different types of issues, pull requests and helps in
categorizing them based on their characteristics. Please take a look at the
different types of labels we use.

- ![Bug](https://img.shields.io/badge/-Bug-%23ee0701) _These issues points to
  the problems causing the project to crash, producing an invalid output or
  causing an error._ If you find a bug, feel free to open an issue with the
  detailed description, screenshots and how to reproduce it. If you experience a
  bug that is already listed in the issues, do comment down your remark and wait
  till our developers get back to you.

- ![Duplicate](https://img.shields.io/badge/-duplicate-%237E7E7E) _It indicates
  similar/existing issues or pull requests._ Do check the existing issues and
  pull request before creating a new one to avoid duplicacy. If you find a
  duplicate issue or PR, please give the reference in the comments.

- ![Enhancement](https://img.shields.io/badge/-enhancement-%232e5783) _It
  indicates a new feature request or enhancement._ Any change or upgrade that
  increases the project capabilities, performance or scalability. In general,
  enhancements include: - Additional functionality - Error/bug repair and
  handling - Better code coverage - Improved performance

- ![Help Wanted](https://img.shields.io/badge/-help%20wanted-%23128a0c)
  _Indicates that a maintainer or developer wants help on an issue or pull
  request._ If you have a particular skill that can help in solving the problem
  then consider reading through these issues as they are a great place to offer
  your expertise. Not everyone can do everything. This is the time, the
  community needs your help so you better dive in!

- ![Invalid](https://img.shields.io/badge/-invalid-%239a9a9a) _It indicates that
  an issue or pull request is no longer relevant._

- ![Question](https://img.shields.io/badge/-question-%23cc317c) _It indicates
  that an issue or pull request needs more information._ These issues are some
  questions regarding the project that might need clarifications and a bit of
  discussion.

- ![Dependencies](https://img.shields.io/badge/-dependencies-%230366d6) _It
  helps to track and resolve vulnerabilities for certain types of dependencies._

- ![WontFix](https://img.shields.io/badge/-wontfix-lightgrey) _It indicates
  issues that are currently not viable to solve or out of scope of the project_

## Making a change with a pull request :zap:

Pull requests with patches, improvements and new features are a great help.

### Fork the project, clone your fork, and add the BIDS Apps remote:

```sh
# Clone your fork of the repo into the current directory
git clone https://github.com/<USERNAME>/bids-apps.github.io.git

# Navigate to the cloned directory
cd bids-apps.github.io

# Assign the original repo to a remote called "upstream"
git remote add upstream git@github.com:bids-apps/bids-apps.github.io.git
```

### Get the latest changes from upstream:

```sh
git checkout master
git pull upstream master
```

### Create a new branch from the main master branch to contain your changes:

```sh
git checkout -b <topic-branch-name>
```

### Add and Commit your changes

```sh
git add <path/to/modified/file/>
git commit -m "write a commit message"
```

Examine the status of your working tree at each step to see if everything is
clean:

```sh
git status
```

Push your topic branch up to your fork:

```sh
git push origin <topic-branch-name>
```

## Build the website locally

Requires to install [Jekyll](https://jekyllrb.com/docs/#prerequisites) (a static
website generator).

```sh
bundle install
bundle exec jekyll serve
```

### Open a Pull Request with a clear title and description against the master branch.

[Open a Pull Request.](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)

## Example Pull Request

![Example Pull Request](https://i.imgur.com/s8yELfK.png)

A maintainer/developer will review and might suggest some changes before merging
them into the repository.

Success!! :tada: Well done! :bowing_man:

## Recognizing Contributions 🗒️

BIDS follows the
[all-contributors](https://github.com/all-contributors/all-contributors#emoji-key)
specification, so we welcome and recognize all contributions from documentation
to testing to code development. You can see a list of current contributors in
the
[BIDS specification](https://github.com/bids-standard/bids-specification/blob/master/src/99-appendices/01-contributors.md).

## Get in touch with us :mailbox_with_mail:

If you have any questions, comments, or suggestions, please feel free to create
an issue [here](https://github.com/bids-apps/bids-apps.github.io/issues)! A
Maintainer or community member will follow up.

If you'd prefer to email then you can contact Franklin at ffein@stanford.edu

## A Special Note :high_brightness:

Thank you for reading through and we look forward to your valuable contribution!
:smiley:

We appreciate the hard work and time of our contributors who have built and
maintained BIDS-Apps! :raised_hands:

You are Awesome! :star2: :star_struck:
