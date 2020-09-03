controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player1_button_a_pressed() {
    
    fire = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 5 5 5 5 5 5 . . . . . 
                    . . . . 5 2 2 2 2 2 2 5 . . . . 
                    . . . 5 2 2 4 4 4 4 2 2 5 . . . 
                    . . 5 2 2 4 5 5 5 4 2 2 5 . . . 
                    . . . 5 2 2 4 4 4 4 2 2 5 . . . 
                    . . . . 5 2 2 2 2 2 2 5 . . . . 
                    . . . . . 5 5 5 5 5 5 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        `, mario, 50, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
let goombas : Sprite = null
let fire : Sprite = null
let mario : Sprite = null
//  Create the game
info.setScore(0)
info.setLife(3)
scene.setBackgroundImage(img`
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555515555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555511555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555551151555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555551551111111155aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111111111115555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaaaa11111111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555111555555551155aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111555555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaa111111111111111111aaaaaaaaaaaaaaaaaaaaaaaa5555115515155115555aaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111155555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111aaaaaaaaaaaaaaaaaaaa5511555515155155555aaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111115555555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaa111111111111111111111111aaaaaaaaaaaaaaaaaa1111111155555155555aaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111111155555555555555555
    aaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111aaaaaaaaaaaaaaaa5555555155555155555aaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111111111555555555555555
    aaaaaaaaaaaaaaaaa1111111111111111111111111111111111aaaaaaaaaaaaaaa5555555151155511555aaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111111111aaaa5555555555
    aaaaaaaaaaaaaaaa11111111111111111111111111111111111aaaaaaaaaaaaaaa5555555151515551555aaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111111111aaaaaaaa555555
    aaaaaaaaaaaaaa1111111111111111111111111111111111111aaaaaaaaaaaaaaaa55555515151111155aaaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaa11111111111111111111111111111111111111aaaaaaaaaaaaaaaa55555515155555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaa11111111111111111111111111111111111111aaaaaaaaaaaaaaaaa555551155555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaa11111111111111111111111111111111111111aaaaaaaaaaaaaaaaaa5555555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaa11111111111111111111111111111111111111aaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111aaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaa11111111111111111111111111111111111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111111111111111111aaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaa111111111111111111111111111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaa1111111111111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111aaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaa11111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111111111111aaaaaaaaaaaaaaaaaaaaa111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111aaaaaaaaaaaaaaaaa111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111aaaaaaaaaaaaaaaaa111111111111111111111111111111aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111aaaaaaaaaaaaaaaaaa111111111111111111111111111aaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111aaaaaaaaaaaaaaaaaaaa11111111111111111111111aaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11111111111111111111111111111111aaaaaaaaaaaaaaaaaaaaaaa1111111111111111aaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111111111111111111111111111111111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111111111111111111111111111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaadddddddaaaaaaaaaaaaaaaaaaaaaaaaaa111111111111111111111111111111111111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaddddddddddddddddddddddddddddddaaaaaaaa111111111111111111111111111111111111111aaaaaaaaaaaaaaaadddddddddddddddddddddddddddaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaadddddddddddddddddddddddddddddddddddddaaaaa111111111111111111111111111111111111111aaaaaaaaaaaaaadddddddddddddddddddddddddddddddaaaaaaaaaaaaaa
    aaaaaaaaaaaaaddddddddddddddddddddddddddddddddddddddddddddaaaaa111111111111111111111111111111111111111aaaaaaaaaaaadddddddddddddddddddddddddddddddddddaaaaaaaaaaaa
    aaaaaaaaaadddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111111111111111111111111111111111aaaaaaaaaaddddddddddddddddddddddddddddddddddddddaaaaaaaaaaa
    aaaaaaadddddddddddddddddddddddddddddddddddddddddddddddddddddddddaa1111111111111111111111111111111111aaaaaaaaaddddddddddddddddddddddddddddddddddddddddaadddddddaa
    aaaaddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaa1111111111111111aaaaaaaaadddddddddddddddddddddddddddddddddddddddddddddddddddd
    aaadddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaddddddddddddddddddddddddddddddddddddddddddddddddddddd
    addddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaadddddddddddddddddddd111111dddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd11dddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddd1111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd11ddd11111dddddddddddddddddd
    dddddddddddddddddddddd111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd111ddddddddddddddddddddddd
    dddddddddddddddd111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddd111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddd1111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddd111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd11111111111111111111dddddddddddddddddddddd111dddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaddddddddddddddddddddddddddddddddddddddaa
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaadddddddddddddddaaaaaaaaaaaaaadddddddddddddaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddddddddddddddddaaddddddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddddddddddddaaaaaaaaaaddddddddddddddddddddaaaaadddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddddddddddddaaaaaaaaaaaaaadddddddddddddaaaaaaaadddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    ddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddddddaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddddaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    ddddddddddddaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5551155aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddddaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5551155aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    dddddddddaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5551155aaaaaaaaaaaaaaaaaaaaaaaaaaaa1111aaaaaa
    dddddddaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5551155aaaaaaaaaaaaaaaaaaaaaaaaaaa11ff1aaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5551155aaaaaaaaaaaaaaaaaaaaaaaaaa11fff1aaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55155aaaaaaaaaaaaaaaaaaaaaaaaaaa1ffff1aaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ffff1aaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11ffff11aaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1fffff111aaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaa1ffffff11111a
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55551155555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaa1fffffff11111
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55551155555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaa1ffffffffffff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55551155555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaa1ffffffffffff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55551155555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaa11fffffffffff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55551155555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaaa11ffffffffff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55551155555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaaaa1ffffffffff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55551155555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaaaa1ffffffffff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa555555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaaaa1fffff111ff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5555555aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa55555555555aaaaaaaaaaaaaaaaaaaaaaaa11fff1a1ff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111aa1ff
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    aaaaaaaaa111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    111111111111aaaaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    11111111111111aaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    11111111111111aaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeee11111aaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeee111aaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeee111aaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa77777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeeeeeaaaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa77ff777fff7aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeeeeeeaaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa777f777f7777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeeeeeeaaaaaaaaa777777777777777777777777777777777777777aaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaa7777f77f77f777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaa7777f7f777f777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111ff7777f117aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11111ff7777f177aaaaaaaaaaaaaaaaaaeeeeeaaaaaaaeee1ff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11ff111ff1fff11aaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeee1ff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaa11ff111ff11ff11aaaaaaaaaaaaaaaaaaeeeeeeeeeeeefee1ff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1ff111ff11ff1aaaaaaaaaaaaaaaaaaaeeffeefeeeeefee1ff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111111111aaaaaaaaaaaaaaaaaaaaaeeeefffffffefeeeff
    eeeeeeeeeeeeee1aaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa222222222222222222222222222aaaaa11aeeeeeefeeeefffffff
    eeeeeeeeeeeeee11aaaaaaaaaaaaa17777777777777777777777777aaaaa111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111222222222222222222222222222a1111a1aeeeeeefeeeeefeeeee
    eeeeeeeeeeeeeeaa1111111aaaaa117777777777777777777777777a11111aaa11111aa111aaaaaaaa1111aaa111aa1111111111aaa222222222222222222222222222aaaaaaa1eeeeeefeeeeefeeeee
    eeeeeeeeeeeeeeaaaaaaaaa111111a7777777777777777777777777aaaaaaaaaaaa111111111111111aaaa1111aa11aaaaaaaaaaaaa2222222222222222222222222221aaaaaaaeefffffffeeefeeeee
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa222222222222222222222222222aaaaaaaaeeeeeefeefffffffff
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa222222222222222222222222222aaaaaaaaeeeeeefeeeeefeeeee
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa222222222222222222222222222aaaaaaaaeeeeeefeeeefeeeeee
    eeeeeeeeeeeeeeaa1111111aaaaaaa7777777777777777777777777aaaaaaaaaaaa8888888888888888888888888aaaaaaaaaaaaaaa222222222222222222222222222aaaaaaaaeefffffffffffeeeee
    eeeeeeeeeeeeee11aaaaaa1aaaaaaa7777777777777777777777777aaaaaaaaaaaa8888888888888888888888888aaaaaaaaaaaaaaa222222222222222222222222222aaaaaaaaeeeeeeefeeeeffffff
    eeeeeeeeeeeeeeaaaaaaaa1aaaaaaa7777777777777777777777777aaaaaaaaaaaa8888888888888888888888888aaaaaaaaaaaaaaaaaa222222222222222222222aaaaaaaaaaaeeeeeeefeeeefeeeee
    eeeeeeeeeeeeeeaaaaaaaaa1aaaaaa7777777777777777777777777aaaaaaaaaaaa8888888888888888888888888aaaaaaaaaaaaaaaaaa222222222222222222222aaaaaaaaaaaeeeeeffffffffeeeee
    eeeeeeeeeeeeeeaaaaaaaaaa1aaaaa7777777777777777777777777aaaaaa11aaaa8888888888888888888888888aaaaa11111aaaaaaaa222222222222222222222aaaaaaaaaaeeffffeefeeeeeffffe
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaa11aa8888888888888888888888888aaaaaaaaa1aaaaaaaa222222222222222222222aaaaaaaaaaeeeeeeefffffffffeee
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaa1aaaa88888888888888888888aaaaaaaaaaaaaaaaaaaaa222222222222222222222aaaaaaaaaaeeeefffefeeeeefffee
    eeeeeeeeeeeeeeaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaa88888888888888888888aaaaaaaaaaaaaaaaaaaaa222222222222222222222aaaaaaaaaaeeffeeeeffeeeeefeee
    eeeeeeeeeeeeeaaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaa88888888888888888888aaaaaaaaaaaaaaaaaaaaa222222222222222222222aaaaaaaaaaeeeeeeeeffeeeeffeee
    eeeeeeeeeeeeeaaaaaaaaaaaaaaaaa7777777777777777777777777aaaaaaaaaaaaaa88888888888888888888aaaaaaaaaaaaaaaaaaaaa222222222222222222222aaaaaaaaaaeeeeeeeefeeeeeeeeee
`)
//  Make the player
mario = sprites.create(img`
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
mario.setKind(SpriteKind.Player)
//  Make player controls
controller.moveSprite(mario, 200, 200)
info.startCountdown(45)
//  Create the enemies
game.onUpdateInterval(750, function on_update_interval() {
    
    goombas = sprites.create(img`
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
        `, 0)
    goombas.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
    goombas.setVelocity(-40, 0)
    goombas.setKind(SpriteKind.Enemy)
})
