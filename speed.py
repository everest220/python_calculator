def speed_conversion_meter_per_second(speed_kilometer_per_hour: float):
    speed_meter_per_hour = speed_kilometer_per_hour * 1000
    speed_meter_per_second = speed_meter_per_hour / 3600
    return speed_meter_per_second


def speed_conversion_kilometer_per_hour(speed_meter_per_second: float):
    speed_meter_per_hour = speed_meter_per_second * 3600
    speed_kilometer_per_hour = speed_meter_per_hour / 1000
    return speed_kilometer_per_hour
