#Python
import os

#Notifier class
from .notifiers import EmailNotifier, WhatsAppNotifier, EmailAWSSESNotifier

#Models
from apps.users.models import User

class Notifier:

    def __init__(self, data):
        self.data = data
        self.users = User.objects.filter(is_admin=True)

    def notify_everyone(self):

        #Define object under observation
        subject = Subject()

        #Define notifiers extends base classs with a abstract method
        email_notifier = EmailNotifier()
        whatsapp_notifier = WhatsAppNotifier()
        email_aws_ses = EmailAWSSESNotifier()

        #Add notifiers to Listener observer
        if os.environ.get('ENV') == 'local':
            Listener(email_notifier, subject, self.data, self.users)

        if os.environ.get('ENV') != 'local':
            Listener(email_aws_ses, subject, self.data, self.users)

        Listener(whatsapp_notifier, subject, self.data, self.users)

        subject.notify_listeners()

class Listener:

    def __init__(self, object, subject, data, users):
        self.object = object
        self.data = data
        self.users = users
        subject.register(self)

    def notify(self):
        for user in self.users:
            self.object.notify(self.data, user)


class Subject:

    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self):
        for listener in self.listeners:
            listener.notify()
