"""Django models utilities."""

# Django
from django.db import models

class CatalogModel(models.Model):
    """Catalogbase model.

     CatalogModel acts as an abstract base classs from which every
     other model in the project will inherit. This class provides
     every table with the following attributes:
        + created (DataTime): store the datetime the object was created.
        + modified (DataTime): Store the last dateime the object was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )

    class Meta:
        """Meta options."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
