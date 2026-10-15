from decimal import Decimal, ROUND_HALF_UP

STORE_NAME = "The Shop Around the Corner"
TAX_RATE = Decimal("0.075")  # 7.5% sales tax
WIDTH = 30
NAME_WIDTH = 10
CENT = Decimal("0.01")

# Decimal is built from strings so money values are stored exactly (float can't hold 4.99 exactly).
ITEMS = [
    ("Notebook", Decimal("4.99"), 2),
    ("Pen Pack", Decimal("7.50"), 1),
    ("Backpack", Decimal("34.99"), 1),
]


def money(amount):
    """Format as $X.XX with the $ attached, so the whole string can be right-aligned."""
    return f"${amount:.2f}"


def to_cents(amount):
    """Round a Decimal to the nearest cent, rounding halves up like a cash register."""
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def validate(items):
    for name, price, qty in items:
        if price < 0:
            raise ValueError(f"{name}: price cannot be negative ({price})")
        if qty <= 0:
            raise ValueError(f"{name}: quantity must be at least 1 ({qty})")


def print_receipt(items):
    border = "=" * WIDTH  # This is where I used the str multiplication trick. (C# equivalent: new string('=', 30))
    divider = "-" * WIDTH

    print(border)
    print(STORE_NAME.center(WIDTH))
    print(border)

    if not items:
        print("No items".center(WIDTH))
        return

    for name, price, qty in items:
        line_total = price * qty
        # Format specs handle alignment: < left-aligns, > right-aligns, the number is the column width.
        # Names longer than NAME_WIDTH are truncated so they can't push the columns out of line.
        print(f"{name[:NAME_WIDTH]:<{NAME_WIDTH}} {money(price):>7} x{qty:>2} {money(line_total):>7}")

    subtotal = sum(price * qty for _, price, qty in items)
    tax = to_cents(subtotal * TAX_RATE)  # Tax is rounded once, so subtotal + tax always equals the printed total.
    total = subtotal + tax

    print(divider)
    print(f"{'Subtotal:':<20}{money(subtotal):>10}")
    print(f"{f'Tax ({TAX_RATE:.1%}):':<20}{money(tax):>10}")
    print(divider)
    print(f"{'Total:':<20}{money(total):>10}")


def main():
    validate(ITEMS)
    print_receipt(ITEMS)


if __name__ == "__main__":
    main()
