---
layout: default
---

<article class="post-container post-container--single">
  <header class="post-header">
    <h1 class="post-title">Available BIDS Apps</h1>
  </header>

  <table>
    {% for app in site.apps %}
    <tr>
      <td>
        <a href="http://github.com/{{ app.gh }}">{{ app.gh }}</a>
      </td>
      <td>
        <img
          src="https://img.shields.io/github/v/tag/{{ app.gh | downcase }}?label=version"
        />
      </td>
      <td>
        <a
          href="http://github.com/{{ app.gh }}/issues?q=is%3Aopen+is%3Aissue+label%3Abug"
        >
          <img src="https://img.shields.io/github/issues-raw/{{ app.gh }}" />
        </a>
      </td>
      <td>
        <a href="https://circleci.com/gh/{{ app.gh }}/tree/master">
          <img src="https://circleci.com/gh/{{ app.gh }}.svg?style=shield" />
        </a>
      </td>
      <td>
        <a href="http://github.com/{{ app.gh }}/pulls">
          <img
            src="https://img.shields.io/github/issues-pr-raw/{{ app.gh }}/bug.svg?maxAge=2592000"
          />
        </a>
      </td>
      <td>
        <a href="https://hub.docker.com/r/{{ app.dh | downcase }}/">
          <img
            src="https://img.shields.io/docker/pulls/{{ app.dh | downcase }}.svg?maxAge=2592000"
          />
        </a>
      </td>
      <td>
        <a href="https://hub.docker.com/r/{{ app.dh | downcase }}/">
          <img
            src="https://images.microbadger.com/badges/image/{{ app.dh | downcase }}.svg"
          />
        </a>
      </td>
    </tr>
    {% endfor %}
  </table>

  {% if page.comments != false and site.disqus_shortname %}
  <section id="disqus_thread"></section>
  <!-- /#disqus_thread -->
  {% endif %} {% if page.comments != false %} {% include disqus.html %} {% endif
  %}
</article>
