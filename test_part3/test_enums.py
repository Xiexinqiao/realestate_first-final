import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) # 将父级目录加入执行目录列表
import unittest
from part3.utils.enums import PropertyType, PropertyStatus

class TestEnums(unittest.TestCase):

    def test_property_type_values(self):
        # 测试 PropertyType 枚举的值
        self.assertEqual(PropertyType.APARTMENT.value, "APARTMENT")
        self.assertEqual(PropertyType.HOUSE.value, "HOUSE")
        self.assertEqual(PropertyType.COMMERCIAL.value, "COMMERCIAL")
        self.assertEqual(PropertyType.LAND.value, "LAND")

    def test_property_status_values(self):
        # 测试 PropertyStatus 枚举的值
        self.assertEqual(PropertyStatus.AVAILABLE.value, "AVAILABLE")
        self.assertEqual(PropertyStatus.SOLD.value, "SOLD")

    def test_property_type_member_count(self):
        # 确认 PropertyType 枚举中成员的数量
        self.assertEqual(len(PropertyType), 4)

    def test_property_status_member_count(self):
        # 确认 PropertyStatus 枚举中成员的数量
        self.assertEqual(len(PropertyStatus), 2)

    def test_property_type_iteration(self):
        # 测试 PropertyType 枚举的迭代
        expected_values = ["APARTMENT", "HOUSE", "COMMERCIAL", "LAND"]
        for index, prop_type in enumerate(PropertyType):
            self.assertEqual(prop_type.value, expected_values[index])

    def test_property_status_iteration(self):
        # 测试 PropertyStatus 枚举的迭代
        expected_values = ["AVAILABLE", "SOLD"]
        for index, prop_status in enumerate(PropertyStatus):
            self.assertEqual(prop_status.value, expected_values[index])

if __name__ == '__main__':
    unittest.main()
