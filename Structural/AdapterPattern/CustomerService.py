from typing import List
from Customer import Customer
from CustomerDto import CustomerDto
from ICustomerService import ICustomerService


class CustomerService(ICustomerService):
    def __init__(self):
        self.customers = []

    def getCustomers(self) -> List:
        return self.customers
    
    def AddCustomer(self, customer: CustomerDto):
        newCustomer = Customer(
            Id = customer.Id,
            CustomerName= customer.FirstName + " " + customer.LastName,
            Address= customer.Address,
            Zip = customer.PostalCode,
            State= customer.State
        )
        self.customers.append(newCustomer)
