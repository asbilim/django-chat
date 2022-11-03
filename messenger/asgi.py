from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messenger.settings')

application = ProtocolTypeRouter({
        "http":get_asgi_application(),
        "websocket":AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    websocket_urlpatterns
                )
            )
        )
    }
)