import pytest

from rest_framework.test import APIClient #POST GET itd coś jak axios
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def unauthotized_client():
    return APIClient()

@pytest.fixture
def client():
    user = User.object.create(
        email='john.doe@wspa.pl',
        first_name='john',
        last_name='doe',
        is_activate=True
    )
    refresh = RefreshToken.for_user(user)
    client = APIClient
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    client.user = user
    return client
