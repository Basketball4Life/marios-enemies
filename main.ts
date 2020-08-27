//  Create the game
info.setScore(0)
info.setLife(3)
//  Make the player
let mario = sprites.create(img`
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
    `, 0)
mario.setPosition(10, 60)
mario.setFlag(SpriteFlag.StayInScreen, true)
//  Make player controls
controller.moveSprite(mario, 200, 200)
//  Create the enemies
game.onUpdateInterval(750, function on_update_interval() {
    let goombas = sprites.create(img`
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
    `)
    goombas.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
    goombas.setVelocity(-30, 0)
})
