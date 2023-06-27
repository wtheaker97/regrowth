import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_root_url_logged_in(client, user):
    url = reverse("home")
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_root_url_logged_out_redirect(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse("login")
