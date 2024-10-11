#!/usr/bin/env python3
# Author: lnotspotl
# Modified for ros2 by: abutalipovvv
import numpy as np

class StandController:
    def __init__(self, default_stance):
        self.def_stance = default_stance
        self.max_reach = 0.065

        self.FR_X = 0.
        self.FR_Y = 0.
        self.FL_X = 0.
        self.FL_Y = 0.

    def updateStateCommand(self, msg, state, command):
        # Обновляем позицию тела на основе сообщений
        state.body_local_position[0] = msg.axes[2] * 0.18
        self.FR_X = msg.axes[1]
        self.FR_Y = msg.axes[0]
        self.FL_X = msg.axes[4]
        self.FL_Y = msg.axes[3]

    @property
    def default_stance(self):
        # Возвращаем копию дефолтного положения ног
        return np.copy(self.def_stance)

    def run(self, state, command):
        # Копируем текущее состояние
        temp = self.default_stance
        temp[2] = [command.robot_height] * 4

        # Обновляем положения ног на основе команд джойстика
        temp[1][0] += self.FR_Y * self.max_reach
        temp[0][0] += self.FR_X * self.max_reach

        temp[1][1] += self.FL_Y * self.max_reach
        temp[0][1] += self.FL_X * self.max_reach
            
        state.foot_locations = temp
        return state.foot_locations
