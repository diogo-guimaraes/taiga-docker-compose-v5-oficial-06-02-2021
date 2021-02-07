# TAIGA DOCKER INSTALAÇÃO

## SOBRE

Este é um arquivo de exemplo do Docker Compose para executar a plataforma de gerenciamento de projetos [Taiga](https://taiga.io) para desenvolvedores ágeis, designers e gerentes de projetos com taiga-events e proxy reverso habilitado para ssl com todas as imagens baseadas em alpine: latest.

## INSTALAÇÃO

1) Clone o repositório.
`git clone https://github.com/PnA-Publicidade/taiga-docker.git taiga_docker`
2) Ajuste `TAIGA_HOST`, `TAIGA_SECRET`, `POSTGRES_PASSWORD`, `RABBIT_PASSWORD` e `REDIS_PASSWORD` no arquivo `variables.env`.
3) mkdir /traefik/acme.json
4) chmod 600 acme.json
4) `docker-compose up`

## USUÁRIO PADRÃO:

O nome de usuário e senha padrão que o taiga cria é `admin` com a senha` 123123`.

### CASO NÃO SEJA CRIADO O USUÁRIO PADRÃO:

```shell
$ ./console python3 manage.py loaddata initial_user --traceback
$ ./console python3 manage.py loaddata initial_project_templates --traceback
```

Taiga para usar na configuração de taiga.
- `TAIGA_SCHEME` - Taiga URL scheme (http/https). Por padrão 'http'.
- `TAIGA_BACK_HOST` - Backend nome do host. Por padrão `back` serviço.
- `TAIGA_FRONT_HOST` - Frontend nome do host. Por padrão `front` serviço.
- `EVENTS_HOST` - Events nome do host. Por padrão `events` serviço.
- `TAIGA_SECRET` - Django chave secreta.

---

---

- `POSTGRES_HOST` - PostgeSQL nome do host. Por padrão `db` serviço.
- `POSTGRES_DB` - Nome do banco de dados.
- `POSTGRES_USER` - PostgreSQL usuario.
- `POSTGRES_PASSWORD` - PostgreSQL senha.

---

- `RABBIT_HOST` - RabbitMQ nome do host. Por padrão `rabbit` serviço.
- `RABBIT_USER` - RabbitMQ usuario.
- `RABBIT_PASSWORD` - RabbitMQ senha.
- `RABBIT_VHOST` - RabbitMQ virtual nome do host.

---

- `REDIS_HOST` - Redis nome do host. Por padrão `redis` serviço.
- `REDIS_PASSWORD` - Redis senha.
- `REDIS_DB` - Redis banco de dados index.

## CONFIGURAÇÃO

Por padrão, o volume de configuração é `./conf` com arquivos de configuração `./conf/back/config.py` para back-end,`./conf/front/config.json` para front-end. Os arquivos de configuração gerados são colocados aqui na primeira execução e podem ser modificados para especificar, por exemplo, Configuração do servidor SMTP.

## PERSISTÊNCIA DE DADOS

Volume `./data` contém dados postgresql e arquivos de mídia taiga para fins de persistência e backup.


## Config.py

```python
from .common import *

PUBLIC_REGISTER_ENABLED = False
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '$ok$l6qr@z2a#hiugxk0b)080xa7jd*s31#ku(56925r*i5i3d'

MEDIA_URL = "https://localhost:8080/media/"
STATIC_URL = "https://localhost:8080/static/"
ADMIN_MEDIA_PREFIX = "https://localhost:8080/static/admin/"
SITES["api"]["scheme"] = "https"
SITES["api"]["domain"] = "localhost"
SITES["front"]["scheme"] = "https"
SITES["front"]["domain"] = "localhost"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "taiga",
        "HOST": "db",
        "USER": "postgres",
        "PASSWORD": "password"
    }
}

DEFAULT_FROM_EMAIL = "pnapptaiga@aquivaleapena.com"
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True # You cannot use both (TLS and SSL) at the same time!
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'pnapptaiga@aquivaleapena.com'
EMAIL_HOST_PASSWORD = '###Pn@229933###'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:password@rabbit:5672/taiga"}

CELERY_ENABLED = True

```