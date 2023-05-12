from abc import ABC, abstractmethod


class IoTDevice(ABC):
    @abstractmethod
    def open(self) -> bool:
        raise NotImplementedError()


def process_iot_device(device: IoTDevice):
    device.open()


class SensorTypeA:
    pass


class SensorTypeB:  # structural subtyping / duck typing
    def open(self) -> bool:
        print('doing something')
        return True


class SensorTypeC(IoTDevice):  # nominal subtyping
    def open(self) -> bool:
        print('doing something')
        return True


iot_device = IoTDevice()
process_iot_device(iot_device)

sensor_a = SensorTypeA()
process_iot_device(sensor_a)  # type checker error

sensor_b = SensorTypeB()
process_iot_device(sensor_b)  # type checker error 

sensor_c = SensorTypeC()
process_iot_device(sensor_c)

