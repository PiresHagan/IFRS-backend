from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from utils.models import TimeStampedMixin

User = get_user_model()


class ModelDefinition(TimeStampedMixin):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('locked', 'Locked'),
        ('deleted', 'Deleted'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=20, default="v1.0")
    config = models.JSONField(default=dict)  # All configuration including product_type, measurement_model, assumptions, formulas, parameters
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='draft'
    )
    
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='created_models'
    )
    last_modified_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='modified_models'
    )
    
    cloned_from = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='clones'
    )
    
    locked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='locked_models'
    )
    locked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-modified_on']
        verbose_name = 'Model Definition'
        verbose_name_plural = 'Model Definitions'

    def __str__(self):
        return f"{self.name} (v{self.version})"

    def is_locked(self):
        return self.locked_by is not None

    def can_edit(self, user):
        if self.status == 'locked':
            return False
        if self.locked_by and self.locked_by != user:
            return False
        return True


class ModelDefinitionHistory(models.Model):
    model = models.ForeignKey(
        ModelDefinition, 
        on_delete=models.CASCADE, 
        related_name='history'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=20)
    config = models.JSONField(default=dict)  # All configuration data at time of save
    saved_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True
    )

    class Meta:
        ordering = ['-saved_at']
        verbose_name = 'Model Definition History'
        verbose_name_plural = 'Model Definition History'

    def __str__(self):
        return f"{self.name} v{self.version} - {self.saved_at}"
