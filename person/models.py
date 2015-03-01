from django.db import models
from django.utils.translation import ugettext_lazy as _

PYTHON_PRACTICE_CHOICES = (('never',  _('Never')),
                           ('1year', _('<1Year')),
                           ('more', _('>1year')))

DJANGO_PRACTICE_CHOICES = (('never',  _('Never')),
                           ('1year', _('<1Year')),
                           ('more', _('>1year')))

OS_CHOICES = (('mac',  _('Mac')),
              ('linux', _('Linux')),
              ('win', _('windows')))

ENGLISH_LEVEL_CHOICES = (('never',  _('Never')),
                         ('beginner', _('Beginner')),
                         ('fluent', _('Fluent')))

GENDER_CHOICES = (('women',  _('Women')),
                  ('man', _('Man')),
                  ('other', _('Other')))
PARTICIPANT_LEVEL_CHOICES = (('beginner',  _('Beginner')),
                             ('intermediate', _('Intermediate')),
                             ('indifferent', _('Indifferent')))

class Person(models.Model):

    first_name = models.CharField(u'Firstname', max_length=30)
    last_name = models.CharField(u'Lastname', max_length=30)
    email = models.EmailField(u'Email')
    birth_date = models.DateField(u'Birth date')
    phone_number = models.CharField(u'Phone number', max_length=20)
    english_level = models.CharField(u'English Level',
                                     choices=ENGLISH_LEVEL_CHOICES,
                                     max_length=10)
    gender = models.CharField(u'Gender', choices=GENDER_CHOICES,
                              max_length=5)
    hobbie = models.ManyToManyField('Hobbie',
                                    default=None,
                                    blank=True,
                                    null=True,
                                related_name="%(app_label)s_%(class)s_related")
    language = models.ManyToManyField('Language',
                                        default=None,
                                        blank=True,
                                        null=True,
                                related_name="%(app_label)s_%(class)s_related")
    nationality = models.ManyToManyField('Nationality',
                                    default=None,
                                    blank=True,
                                    null=True,
                            related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True

class Mentor(Person):
    participant_level = models.CharField(u'participant level',
                                         choices=PARTICIPANT_LEVEL_CHOICES,
                                         max_length=12)

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Participant(Person):
    python_practice_since = models.CharField(u'Python practice since',
                                             choices=PYTHON_PRACTICE_CHOICES,
                                             max_length=5)
    django_practice_since = models.CharField(u'Django practice since',
                                             choices=DJANGO_PRACTICE_CHOICES,
                                             max_length=5)
    os = models.CharField(u'Operating System', choices=OS_CHOICES,
                          max_length=20)

    Mentor = models.ForeignKey('Mentor', default=None, blank=True,
                               null=True, related_name="participants")

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Language(models.Model):

    name = models.CharField(u'Language', max_length=64)
    iso = models.CharField(u'ISO', max_length=3, primary_key=True)

    def __str__(self):
        return u"%s" % (self.name)

class Hobbie(models.Model):

    name = models.CharField(u'Hobbie', max_length=128)

    def __str__(self):
        return u"%s" % (self.name)

class Nationality(models.Model):

    name = models.CharField(u'Nationality', max_length=64)
    iso = models.CharField(u'ISO', max_length=3, primary_key=True)

    def __str__(self):
        return u"%s" % (self.name)
