import pytest
from django.urls import reverse
from django.test import Client
from letting.models import Letting, Address


pytestmark = pytest.mark.django_db
@pytest.fixture
def letting_data():
    return {'title': 'Test Letting', 'address': 'Test Address'}

@pytest.fixture
def letting_instance(letting_data):
    return Letting.objects.create(**letting_data)

def test_index_view():
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == 200

# @pytest.mark.django_db
# def test_letting_index_view():
#     print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#     client = Client()
#     print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
#     response = client.get(reverse('lettings_index'))
#     print('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
#     assert response.status_code == 200
#     print('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')

# @pytest.mark.django_db
# def test_address_view():
#     pytestmark = pytest.mark.django_db
#     address = Address.objects.get(id=1)
#     expected_value = "Bedford Street"
#     assert str(address) == expected_value 

@pytest.fixture
def address_data():
    return {
        'number': 7217,
        'street': 'Bedford Street',
        'city': 'Brunswick',
        'state': 'GA',
        'zip_code': 31525,
        'country_iso_code': 'USA',
    }

@pytest.fixture
def address_instance(address_data):
    return Address.objects.create(**address_data)

def test_address_view(address_instance):
    address = Address.objects.get(id=address_instance.id)
    expected_value = "7217 Bedford Street" 
    assert str(address) == expected_value

def test_custom_404_view():
    client = Client()
    response = client.get(reverse('custom_404'))
    assert response.status_code == 404
    assert 'Erreur 404' in str(response.content)

def test_custom_500_view():
    client = Client()
    response = client.get(reverse('custom_500'))
    assert response.status_code == 500
    assert 'Erreur 500' in str(response.content)