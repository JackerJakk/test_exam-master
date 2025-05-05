from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView
from db.models import *

app = Starlette()
admin = Admin(
    engine=db.init(),
    title="restaurant bot",
    base_url="/",
    middlewares=[Middleware(SessionMiddleware, secret_key="123456789")] # noqa
)

admin.add_view(ModelView(User))
admin.add_view(ModelView(Category))
admin.add_view(ModelView(Food))

admin.mount_to(app)