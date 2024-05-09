import math

def orientation(p, q, r):
    value = (q[1]-p[1]) * (r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
    if value == 0:
        return 0 #collinear
    return 1 if value > 0 else -1 # 1->anticlockwise, -1-> anticlockwise  

def polar_angle(p0, p1):
    return math.atan2(p1[1]-p0[1], p1[0]-p0[0])

def dist(p0, p):
    return math.dist(p0, p)

def graham_scan(points):
    if (len(points) < 3):
        return "Not possible"
    p0 = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: (polar_angle(p0, p), dist(p0, p)))
    
    stack = []
    stack.append(points[0])
    stack.append(points[1])
    stack.append(points[2])

    for i in range(3, len(points)):
        while (len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) == 1):
            stack.pop()
        stack.append(points[i])

    return stack

points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
print("Convex Hull:", graham_scan(points))
