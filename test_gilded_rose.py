# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
    
    # test case1
    def test_quality_degrades_twice_as_fast_after_sell_date(self):
        items = [Item("Elixir of the Mongoose", 0, 10), Item("Conjured Mana Cake", 0, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(8, items[0].quality) 
        self.assertEqual(4, items[1].quality)  # Conjured quality degrades twice as fast

    # test case2
    def test_quality_is_never_negative(self):
        items = [Item("Elixir of the Mongoose", 5, 0), Item("Conjured Mana Cake", 5, 1)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(0, items[0].quality)  # quality is never negative
        self.assertEqual(0, items[1].quality)  # Conjured quality degrades, but is never negative

    # test case3
    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 2, 49), Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(50, items[0].quality)  # Aged Brie，quality increases but never more than 50
        self.assertEqual(50, items[1].quality)  # Backstage passes，quality increases but never more than 50

    # test case4
    def test_sulfuras_never_decreases_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(80, items[0].quality)  # Sulfuras quality never changes

    # test case5
    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(0, items[0].quality)  # Backstage passes quality drops to zero after concert

if __name__ == '__main__':
    unittest.main()
