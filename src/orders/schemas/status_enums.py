from enum import StrEnum




class OrderStatusEnum(StrEnum):
    PENDING = "PENDING"
    CANCELED = "CANCELED"
    IN_PROCESS = "IN_PROCESS"
    READY = "READY"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVRED = "DELIVRED"


class ItemStatusEnum(StrEnum):
    PENDING = "PENDING"
    IN_PROCESS = "IN_PROCESS"
    READY = "READY"
    CANCLED = "CANCELED"