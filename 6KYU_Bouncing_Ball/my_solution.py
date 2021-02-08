def bouncing_ball(h, bounce, window):
    if h != 0 and bounce > 0 and bounce < 1 and window < h:
        num_times = 1
        h *= bounce
        while h > window: 
            h *= bounce
            num_times += 2
        return num_times
    
    else: return -1 
