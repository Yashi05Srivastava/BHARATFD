import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_faq_list_api():
    client = APIClient()
    url = reverse('faq-list')
    
    # Fetch FAQs without language parameter
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
