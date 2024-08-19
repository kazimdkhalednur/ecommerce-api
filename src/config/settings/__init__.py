from .base import ENVIRONMENT

if ENVIRONMENT == "local":
    from .local import *
elif ENVIRONMENT == "staging":
    from .staging import *
elif ENVIRONMENT == "production":
    from .production import *
