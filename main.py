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
    """),
    0)
mario.set_position(10, 60)
mario.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
# Make player controls
controller.move_sprite(mario, 200, 200)
# Create the enemies

def on_update_interval():
    goombas = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . e e e e e e . . . .
    . . . . . e f e e e e f e . . .
    . . . . e e 1 f e e f 1 e e . .
    . . . e e e 1 f f f f 1 e e e .
    . . . e e e 1 f e e f 1 e e e .
    . . . e e e 1 1 e e 1 1 e e e .
    . . . . e e e e e e e e e e . .
    . . . . . d d d d d d d d . . .
    . . . . . d d d d d d d d . . .
    . . . f f d d d d d d d d f f .
    . . . f f f d d d d d d f f f .
    . . . f f f f . . . . f f f f .
    . . . . f f f . . . . f f f . .
    """))
    goombas.set_position(scene.screen_width(), randint(0,scene.screen_height()))
    goombas.set_velocity(-30,0)
    
game.on_update_interval(750, on_update_interval)