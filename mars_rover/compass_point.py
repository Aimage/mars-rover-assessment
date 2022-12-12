
class CompassPoint():
    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right

COMPASS_MAP = {
        "N" : CompassPoint("W", "E"),
        "S" : CompassPoint("E", "W"),
        "E" : CompassPoint("N", "S"),
        "W" : CompassPoint("S", "N")
}
