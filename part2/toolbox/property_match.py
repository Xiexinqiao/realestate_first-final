# toolbox/property_match.py

from toolbox.models import Property, Client

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
