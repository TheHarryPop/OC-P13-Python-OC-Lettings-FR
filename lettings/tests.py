import pytest
from django.urls import reverse

from .models import Letting, Address


@pytest.fixture
def address():
    address = Address.objects.create(number="1", street="la joie", city="South Park",
                                     state="florida", zip_code="76560", country_iso_code="222")
    return address


@pytest.fixture
def letting(address):
    letting = Letting.objects.create(title="Maison", address=address)
    print(letting.address)
    return letting


class TestLettingsView:
    @pytest.mark.django_db
    def test_retrieve_letting_index(self, client, letting):
        response = client.get(reverse('lettings_index'))

        assert response.status_code == 200
        assert b'<title>Lettings</title>' in response.content

    @pytest.mark.django_db
    def test_retrieve_letting_letting(self, client, letting):
        response = client.get(reverse('letting', args=[letting.id]))

        assert response.status_code == 200
        assert b'<title>Maison</title>' in response.content
