from django.db import models


class NotesMixin():
    notes = models.ManyToManyField(to='Note')