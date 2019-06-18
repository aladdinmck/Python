import os
def turn(speed, duration):
    cmd = '~/run ' + str(speed) + ' ' + str(duration) + ' 0 0 0 0 0 0'
    os.system(cmd)

def move_vertical(speed, distance=0):
    cmd = '~/run 0 0' + str(speed) + ' ' + str(distance) + ' 0 0 0 0'
    os.system(cmd)
    return 
  
def move_lateral(speed, distance=0):
    cmd = '~/run 0 0 0 0 ' + str(speed) + ' ' + str(distance) + ' 0 0'
    os.system(cmd)
    return
  
def move_chain(speed, distance=0):
    cmd = '~/run 0 0 0 0 0 0 '  + str(speed) + ' ' + str(distance) + ''
    os.system(cmd)
    return
  
def custom_move(vert_speed=0, vert_distance=0, lat_speed=0, lat_distance=0, chain_speed=0, chain_distance=0):
    cmd = '~/run 0 0 ' + str(vert_speed) + ' ' + str(chain_speed) + ' ' + str(chain_distance)
    os.system(cmd)
