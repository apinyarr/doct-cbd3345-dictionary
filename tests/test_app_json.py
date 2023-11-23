import pytest
from app.main import app

@pytest.fixture
def client():
  app.testing = True
  with app.test_client() as client:
      yield client

def test_get_data_first(client):
  response = client.get('/search?word=test')
  assert response.status_code == 200
  assert response.content_type == 'application/json'
  assert response.is_json
  # data = response.get_json()
  # assert 'key' in data
  # assert data['key'] == 'value'

def test_get_data_second(client):
  response = client.get('/search?word=old')
  assert response.status_code == 200
  assert response.content_type == 'application/json'
  assert response.is_json

def test_get_data_thrid(client):
  response = client.get('/search?word=min')
  assert response.status_code == 200
  assert response.content_type == 'application/json'
  assert response.is_json