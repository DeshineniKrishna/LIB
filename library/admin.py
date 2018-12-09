# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User,Admin,Book_detail,Issue_master,Feedback,Orderbook,DonateBook,NewsFeed

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Book_detail)
admin.site.register(Issue_master)
admin.site.register(Feedback)
admin.site.register(Orderbook)
admin.site.register(DonateBook)
admin.site.register(NewsFeed)


# Register your models here.
