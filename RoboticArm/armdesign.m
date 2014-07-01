% Use for simulating the 4DOF robotic arm with parameter values according to D-H convertion.
% Works only if RVC toolbox is installed



startup_rvc


%offset and Link lenght remains same from construction point of view

clc 
clear
l(1)=Link([0,1,0,-90,0])  %offset should be made zero while constructing 
l(2)=Link([90,0,2,0,0])
l(3)=Link([45,0,2,0,0])
l(4)=Link([45,0,2,-90,0])

Robo=SerialLink(l)
Robo.plot([1,1,1,1])
qe=[0,30,40,40]
Tf=fkine(Robo,qe)

m=[1,1,1,0,0,1]
in=[0,0,0,0]
We=ikine(Robo,Tf,in,m)

me=fkine(Robo,We)
Tf*[0;0;0;1]
me*[0;0;0;1]
