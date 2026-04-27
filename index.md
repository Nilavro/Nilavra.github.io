---
layout: default
title: Home
description: "Academic website of Nilavra Pathak, Senior Machine Learning Scientist at Expedia Group."
---

<section class="home-hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">Machine Learning · Control · Economics · Decision Systems</p>
      <h1>Nilavra Pathak</h1>
      <p class="hero-title">Senior Machine Learning Scientist at Expedia Group</p>
      <p class="lead">
        I build data-driven decision systems for marketing science, measurement,
        bidding, budget allocation, counterfactual evaluation, and large-scale
        optimization under uncertainty.
      </p>
      <div class="hero-actions">
        <a class="button primary" href="{{ '/research/' | relative_url }}">Research portfolio</a>
        <a class="button secondary" href="{{ '/publications/' | relative_url }}">Publications</a>
        <a class="button ghost" href="{{ '/assets/cv.pdf' | relative_url }}">CV</a>
      </div>
    </div>

    <aside class="profile-card">
      <img src="{{ '/assets/profile-pic.jpg' | relative_url }}" alt="Nilavra Pathak">
      <div>
        <h2>Nilavra Pathak</h2>
        <p>Senior Machine Learning Scientist<br>Expedia Group</p>
      </div>
    </aside>
  </div>
</section>

<section class="wrap section two-col">
  <div>
    <p class="kicker">About</p>
    <h2>Decision systems for real-world allocation problems</h2>
  </div>
  <div>
    <p>
      My work sits at the intersection of machine learning, economics, system
      identification, and control. I am interested in replacing heuristic,
      manually tuned business decision-making with systematic, measurable, and
      feedback-driven decision systems.
    </p>
    <p>
      In practice, this includes marketing budget allocation, bidding, campaign
      automation, response-curve forecasting, counterfactual measurement,
      regret-aware policy evaluation, and semi-synthetic simulation.
    </p>
  </div>
</section>

<section class="wrap section">
  <div class="section-heading">
    <p class="kicker">Research portfolio</p>
    <h2>Selected research directions</h2>
  </div>
  <div class="card-grid">
    {% assign sorted_research = site.research | sort: "order" %}
    {% for item in sorted_research %}
      <a class="research-card" href="{{ item.url | relative_url }}">
        <span class="card-number">{{ item.order | default: forloop.index }}</span>
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
      </a>
    {% endfor %}
  </div>
</section>

<section class="wrap section split-panel">
  <div>
    <p class="kicker">Current focus</p>
    <h2>From prediction to control</h2>
  </div>
  <div class="pill-list">
    <span>Response curves</span>
    <span>Budget optimization</span>
    <span>Retrospective regret</span>
    <span>Marginality zones</span>
    <span>Performative control</span>
    <span>Energy economist</span>
  </div>
</section>

<section class="wrap section">
  <div class="section-heading">
    <p class="kicker">News</p>
    <h2>Latest updates</h2>
  </div>
  {% for post in site.posts limit:3 %}
    <article class="news-card">
      <time>{{ post.date | date: "%B %d, %Y" }}</time>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
    </article>
  {% endfor %}
</section>
