# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:36:41 2022

@author: Mahmoud Saeed
"""

import TV , Light , TurnOnLight , TurnOnTv , TurnOffTv , TurnOffLight , RemoteControl

light = Light.Light()
tv  = TV.TV()
remoteControl = RemoteControl.RemoteControl()
turn_on_light = TurnOnLight.TurnOnLight(light)
turn_off_light = TurnOffLight.TurnOffLight(light)
turn_on_tv = TurnOnTv.TurnOnTv(tv)
turn_off_tv = TurnOffTv.TurnOffTv(tv)

remoteControl.addCommand(0,turn_on_light ,turn_off_light)
remoteControl.addCommand(1,turn_on_tv ,turn_off_tv)

remoteControl.onButtonPressed(0);
remoteControl.onButtonPressed(1);
remoteControl.offButtonPressed(0);
remoteControl.offButtonPressed(1);


