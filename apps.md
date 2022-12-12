---
layout: default
---

<article class="post-container post-container--single">
  <header class="post-header">
    <h1 class="post-title">Available BIDS Apps</h1>
  </header>

  <table>
    {% for app in site.apps %}
      {% if app.branch %}
        {% assign branch = app.branch %}
      {% else %}
        {% assign branch = "master" %}
      {% endif %}
      <tr>
        <td>
          <a href="https://github.com/{{ app.gh }}">{{ app.gh }}</a>
        </td>
        <td>
          <img
            src="https://img.shields.io/github/v/tag/{{ app.gh | downcase }}?label=version"
          />
        </td>
        <td>
          <a
            href="https://github.com/{{ app.gh }}/issues?q=is%3Aopen+is%3Aissue+label%3Abug"
          >
            <img src="https://img.shields.io/github/issues-raw/{{ app.gh }}" />
          </a>
        </td>
        <td>
          {% if app.ci == "travis" %}
              <a href="https://app.travis-ci.com/{{ app.gh }}">
                <img src="https://app.travis-ci.com/{{ app.gh }}.svg?branch={{ branch }}" />
              </a>
          {% elsif app.ci == "gh" %}
              <a href="https://github.com/{{ app.gh }}/actions/workflows/{{ app.workflow }}.yml/">
                <img src="https://github.com/{{ app.gh }}/actions/workflows/{{ app.workflow }}.yml/badge.svg?branch={{ branch }}" />
              </a>
          {% elsif app.ci == "none" %}
            <img src="https://img.shields.io/badge/CI-unavailable-lightgrey" />
          {% else %}
            <a href="https://circleci.com/gh/{{ app.gh }}/tree/{{ branch }}">
              <img src="https://circleci.com/gh/{{ app.gh }}.svg?style=shield" />
            </a>
          {% endif %}
        </td>
        <td>
          <a href="https://github.com/{{ app.gh }}/pulls">
            <img
              src="https://img.shields.io/github/issues-pr-raw/{{ app.gh }}/bug.svg"
            />
          </a>
        </td>
        <td>
          <a href="https://hub.docker.com/r/{{ app.dh | downcase }}/">
            <img
              src="https://img.shields.io/docker/pulls/{{ app.dh | downcase }}.svg"
            />
          </a>
        </td>
      </tr>
    {% endfor %}
  </table>

</article>
