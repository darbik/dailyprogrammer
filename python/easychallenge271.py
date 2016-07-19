# Daily Programmer Easy Challenge 271 https://www.reddit.com/r/dailyprogrammer/comments/4nvrnx/20160613_challenge_271_easy_critical_hit/

d = float(raw_input("The number of sides on your die: "))
h = float(raw_input("The amount of health left on your enemy: "))
crit_chance = 1 / d
output = 0

if h > d and h != d + 1:

    exponent = (h - 1) // d     # d = 100, h = 200 is off by 0.01, not sure why :/
    y = d * exponent
    x = (crit_chance) ** (exponent + 1) 
    output = x * (h - (y - 1))
    
    print "%.9f" % output

elif h == d + 1 or h == d:

    output = crit_chance

    print crit_chance

elif h != 1 and h < d:

    output = h / d
    
    print "%.4f" % output 

else:

    print 1
