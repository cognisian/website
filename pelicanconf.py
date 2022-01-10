AUTHOR = 'Sean Chalmers'
SITENAME = 'ArtificialBelligerence'
SITESUBTITLE='Programmer, Developer of Code'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = [
    "/home/schalmers/Projects/pelican-plugins",
    "plugins/pelican-plugins"
]
PLUGINS = ["sitemap", 'i18n_subsites']

# sitemap plugin settings
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{category}/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Turn off the author, category, tags pages
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
TAG_URL = ''
TAG_SAVE_AS = ''

# Turn off the author, category, tags archive pages
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

STATIC_PATHS = [
    'images',
    'extra/robots.txt'
]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {
            'path': 'robots.txt'
    },
}

#
# THEME
#
THEME = '/home/schalmers/Projects/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

FAVICON = ''
SITELOGO = ''
SITELOGO_SIZE = 0 #width
BANNER = ''
BANNER_SUBTITLE = 'Programmer, Developer of Code'
BANNER_ALL_PAGES = False

BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = False

DEFAULT_PAGINATION = 10

# MENU
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('Writing', '/pages/poetry.html'),
    ('About', '/pages/about.html'),
)

GITHUB_URL = 'https://github.com/cognisian'

LINKS = (
    ('Python.org', 'https://www.python.org/'),
    ('Pelican', 'https://getpelican.com/'),
    ('Theme', 'https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3'),
)

# Social widget
DISABLE_SIDEBAR_TITLE_ICONS = False
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/seanchalmers'),
    ('github', GITHUB_URL),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

