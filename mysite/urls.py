from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





# manually added

admin.site.site_header = 'Apna Zone Administration'      # default: "Django Administration"
admin.site.index_title = 'My Project'                 # default: "Site administration"
admin.site.site_title  = 'Apna Zone'                   # default: "Django site admin"
