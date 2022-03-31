from graphics import Point, Text


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        center = self.shape.getCenter()
        center_x = center.getX()
        center_y = center.getY()
        label_text = Text(Point(center_x, center_y), label)
        self.text = label_text
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        point_x = point.getX()
        point_y = point.getY()
        shape_x1 = self.shape.getP1().getX()
        shape_y1 = self.shape.getP1().getY()
        shape_x2 = self.shape.getP2().getX()
        shape_y2 = self.shape.getP2().getY()
        if shape_x1 <= point_x <= shape_x2:
            if shape_y2 <= point_y < shape_y1:
                return True
        return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret
