from typing import Type
from .base import Report

REPORTS: dict[str, Type[Report]] = {}

def register_report(name: str):
    def decorator(cls):
        if name in REPORTS:
            raise ValueError(f"Отчет с именем {name} уже зарегистрирован")
        
        REPORTS[name] = cls
        return cls
    
    return decorator

def get_report(name: str) -> Report:
    try:
        return REPORTS[name]()
    except KeyError:
        raise ValueError(f"Неизвестный отчет: {name}")
    