# 生成器模式
class AbstractHouse:
    pass


class AbstractBuilder:
    """生成器基类"""
    house: AbstractHouse

    def build_walls(self):
        raise NotImplementedError

    def build_doors(self):
        raise NotImplementedError
    
    def build_windows(self):
        raise NotImplementedError
    
    def get_result(self) -> AbstractHouse:
        return self.house
    

class Castle(AbstractHouse):
    """城堡产品"""
    pass


class Church(AbstractHouse):
    """教堂产品"""
    pass


class CastleBuilder(AbstractBuilder):
    """城堡生成器"""
    def __init__(self):
        self.house = Castle()

    def build_walls(self):
        print("Build walls for castle")

    def build_doors(self):
        print("Build doors for castle")

    def build_windows(self):
        print("Build windows for castle")


class ChurchBuilder(AbstractBuilder):
    """教堂生成器"""
    def __init__(self):
        self.house = Church()

    def build_walls(self):
        print("Build walls for church")

    def build_doors(self):
        print("Build doors for church")

    def build_windows(self):
        print("Build windows for church")


if __name__ == '__main__':
    house: AbstractHouse

    use_builder: AbstractBuilder = CastleBuilder()

    use_builder.build_walls()
    use_builder.build_doors()
    use_builder.build_windows()

    house = use_builder.get_result()
