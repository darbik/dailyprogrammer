# Daily Programmer Easy Challenge 272 https://www.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/

vals = {
        'A': {'count' : 9}, 'B': {'count': 2}, 'C': {'count': 2}, 'D': {'count': 4}, 
        'E': {'count': 12}, 'F': {'count': 2}, 'G': {'count': 3}, 'H': {'count': 2},
        'I': {'count': 9}, 'J': {'count': 1}, 'K': {'count': 1}, 'L': {'count': 4},
        'M': {'count': 2}, 'N': {'count': 6}, 'O': {'count': 8}, 'P': {'count': 2},
        'Q': {'count': 1}, 'R': {'count': 6}, 'S': {'count': 4}, 'T': {'count': 6},
        'U': {'count': 4}, 'V': {'count': 2}, 'W': {'count': 2}, 'X': {'count': 1},
        'Y': {'count': 2}, 'Z': {'count': 1}, '_': {'count': 2}
}

tiles = 'AEERTYOXMCNB_S'

for x in list(tiles):

    vals[x]['count'] -= 1
        
    if vals[x]['count'] < 0:

        print "Invalid input. More %s's have been taken from the bag than possible." % x        
        sys.exit()

tiles_sorted = sorted(vals.items(), key=lambda (k, v): v, reverse=True)
i = tiles_sorted[0][1].get('count')
multiples = False    # to control the flow for when there are multiple characters with the same count 

for y, x in tiles_sorted:
        
    if multiples is False and vals[y]['count'] == i:

        print "\n%2i :" % i,

    if vals[y]['count'] == i:       # keys are being missed here i think
        
        print y,
        multiples = True

    else:
         
        i -=1
        multiples = False 
