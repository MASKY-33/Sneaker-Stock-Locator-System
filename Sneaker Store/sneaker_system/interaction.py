from warehouse_management.logic import locate_sneaker

while True:
    model_name = input("Type here the sneaker-model you're searching for, (or type 'stop' to stop): ").lower()

    if model_name == "stop":
        print("Thankyou, Bye!")
        break

    locate_sneaker_result = locate_sneaker(model_name)
    print(locate_sneaker_result)