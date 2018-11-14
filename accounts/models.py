from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser, UserManager)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from accounts import constants as c
# from trades import models as

# from ghanalaw.utils.mails import send_mail

COUNTRIES = c.COUNTRIES


class NewManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True,)
    company_name = models.CharField(_('company name'), max_length=50, blank=True)
    phone = models.CharField(_('phone'), max_length=15)
    country = models.CharField(_('country'), max_length=5, choices=COUNTRIES, blank=True)
    is_rahman = models.BooleanField(
        _('rahman status'),
        default=False,
        help_text=_(
            'Lower than admin and higher than regular user'
        )
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_verified = models.BooleanField(
        _('verified'),
        default=False,
        help_text=_(
            'Designates whether this user is verified by email. '
        ),
    )
    last_login = models.DateTimeField(
        _('last css'),
        auto_now=True
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = NewManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    # def email_user(self, subject, email_template_name, context,
    #                html_email_template_name=None, from_email=None, **kwargs):
    #     """
    #     Sends an email to this User.
    #     """
    #     send_mail(
    #         subject, email_template_name, context, [self.email],
    #         html_email_template_name, from_email, **kwargs)
