# 工厂方法模式

class Transport(object):
    """运输工具的基类"""

    def deliver(self):
        raise NotImplementedError
    

class Truck(Transport):
    """卡车"""
    def deliver(self):
        print('卡车运输货物')


class Ship(Transport):
    """轮船"""
    def deliver(self):
        print('轮船运输货物')


class TransportCreator(object):
    """创建者基类"""
    def createTransport(self) -> Transport:
        raise NotImplementedError
    

class TruckCreator(TransportCreator):
    """卡车创造者"""
    def createTransport(self) -> Transport:
        return Truck()
    

class ShipCreator(TransportCreator):
    """轮船创造者"""
    def createTransport(self) -> Transport:
        return Ship()
    

if __name__ == "__main__":
    use_transport: TransportCreator

    use_transport = TruckCreator()

    trans = use_transport.createTransport()

    trans.deliver()