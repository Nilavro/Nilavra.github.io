---
layout: page
title: Research
subtitle: "Selected research directions and project portfolios."
permalink: /research/
---

My research focuses on machine learning, control, economics, and decision systems, with applications in marketing science, budget allocation, bidding, energy systems, and semi-synthetic simulation environments.

<div class="research-list">
{% for item in site.research %}
  <a class="research-card" href="{{ item.url | relative_url }}">
    <h2>{{ item.title }}</h2>
    <p>{{ item.summary }}</p>
  </a>
{% endfor %}
</div>
