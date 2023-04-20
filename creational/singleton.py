# 单例模式
class Truck:
    _inst = None

    def start(self):
        print("Start the car")

    @classmethod
    def get_inst(cls):
        if cls._inst == None:
            cls._inst = Truck()
        return cls._inst


if __name__ == '__main__':
    Truck.get_inst().start()
    