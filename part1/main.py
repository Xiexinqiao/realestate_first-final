# main.py

from data_loader import load_properties, load_requests


def main():
    properties = load_properties('data/real_estate_properties_dataset.csv')
    request_manager = load_requests('data/client_requests_dataset.csv')

    print("Loaded properties:")
    for prop in properties.in_order_traversal(properties.root):
        print(prop)

    print("\nLoaded requests:")
    while not request_manager.request_queue.empty():
        print(request_manager.request_queue.get())


if __name__ == "__main__":
    main()
