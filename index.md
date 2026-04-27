---
layout: default
title: Home
description: "Academic website of Nilavra Pathak, Senior Machine Learning Scientist at Expedia Group."
---

<section class="hero">
  <div class="hero-text">
    <p class="eyebrow">Machine Learning · Control · Economics · Decision Systems</p>
    <h1>Nilavra Pathak</h1>
    <p class="subtitle">
      Senior Machine Learning Scientist at Expedia Group working on large-scale
      data-driven decision systems for marketing, measurement, bidding, budget
      allocation, and counterfactual evaluation.
    </p>
    <div class="button-row">
      <a class="button" href="{{ '/research/' | relative_url }}">View Research</a>
      <a class="button secondary" href="{{ '/assets/cv.pdf' | relative_url }}">Download CV</a>
    </div>
  </div>
  <div class="profile-card">
    <img src="{{ '/assets/profile-placeholder.svg' | relative_url }}" alt="Nilavra Pathak profile placeholder">
    <p>Senior Machine Learning Scientist<br>Expedia Group</p>
  </div>
</section>

<section class="section">
  <h2>Research Focus</h2>
  <div class="card-grid">
    <a class="card" href="{{ '/research/response-curve-forecasting/' | relative_url }}">
      <h3>Response Curve Forecasting</h3>
      <p>System identification and forecasting for marketing spend-response systems.</p>
    </a>
    <a class="card" href="{{ '/research/certified-retrospective-regret/' | relative_url }}">
      <h3>Retrospective Regret</h3>
      <p>Auditing allocation policies using constraint-faithful hindsight oracles.</p>
    </a>
    <a class="card" href="{{ '/research/marginality-zone-detection/' | relative_url }}">
      <h3>Marginality Zone Detection</h3>
      <p>Nonparametric methods for finding operationally meaningful spend regions.</p>
    </a>
  </div>
</section>

<section class="section">
  <h2>Selected Portfolio</h2>
  <div class="research-list">
    {% for item in site.research %}
      <a class="research-card" href="{{ item.url | relative_url }}">
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
      </a>
    {% endfor %}
  </div>
</section>

<section class="section">
  <h2>Latest Updates</h2>
  {% for post in site.posts limit:3 %}
    <article class="news-item">
      <p class="date">{{ post.date | date: "%B %d, %Y" }}</p>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
    </article>
  {% endfor %}
</section>
