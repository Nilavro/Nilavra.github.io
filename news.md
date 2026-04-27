---
layout: page
title: News
subtitle: "Research updates, talks, papers, project notes, and optional external research feed."
permalink: /news/
---

## My Updates

{% for post in site.posts %}
<article class="news-card">
  <time>{{ post.date | date: "%B %d, %Y" }}</time>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p>{{ post.excerpt | strip_html }}</p>
</article>
{% endfor %}

## External Research Feed

<p class="muted">
This optional section reads from <code>data/research_news.json</code>. You can edit that JSON file manually or later automate it with a GitHub Action.
</p>

<div id="external-news" class="external-news">
  <p class="muted">Loading external research feed…</p>
</div>

<script src="{{ '/assets/js/news.js' | relative_url }}"></script>
