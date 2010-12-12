Django-blahhg - Embeddable blogging app for Django
==================================================
Django-blahhg is an attempt to provide a blogging app that can be easily 
embedded in another web site.

Author
------
George Lesica<br />
<glesica@gmail.com>

Prerequisites
-------------
Blahhg has the following package requirements:

  * markdown
  * django-taggit (also needed in `INSTALLED_APPS`)

It also requires that `django.contrib.humanize` be in your `INSTALLED_APPS`.

Installing
----------
Install the package either using the included setup.py file or through 
pip or put the `blahhg` directory somewhere on your `PYTHONPATH`.

If you use the latter method, take a look at the prerequisites to make sure 
you have everything installed.

As of the current version, `blahhg.urls` must be included in your project 
URLs file at `/blog` to work. This will change in the future.

Settings
--------
### General ###
  * `BLAHHG_TITLE` (required) - the title for the blog.
  * `BLAHHG_DESCRIPTION` (required) - a very brief (one sentence) description 
of the blog.

### Display ###
  * `BLAHHG_LIST_SIZE` (required) - the default size of entry lists.
  * `BLAHHG_USE_COMMENTS` (required) - boolean, whether to try to include 
the comments template in entry detail view.
  * `BLAHHG_USE_SOCIAL` (required) - boolean, whether to try to include the 
social template in entry detail view.

### Feeds ###
  * `BLAHHG_FEED_SIZE` (required) - the number of entries to provide in 
RSS and Atom feeds.
  
Using
-----
Once the app is installed you must supply several templates.

  * `blog.html` - template for the main blog page, a list of new entries.
  * `entry.html` - template for displaying a single entry.
  * `comments.html` - template that displays comments and a comment form.
  * `social.html` - social networking buttons and the like.

Most of these can be quite simple since Blahhg provides pre-built templates 
for displaying most of the elements of a blog. The following built-in 
templates can be used via the `include` template tag:

  * `entry-list.html` - a list of entries plus excerpts.
  * `entry-list-item.html` - an element of the type of list above.
  * `entry-detail.html` - a single entry including text.

For example, a simple `blog.html` file might look like this:

    {% extends "base.html" %}

    {% block content %}
    <h2>My Cool Blog</h2>
    {% include "blahhg/entry-list.html" %}
    {% endblock %}

RSS and Atom feeds are available at `feeds/rss` and `feeds/atom`.
