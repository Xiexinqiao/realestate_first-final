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

    def __repr__(self):
        return f"Property({self.property_ID}, {self.address}, {self.price}, {self.property_type}, {self.status}, {self.owner})"

    def __eq__(self, other):
        return self.property_ID == other.property_ID

    def __lt__(self, other):
        return self.property_ID < other.property_ID

class Client:
    def __init__(self, client_ID, name, contact_info, budget):
        self.client_ID = client_ID
        self.name = name
        self.contact_info = contact_info
        self.budget = budget

    def __repr__(self):
        return f"Client({self.client_ID}, {self.name}, {self.contact_info}, {self.budget})"
