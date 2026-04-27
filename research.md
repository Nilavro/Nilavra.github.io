---
layout: page
title: Research
subtitle: "Selected research directions and project portfolios."
permalink: /research/
---

My research focuses on machine learning, control, economics, and decision systems, with applications in marketing science, budget allocation, bidding, energy systems, and semi-synthetic simulation environments.

<div class="research-list">
{% assign sorted_research = site.research | sort: "order" %}
{% for item in sorted_research %}
  <a class="research-row" href="{{ item.url | relative_url }}">
    <span>{{ item.order | default: forloop.index }}</span>
    <div>
      <h2>{{ item.title }}</h2>
      <p>{{ item.summary }}</p>
    </div>
  </a>
{% endfor %}
</div>
