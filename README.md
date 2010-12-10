Django-blahhg - Embeddable blogging app for Django
==================================================
Django-blahhg is an attempt to provide a blogging app that can be easily 
embedded in another web site.

Author
------
George Lesica<br />
<glesica@gmail.com>

Installing
----------

Settings
--------
=== General ===
  * `BLAHHG_TITLE` (required) - the title for the blog.
  * `BLAHHG_DESCRIPTION` (required) - a very brief (one sentence) description 
    of the blog.
=== Display ===
  * `BLAHHG_LIST_SIZE` (required) - the default size of entry lists.
  * `BLAHHG_USE_COMMENTS` (required) - boolean, whether to try to include 
    the comments template in entry detail view.
  * `BLAHHG_USE_SOCIAL` (required) - boolean, whether to try to include the 
    social template in entry detail view.
=== Feeds ===
  * `BLAHHG_FEED_SIZE` (required) - the number of entries to provide in 
    RSS and Atom feeds.
  
Using
-----
