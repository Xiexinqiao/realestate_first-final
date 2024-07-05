# utils/enums.py

from enum import Enum

class PropertyType(Enum):
    APARTMENT = "APARTMENT"
    HOUSE = "HOUSE"
    COMMERCIAL = "COMMERCIAL"
    LAND = "LAND"

class PropertyStatus(Enum):
    AVAILABLE = "AVAILABLE"
    SOLD = "SOLD"
