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
      <td><a href="http://github.com/BIDS-Apps/{{ app }}">bids/{{ app }}</a></td>
      <td><img src="https://images.microbadger.com/badges/version/bids/{{ app | downcase }}.svg" /></td>
      <td>
        <a href="http://github.com/BIDS-Apps/{{ app }}/issues?q=is%3Aopen+is%3Aissue+label%3Abug">
          <img src="https://img.shields.io/github/issues-raw/BIDS-Apps/{{ app }}/bug.svg?maxAge=2592000" />
        </a>
      </td>
      <td>
        <a href="https://circleci.com/gh/BIDS-Apps/{{ app }}/tree/master">
          <img src="https://img.shields.io/circleci/project/BIDS-Apps/{{ app }}/master.svg?maxAge=2592000" />
        </a>
      </td>
      <td>
        <a href="http://github.com/BIDS-Apps/{{ app }}/pulls">
          <img src="https://img.shields.io/github/issues-pr-raw/BIDS-Apps/{{ app }}/bug.svg?maxAge=2592000" />
        </a>
      </td>
      <td>
        <a href="https://hub.docker.com/r/bids/{{ app | downcase }}/">
          <img src="https://img.shields.io/docker/pulls/bids/{{ app | downcase }}.svg?maxAge=2592000" />
        </a>
      </td>
	  <td>
        <a href="https://hub.docker.com/r/bids/{{ app | downcase }}/">
          <img src="https://images.microbadger.com/badges/image/bids/{{ app | downcase }}.svg" />
        </a>
      </td>
    </tr>
  {% endfor %}
  </table>
  {% if page.comments != false and site.disqus_shortname %}<section id="disqus_thread"></section><!-- /#disqus_thread -->{% endif %}
  {% if page.comments != false %}{% include disqus.html %}{% endif %}
  </article>
