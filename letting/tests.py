import pytest
from django.urls import reverse
from django.http import Http404
from django.test import RequestFactory, Client
from letting.models import Letting

from letting.views import index, lettings_index, letting, custom_404, custom_500

# @pytest.fixture
# def letting_data():
#     return {'title': 'Test Letting', 'address': 'Test Address'}

# @pytest.fixture
# def letting_instance(letting_data):
#     return Letting.objects.create(**letting_data)

def test_index_view():
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == 200


def test_letting_index_view():
    client = Client()
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200