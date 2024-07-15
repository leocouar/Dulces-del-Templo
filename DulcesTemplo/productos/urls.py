from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from productos import views

router = routers.DefaultRouter()
router.register(r'productos',views.ProductoView,'productos')

urlpatterns =[
    path('api/v1/',include(router.urls)),
    path('docs/',include_docs_urls(title='Productos API')),
    #     path(
    #     "openapi",
    #     get_schema_view(title="Your Project", description="API for all things …"),
    #     name="openapi-schema",
    # ),
]