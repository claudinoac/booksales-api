# BookSaleAPI

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A web book ordering system based on Tornado framework and SQLAlchemy ORM.


## Table of Contents:


- [Installation](#installation)
- [Setup](#setuo)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

---

## Installation:

### Requisites:
- Install [docker](https://www.docker.com/products/docker-desktop) and [docker-compose](https://docs.docker.com/compose/install/)


### Clone:

- Clone this repository:
	- ` git clone git@github.com:claudinoac/booksale-api`

### Setup:

- Run `make init`
- Wait until the command ends.
- The containers should be all up and running
- If you want to have the database populated, just use the command `make populate` right after `make init`
- Access the host [http://localhost:9090](http://localhost:9090') appending one of the available endpoints

---
### Available Endpoints


| Endpoint                    | Available Methods | Description                                   |
| --------------------------- | ----------------- | --------------------------------------------- |
| /books                      | GET               | Will return a list of all books               |
| /books/< book_id >          | GET               | Will return info about the book if exists     |
| /books/new                  |  POST             | Will create a new book                        |  
| /customers                  | GET               | Will return a list of all customers           |
| /customers/ < customer_id > | GET               | Will return info about the customer if exists |
| /customers/new              | POST              | Will create a new book                        |
| /sales                      | GET               | Will return a list of all orders              |
| /sale/< sale_id >           | GET               | Will return info about the sale if exists     |
| /sale/new                   | POST              | Will create a new order                       |


## Fixtures

The database starts empty. The data needs to be populated from some script.
For that, we have the script in `./fixtures/create_entities.py`.
The script is called from the command `make populate` if you execute it. 
This 


## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/claudinoac/booksale-apigit`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/claudinoac/booksale-api/compare/" target="_blank">`https://github.com/claudinoac/booksale-api/compare/`</a>.

---

## Team

### Maintainers:
| <a href="http://github.com/claudinoac" target="_blank">**Alisson Claudino**</a>|
| :---: |
| [![Alisson Claudino](https://avatars3.githubusercontent.com/u/23270841?s=200&v=4)](http://fvcproductions.com)  |
| <a href="http://github.com/claudinoac" target="_blank">`github.com/claudinoac`</a> |

### Contributors:
---

## FAQ

- **How can I can do ...?**
    - Response will be here

---

## Support

Reach out to me at one of the following places!

- Twitter at <a href="http://twitter.com/_claudinoac" target="_blank">`@_claudinoac`</a>

---

## License

- **[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)**

