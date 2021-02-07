from .common import *

PUBLIC_REGISTER_ENABLED = True
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '$ok$l6qr@z2a#hiugxk0b)080xa7jd*s31#ku(56925r*i5i3d'

MEDIA_URL = "https://backtaiga.valeapna.com/media/"
STATIC_URL = "https://backtaiga.valeapna.com/static/"
ADMIN_MEDIA_PREFIX = "https://backtaiga.valeapna.com/static/admin/"
SITES["api"]["scheme"] = "https"
SITES["api"]["domain"] = "backtaiga.valeapna.com"
SITES["front"]["scheme"] = "https"
SITES["front"]["domain"] = "taiga.valeapna.com"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "taiga",
        "HOST": "db",
        "USER": "postgres",
        "PASSWORD": "password"
    }
}

DEFAULT_FROM_EMAIL = "pnappproj@valeapna.com"
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 4 #seconds
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True # You cannot use both (TLS and SSL) at the same time!
EMAIL_HOST = 'email.valeapna.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'pnappproj@valeapna.com'
EMAIL_HOST_PASSWORD = '###Pn@229933###'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:password@rabbit:5672/taiga"}

CELERY_ENABLED = True
WEBHOOKS_ENABLED = True
WEBHOOKS_BLOCK_PRIVATE_ADDRESS = True

# Configurações do módulo de feedback
FEEDBACK_ENABLED = True
FEEDBACK_EMAIL = "pnapptaiga@aquivaleapena.com"

MAX_PENDING_MEMBERSHIPS = 30 # Número máximo de associações não confirmadas em um projeto