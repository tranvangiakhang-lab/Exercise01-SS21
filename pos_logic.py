import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


DRINK_MENU = {
    "P1": {
        "name": "Phin Sữa Đá",
        "price": 35000
    },
    "F1": {
        "name": "Freeze Trà Xanh",
        "price": 55000
    },
    "T1": {
        "name": "Trà Sen Vàng",
        "price": 45000
    }
}


class ItemNotFoundError(Exception):
    """Exception khi mã đồ uống không tồn tại."""
    pass


class InvalidQuantityError(Exception):
    """Exception khi số lượng nhập <= 0."""
    pass


def view_menu():
    """
    Hiển thị danh sách đồ uống.
    """
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - {item['name']} - "
            f"{item['price']:,} VNĐ"
        )


def add_to_order(order, drink_code, quantity):
    """
    Thêm món uống vào giỏ hàng.

    Args:
        order: danh sách giỏ hàng.
        drink_code: mã đồ uống.
        quantity: số lượng.

    Raises:
        ItemNotFoundError:
            Khi mã đồ uống không tồn tại.
        InvalidQuantityError:
            Khi số lượng <= 0.
    """

    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)

    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    item = {
        "code": drink_code,
        "name": DRINK_MENU[drink_code]["name"],
        "price": DRINK_MENU[drink_code]["price"],
        "quantity": quantity
    }

    order.append(item)

    logging.info(
        f"Added {quantity} of {drink_code} to order"
    )


def calculate_total(order):
    """
    Tính tổng tiền trong giỏ hàng.

    Args:
        order: danh sách món đã đặt.

    Returns:
        Tổng tiền.
    """

    total = 0

    for item in order:
        total += item["price"] * item["quantity"]

    return total


def view_order(order):
    """
    Hiển thị giỏ hàng hiện tại.
    """

    if not order:
        print(
            "Giỏ hàng trống, vui lòng chọn món (Chức năng 2)."
        )
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")

    print(
        "Mã SP | Tên đồ uống | Đơn giá | "
        "Số lượng | Thành tiền"
    )

    print("-" * 70)

    for item in order:
        amount = item["price"] * item["quantity"]

        print(
            f"{item['code']} | "
            f"{item['name']} | "
            f"{item['price']:,} | "
            f"{item['quantity']} | "
            f"{amount:,} VNĐ"
        )

    print("-" * 70)

    print(
        f"Tổng tiền cần thanh toán: "
        f"{calculate_total(order):,} VNĐ"
    )


def checkout(order):
    """
    Thanh toán đơn hàng.

    Returns:
        True nếu thanh toán thành công.
    """

    if not order:
        print(
            "Giỏ hàng trống, vui lòng chọn món (Chức năng 2)."
        )
        return False

    total = calculate_total(order)

    print(
        f"Tổng tiền cần thanh toán: {total:,} VNĐ"
    )

    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    )

    if confirm.lower() == "y":
        logging.info("Checkout successful")

        order.clear()

        print("Thanh toán thành công.")
        print("Giỏ hàng đã được làm trống.")

        return True

    elif confirm.lower() == "n":
        print(
            "Đã hủy thao tác thanh toán. "
            "Quay lại menu chính."
        )

    else:
        print(
            "Lựa chọn không hợp lệ. "
            "Thanh toán đã bị hủy."
        )

    return False