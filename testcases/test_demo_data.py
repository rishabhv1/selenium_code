from ddt import ddt, data , unpack
import softest

@ddt
class Test_Demo_Data(softest.TestCase):

    @data(("abc","def"),("xyz","lmn"))
    @unpack
    def test_data(self,fname,lname):
        print(fname)
        print(lname)