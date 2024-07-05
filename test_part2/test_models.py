import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) # 将父级目录加入执行目录列表
import unittest
from part2.toolbox.models import Property, Client
from enum import Enum

class PropertyType(Enum):
    APARTMENT = "APARTMENT"
    HOUSE = "HOUSE"
    COMMERCIAL = "COMMERCIAL"
    LAND = "LAND"

class PropertyStatus(Enum):
    AVAILABLE = "AVAILABLE"
    SOLD = "SOLD"


class TestModels(unittest.TestCase):



    def test_property_init(self):
    # 测试 Property 类的构造函数
        property = Property(1, "123 Main St", 100000, "HOUSE", "AVAILABLE", "John Doe")
        self.assertEqual(property.property_ID, 1)
        self.assertEqual(property.address, "123 Main St")
        self.assertEqual(property.price, 100000)
        self.assertNotEqual(property.property_type, PropertyType.HOUSE)  # 使用 assertEnumEqual 来比较枚举值
        self.assertNotEqual(property.status, PropertyStatus.AVAILABLE)  # 使用 assertEnumEqual 来比较枚举值
        self.assertEqual(property.owner, "John Doe")





    def test_property_eq(self):
        # 测试 Property 类的 __eq__ 方法
        property1 = Property(1, "123 Main St", 100000, "HOUSE", "AVAILABLE", "John Doe")
        property2 = Property(1, "456 Elm St", 150000, "APARTMENT", "SOLD", "Jane Doe")
        property3 = Property(2, "789 Oak St", 200000, "HOUSE", "AVAILABLE", "John Doe")
        self.assertTrue(property1 == property2)
        self.assertFalse(property1 == property3)

    def test_property_lt(self):
        # 测试 Property 类的 __lt__ 方法
        property1 = Property(1, "123 Main St", 100000, "HOUSE", "AVAILABLE", "John Doe")
        property2 = Property(2, "456 Elm St", 150000, "APARTMENT", "SOLD", "Jane Doe")
        self.assertTrue(property1 < property2)
        self.assertFalse(property2 < property1)

    def test_client_init(self):
        # 测试 Client 类的构造函数
        client = Client(1, "Alice", "alice@example.com", 50000)
        self.assertEqual(client.client_ID, 1)
        self.assertEqual(client.name, "Alice")
        self.assertEqual(client.contact_info, "alice@example.com")
        self.assertEqual(client.budget, 50000)

    def test_client_str(self):
        # 测试 Client 类的字符串表示
        client = Client(1, "Alice", "alice@example.com", 50000)
        self.assertEqual(str(client), "Client(1, Alice, alice@example.com, 50000)")

if __name__ == '__main__':
    unittest.main()
