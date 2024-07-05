import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) 
from unittest.mock import MagicMock
from part2.toolbox.property_match import PropertyMatcher
from part2.toolbox.models import Property, Client
class TestPropertyMatcher(unittest.TestCase):

    def setUp(self):
        # 创建模拟的属性对象
        self.property1 = MagicMock(spec=Property)
        self.property1.price = 300000
        self.property1.property_type = 'house'
        self.property1.address = '123 Main St'
        self.property1.views = 0

        self.property2 = MagicMock(spec=Property)
        self.property2.price = 450000
        self.property2.property_type = 'apartment'
        self.property2.address = '456 Elm St'
        self.property2.views = 0

        # 创建模拟的客户对象
        self.client = MagicMock(spec=Client)
        self.client.budget = 400000

        # 创建PropertyMatcher实例
        self.matcher = PropertyMatcher([self.property1, self.property2])

    def test_match_properties(self):
        # 测试匹配标准：价格范围在300k-400k，类型为house，位于'123 Main St'
        criteria = {'price_range': (300000, 400000), 'property_type': 'house', 'location': '123 Main St'}
        matches = self.matcher.match_properties(self.client, criteria)

        # 验证只有property1被匹配
        self.assertEqual(len(matches), 1)
        self.assertIn(self.property1, matches)
        self.assertNotIn(self.property2, matches)

        # 验证property1的views和price已经被更新
        self.property1.increment_views.assert_called_once()
        self.property1.adjust_price.assert_called_once()

        # 检查property2没有被调用这些方法
        self.property2.increment_views.assert_not_called()
        self.property2.adjust_price.assert_not_called()

if __name__ == '__main__':
    unittest.main()