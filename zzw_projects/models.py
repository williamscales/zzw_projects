from django.db import models

from mezzanine.core.models import Orderable, RichText
from mezzanine.pages.models import Page


class ProjectList(Page, RichText):
    """Page bucket for projects."""
    pass


class Project(Orderable, RichText):
    """A project."""
    project_list = models.ForeignKey("ProjectList", related_name='projects')
    title = models.CharField("Title", max_length=255)
    image = models.ImageField("Image", upload_to="projects")
