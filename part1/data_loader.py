# data_loader.py

import csv
from toolbox.models import Property, Client
from toolbox.avl_tree import AVLTree
from toolbox.request_manager import RequestManager

def load_properties(file_path):
    properties = AVLTree()
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            property = Property(int(row['property_ID']), row['address'], int(row['price']), row['property_type'], row['status'], row['owner'])
            properties.insert(property.property_ID, property)
    return properties

def parse_budget(budget_str):
    try:
        return int(budget_str.strip().split()[-1])
    except ValueError:
        return None

def load_clients(file_path):
    clients = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            budget = parse_budget(row['budget'])
            if budget is not None:
                client = Client(int(row['client_ID']), row['name'], row['contact_info'], budget)
                clients.append(client)
    return clients

def load_requests(file_path):
    request_manager = RequestManager()
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            budget = parse_budget(row['budget'])
            if budget is not None:
                client = Client(int(row['client_ID']), row['name'], row['contact_info'], budget)
                request_manager.add_request(client)
    return request_manager
