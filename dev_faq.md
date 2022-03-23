---
layout: default
---

<article class="post-container post-container--single">
  <header class="post-header">
    <h1 class="post-title">Developer FAQ</h1>
  </header>

    <h2>Versioning</h2>
    <ol>
    <li>When is a new image deposited to Docker Hub?<br>

Even though Docker image is being build on the CI server each time you push a commit to the repository it is not automatically being pushed to Docker Hub. Only if you tag a commit, push the tag to GitHub, and the tests you configured pass a new image will be deposited in Docker Hub. How to tag a new release?
{% highlight bash %}
git tag v0.0.1
git push --tags
{% endhighlight %}</li>

<li>How should I version my BIDS App?<br>
Since most BIDS Apps are just thin wrappers around existing pipelines it would be most sensible to use the same version as the software they are wrapping. For example in case of HCP Pipelines this would be v3.17.0</li>

<li>What if I would like to release a new version of a BIDS App, but the pipeline version is the same - I only changed the runscript or the Dockerfile?<br>
According to semantic versioning we should use the "+" signed followed by the build number. Unfortunately Docker Hub does not support semantic versioning. The best option is to use the "-" sign followed by the build number. For example v3.17.0-3</li>

<li>Where should I describe changes between versions?<br>
After tagging a new release it is important to provide a list of changes on the GitHub Releases page. It accepts markdown syntax and allows you to explain in detail what has changed. Here's an <a href="https://github.com/BIDS-Apps/example/releases">example</a>.</li>

<li>How can I check a version of a container I have available locally?<br>
Inside each BIDS App there is a /version file with the version number. This file is automatically populated with tag used to trigger the build on the CI server.</li>

<li>How can I download a particular version of a BIDS App?<br>
All versions of BIDS Apps are archived on Docker Hub. To access a particular version you should refer to a specific Docker Hub tag. For example:
{% highlight bash %}
docker pull bids/example:v0.0.5
{% endhighlight %}
</li>
</ol>

{% if page.comments != false and site.disqus_shortname %}<section id="disqus_thread"></section><!-- /#disqus_thread -->{% endif %}
{% if page.comments != false %}{% include disqus.html %}{% endif %}

</article>
