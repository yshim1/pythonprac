# Write your code below:
import surfshop, unittest

class surfTest(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()
    #print('Cart has been emptied.')
  
  def test_add_surfboards(self):
    for num in [2,4]:
     with self.subTest():
       expected_result = 'Successfully added {} surfboards to cart!'.format(num)
       message = 'Expected add_surfboards('+str(num)+') to return '+str(expected_result)
       self.assertEqual(self.cart.add_surfboards(num), expected_result, message)
       #self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5) ('Business in offseason, quantity increased)
  
  def test_apply_locals_discount(self):
    self.assertTrue(self.cart.apply_locals_discount())

unittest.main()