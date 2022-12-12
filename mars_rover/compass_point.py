
class CompassPoint():
    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right

COMPASS_MAP = {
        "N" : CompassPoint("O", "E"),
        "S" : CompassPoint("E", "O"),
        "E" : CompassPoint("N", "S"),
        "O" : CompassPoint("S", "N")
}
