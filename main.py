# Create the game 
info.set_score(0)
info.set_life(3)

# Make the player 
mario = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . 2 2 2 2 2 2 2 . . . . . .
    . . 2 2 2 2 2 2 2 2 2 2 . . . .
    . . e e e d d f d . . . . . . .
    . e d e d d d f d d . . . . . .
    . e d e e d d d f d d . . . . .
    . e e d d d d f f f f . . . . .
    . . . d d d d d d d . . . . . .
    . . 2 2 a 2 2 a 2 . . . . . . .
    . 2 2 2 a 2 2 a 2 2 . . . . . .
    2 2 2 2 a a a a 2 2 2 . d . . .
    2 2 2 a 5 a a 5 a 2 d d d . . .
    d d 2 a a a a a a 2 d d d . . .
    d d d a a a a a a 2 2 2 . . . .
    d d . e e . . e e . . . . . . .
    . . e e e . . e e e . . . . . .
"""))
mario.set_position(10, 60)
mario.set_flag(SpriteFlag.StayInScreen, True)
# Make player controls
controller.move_sprite(mario, 200, 200)

# Create the basket to make the points

# Shoot the projectiles at the basket
