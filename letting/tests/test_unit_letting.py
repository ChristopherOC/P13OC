import pytest
from django.urls import reverse
from django.http import Http404
from django.test import RequestFactory, Client
from letting.models import Letting, Address

from letting.views import index, lettings_index, letting, custom_404, custom_500

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

@pytest.mark.django_db
def test_address_model(get_dummy_db):
    address = Address.objects.get(id=1)
    expected_value = "6 rue du moulin"
    assert str(address) == expected_value