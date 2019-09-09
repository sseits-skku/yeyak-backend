from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('account/', include('account.urls')),
    path('card/', include('card.urls')),
    path('seminar/', include('seminar.urls'))
]

if settings.DEBUG:
    from django.contrib import admin
    import debug_toolbar

    urlpatterns += [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls',
                                  namespace='rest_framework')),
        path('__debug__', include(debug_toolbar.urls))
    ]
