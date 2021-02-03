import numpy as np

N0 = 2

x0 = np.linspace(-N0,N0,100)
y0 = np.linspace(-N0,N0,100)

xx0,yy0 = np.meshgrid(x0,y0)

print (xx0)
print (yy0)

z0 = -np.sqrt(10.0 - xx0**3.0 - yy0**2.0)

def pz_x(x,y):
    return 1.5*x**2.0/np.sqrt(10.0-x**3.0-y**2.0)
    #return x/np.sqrt(10.0-x**2.0-y**2.0)

def pz_y(x,y):
    return y/np.sqrt(10.0-x**2.0-y**2.0)

# x_0,y_0
x_0 = 1.0
y_0 = -1.91

gamma_0 = 1e-4
ratio = 0.98


N = 40
gamma_cal = gamma_0
x_cal = x_0
y_cal = y_0

xx = np.array([])
yy = np.array([])
d_Fx = 0
d_Fy = 0
x_old_1 = 0
y_old_1 = 0
d_Fx_old_1 = 0
d_Fy_old_1 = 0
for i0 in range(N):
    #gamma_cal *= ratio
    print ("Iteration: {}".format(i0))
    #print ("\tgamma: ",gamma_cal)
    
    if i0 == 0:
        gamma_cal *= ratio
        # get old value
        d_Fx_old_1 = pz_x(x_cal,y_cal)
        d_Fy_old_1 = pz_y(x_cal,y_cal)
        
        x_old_1 = x_cal
        y_old_1 = y_cal
        
        # update
        x_cal += - gamma_cal*d_Fx_old_1
        y_cal += - gamma_cal*d_Fy_old_1
        
    
    else:
        
        d_Fx = pz_x(x_cal,y_cal)
        d_Fy = pz_y(x_cal,y_cal)
        
        AA = np.abs( (x_cal - x_old_1)*(d_Fx - d_Fx_old_1) + (y_cal - y_old_1)*(d_Fy - d_Fy_old_1) )
        BB = (d_Fx - d_Fx_old_1)**2.0 + (d_Fy - d_Fy_old_1)**2.0
        
        # get gamma_n
        gamma_cal = AA / BB
        
        print ("AA: {}, BB: {}".format(AA,BB))
        
        # store 
        d_Fx_old_1 = d_Fx
        d_Fy_old_1 = d_Fy
        
        x_old_1 = x_cal
        y_old_1 = y_cal
        
        # update 
        x_cal += -gamma_cal*d_Fx
        y_cal += -gamma_cal*d_Fy
        
    
        print ("\tgamma: ",gamma_cal)
        
    if  gamma_cal > 1e3:
        print ("----------------------gamma={} exceeds threshold: 1000.".format(gamma_cal))
        break
    
    print ("\tcoordinates: ({},{})".format(x_cal,y_cal))
    print ("\tz: {}".format(-np.sqrt(10.0-x_cal**3.0-y_cal**2.0)))
    
    xx = np.append(xx,x_cal)
    yy = np.append(yy,y_cal)
    
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.figure(0)
plt.imshow(z0,extent=[-N0,N0,N0,-N0],cmap=mpl.cm.jet)
plt.colorbar()
plt.contour(xx0,yy0,z0,colors='k',levels=20)
plt.plot(xx,yy,'r.-')
#plt.colorbar()
plt.show()
