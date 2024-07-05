# toolbox/property_match.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) 
from toolbox.models import Property, Client
import matplotlib.pyplot as plt

class PropertyMatcher:
    def __init__(self, properties):
        self.properties = properties

    def match_properties(self, client, criteria):
        matched_properties = []
        for property in self.properties:
            if self._match(property, client, criteria):
                matched_properties.append(property)
                property.increment_views()
                property.adjust_price()
        return matched_properties

    def _match(self, property, client, criteria):
        if criteria.get('price_range'):
            min_price, max_price = criteria['price_range']
            if not (min_price <= property.price <= max_price):
                return False
        if criteria.get('property_type') and property.property_type != criteria['property_type']:
            return False
        if criteria.get('location') and criteria['location'] not in property.address:
            return False
        if property.price > client.budget:
            return False
        return True

    def analyze_property_trends(self):
        prices = [prop.price for prop in self.properties]
        plt.hist(prices, bins=10)
        plt.title('Property Price Distribution')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()

    def analyze_client_preferences(self, clients):
        budgets = [client.budget for client in clients]
        plt.hist(budgets, bins=10)
        plt.title('Client Budget Distribution')
        plt.xlabel('Budget')
        plt.ylabel('Frequency')
        plt.show()
