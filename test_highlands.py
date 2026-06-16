import unittest

from pos_logic import (
    calculate_total,
    add_to_order,
    InvalidQuantityError
)


class TestHighlandsPOS(unittest.TestCase):
    """
    Unit test cho Highlands Mini POS.
    """

    def test_calculate_total(self):
        """
        Test tính tổng tiền.
        """

        mock_order = [
            {
                "code": "P1",
                "name": "Phin Sữa Đá",
                "price": 35000,
                "quantity": 2
            },
            {
                "code": "F1",
                "name": "Freeze Trà Xanh",
                "price": 55000,
                "quantity": 1
            }
        ]

        result = calculate_total(mock_order)

        self.assertEqual(
            result,
            125000
        )


    def test_invalid_quantity(self):
        """
        Test lỗi số lượng âm.
        """

        order = []

        with self.assertRaises(
            InvalidQuantityError
        ):

            add_to_order(
                order,
                "P1",
                -1
            )


if __name__ == "__main__":
    unittest.main()