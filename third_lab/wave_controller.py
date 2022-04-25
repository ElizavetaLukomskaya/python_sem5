import pygame
from wave import Wave

class WaveController:
    def __init__(self, screen, maxX, maxY, *groups):
        self.wave_number = 0
        self.screen = screen
        self.groups = groups
        self.amount = 10
        self.maxX = maxX
        self.maxY = maxY

    def new_wave(self, target):
        self.wave_number += 1
        wave = Wave(self.get_types(), self.screen, self.amount, self.maxX, self.maxY, self.groups)
        wave.start_wave(target)
        self.amount += 1

    def get_types(self):
        types = [ ]
        if self.wave_number >= 1:
            types.append("walker")
            types.append("crawler")
        if self.wave_number > 5:
            types.append("brute")
        if self.wave_number > 10:
            types.append("spider")
        if self.wave_number > 15:
            types.append("runner")
        if self.wave_number > 20:
            types.append("motorcycle")
        if self.wave_number > 25:
            types.append("helicopter")
        return types
