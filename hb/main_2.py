from hitbox import Hitbox

hb1 = Hitbox(x = 0,y = 100, width = 100, height = 100)
hb2 = Hitbox(x = 150,y = 100, width = 100, height = 100)
hb3 = Hitbox(x = 300,y = 100, width = 100, height = 100)

intersection = hb1.intersects(hb2)
print(intersection)
intersection2 = hb2.intersects(hb3)
print(intersection2)
intersection3 = hb3.intersects(hb1)
print(intersection3)