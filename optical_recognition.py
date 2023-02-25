from algorithm import Solution
import cv2
import numpy as np

class OpticalRecognizer:
    def interp(img, offset=(0,0)):
        def rgb2col(rgb):
            colors = {
                'WHITE': [255, 255, 255],
                'YELLOW': [255, 255, 0],
                'ORANGE': [254, 102, 1],
                'BLUE': [0, 204, 255],
                'BLACK': [56, 56, 56]}
            mindist = 3 * 255**2
            closest = None
            for color in colors:
                d = np.linalg.norm(np.array(colors[color])[::-1] - rgb)
                if d < mindist:
                    mindist = d
                    closest = color
            return closest

        loc2rc = {
            'f1': (14,94),
            'f2': (46,16),
            'f3': (81,8),
            'f4': (141,110),
            'm1': (28,72),
            'm2': (64,111),
            'm3': (102,111),
            'm4': (117,93),
            'l1': (43,85),
            'l2': (58,92),
            'l3': (88,49),
            'l4': (64,70),
            'l5': (81,70),
            'r1': (44,136),
            'r2': (58,130),
            'r3': (85,173),
            'r4': (64,150),
            'r5': (81,151),
        }

        state = {}
        for loc in loc2rc:
            r,c = loc2rc[loc]
            rc = (r+offset[0], c+offset[1])
            state[loc] = rgb2col(img[rc])

        return state

if __name__ == "__main__":
    path = "./all.jpg"
    img = cv2.imread(path)
    offset = (686,1796)
    state = OpticalRecognizer.interp(img, offset=offset)
    plan = Solution.solve(state)
    print(plan[::-1])