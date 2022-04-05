import pytest
from django.urls import reverse

from .models import Letting, Address


class TestLettingsView:
    @pytest.mark.django_db
    def test_retrieve_letting_index(self, client):
        address_1 = Address.objects.create(number="1", street="la joie", city="south park",
                                           state="florida", zip_code="76560", country_iso_code="222")
        Letting.objects.create(title="Maison", address=address_1)
        response = client.get(reverse('lettings_index'))

        assert response.status_code == 200
        assert "Maison" in str(response.content)
