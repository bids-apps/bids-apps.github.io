---
layout: default
---

<article class="post-container post-container--single">

  <header class="post-header">
    <h1 class="post-title">Available BIDS Apps</h1>
  </header>

  <h2>All apps</h2>

  {% include app_table.html apps=site.apps status="active" %}

  <div style="width: 100%; padding: 20px">
    <hr style="height:5px; background-color:#00A4BD; border-width:0;">
  </div>

  <h2>Unmaintainted apps</h2>

  {% include app_table.html apps=site.apps status="unmaintained" %}

  <div style="width: 100%; padding: 20px">
    <hr style="height:5px; background-color:#00A4BD; border-width:0;">
  </div>

  <h2>Apps sorted by input type</h2>

  {% include app_subtable.html apps=site.apps ds_type="raw" datatype="anat" %}
  {% include app_subtable.html apps=site.apps ds_type="raw" datatype="func" %}
  {% include app_subtable.html apps=site.apps ds_type="raw" datatype="dwi" %}

  {% include app_subtable.html apps=site.apps ds_type="derivative" datatype="anat" %}
  {% include app_subtable.html apps=site.apps ds_type="derivative" datatype="func" %}
  {% include app_subtable.html apps=site.apps ds_type="derivative" datatype="dwi" %}

</article>
