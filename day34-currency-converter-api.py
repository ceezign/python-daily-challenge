import requests

API_URL = "https://open.er-api.com/v6/latest/"

def get_exchange_rate(base_currency):
    try:
        response = requests.get(API_URL + base_currency)
        data = response.json()
        if data["result"] == "success":
            return data["rates"]
        else:
            print("Error get data rate", data.get("error-type"))
            return None

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    try:
        if to_currency.upper() not in rates:
            print(f"{to_currency} not available in rates list")
            return None

        converted_amount = amount * rates[to_currency.upper()]
        return converted_amount
    except Exception as e:
        print("Conversion Error:", e)
        return None

def main():
    print("Real-Time Currency Converter")
    from_currency  = input("enter te base currency (e.g. USD, EUR, GBP): ").upper()
    to_currency = input("Enter the target currency: ").upper()
    amount = float(input("enter the amount to convert: "))

    print("\nFetching real-time exchange rate...")
    rates = get_exchange_rate(from_currency)

    if rates:
        converted = convert_currency(amount, from_currency, to_currency, rates)
        if converted is not None:
            print(f"\n {amount:.2f} {from_currency}  = {converted:.2f} {to_currency}")
        else:
            print("Conversion Failed")
    else:
        print("Unable to retrieve exchange rates. ")

if __name__ == "__main__":
    main()