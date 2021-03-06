from django.db import models
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

import hashlib


def generate_message_token():
    # /!\ birthday problem
    return get_random_string(length=32)


def hexdigest_sha256(*args):
    r = hashlib.sha256()
    for arg in args:
        r.update(str(arg).encode('utf-8'))
    return r.hexdigest()


class MessageCorrespondent(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=64, default=generate_message_token, unique=True)


class MessageThread(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=64, default=generate_message_token, unique=True)


class MessageManager(models.Manager):
    def get_queyset(self):
        qs = super().get_queryset()
        # Does not work so well as prefetch_related is limited to one content type for generic foreign keys
        qs = qs.prefetch_related('author')
        return qs


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(MessageThread)
    author_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    author_id = models.PositiveIntegerField(null=True, blank=True)
    author = GenericForeignKey('author_type', 'author_id')
    from_email = models.EmailField()
    content = models.TextField(blank=True)
    token = models.CharField(max_length=64, default=generate_message_token, unique=True)

    objects = MessageManager()

    class Meta:
        ordering = ['created']

    def send_notification(self, subject, sender, dests, reply_to=None, message_id=None, reference=None, footer=None):
        messages = []
        for dest_name, dest_email in dests:
            correspondent, created = MessageCorrespondent.objects.get_or_create(email=dest_email)
            token = self.thread.token + correspondent.token + hexdigest_sha256(settings.SECRET_KEY, self.thread.token, correspondent.token)[:16]
            if reply_to:
                reply_to_name, reply_to_email = reply_to
                reply_to_list = ['%s <%s>' % (reply_to_name, reply_to_email.format(token=token))]
            else:
                reply_to_list = []
            headers = dict()
            if message_id:
                headers.update({
                    'Message-ID': message_id.format(id=self.token),
                })
            if message_id and reference:
                headers.update({
                    'References': message_id.format(id=reference),
                })
            body = self.content
            if footer is not None:
                body += footer
            messages.append(EmailMessage(
                subject=subject,
                body=body,
                from_email='%s <%s>' % sender,
                to=['%s <%s>' % (dest_name, dest_email)],
                reply_to=reply_to_list,
                headers=headers,
            ))
        connection = get_connection()
        connection.send_messages(messages)

    @property
    def author_display(self):
        if self.author:
            author_class = ContentType.objects.get_for_model(self.author).model_class()
            if author_class == get_user_model():
                return self.author.get_full_name()
            else:
                return str(self.author)
        else:
            return self.from_email

    def __str__(self):
        return _("Message from %(author)s") % {'author': self.author_display}
