# toolbox/models.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) 
from enum import Enum

class PropertyType(Enum):
    APARTMENT = "APARTMENT"
    HOUSE = "HOUSE"
    COMMERCIAL = "COMMERCIAL"
    LAND = "LAND"

class PropertyStatus(Enum):
    AVAILABLE = "AVAILABLE"
    SOLD = "SOLD"

class Property:
    def __init__(self, property_ID, address, price, property_type, status, owner=None):
        self.property_ID = property_ID
        self.address = address
        self.price = price
        self.property_type = PropertyType[property_type]
        self.status = PropertyStatus[status]
        self.owner = owner
        self.views = 0  # 初始化查看次数

    def __repr__(self):
        return f"Property({self.property_ID}, {self.address}, {self.price}, {self.property_type}, {self.status}, {self.owner}, {self.views})"

    def __eq__(self, other):
        return self.property_ID == other.property_ID

    def __lt__(self, other):
        return self.property_ID < other.property_ID

    def increment_views(self):
        self.views += 1

    def adjust_price(self):
        if self.views > 10:  # 示例条件
            self.price += self.price * 0.1  # 增加10%
        elif self.views < 5:
            self.price -= self.price * 0.05  # 减少5%

class Client:
    def __init__(self, client_ID, name, contact_info, budget):
        self.client_ID = client_ID
        self.name = name
        self.contact_info = contact_info
        self.budget = budget

    def __repr__(self):
        return f"Client({self.client_ID}, {self.name}, {self.contact_info}, {self.budget})"
