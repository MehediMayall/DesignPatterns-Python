
from CustomerDto import CustomerDto
from CustomerService import CustomerService


newCustomer = CustomerDto(
    Id = 1,
    FirstName= "Mehedi",
    LastName= "Hasan",
    Address= "Some address",
    PostalCode= 1225,
    State= "Dhaka"
)

customerService = CustomerService()
customerService.AddCustomer(newCustomer)

for customer in customerService.getCustomers():
    print(f"Id: {customer.Id}, Name: {customer.CustomerName}, Address: {customer.Address}")
