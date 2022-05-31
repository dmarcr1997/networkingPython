class MyRouter(object):
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    
    def print_router(self, manuf_date):
        print("The router nameis: " + self.routername)
        print("The router model is: " + self.model)
        print("The serial number is: " + self.serialno)
        print("The IOS version is: " + self.ios)
        print("The model and date combined: ", self.model + manuf_date)

router1 = MyRouter('R1', '2600', '123456', '12.4')
router1.print_router('20150101')
print(getattr(router1, 'ios'))
setattr(router1, 'ios', '12.1')
print(hasattr(router1, 'ios'))
delattr(router1, 'ios')
print(isinstance(router1, MyRouter))

#class MyNewRouter(MyRouter) - child class
#issubclass() - to check if child class