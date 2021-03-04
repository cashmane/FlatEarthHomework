import numpy as np
import matplotlib.pyplot as plt


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
    if x**2+y**2 < radius**2 and 0 <= z < 4750000:
        return True
    else:
        return False

if __name__ == "__main__":
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    r_earth = 20037*km #radius of globe Earth
    h = 500.0*km #relatively coarse step size
    #set grid size same in x,y,z
    dx, dy, dz = h, h, h#200*km
    #x, y, z define boundaries of grid, here 7000 km
    x = np.arange(-21000*km, 21000*km, dx)
    len_x = x.shape[0]
    y = x.copy()
    z = np.arange(-5000*km, 5000*km, dz)
    #define points on the north pole, south pole, and equator
    point_northpole = np.array([0, 0, 4750*km])
    point_equator   = np.array([10018.5*km, 0, 4750*km]) #<--FIX
    point_southpole = np.array([20037*km, 0, 4750*km]) #<--FIX
    ##Sample North Pole calc
    ##You might consider making this a function
    grav_vec_northpole = 0
    grav_vec_equator = 0
    grav_vec_southpole = 0
    height = [1*km, 10*km, 100*km, 1000*km, 10000*km, 100000*km, 1000000*km]
    yvals = []
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
    #print("Should be something like [0,0,-9.8] m/s^2")
    for i in range(len(height)):
        grav_vec_northpole = 0
        point_northpole[2] += height[i]
        for idx, xx in enumerate(x):
            #this is a trick to tell how long it will take
            #print(idx, " of ", len_x, "x steps.")
            for yy in y:
                for zz in z:
                    if point_in_sphere(xx,yy,zz, r_earth):#FIX THIS, MAKE THIS A VALID FUNCTION
                        m = rho*h**3 #FIX THIS, MAKE THIS A VALID MASS ELEMENT rho*dV
                        point = np.array([xx,yy,zz])
                        grav_vec_northpole += grav_accel(point, point_northpole, m)
                        grav_vec_equator += grav_accel(point, point_equator, m)
                        grav_vec_southpole += grav_accel(point, point_southpole, m)
        yvals.append(np.around(grav_vec_northpole[2], 6))
        point_northpole = np.array([0, 0, 4750*km])
    for i in range(len(yvals)):
        yvals[i] = abs(yvals[i])

    plt.plot(height, yvals)
    #plt.ylim(0, -10.5)
    #plt.xlim(0, 1e9)
    plt.title('Gravitational Acceleration at Height')
    plt.xlabel('Height in meters')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('Gravitational Acceleration')
    plt.show()

    

    
