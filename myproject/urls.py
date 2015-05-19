from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


from tweet.views import HomePageView, FormHorizontalView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView, LoginView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import tweet

admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="home"),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    
    # Examples:
    # url(r'^$', 'djow.views.home', name='home'),
    # url(r'^djow/', include('djow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^account/edit/', 'custom_user.views.custom_user_update', name='custom_user_update'),
    url(r"^account/", include("account.urls")),    
)
#demo URL


urlpatterns += patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r"^login/", LoginView.as_view(), name='login'),
    url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
)

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
