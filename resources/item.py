from flask_restful import Resource, reqparse
from models.item_model import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('description',
        type=str,
        required=False
    )

    def get(self, name):
        """Get a specific item by name"""
        item = ItemModel.find_by_name(name)
        if item:
            return item.to_dict(), 200
        return {"message": "Item not found"}, 404

    def post(self, name):
        """Create a new item"""
        if ItemModel.find_by_name(name):
            return {"message": f"An item with name '{name}' already exists."}, 400
        
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data.get('description', ''))
        
        try:
            item.save_to_db()
            return item.to_dict(), 201
        except Exception as e:
            return {"message": f"An error occurred inserting the item: {str(e)}"}, 500

    def put(self, name):
        """Create or update an item"""
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        
        if item:
            item.price = data['price']
            item.description = data.get('description', '')
        else:
            item = ItemModel(name, data['price'], data.get('description', ''))
            
        item.save_to_db()
        return item.to_dict(), 200

    def delete(self, name):
        """Delete an item"""
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item deleted"}, 200
        return {"message": "Item not found"}, 404


class ItemList(Resource):
    def get(self):
        """Get all items"""
        return {"items": [item.to_dict() for item in ItemModel.find_all()]}, 200 