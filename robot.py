#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive
import ctre
from networktables import NetworkTables


class Maserbot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        NetworkTables.initialize()
        self.instructions = NetworkTables.getTable("RosTwist")
        self.timer = wpilib.Timer()
        
        self.controller = wpilib.XboxController(0)

        frontLeft =  ctre.WPI_VictorSPX(1)
        rearLeft =  ctre.WPI_VictorSPX(2)
        left = wpilib.SpeedControllerGroup(frontLeft, rearLeft)

        frontRight =  ctre.WPI_VictorSPX(3)
        rearRight =  ctre.WPI_VictorSPX(4)
        right = wpilib.SpeedControllerGroup(frontRight, rearRight)

        self.drive = wpilib.drive.DifferentialDrive(left, right)

    def autonomousInit(self):
       """This function is run once each time the robot enters autonomous mode."""
       self.timer.reset()
       self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        x = float(self.instructions.getRaw("x", 0))
        y = float(self.instructions.getRaw("y", 0))
        print("Moving to: ", x, y)
        self.drive.arcadeDrive(y,x)

        # if self.timer.get() < 2.0:
        #    self.drive.arcadeDrive(-0.5, 0)
        # else:
        #    self.drive.arcadeDrive(0,0)


    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        # self.drive.arcadeDrive(0, 0)
        x = self.controller.getRawAxis(0) * -1
        y = self.controller.getRawAxis(1)
        print(x, )
        self.drive.arcadeDrive(y,x)

if __name__ == "__main__":
    wpilib.run(Maserbot)