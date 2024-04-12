from abc import  ABC, abstractmethod
from typing import List

from CustomerDto import CustomerDto

class ICustomerService(ABC):
    def getCustomers(self)-> List:
        pass

    def AddCustomer(NewCustomer: CustomerDto):
        pass