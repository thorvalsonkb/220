from graphics import Point, Text


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        point_x1 = self.shape.getP1().getX()
        point_y1 = self.shape.getP1().getY()
        point_x2 = self.shape.getP2().getX()
        point_y2 = self.shape.getP2().getY()
        center_x = (point_x2 + point_x1) / 2
        center_y = (point_y1 + point_y2) / 2
        label_text = Text(Point(center_x, center_y), label)
        self.text = label_text

    def get_label(self):
        return self.text

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
            if shape_y1 <= point_y <= shape_y2:
                return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)
