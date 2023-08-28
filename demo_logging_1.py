import Logger_Demo
import logging
logging.basicConfig(level=logging.DEBUG,filename="demologs.log",filemode="w",format='%(asctime)s - %(levelname)s : %(message)s')
class Demo_Logging_1:

    def add_numbers(self,a,b):
        return a + b

    def multiply_numbers(self,a,b):
        return a * b
dl = Demo_Logging_1()
sum = dl.add_numbers(5,2)
multiply_result = dl.multiply_numbers(5,2)


logging.warning("The addition of two numbers is: {}".format(sum))
logging.warning("The multiplication two numbers is: {}".format(multiply_result))