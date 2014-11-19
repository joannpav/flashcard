from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^$', 'flash_card.views.home', name='home'),
    url(r'^make_card/', 'flash_card.views.make_card', name='make_card'),
	url(r'^createCard/', 'flash_card.views.createCard', name='createCard'),
	url(r'^ocr/', 'flash_card.views.ocr', name='ocr'),
	url(r'^cardBox/', 'flash_card.views.viewCardList', name='cardBox'),
    url(r'^quiz/', 'flash_card.views.quiz', name='quiz'),
    #url(r'^admin/', include(admin.site.urls)),
)
