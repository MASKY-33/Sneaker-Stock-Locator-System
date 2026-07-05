# Package...Modules learning


sneaker_stock = {
    "airmax" : "Stelling A1",
    "jordan1" : "Stelling B3",
    "jeezy" : "Stelling C2"
}

def locate_sneaker(model_name):

    try:
        if model_name in sneaker_stock:
            
            sneaker_stock[model_name]
            return f"{model_name} located in {sneaker_stock[model_name]}"
        else:
            return "Model not in stock."

    except IOError:
        return "Error occured! Please follow the steps asked to find your sneaker-model."
