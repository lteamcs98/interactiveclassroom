from ball import Ball  # import the Ball class

# Create a Ball object and store its address in the variable myball.
myball = Ball(5.0, 4.0, 3.0, 6.0)

print "Ball location " + str(myball.x) + ", " + str(myball.y)

# move the ball at current velocity for 0.1 seconds
myball.update_position(0.1) 

print "Ball location " + str(myball.x) + ", " + str(myball.y)
