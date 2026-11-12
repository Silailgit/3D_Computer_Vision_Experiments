import numpy as np
import matplotlib.pyplot as plt

def project_points(points, K, R, t):

    cam = points @ R.T + t            
    cam = cam[cam[:, 2] > 0]
    pix = cam @ K.T                   
    return pix[:, :2] / pix[:, 2:3]   

cube = np.array([[x, y, z] for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)], float)

K = np.array([[800, 0, 320],
              [0, 800, 240],
              [0,   0,   1]], float)   

R = np.eye(3)                          
t = np.array([0, 0, 5.0])              

uv = project_points(cube, K, R, t)

plt.scatter(uv[:, 0], uv[:, 1])
plt.xlim(0, 640); plt.ylim(480, 0)     # görüntüde y aşağı doğru
plt.gca().set_aspect("equal"); plt.show()
