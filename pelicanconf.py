AUTHOR = 'cmiya'
SITENAME = 'CTRL+ALT+DH'
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Site Theme
THEME="custom-theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Contact Us", "ctrlaltdh@gmail.com"),
    ("CTS", "https://www.uoguelph.ca/arts/cts"),
)

# Social widget
SOCIAL = (
    ("Instagram", "@CtrlAltDH"),
    ("GitHub", "https://github.com/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Tags

# Generate tag pages automatically
TAG_SAVE_AS = 'tag/{slug}.html'     # URL for each tag page
TAG_URL = 'tag/{slug}.html'

# Generate a tags index page listing all tags (optional)
TAGS_SAVE_AS = 'tags.html'          # The tags index page URL

# Menu

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False


MENUITEMS = [
    ('About', '/pages/about.html'),
    ('Team', '/pages/team.html'),
    ('Submissions', '/pages/submissions.html'),
    ('Browse', '/tags.html'),
    ('News', '/news.html'),
]

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'tags', 'news']