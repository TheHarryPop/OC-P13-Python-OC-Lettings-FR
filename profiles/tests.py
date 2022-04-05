import pytest
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


@pytest.fixture
def profile():
    user = User.objects.create_user(username='Aquaman', first_name='Aqua', last_name='Man',
                                    email='aqua@man.com')
    profile = Profile.objects.create(user=user, favorite_city='Denver')
    return profile


class TestProfileView:
    @pytest.mark.django_db
    def test_retrieve_profile_index(self, client, profile):
        response = client.get(reverse('profiles_index'))

        assert response.status_code == 200
        assert b'<title>Profiles</title>' in response.content

    @pytest.mark.django_db
    def test_retrieve_profile_profile(self, client, profile):
        response = client.get(reverse('profile', args=[profile.user.username]))

        assert response.status_code == 200
        assert b'<title>Aquaman</title>' in response.content
