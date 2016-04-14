# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = os.environ.get("TREEUP_SECRET")

# Secret key for signing cookies
SECRET_KEY = os.environ.get("TREEUP_SECRET")

LOGO_URL = os.environ.get("TREEUP_LOGO_URL", None)
MISSION = os.environ.get("TREEUP_MISSION", "Mission goes here")
TAGLINE = os.environ.get("TREEUP_TAGLINE", "Tagline goes here")
CHARITY = os.environ.get("TREEUP_CHARITY", "Charity Name")
