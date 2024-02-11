""""
Fichier permettant de tester les différentes
fonctionnalités de l'application profiles
et ses vues.
"""
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
class TestProfiles:
    # Classe de tests pour les vues et les modèles de Profiles.

    @classmethod
    def setup_class(cls):
        # Initialise le client pour les tests.
        cls.client = Client()

    def test_profiles_index_view(self):
        # Test de la vue profile_index
        response = self.client.get(reverse('profiles_index'))

        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles_index.html')

    def setup_method(self):
        # Initialise la création d'un test user.
        self.user = User.objects.create_user(username="Testuser2",
                                             password="Testpwd",
                                             email="fakemail@fake.com")
        self.profile = Profile.objects.create(user=self.user, favorite_city="CityTest")

    def test_profile_detail(self):
        # Test la vue profile.
        response = self.client.get(reverse('profile', args=["Testuser2"]))

        assert response.status_code == 200
        assertTemplateUsed(response, "profile.html")

    def test_profile_model(self):
        # Test la méthode __str__ de l'objet Profile.
        assert str(self.profile) == self.user.username
