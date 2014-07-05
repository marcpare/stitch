import numpy as np
# Implementing the calculation described at
# http://stackoverflow.com/questions/11687281/transformation-between-two-set-of-points

#   b    =      A         *    x
# [xp0]     [ x0 y0 1 0]
# [yp0]     [-y0 x0 0 1]
# [xp1]     [ x1 y1 1 0]     [M11]
# [yp1]  =  [-y1 x1 0 1]  *  [M12]
# [xp2]     [ x2 y2 1 0]     [M13]
# [yp2]     [-y2 x2 0 1]     [M23]
# [xp3]     [ x3 y3 1 0]
# [yp3]     [-y3 x3 0 1]

# [M11], [M12] define rotation and scaling
# [M13] is x translation
# [M23] is y translation

def estimate_similarity(xs, ys, x2s, y2s):
    N = len(xs)
    
    # build b
    b = np.empty((N+N, 1))
    b[::2,0] = xs
    b[1::2,0] = ys
    
    # build A
    A = np.empty((N+N, 4))
    A[::2, 0] = x2s
    A[1::2,0] = -y2s
    A[::2, 1] = y2s
    A[1::2, 1] = x2s
    A[::2, 2] = np.ones(N)
    A[1::2, 2] = np.zeros(N)
    A[::2, 3] = np.zeros(N)
    A[1::2, 3] = np.ones(N)
    
    A = np.linalg.lstsq(A, b)[0][:,0]
    M = [[ A[0], A[1], A[2]],
         [-A[1], A[0], A[3]]]
    return np.array(M)

def estimate_translation(points1, points2):
    """ A further reduction, only calculating Tx, Ty, and a uniform scale S

       b    =      A         *    x
     [xp0]     [ x0 1 0]
     [yp0]     [-y0 0 1]
     [xp1]     [ x1 1 0]     [M11]
     [yp1]  =  [-y1 0 1]  *  [M13]
     [xp2]     [ x2 1 0]     [M23]
     [yp2]     [-y2 0 1]     
     [xp3]     [ x3 1 0]
     [yp3]     [-y3 0 1]

     [M11] defines scaling (S)
     [M13] is x translation (Tx)
     [M23] is y translation (Ty)
    """
    xs = points1[:,0]
    ys = points1[:,1]
    x2s = points2[:,0]
    y2s = points2[:,1]
    N = len(xs)
    
    # build b
    b = np.empty((N+N, 1))
    b[::2,0] = xs
    b[1::2,0] = ys
    
    # build A
    A = np.empty((N+N, 3))
    A[::2, 0] = x2s
    A[1::2,0] = y2s
    A[::2, 1] = np.ones(N)
    A[1::2, 1] = np.zeros(N)
    A[::2, 2] = np.zeros(N)
    A[1::2, 2] = np.ones(N)
    
    A = np.linalg.lstsq(A, b)[0][:,0]
    M = [[1, 0, A[1]],
         [0, 1, A[2]]]
    return (A[0], A[1], A[2], np.array(M))

if __name__ == "__main__":
    
    N = 10
    xs = np.arange(N)
    ys = np.zeros(N)

    # perform a shift, introduce some noise
    x2s = xs + np.random.rand(N) + 2
    y2s = ys + np.random.rand(N) + 5
    
    # should return an x translation of ~2.5 (the random noise adds an average of 0.5)
    # and a y translation of ~5.5
    M = estimate_similarity(xs, ys, x2s, y2s)
    print M
    
    points1 = np.vstack((xs, ys)).T
    points2 = np.vstack((x2s, y2s)).T
    
    print estimate_translation(points1, points2)