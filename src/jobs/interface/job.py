from abc import ABC, abstractmethod
from typing import Optional, Type
from apscheduler.triggers.base import BaseTrigger

class Job(ABC):
    @abstractmethod
    def __init__(
        self, 
        description: str, 
        trigger: Type[BaseTrigger],
        active: bool = True,
        misfire_grace_time: Optional[int] = None
    ):
        self._description = description
        self._trigger = trigger
        self._active = active
        self._misfire_grace_time = misfire_grace_time

    @property
    def description(self):
        return self._description

    @property
    def trigger(self):
        return self._trigger

    @property
    def misfire_grace_time(self):
        return self._misfire_grace_time

    @property
    def active(self):
        return self._active

    @abstractmethod
    def action(self):
        raise NotImplementedError