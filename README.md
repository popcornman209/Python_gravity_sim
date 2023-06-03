# Python Gravity Sim
I simple gravity simulator I made from scratch in python.

if you want to use it just do ```import gravity```
to create a body just do ```body = gravity.object(mass, startingPos, startingVelocity, size)```
then to calculate how much the body will move just do ```body.calculate(body2)``` (body2 being the other body in the simulation)
then to move the body (after all bodies have been calculated) do ```body.move(offset)``` offset is the camera offset, incase you want to be able to look around.

save.py and save_loader.py are files for saving what happended, incase something cool happened you can load the save.
collision.py is using the gravity library to do gravity simulations, but it has collisions
test.py is also using the gravity library but the objects cannot interact
