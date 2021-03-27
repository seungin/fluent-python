invoice = """
0.....6.................................40.......50...55........
1909  Pimoroni PiBrella                    $17.50    3    $52.50
1489  6mm Tactile Switch x20                $4.95    2     $9.90
1510  Panavise Jr. - PV-201                $28.00    1    $28.80
1601  PiTFT Mini Kit 320x240               $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 50)
QUANTITY = slice(50, 55)
ITEM_TOTAL = slice(55, None)


def test_invoice():
    # slice object
    items = invoice.split("\n")[2:]
    second_item = items[1]
    assert second_item[SKU].strip() == "1489"
    assert second_item[DESCRIPTION].strip() == "6mm Tactile Switch x20"
    assert second_item[UNIT_PRICE].strip() == "$4.95"
    assert second_item[QUANTITY].strip() == "2"
    assert second_item[ITEM_TOTAL].strip() == "$9.90"
