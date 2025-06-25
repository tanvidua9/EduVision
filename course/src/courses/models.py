from django.db import models


class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # uuid = models.UUIDField(default=uuid.uuid1, unique=True)
    public_id = models.CharField(max_length=130, blank=True, null=True, db_index=True)
    access = models.CharField(
        max_length=10, 
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )

    # @property decorator in Python is used to define a method that you can access like an attribute — without needing parentheses ()
    # Using @property makes it read-only
    @property    
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
