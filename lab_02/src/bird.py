from src.colors import *
import copy
from math import cos, sin, radians, pi

def transform_y_coord(coord):
    return CANV_Y - coord 

class Bird:
    """
        Bird representation.
    """

    eps = 1e-6
    body_a = CANV_X / 8
    body_b = body_a / 2
    head_radius = body_b * 2 / 3

    body_color = "DarkGoldenrod1"
    head_color = "DarkGoldenrod2"
    beak_color = "DarkOrange1"
    wing_color = "orange"
    leg_color = beak_color
    limb_color = "#f50a7f"
    eye_color = "#28b549"

    def __init__(self, *args, **kwargs):
        self.center = [CANV_X / 2, CANV_Y / 2]
        self.body_a = CANV_X / 8
        self.body_b = self.body_a / 2
        self.head_radius = self.body_b * 2 / 3

        self.body = self.get_body(*self.center)
        self.head = self.get_head()
        self.beak = self.get_beak()
        self.wing = self.get_wing()
        self.left_leg = self.get_left_leg()
        self.right_leg = self.get_right_leg()
        self.tail = self.get_tail()

    def reset(self):
        self.__init__()

    def get_body(self, a, b):
        """
            Get bird body dots.
        """

        body = []
        t = 0

        while 2 * pi - t > Bird.eps:
            body.extend([-self.body_a*cos(t) + self.center[0], \
                self.body_b*sin(t) + self.center[1]])
            t += 0.1

        
        body.extend([body[0], body[1]])

        return body

    def get_head(self):
        """
            Get bird head dots.
        """

        body = self.body
        ind = 114
        start_p = [body[ind], body[ind + 1]]

        head = []
        t = 0

        while 2 * pi - t > Bird.eps:
            head.extend([self.head_radius*cos(t) + start_p[0], \
                self.head_radius*sin(t) + start_p[1] - self.head_radius])
            t += 0.1

        head.extend([head[0], head[1]])

        return head

    def get_beak(self):
        """
            Get bird beak dots.
        """

        head = copy.deepcopy(self.head)
        for i in range(1, len(head), 2):
            head[i] = transform_y_coord(head[i])

        beak = []

        beak.append([head[0] - 2*self.head_radius, head[1] + self.head_radius * 1 / 3])
        beak.append([head[0] - 2*self.head_radius, head[1] - self.head_radius * 1 / 3])
        beak.append([head[0] - self.head_radius * 8 / 3, head[1]])

        for i in range(len(beak)):
            beak[i][1] = transform_y_coord(beak[i][1])

        return beak

    def get_wing(self):
        """
            Get bird wing dots.
        """

        wing = []

        wing.append([self.center[0], self.center[1]])
        wing.append([self.center[0] + 1/2 * self.body_a, self.center[1]])
        wing.append([self.center[0] + 5/8 * self.body_a, self.center[1] - 4/3 * self.body_b])

        for i in range(len(wing)):
            wing[i][1] = transform_y_coord(wing[i][1])

        return wing

    def get_left_leg(self):
        """
            Get bird left leg dots.
        """

        l_leg = []
        l_leg.append(self.center[0] - 3/4 * self.body_a)
        l_leg.append(self.center[1] - 5/8 * self.body_b)
        l_leg.append(self.center[0] - self.body_a)
        l_leg.append(self.center[1] - 2 * self.body_b)


        for i in range(1, len(l_leg), 2):
            l_leg[i] = transform_y_coord(l_leg[i])

        return l_leg

    def get_right_leg(self):
        """
            Get bird right leg dots.
        """
        
        r_leg = []
        r_leg.append(self.center[0] - 1/4 * self.body_a)
        r_leg.append(self.center[1] - 5/8 * self.body_b)
        r_leg.append(self.center[0])
        r_leg.append(self.center[1] - 2 * self.body_b)


        for i in range(1, len(r_leg), 2):
            r_leg[i] = transform_y_coord(r_leg[i])

        return r_leg

    def get_tail(self):
        """
            Get fish tail dots.
        """

        tail = []

        tail.append([self.center[0] + self.body_a, self.center[1] + self.body_b * 1 / 3])
        tail.append([self.center[0] + self.body_a, self.center[1] - self.body_b * 1 / 3])
        tail.append([self.center[0] + self.body_a + self.body_b / 2, self.center[1]])

        for i in range(len(tail)):
            tail[i][1] = transform_y_coord(tail[i][1])

        return tail

    def draw(self, canvas):
        """
            Draw bird to canvas.
        """

        canvas.create_line(*self.body, fill=Bird.body_color, width=2)
        canvas.create_line(*self.head, fill=Bird.head_color, width=2)
        canvas.create_polygon(*self.beak,fill=Bird.beak_color)
        canvas.create_polygon(*self.tail,fill=Bird.head_color)
        canvas.create_polygon(*self.wing,fill=Bird.wing_color)
        canvas.create_line(*self.left_leg, fill=Bird.leg_color, width=2)
        canvas.create_line(*self.right_leg, fill=Bird.leg_color, width=2)


        y_offset = 10
        canvas.create_oval(self.center[0]-2,transform_y_coord(self.center[1])+2, \
            self.center[0]+2, transform_y_coord(self.center[1])-2, fill="red")
        canvas.create_text(self.center[0], transform_y_coord(self.center[1])-y_offset,
        fill="red",
        font="-family {Consolas} -size 10",
        text="({:.3f}; {:.3f})".format(self.center[0], self.center[1]))

    def move(self, dx, dy):
        """
            Move model.
        """

        self.center = [self.center[0] + dx, self.center[1] + dy]
        
        
        for i in range(0, len(self.body), 2):
            self.body[i] += dx
            self.body[i+1] -= dy

        for i in range(0, len(self.head), 2):
            self.head[i] += dx
            self.head[i+1] -= dy

        for i in range(len(self.beak)):
            self.beak[i][0] += dx
            self.beak[i][1] -= dy

        for i in range(len(self.wing)):
            self.wing[i][0] += dx
            self.wing[i][1] -= dy

        for i in range(0, len(self.left_leg), 2):
            self.left_leg[i] += dx
            self.left_leg[i+1] -= dy

        for i in range(0, len(self.right_leg), 2):
            self.right_leg[i] += dx
            self.right_leg[i+1] -= dy

        for i in range(len(self.tail)):
            self.tail[i][0] += dx
            self.tail[i][1] -= dy

    def rotate(self, rx, ry, angle):
        """
            Rotate model.
        """

        def x_rotate(rx, ry, x, y):
            return rx + (x - rx) * cosa + (y - ry) * sina

        def y_rotate(rx, ry, x, y):
            return ry - (x - rx) * sina + (y - ry) * cosa

        cosa = cos(radians(angle))
        sina = sin(radians(angle))

        x = self.center[0]
        y = self.center[1]

        self.center[0] = x_rotate(rx, ry, x, y)
        self.center[1] = y_rotate(rx, ry, x, y)

        for i in range(0, len(self.body), 2):
            x = self.body[i]
            y = self.body[i+1]
            self.body[i] = x_rotate(rx, ry, x, y)
            self.body[i+1] = y_rotate(rx, ry, x, y)

        for i in range(0, len(self.head), 2):
            x = self.head[i]
            y = self.head[i+1]
            self.head[i] = x_rotate(rx, ry, x, y)
            self.head[i+1] = y_rotate(rx, ry, x, y)

        for i in range(len(self.beak)):
            x = self.beak[i][0]
            y = self.beak[i][1]
            self.beak[i][0] = x_rotate(rx, ry, x, y)
            self.beak[i][1] = y_rotate(rx, ry, x, y)

        for i in range(len(self.wing)):
            x = self.wing[i][0]
            y = self.wing[i][1]
            self.wing[i][0] = x_rotate(rx, ry, x, y)
            self.wing[i][1] = y_rotate(rx, ry, x, y)

        for i in range(0, len(self.left_leg), 2):
            x = self.left_leg[i]
            y = self.left_leg[i+1]
            self.left_leg[i] = x_rotate(rx, ry, x, y)
            self.left_leg[i+1] = y_rotate(rx, ry, x, y)

        for i in range(0, len(self.right_leg), 2):
            x = self.right_leg[i]
            y = self.right_leg[i+1]
            self.right_leg[i] = x_rotate(rx, ry, x, y)
            self.right_leg[i+1] = y_rotate(rx, ry, x, y)

        for i in range(len(self.tail)):
            x = self.tail[i][0]
            y = self.tail[i][1]
            self.tail[i][0] = x_rotate(rx, ry, x, y)
            self.tail[i][1] = y_rotate(rx, ry, x, y)

    def scale(self, mx, my, kx, ky):
        """
            Scale model.
        """
        def scale_x(x):
            return kx*x + (1 - kx) * mx

        def scale_y(y):
            return ky*y + (1 - ky) * my

        self.center = [kx*self.center[0] + (1 - kx) * mx, ky*self.center[1] + (1 - ky) * my]
        self.body_a *= kx
        self.body_b *= ky
        self.head_radius = self.body_b * 2 / 3


        for i in range(0, len(self.body), 2):
            self.body[i] = scale_x(self.body[i])
            self.body[i+1] = scale_y(self.body[i + 1])

        for i in range(0, len(self.head), 2):
            self.head[i] = scale_x(self.head[i])
            self.head[i+1] = scale_y(self.head[i+1])

        for i in range(len(self.beak)):
            self.beak[i][0] = scale_x(self.beak[i][0])
            self.beak[i][1] = scale_y(self.beak[i][1])

        for i in range(len(self.wing)):
            self.wing[i][0] = scale_x(self.wing[i][0])
            self.wing[i][1] = scale_y(self.wing[i][1])

        for i in range(0, len(self.left_leg), 2):
            self.left_leg[i] = scale_x(self.left_leg[i])
            self.left_leg[i+1] = scale_y(self.left_leg[i+1])

        for i in range(0, len(self.right_leg), 2):
            self.right_leg[i] = scale_x(self.right_leg[i])
            self.right_leg[i+1] = scale_y(self.right_leg[i+1])

        for i in range(len(self.tail)):
            self.tail[i][0] = scale_x(self.tail[i][0])
            self.tail[i][1] = scale_y(self.tail[i][1])
