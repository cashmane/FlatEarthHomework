import numpy as np

def grav_accel(p1, p2, m):
    """ p1 = point where the mass element is
        p2 = point you are interested in
        m  = mass
        returns a vector of the gravitational accleration"""
    G = 6.6743e-11
    #FILL THE NEXT THREE LINES IN WITH CORRECT CODE
    #m = 0
    dist = p2-p1
    r = np.linalg.norm(dist)
    rhat = (p2-p1)/r
    
    
    return -1*G*m/r**2*rhat

def point_in_sphere(x,y,z, radius=None):
    #FILL THIS IN WITH A VALID MASK CONDITION
    #THAT RETURNS TRUE WHEN X,Y,Z IN THE SPHERE
    if x**2+y**2+z**2 < radius**2:
        return True
    else:
        return False

if __name__ == "__main__":
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    r_earth = 6378*km #radius of globe Earth
    h = 200.0*km #relatively coarse step size
    #set grid size same in x,y,z
    dx, dy, dz = h, h, h
    #x, y, z define boundaries of grid, here 7000 km
    x = np.arange(-7000*km, 7000*km, dx)
    len_x = x.shape[0]
    y = x.copy()
    z = y.copy()
    #define points on the north pole, south pole, and equator
    point_northpole = np.array([0, 0, 6378*km])
    point_equator   = np.array([6378*km, 0, 0]) #<--FIX
    point_southpole = np.array([0, 0, -6378*km]) #<--FIX
    ##Sample North Pole calc
    ##You might consider making this a function
    grav_vec_northpole = 0
    grav_vec_equator = 0
    grav_vec_southpole = 0
    for idx, xx in enumerate(x):
        #this is a trick to tell how long it will take
        print(idx, " of ", len_x, "x steps.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz, r_earth):#FIX THIS, MAKE THIS A VALID FUNCTION
                    m = rho*h**3 #FIX THIS, MAKE THIS A VALID MASS ELEMENT rho*dV
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
                    grav_vec_equator += grav_accel(point, point_equator, m)
                    grav_vec_southpole += grav_accel(point, point_southpole, m)
    print("The gravity vector at the north pole is...", np.around(grav_vec_northpole, 6))
    print("The gravity vector at the equator is...", np.around(grav_vec_equator, 6))
    print("The gravity vector at the south pole is...",np.around(grav_vec_southpole, 6))
    print("Should be something like [0,0,-9.8] m/s^2")
