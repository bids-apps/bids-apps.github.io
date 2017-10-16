---
layout: default
---
<article class="post-container post-container--single">
  <header class="post-header">
    <h1 class="post-title">Tutorials</h1>
  </header>

  <h2>Running a BIDS App locally</h2>
  <p>Running a BIDS App on a local system can be performed using Docker, which is easy to install on all three major operating systems. After installing and starting docker, download the relevant data, <a href="https://drive.google.com/drive/folders/0B2JWN60ZLkgkMGlUY3B4MXZIZW8">ds005.tar</a>, and untar it in a directory. <i>ds005</i>  will be our input directory in the following example. Create an <i>outputs</i> directory as well. To run the first stage of the example BIDS App for participant number 01, open a console (terminal or cmd) and type:</p>
  {% highlight bash %}
  docker run -ti --rm \
      -v /Users/srycajal/data/ds005:/bids_dataset:ro \
      -v /Users/srycajal/outputs:/outputs \
      bids/example:0.0.4 \
      /bids_dataset /outputs participant --participant_label 01
  {% endhighlight %}
  <p>This command runs docker with some flags and then binds the input directory on our local machine, e.g., <i>/Users/srycajal/data/ds005</i>, to a preset directory inside of the docker container (<i>/bids_dataset</i>). You must use the absolute path to both of these directories. Similarly, we bind the <i>outputs</i> directory on our local machine e.g., <i>/Users/srycajal/outputs</i> to the <i>/outputs</i> directory inside the container. This is the path where results should be stored. Next, the command lists the docker container to download from Docker Hub and run: <i>bids/example:0.0.4</i>. Finally, <i>--participant_label 01</i> limits the data that will be used to just the first subject in the dataset. If we wanted to run all the participants, we would simply remove <i>--participant_label 01</i>. Or we could select a couple of participants like this: <i>--participant_label 01 03</i>. If the BIDS App was not run before on this machine, the docker image will be automatically downloaded from Docker Hub. </p>


  <h2>Running a BIDS App on a cluster (HPC)</h2>
  <p>Before a BIDS App can be run on a cluster, it first needs to be saved to an Singularity-compatible image file. This step needs to be performed outside of the cluster (for example on a laptop) and requires Docker:</p>
  {% highlight bash %}
  docker run --privileged -ti --rm  \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v /home/srycajal/singularity_images:/output \
      singularityware/docker2singularity \
      bids/example:0.0.4
  {% endhighlight %}
  <p>Where /home/srycajal/singularity_images is a path where the image will be stored. After transferring the .img file to a cluster it can be run like any other executable:</p>
  {% highlight bash %}
  ./bids_example-0.0.4.img /bids_dataset /outputs participant --participant_label 01
  {% endhighlight %}
  <p>To learn more, read the <a href="http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005209">PLOS paper</a> consult this <a href="https://neurohackweek.github.io/docker-for-scientists/">tutorial</a> and watch the <a href="https://www.slideshare.net/chrisfilo1/docker-for-scientists">workshop video</a>. Additional links and tips can be found here: <a href="https://sites.google.com/a/email.arizona.edu/bmw/resources/bids">BIDS Links and Tips</a>.</p>
  <p><a href="/dev_faq">Developer FAQ</a></p>

  {% if page.comments != false and site.disqus_shortname %}<section id="disqus_thread"></section><!-- /#disqus_thread -->{% endif %}
  {% if page.comments != false %}{% include disqus.html %}{% endif %}
  </article>
