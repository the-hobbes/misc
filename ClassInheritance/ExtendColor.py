from Color import Color
# http://stackoverflow.com/questions/14583761/typeerror-module-init-takes-at-most-2-arguments-3-given


class ExtendColor(Color):
    def getColor(self):
        return self.color + "......extended!"


def main():
    c = ExtendColor("blue")
    print c.getColor()

main()
