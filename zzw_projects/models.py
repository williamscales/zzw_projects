from django.db import models
from mezzanine.pages.models import Displayable
from mezzanine.core.models import Orderable, RichText


class Project(Displayable, Orderable, RichText):
    """A project."""
    image = models.ImageField(upload_to="projects")
