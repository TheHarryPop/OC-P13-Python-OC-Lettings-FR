from django.urls import reverse


class TestSiteView:
    def test_retrieve_index(self, client):
        response = client.get(reverse('index'))
        assert response.status_code == 200
        assert b'<title>Holiday Homes</title>' in response.content
