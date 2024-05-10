def buildKdtree(points, axis=0):
    if not points:
        return None
    points.sort(key = lambda x:x[axis])
    median = len(points)//2
    return {"point": points[median], "axis": axis, "left": buildKdtree(points[:median], (axis+1)%len(points[0])), "right": buildKdtree(points[median+1:], (axis+1)%len(points[0]))}

def print_tree(root, level=0, side=None):
    if root is None:
        return
    prefix = ""
    if side is not None:
        prefix = side + "---- "
    print("  "*level + prefix + str(root["point"]))
    print_tree(root["left"], level+1, "L")
    print_tree(root["right"], level+1, "R")

points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
print_tree(buildKdtree(points))
