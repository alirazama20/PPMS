# Create your models here.
from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# -----------------------------
# Base Models
# -----------------------------

class SoftDeleteManager(models.Manager):
    """Manager to exclude soft deleted objects by default"""
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class BaseModel(models.Model):
    """
    Base model with common fields for all models including soft delete
    """
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    # Soft delete fields
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # User tracking fields
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name="%(app_label)s_%(class)s_created"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name="%(app_label)s_%(class)s_updated"
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name="%(app_label)s_%(class)s_deleted"
    )
    
    # Managers
    objects = SoftDeleteManager()  # default manager - excludes soft deleted
    all_objects = models.Manager()  # include all objects
    
    class Meta:
        abstract = True
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['uid']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f"{self.__class__.__name__} - {self.uid}"
    
    def soft_delete(self, deleted_by=None):
        """Soft delete the instance"""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.deleted_by = deleted_by
        self.save(update_fields=['is_deleted', 'deleted_at', 'deleted_by'])
    
    def restore(self):
        """Restore the soft deleted instance"""
        self.is_deleted = False
        self.deleted_at = None
        self.deleted_by = None
        self.save(update_fields=['is_deleted', 'deleted_at', 'deleted_by'])
    
    def hard_delete(self):
        """Permanently delete the instance"""
        super().delete()
    
    def save(self, *args, **kwargs):
        """Override save to add custom logic if needed"""
        # Add any pre-save logic here
        if not self.uid:
            self.uid = uuid.uuid4()
        super().save(*args, **kwargs)
    
    @classmethod
    def get_by_uid(cls, uid):
        """Get object by uid"""
        try:
            return cls.objects.get(uid=uid)
        except (cls.DoesNotExist, ValueError):
            return None