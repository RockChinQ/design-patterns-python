# 桥接模式
class AbstractDevice:
    """设备基类"""
    enabled = False
    volume = 0
    channel = 0

    def isEnabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def getVolume(self):
        return self.volume

    def setVolume(self, percent):
        self.volume = percent
    
    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        self.channel = channel


class Radio(AbstractDevice):
    """收音机"""
    pass


class Television(AbstractDevice):
    """电视机"""
    pass


class Remote:
    """遥控器"""
    device: AbstractDevice

    def __init__(self, device: AbstractDevice):
        self.device = device

    def togglePower(self):
        self.device.enable() if not self.device.isEnabled() else self.device.disable()

    def volumeDown(self):
        self.device.setVolume(self.device.getVolume() - 10)

    def volumeUp(self):
        self.device.setVolume(self.device.getVolume() + 10)

    def channelDown(self):
        self.device.setChannel(self.device.getChannel() - 1)

    def channelUp(self):
        self.device.setChannel(self.device.getChannel() + 1)


class AdvancedRemote(Remote):
    """高级遥控器"""
    def mute(self):
        self.device.setVolume(0)


if __name__ == "__main__":
    radio = Radio()
    remote = Remote(radio)
    remote.togglePower()
    remote.channelUp()
    print(radio.isEnabled())
    print(radio.getChannel())

    tv = Television()
    remote = AdvancedRemote(tv)
    remote.togglePower()
    remote.mute()
    print(tv.isEnabled())
    print(tv.getVolume())
