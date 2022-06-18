from abc import ABC, abstractmethod
from typing import Optional

class Job(ABC):
    @abstractmethod
    def __init__(
        self, 
        name: str, 
        trigger: str, 
        seconds: Optional[int] = None, 
        hours: Optional[int] = None, 
        misfire_grace_time: Optional[int] = None
    ):
        self._name = name
        self._trigger = trigger
        self._seconds = seconds
        self._hours = hours
        self._misfire_grace_time = misfire_grace_time

    @property
    def name(self):
        return self._name

    @property
    def trigger(self):
        return self._trigger

    @property
    def seconds(self):
        return self._seconds

    @property
    def hours(self):
        return self._hours

    @property
    def misfire_grace_time(self):
        return self._misfire_grace_time

    @abstractmethod
    def action(self):
        raise NotImplementedError