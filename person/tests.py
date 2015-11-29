from django.test import TestCase

from person.models import Participant

class ParticipantTestCase(TestCase):
    from person.models import Participant

class ParticipantTestCase(TestCase):

    def test_participant_create_one_person(self):
        fanta = Participant.objects.create(first_name='fanta',
                last_name= 'carrot',email='test.test@gmail.com',birth_date='2015-03-09',
                phone_number='000000000',english_level='Never',gender='women' )

        self.assertEqual(fanta.first_name, 'fanta'),
        (fanta.last_name, 'carrot'),
        (fanta.email, 'test.test@gmail.com'),
        (fanta.birth_date,'2015-03-09'),
        (fanta.phone_number, '000000000'),
        (fanta.english_level,'Never'),
        (fanta.gender,'women')

    
