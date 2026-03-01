import unittest

def snake_order_garden(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                result.append(matrix[i][j])
        else:
            for j in range(cols-1, -1, -1):
                result.append(matrix[i][j])
    return result

class TestSnakeOrder(unittest.TestCase):
    def test_example(self):
        garden = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 16, 15, 14, 13]
        self.assertEqual(snake_order_garden(garden), expected)
    
    def test_small(self):
        garden = [[1, 2], [3, 4]]
        expected = [1, 2, 4, 3]
        self.assertEqual(snake_order_garden(garden), expected)

if __name__ == '__main__':
    garden = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Для робота:", snake_order_garden(garden))
    unittest.main()


