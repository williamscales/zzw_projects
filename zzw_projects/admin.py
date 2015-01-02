from django.contrib import admin

from copy import deepcopy

from mezzanine.core.admin import StackedDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from zzw_projects.models import Project, ProjectList

project_extra_fieldsets = ((None, {'fields': ('title',)}),)


class ProjectInline(StackedDynamicInlineAdmin):
    model = Project


class ProjectListAdmin(PageAdmin):
    inlines = (ProjectInline,)
    #fieldsets = deepcopy(PageAdmin.fieldsets) + project_extra_fieldsets

admin.site.register(ProjectList, ProjectListAdmin)
