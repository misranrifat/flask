import json
import pytest
from app import app
from models.item_model import ItemModel

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear database before each test
        ItemModel.items_db = []
        yield client

def test_get_all_items_empty(client):
    response = client.get('/items')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == {'items': []}

def test_create_and_get_item(client):
    # Create item
    response = client.post('/items/test_item', 
                          data={'price': 19.99, 'description': 'Test item description'})
    assert response.status_code == 201
    
    # Get the item
    response = client.get('/items/test_item')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'test_item'
    assert data['price'] == 19.99
    assert data['description'] == 'Test item description'

def test_update_item(client):
    # Create item
    client.post('/items/test_item', data={'price': 19.99})
    
    # Update item
    response = client.put('/items/test_item', 
                         data={'price': 29.99, 'description': 'Updated description'})
    assert response.status_code == 200
    
    # Verify update
    response = client.get('/items/test_item')
    data = json.loads(response.data)
    assert data['price'] == 29.99
    assert data['description'] == 'Updated description'

def test_delete_item(client):
    # Create item
    client.post('/items/test_item', data={'price': 19.99})
    
    # Delete item
    response = client.delete('/items/test_item')
    assert response.status_code == 200
    
    # Verify deletion
    response = client.get('/items/test_item')
    assert response.status_code == 404 