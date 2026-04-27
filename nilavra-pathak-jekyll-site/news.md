---
layout: page
title: News
subtitle: "Research updates, talks, papers, project notes, and optional external research feed."
permalink: /news/
---

## My Updates

{% for post in site.posts %}
<article class="news-item">
  <p class="date">{{ post.date | date: "%B %d, %Y" }}</p>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p>{{ post.excerpt | strip_html }}</p>
</article>
{% endfor %}

## External Research Feed

<p class="muted">
This optional feed is populated from <code>data/research_news.json</code>.
If you enable the included GitHub Action, it can refresh daily.
</p>

<div id="external-news" class="external-news">
  <p>Loading external research feed...</p>
</div>

<script src="{{ '/assets/js/news.js' | relative_url }}"></script>
