import json

name = input("Enter product Name: ")
quantity = str(input("Enter weights : "))
type = input("Enter Type of Product: ")
productPrice = str(input("Enter Product Price Kg : "))

# Used for Writing the Data onto the JSON file
def write_json(data, filename):
    with open(filename, 'w') as inventry:
        json.dump(data, inventry, indent=4)


try:
    inventryDetail = {
        "productName": name,
        "productQuantity": quantity,
        "productType": type,
        "productPrice": productPrice
    }
    with open('inventryBook.json') as inventry:
        dataOnFile = json.load(inventry)
        temp = dataOnFile["productDetail"]
        temp.append(inventryDetail)
    write_json(dataOnFile, 'inventryBook.json')
except:
    inventryDetail = {
        "productDetail": [
            {
                "productName": name,
                "productQuantity": quantity,
                "productType": type,
                "productPrice": productPrice}
        ]}
    with open('inventryBook.json', 'w') as inventry:
        json.dump(inventryDetail, inventry, indent=4)