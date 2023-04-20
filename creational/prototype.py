# 原型模式
class Prototype:
    """原型基类"""
    def clone(self):
        raise NotImplementedError
    

class Car(Prototype):
    """汽车原型基类"""
    weight: int = 1000
    height: float = 2

    def clone(self):
        new_car = Car()
        new_car.weight = self.weight
        new_car.height = self.height
        return new_car
    

if __name__ == "__main__":
    car0 = Car()
    car0.weight = 2000
    car0.height = 2.3

    car1 = car0.clone()

    print("car0: w:{} h:{}".format(car0.weight, car0.height))
    print("car1: w:{} h:{}".format(car1.weight, car1.height))