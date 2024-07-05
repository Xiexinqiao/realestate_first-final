# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from data_loader import load_properties, load_clients
from toolbox.property_match import PropertyMatcher


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Real Estate Property Management System")
        self.geometry("800x600")

        self.properties = load_properties('data/real_estate_properties_dataset.csv')
        self.clients = load_clients('data/client_requests_dataset.csv')

        self.create_widgets()

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self)

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='View Properties')
        self.create_tab1_widgets()

        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='Client Requests')
        self.create_tab2_widgets()

        self.tab_control.pack(expand=1, fill='both')

    def create_tab1_widgets(self):
        frame = ttk.Frame(self.tab1)
        frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame)
        self.tree['columns'] = ('ID', 'Address', 'Price', 'Type', 'Status', 'Owner', 'Views')
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", anchor=tk.CENTER, width=80)
        self.tree.column("Address", anchor=tk.W, width=120)
        self.tree.column("Price", anchor=tk.CENTER, width=100)
        self.tree.column("Type", anchor=tk.CENTER, width=80)
        self.tree.column("Status", anchor=tk.CENTER, width=80)
        self.tree.column("Owner", anchor=tk.CENTER, width=100)
        self.tree.column("Views", anchor=tk.CENTER, width=80)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Address", text="Address", anchor=tk.W)
        self.tree.heading("Price", text="Price", anchor=tk.CENTER)
        self.tree.heading("Type", text="Type", anchor=tk.CENTER)
        self.tree.heading("Status", text="Status", anchor=tk.CENTER)
        self.tree.heading("Owner", text="Owner", anchor=tk.CENTER)
        self.tree.heading("Views", text="Views", anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.load_properties()

        self.tree.bind('<ButtonRelease-1>', self.on_tree_select)

        control_frame = ttk.Frame(frame)
        control_frame.pack(fill=tk.X)

        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(control_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        search_button = ttk.Button(control_frame, text="Search", command=self.search_properties)
        search_button.pack(side=tk.LEFT, padx=5, pady=5)

    def load_properties(self):
        for prop in self.properties.in_order_traversal(self.properties.root):
            self.tree.insert("", tk.END, values=(
            prop.property_ID, prop.address, prop.price, prop.property_type.value, prop.status.value, prop.owner,
            prop.views))

    def on_tree_select(self, event):
        selected_item = self.tree.selection()[0]
        prop = self.tree.item(selected_item, "values")
        messagebox.showinfo("Property Details",
                            f"ID: {prop[0]}\nAddress: {prop[1]}\nPrice: {prop[2]}\nType: {prop[3]}\nStatus: {prop[4]}\nOwner: {prop[5]}\nViews: {prop[6]}")

    def search_properties(self):
        query = self.search_var.get().strip()
        if not query:
            messagebox.showwarning("Search Error", "Please enter a search query")
            return

        # Example: simple search by address or ID
        matching_properties = []
        for prop in self.properties.in_order_traversal(self.properties.root):
            if query.lower() in prop.address.lower() or query == str(prop.property_ID):
                matching_properties.append(prop)

        if not matching_properties:
            messagebox.showinfo("No Results", "No matching properties found")
        else:
            for item in self.tree.get_children():
                self.tree.delete(item)
            for prop in matching_properties:
                self.tree.insert("", tk.END, values=(
                prop.property_ID, prop.address, prop.price, prop.property_type.value, prop.status.value, prop.owner,
                prop.views))

    def create_tab2_widgets(self):
        frame = ttk.Frame(self.tab2)
        frame.pack(fill=tk.BOTH, expand=True)

        self.request_list = tk.Listbox(frame)
        self.request_list.pack(fill=tk.BOTH, expand=True)
        self.load_requests()

        control_frame = ttk.Frame(frame)
        control_frame.pack(fill=tk.X)

        process_button = ttk.Button(control_frame, text="Process Request", command=self.process_request)
        process_button.pack(side=tk.LEFT, padx=5, pady=5)

    def load_requests(self):
        for client in self.clients:
            self.request_list.insert(tk.END,
                                     f"{client.client_ID}: {client.name}, {client.contact_info}, Budget: {client.budget}")

    def process_request(self):
        selected_index = self.request_list.curselection()
        if not selected_index:
            messagebox.showwarning("Process Error", "Please select a request to process")
            return

        request_str = self.request_list.get(selected_index)
        client_id = int(request_str.split(":")[0])
        client = next(c for c in self.clients if c.client_ID == client_id)

        matcher = PropertyMatcher(self.properties.in_order_traversal(self.properties.root))
        criteria = {}  # 可以根据需要添加更多搜索条件
        matched_properties = matcher.match_properties(client, criteria)

        if not matched_properties:
            messagebox.showinfo("No Matching Properties", "No properties match the client's criteria")
        else:
            result = "\n".join(
                f"ID: {prop.property_ID}, Address: {prop.address}, Price: {prop.price}" for prop in matched_properties)
            messagebox.showinfo("Matching Properties", result)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
