# Inverted pendulum

Python code to control behaviour of an inverted pendulum system. An example of the system can be viewed by clicking the inverted_pendulum GIF file.

The inverted_pendulum.py program is used to maintain a pendulum in an upright position between -5<sup>o</sup> and 5<sup>o</sup> using a PID controller, with a unit impulse applied at t = 0.<br>
Upon running the program, a graph shows trajectory of the angle of pendulum.<br>

The forced_response.py program plots a graph of the trajectory of the system (without a PID controller) upon a force sin(100t<sup>2</sup>) being applied at rest, with the θ(t) and x(t) trajectories being plotted on a graph.<br>
Code can be edited to show either trajectory (or both) by commenting out unwanted lines.<br>

θ(t) = angle of rod
x(t) = horizontal position of cart
