from typing import Protocol

#
# https://peps.python.org/pep-0544/ 
#

class IoTDevice(Protocol):
    def open(self) -> bool:
        ...


def process_iot_device(device: IoTDevice):
    device.open()


class SensorTypeA:
    pass


class SensorTypeB:
    def open(self) -> bool:
        print('doing something')
        return True


# https://peps.python.org/pep-0544/#explicitly-declaring-implementation
class SensorTypeC(IoTDevice):
    def open(self) -> bool:
        print('doing something')
        return True


iot_device = IoTDevice()
process_iot_device(iot_device)

sensor_a = SensorTypeA()
process_iot_device(sensor_a)

sensor_b = SensorTypeB()
process_iot_device(sensor_b)

sensor_c = SensorTypeC()
process_iot_device(sensor_c)


