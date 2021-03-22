import json

import requests

CUSTOMER_ADD_URI = "/customers/new"
SALE_ADD_URI = "/sales/new"
BOOK_ADD_URI = "/books/new"

CUSTOMER_LIST_URI = "/customers"
SALE_LIST_URI = "/sales"
BOOK_LIST_URI = "/books"

BOOK_GET_URI = "/books/{book_id}"
CUSTOMER_GET_URI = "/customers/{customer_id}"
SALE_GET_URI = "/sales/{sale_id}"


SERVER_URL = "http://localhost:9090"


def insert_customers():
    customers_data = [
        {
            "first_name": "customer",
            "last_name": "user 1",
            "email": "customer2@user1.com.br",
            "phone": "555199767676",
        },
        {
            "first_name": "customer",
            "last_name": "user 2",
            "email": "customer2@user2.com.br",
            "phone": "555199177643",
        },
        {
            "first_name": "customer",
            "last_name": "user 3",
            "email": "customer3@user3.com.br",
            "phone": "555199755675",
        },
    ]
    print("\n########### CREATING CUSTOMERS ###########\n")
    for customer in customers_data:
        customer_name = " ".join([customer["first_name"], customer["last_name"]])
        print(
            f"\n########## CREATING CUSTOMER {customer_name} USING ENDPOINT {CUSTOMER_ADD_URI} ###########\n"
        )
        result = requests.post(SERVER_URL + CUSTOMER_ADD_URI, data=json.dumps(customer))
        if result.status_code == 201:
            print(f"\n Result data -> {result.json()}\n")
        else:
            print(f"\n Error while creating order -> {result.json()}\n")


def insert_books():
    books_data = [
        {
            "ISBN": 9789000307975,
            "title": "Vrienden voor het leven",
            "author": "Maeve Binchy",
            "price": 450.99,
            "year": 1990,
            "language": "english",
        },
        {
            "ISBN": 9780552159722,
            "title": "Deception point",
            "author": "Dan Brown",
            "price": 740.0,
            "year": 1865,
            "language": "portuguese",
        },
        {
            "ISBN": 9789022558027,
            "title": "Magic staff",
            "author": "Terry Brooks",
            "price": 2350.99,
            "year": 1954,
            "language": "deutsch",
        },
        {
            "ISBN": 9781841499789,
            "title": "Bloodfire Quest",
            "author": "Terry Brooks",
            "price": 3600.76,
            "year": 2004,
            "language": "spanish",
        },
        {
            "ISBN": 9781409117933,
            "title": "A Week in Winter",
            "author": "Maeve Binchy",
            "price": 10500.76,
            "year": 2010,
            "language": "japanese",
        },
        {
            "ISBN": 9789460681387,
            "title": "Blue Curacao",
            "author": "Linda van Rijn",
            "price": 48.99,
            "language": "english",
            "year": 1750,
        },
    ]
    print("\n########### CREATING BOOKS ###########\n")
    for book in books_data:
        print(
            f"\n########## CREATING BOOK {book['title']} USING ENDPOINT {BOOK_ADD_URI} ###########\n"
        )
        result = requests.post(SERVER_URL + BOOK_ADD_URI, data=json.dumps(book))
        if result.status_code == 201:
            print(f"\n Result data -> {result.json()}\n")
        else:
            print(f"\n Error while creating order -> {result.json()}\n")


def insert_orders():
    sales_data = [
        {"customer": 2, "books": [2, 3, 4]},
        {"customer": 1, "books": [1, 6]},
        {"customer": 1, "books": [4, 3]},
        {"customer": 3, "books": [1, 2]},
    ]
    print("\n########### CREATING ORDERS ###########\n")
    for sale in sales_data:
        print(
            f"\n########## CREATING ORDER USING ENDPOINT {SALE_ADD_URI} ###########\n"
        )
        result = requests.post(SERVER_URL + SALE_ADD_URI, data=json.dumps(sale))
        if result.status_code == 201:
            print(f"\n Result data -> {result.json()}\n")
        else:
            print(f"\n Error while creating order -> {result.json()}\n")


def get_customer(customer_id):
    customer_uri = CUSTOMER_GET_URI.format(customer_id=customer_id)
    print(
        f"\n###### GETTING CUSTOMER WITH ID {customer_id} using endpoint {customer_uri} ######"
    )
    result = requests.get(SERVER_URL + customer_uri)
    print(f"Result data -> {result.json()}")


def get_book(book_id):
    book_uri = BOOK_GET_URI.format(book_id=book_id)
    print(f"\n###### GETTING BOOK WITH ID {book_id} using endpoint {book_uri} ######")
    result = requests.get(SERVER_URL + book_uri)
    print(f"Result data -> {result.json()}")


def get_sale(sale_id):
    sale_uri = SALE_GET_URI.format(sale_id=sale_id)
    print(f"\n###### GETTING ORDER WITH ID {sale_id} using endpoint {sale_uri} ######")
    result = requests.get(SERVER_URL + sale_uri)
    print(f"Result data -> {result.json()}")


if __name__ == "__main__":
    insert_customers()
    insert_books()
    insert_orders()
    get_customer(2)
    get_book(4)
    get_book(5)
    get_sale(3)
