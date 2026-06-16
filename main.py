import logging
import unittest


logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)



class InvalidAmountError(Exception):
    """
    Lỗi xảy ra khi số tiền giao dịch <= 0.
    """


class InsufficientBalanceError(Exception):
    """
    Lỗi xảy ra khi số dư ví không đủ.
    """




class Wallet:
    """
    Class quản lý ví MoMo.

    Attributes:
        balance: số dư hiện tại của ví.
    """

    def __init__(self):
        """
        Khởi tạo ví với số dư ban đầu bằng 0.
        """

        self.balance = 0



    def deposit(self, amount):
        """
        Nạp tiền vào ví.

        Args:
            amount: số tiền cần nạp.

        Raises:
            InvalidAmountError:
                Nếu số tiền nhỏ hơn hoặc bằng 0.
        """

        if amount <= 0:
            raise InvalidAmountError()

        self.balance += amount



    def transfer(self, amount):
        """
        Chuyển tiền từ ví.

        Args:
            amount: số tiền muốn chuyển.

        Raises:
            InvalidAmountError:
                Nếu số tiền không hợp lệ.

            InsufficientBalanceError:
                Nếu số dư không đủ.
        """

        if amount <= 0:
            raise InvalidAmountError()


        if amount > self.balance:
            raise InsufficientBalanceError()


        self.balance -= amount



    def get_balance(self):
        """
        Lấy số dư hiện tại.

        Returns:
            Số dư ví.
        """

        return self.balance




wallet = Wallet()




def deposit_money():
    """
    Xử lý chức năng nạp tiền.
    """

    print("\n--- NẠP TIỀN VÀO VÍ ---")


    try:

        amount = int(
            input("Nhập số tiền cần nạp: ")
        )


        wallet.deposit(amount)


        logging.info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {wallet.balance}"
        )


        print(
            f"Nạp tiền thành công: "
            f"+{amount:,} VND"
        )

        print(
            f"Số dư hiện tại: "
            f"{wallet.balance:,} VND"
        )


    except ValueError:

        logging.error(
            "ValueError: Invalid numeric input "
            "for deposit."
        )


        print(
            "Lỗi: Vui lòng nhập số tiền hợp lệ."
        )


    except InvalidAmountError:

        logging.error(
            f"InvalidAmountError: "
            f"Attempted to process {amount} VND."
        )


        print(
            "Lỗi: Số tiền giao dịch phải lớn hơn 0."
        )



def transfer_money():
    """
    Xử lý chức năng chuyển tiền.
    """

    print("\n--- CHUYỂN TIỀN ---")


    phone = input(
        "Nhập số điện thoại người nhận: "
    )


    try:

        amount = int(
            input("Nhập số tiền cần chuyển: ")
        )


        if amount >= 10000000:

            logging.warning(
                f"High value transaction detected: "
                f"{amount} VND to {phone}"
            )


        wallet.transfer(amount)


        logging.info(
            f"Transfer successful: "
            f"-{amount} VND to {phone}. "
            f"Current Balance: {wallet.balance}"
        )


        print(
            f"Chuyển tiền thành công tới "
            f"số điện thoại {phone}."
        )


        print(
            f"Số tiền đã chuyển: "
            f"{amount:,} VND"
        )


        print(
            f"Số dư còn lại: "
            f"{wallet.balance:,} VND"
        )


    except ValueError:

        logging.error(
            "ValueError: Invalid numeric input."
        )


        print(
            "Lỗi: Vui lòng nhập số tiền hợp lệ."
        )


    except InvalidAmountError:

        logging.error(
            f"InvalidAmountError: "
            f"Attempted to process {amount} VND."
        )


        print(
            "Lỗi: Số tiền giao dịch phải lớn hơn 0."
        )


    except InsufficientBalanceError:

        logging.error(
            f"InsufficientBalanceError: "
            f"Attempted to transfer {amount} "
            f"VND with balance "
            f"{wallet.balance} VND."
        )


        print(
            "Giao dịch thất bại: "
            "Số dư của bạn không đủ."
        )



def show_balance():
    """
    Hiển thị số dư hiện tại.
    """

    logging.info(
        f"Balance checked. "
        f"Current Balance: {wallet.balance}"
    )


    print("\n--- SỐ DƯ VÍ MOMO ---")


    print(
        f"Số dư hiện tại: "
        f"{wallet.balance:,} VND"
    )



def display_menu():
    """
    Hiển thị menu chương trình.
    """

    print(
        """
========== VÍ MOMO GIẢ LẬP ==========

1. Nạp tiền vào ví

2. Chuyển tiền

3. Xem số dư hiện tại

4. Thoát chương trình

====================================
"""
    )



def main():
    """
    Điều khiển chương trình CLI.
    """

    while True:

        display_menu()


        choice = input(
            "Chọn chức năng (1-4): "
        )


        if choice == "1":

            deposit_money()


        elif choice == "2":

            transfer_money()


        elif choice == "3":

            show_balance()


        elif choice == "4":

            logging.info(
                "System shutdown"
            )

            print(
                "Cảm ơn bạn đã sử dụng dịch vụ"
            )

            break



        else:

            print(
                "Lựa chọn không hợp lệ."
            )


class TestWallet(unittest.TestCase):
    """
    Kiểm thử class Wallet.
    """


    def test_deposit_success(self):
        """
        Kiểm tra nạp tiền thành công.
        """

        wallet_test = Wallet()

        wallet_test.deposit(500000)

        self.assertEqual(
            wallet_test.balance,
            500000
        )



    def test_transfer_insufficient_balance(self):
        """
        Kiểm tra chuyển tiền khi thiếu số dư.
        """

        wallet_test = Wallet()

        wallet_test.deposit(300000)


        with self.assertRaises(
            InsufficientBalanceError
        ):

            wallet_test.transfer(500000)



    def test_invalid_amount(self):
        """
        Kiểm tra nạp tiền âm.
        """

        wallet_test = Wallet()


        with self.assertRaises(
            InvalidAmountError
        ):

            wallet_test.deposit(-100000)



if __name__ == "__main__":

    main()