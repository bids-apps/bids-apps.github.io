---
layout: default
---
<article class="post-container post-container--single">
  <header class="post-header">
    <h1 class="post-title">Tutorials</h1>
  </header>

  <h2>Running a BIDS App locally</h2>
  <p>Running a BIDS App on a local system can be performed using Docker, which is easy to install on all three major operating systems. To run the first stage of the example BIDS App for participant number 01 the user needs to open a console (terminal or cmd) and type:</p>
  {% highlight bash %}
  docker run -ti --rm \
      -v /Users/srycajal/data/ds005:/bids_dataset:ro \
      -v /Users/srycajal/outputs:/outputs \
      bids/example:0.0.4 \
      /bids_dataset /outputs participant --participant_label 01
  {% endhighlight ruby %}
  <p>Where /Users/srycajal/data/ds005 is the path to the input dataset and /Users/srycajal/outputs the path where results should be stored. If the BIDS App was not run before on this machine, the docker image will be automatically downloaded from the Docker Hub.</p>
  <h2>Running a BIDS App on a cluster (HPC)</h2>
  <p>Before a BIDS App can be run on a cluster, it first needs to be saved to an Singularity-compatible image file. This step needs to be performed outside of the cluster (for example on a laptop) and requires Docker:</p>
  {% highlight bash %}
  docker run --privileged -ti --rm  \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v D:\\singularity_images:/output \
      filo/docker2singularity \
      bids/example:0.0.4
  {% endhighlight %}
  <p>Where D:\\singularity_images is a path where the image will be stored. After transferring the .img file to a cluster it can be run like any other executable:</p>
  {% highlight bash %}
  ./bids_example-0.0.4.img /bids_dataset /outputs participant --participant_label 01
  {% endhighlight %}
  </section>
  {% if page.comments != false and site.disqus_shortname %}<section id="disqus_thread"></section><!-- /#disqus_thread -->{% endif %}
</article>
{% if page.comments != false %}{% include disqus.html %}{% endif %}
