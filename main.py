import logging

from pos_logic import (
    view_menu,
    add_to_order,
    view_order,
    checkout,
    ItemNotFoundError,
    InvalidQuantityError
)


current_order = []


def show_menu():
    """
    Hiển thị menu CLI.
    """

    print(
        """
========== HIGHLANDS MINI POS ==========
1. Xem thực đơn
2. Thêm món vào giỏ
3. Xem giỏ hàng & Tính tổng tiền
4. Thanh toán & Xóa giỏ hàng
5. Thoát ca làm việc
========================================
"""
    )


def handle_add_order():
    """
    Xử lý chức năng thêm món.
    """

    print("\n--- THÊM MÓN VÀO GIỎ ---")

    drink_code = input(
        "Nhập mã đồ uống: "
    )

    try:
        quantity = int(
            input("Nhập số lượng: ")
        )

        add_to_order(
            current_order,
            drink_code,
            quantity
        )

        print(
            f"Đã thêm {quantity} x "
            f"{current_order[-1]['name']} "
            "vào giỏ hàng."
        )

    except ValueError:

        print(
            "Vui lòng nhập số lượng là một số nguyên!"
        )

        logging.error(
            "ValueError - Invalid quantity input"
        )

    except ItemNotFoundError as error:

        print(
            "Mã đồ uống không hợp lệ, "
            "vui lòng kiểm tra lại thực đơn!"
        )

        logging.warning(
            f"ItemNotFoundError - Code: {error}"
        )

    except InvalidQuantityError as error:

        print(
            "Số lượng phải lớn hơn 0!"
        )

        logging.warning(
            f"InvalidQuantityError - Quantity: {error}"
        )


def main():
    """
    Hàm chạy chương trình chính.
    """

    while True:

        show_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        if choice == "1":

            view_menu()

        elif choice == "2":

            handle_add_order()

        elif choice == "3":

            view_order(current_order)

        elif choice == "4":

            checkout(current_order)

        elif choice == "5":

            logging.info(
                "Cashier logged out. System shutdown."
            )

            print(
                "Đã thoát ca làm việc. Hẹn gặp lại!"
            )

            break

        else:

            print(
                "Lựa chọn không hợp lệ!"
            )


if __name__ == "__main__":
    main()