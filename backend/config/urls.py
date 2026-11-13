from django.conf import settings
from django.contrib import admin
from django.http import FileResponse, JsonResponse
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


def health_check(request):
    return JsonResponse({
        "status": "ok",
        "service": "royal-agate-export",
        "environment": "development" if request.META.get("HTTP_HOST", "").startswith("localhost") else "production",
    })


def frontend_app(request):
    index_file = settings.BASE_DIR / "frontend-dist" / "index.html"
    return FileResponse(index_file.open("rb"), content_type="text/html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health_check, name="health-check"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/v1/catalogue/", include("apps.catalogue.urls")),
    path("api/v1/inventory/", include("apps.inventory.urls")),
    path("api/v1/accounts/", include("apps.accounts.urls")),
    path("api/v1/cart/", include("apps.cart.urls")),
    path("api/v1/orders/", include("apps.orders.urls")),
    path("api/v1/payments/", include("apps.payments.urls")),
    path("api/v1/dashboard/", include("apps.dashboard.urls")),
    path("api/v1/reviews/", include("apps.reviews.urls")),
    path("api/v1/contact/", include("apps.contact.urls")),
    path("api/v1/content/", include("apps.content.urls")),
]

if (settings.BASE_DIR / "frontend-dist" / "index.html").is_file():
    urlpatterns.append(
        re_path(r"^(?!api/|admin/|static/).*$", frontend_app)
    )
