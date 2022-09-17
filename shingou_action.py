from enum import Enum
import sys
class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
def act_shingou(color):
    shingou = Shingou(color)
    if shingou is Shingou.RED:
        print ("とまれ")
    elif shingou is Shingou.BLUE:
        print ("すすめ")
    elif shingou is Shingou.YELLOW:
        print("ちゅうい")
    
if __name__ == "__main__":
    args = sys.argv
    act_shingou(int(args[1]))