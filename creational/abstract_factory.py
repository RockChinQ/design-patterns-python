# 抽象工厂模式
class AbstractChair:
    """椅子基类"""
    def sit(self):
        raise NotImplementedError
    

class AbstractCoffeeTable:
    """咖啡桌基类"""
    def put_on(self):
        raise NotImplementedError
    

class AbstractSofa:
    """沙发基类"""
    def sit_on(self):
        raise NotImplementedError


class VictorianChair(AbstractChair):
    def sit(self):
        print('Sit VictorianChair')


class VictorianCoffeeTable(AbstractCoffeeTable):
    def put_on(self):
        print('Put on VictorianCoffeeTable')


class VictorianSofa(AbstractSofa):
    def sit_on(self):
        print('Sit on VictorianSofa')


class ModernChair(AbstractChair):
    def sit(self):
        print('Sit ModernChair')


class ModernCoffeeTable(AbstractCoffeeTable):
    def put_on(self):
        print('Put on ModernCoffeeTable')


class ModernSofa(AbstractSofa):
    def sit_on(self):
        print('Sit on ModernSofa')


class AbstractFurnitureFactory:
    """抽象工厂基类"""
    def create_chair(self) -> AbstractChair:
        raise NotImplementedError

    def create_coffee_table(self) -> AbstractCoffeeTable:
        raise NotImplementedError

    def create_sofa(self) -> AbstractSofa:
        raise NotImplementedError


class VictorianFactory(AbstractFurnitureFactory):
    """维多利亚工厂"""
    def create_chair(self) -> AbstractChair:
        return VictorianChair()

    def create_coffee_table(self) -> AbstractCoffeeTable:
        return VictorianCoffeeTable()

    def create_sofa(self) -> AbstractSofa:
        return VictorianSofa()
    

class ModernFactory(AbstractFurnitureFactory):
    """现代工厂"""
    def create_chair(self) -> AbstractChair:
        return ModernChair()

    def create_coffee_table(self) -> AbstractCoffeeTable:
        return ModernCoffeeTable()

    def create_sofa(self) -> AbstractSofa:
        return ModernSofa()
    

if __name__ == "__main__":
    use_factory: AbstractFurnitureFactory

    use_factory = VictorianFactory()

    chair = use_factory.create_chair()
    coffee_table = use_factory.create_coffee_table()
    sofa = use_factory.create_sofa()

    chair.sit()
    coffee_table.put_on()
    sofa.sit_on()
    