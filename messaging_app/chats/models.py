import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom manager for user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        # Ensure email is provided
        if not email:
            raise ValueError("Email is required!")
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields) # Set & normalize email address
        user.set_password(password)  # Set the password
        user.save(using=self._db)  # Save the user to the database

        return user

    def create_superuser(self, email, username, password=None, **extra_fields ):
        user = self.create_user(email, password, username, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)  # Save the superuser to the database

        # Call create_user to handle superuser creation
        return user


# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False, blank=False, max_length=255) # Email is unique and required
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    REQUIRED_FIELDS = ['email']  # Specify the fields that are required when creating a user (excluding the username)
   
    objects = CustomUserManager()  # Custom manager for handling user creation

    def __str__(self):
        return self.username

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(CustomUser, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id}"

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} in Conversation {self.conversation.conversation_id}"

    def __str__(self):
        return f"Message from {self.sender} in Conversation {self.conversation.id}"
