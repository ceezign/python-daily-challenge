# Change maker program
## currency in naira

def make_change_naira(purchase_price, payment_amount):

    purchase_kobo = round(purchase_price * 100)
    payment_kobo = round(payment_amount * 100)

    if payment_kobo < purchase_kobo:
        return "Insufficient payments"

    change = payment_kobo - purchase_kobo

    if change == 0:
        return "Exact Payment received , No change "

    denomination = {
        "₦1000 note": 100000,
        "₦500 note" : 50000,
        "₦200 note": 20000,
        "₦100 note": 10000,
        "₦50 note": 5000,
        "₦20 note": 2000,
        "₦10 note": 1000,
        "₦5 note": 500,
        "₦2 note": 200,
        "₦1 note": 100,
        "₦50 kobo": 50,
        "₦25 kobo": 25,
        "10 kobo": 10,
        "5 kobo": 5,
        "1 kobo": 1,
    }

    change_breakdown = {}

    for name, value in denomination.items():
        count = change // value
        if count > 0 :
            change_breakdown[name] = count
            count -= change * value

    #  display result
    result = f"Change owed: ₦{(payment_amount - purchase_price):,.2f}\nBreakdown:"
    for name, count in change_breakdown.items():
        result += f"\n- {count} x {name}"
    return result

print(make_change(1375.50, 2000))



