from django.db import models

class Message(models.Model):
    STATUSES = (
        (1, "sent"),
        (2, "wait")
    )
    title=models.CharField(max_length=100)
    body=models.TextField()
    status=models.PositiveSmallIntegerField(choices=STATUSES, default=2)

    def __str__(self):
        return '{} ({})'.format(self.title, self.status)
