import pytest
from django.urls import reverse
from django.test import Client
from letting.models import Letting, Address
from django.http import Http404
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
class TestLettings:

    @classmethod
    def setup_class(cls):
        # Initialise le client pour les tests.
        cls.client = Client()

    @pytest.fixture
    def letting_data(self):
        return {'title': 'Test Letting', 'address': 'Test Address'}

    @pytest.fixture
    def letting_instance(self, letting_data):
        return Letting.objects.create(**letting_data)

    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_letting_index_view(self):
        client = Client()
        response = client.get(reverse('lettings_index'))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_address_view(self, address_instance):
        address = Address.objects.get(id=address_instance.id)
        expected_value = "7217 Bedford Street"
        assert str(address) == expected_value

    @pytest.fixture
    def address_data(self):
        return {
            'number': 7217,
            'street': 'Bedford Street',
            'city': 'Brunswick',
            'state': 'GA',
            'zip_code': 31525,
            'country_iso_code': 'USA',
        }

    @pytest.fixture
    def address_instance(self, address_data):
        return Address.objects.create(**address_data)

    def test_custom_404_view(self):
        client = Client()
        response = client.get(reverse('custom_404'))
        assert response.status_code == 404
        assert 'Erreur 404' in str(response.content)

    def test_error_404_view(self):
        response = self.client.get(reverse('letting', args=[35]))
        assert response.status_code == 404
        assertTemplateUsed(response, '404.html')


    def test_custom_500_view(self):
        client = Client()
        response = client.get(reverse('custom_500'))
        assert response.status_code == 500
        assert 'Erreur 500' in str(response.content)