from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from zzw_projects.models import Project

admin.site.register(Project, PageAdmin)
