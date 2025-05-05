class ItemModel:
    # In-memory database
    items_db = []

    def __init__(self, name, price, description=''):
        self.name = name
        self.price = price
        self.description = description

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description
        }

    def save_to_db(self):
        # Check if item already exists
        existing_item = self.find_by_name(self.name)
        if existing_item:
            # Update existing item
            existing_item.price = self.price
            existing_item.description = self.description
        else:
            # Add new item
            ItemModel.items_db.append(self)

    def delete_from_db(self):
        ItemModel.items_db = [item for item in ItemModel.items_db if item.name != self.name]

    @classmethod
    def find_by_name(cls, name):
        return next((item for item in cls.items_db if item.name == name), None)

    @classmethod
    def find_all(cls):
        return cls.items_db.copy() 