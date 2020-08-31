# Create the game
info.set_score(0)
info.set_life(3)
scene.set_background_image(img("""
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 a a a a a a a a a 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a 5 5 5 5 5 5 5 5 5 5
    a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a 5 5 5 5 5 5
    a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a 1 1 a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a 1 a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a
    a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a
    a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a
    a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a d d d d d d d a a
    a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a
    d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a d d d d d d d d d d d d d d d a a a a a a a a a a a a a a d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d d d d d d d d d d d d d a a d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d a a a a a d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a d d d d d d d d d d d d d a a a a a a a a d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 a a a a a a a a a a a a a a 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 a a a a a a a a a a a a a a a a 5 5 5 5 5 a a a a a a 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 a a a a a a a a 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 a a a a a a a a a a a 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 a a a a a a a a a a a a a a 1 1 1 a a a a a a a a a a a a a a a a a a a a a
    d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a 1 1 a a a a a a a a a a f f a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f f a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f f f a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f f f a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f f f a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f f f f a a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a f f f f f f a a a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a f f f f f f f f a a a a
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a f f f f f f f f f f f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a f f f f f f f f f f f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a f f f f f f f f f f f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a f f f f f f f f f f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a f f f f f f f f f f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a f f f f f f f f f f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a f f f f f f f a a f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a 1 a a a a a a a a 5 5 5 5 5 5 5 5 5 5 5 a a a a a a a a a a a a a a a a a a a a a a a a f f f f f a a a f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 a a a a a a a a a a a a a a a a a a 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 a a a a a a a a a a a a a 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 a a a a a a 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 f f 7 7 7 f f f 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 f 7 7 7 f 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 f 7 7 f 7 7 f 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 f 7 f 7 7 7 f 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 f f 7 7 7 7 f 1 1 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 f f 7 7 7 7 f 1 7 7 a a a a a a a a a a a a a a a a a a e e e e e a a a a a a a e e e e f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 f f 1 1 1 f f 1 f f f 1 1 a a a a a a a a a a a a a a a a a a e e e e e e e e e e e e e e e e f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 f f 1 1 1 f f 1 1 f f 1 1 a a a a a a a a a a a a a a a a a a e e e e e e e e e e e e f e e e f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a e e e e e e e e a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 f f 1 1 1 f f 1 1 f f 1 a a a a a a a a a a a a a a a a a a a e e f f e e f e e e e e f e e e f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 1 1 1 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a e e e e f f f f f f f e f e e e f f
    e e e e e e e e e e e e e e 1 a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a 1 1 a e e e e e e f e e e e f f f f f f f
    e e e e e e e e e e e e e e 1 1 a a a a a a a a a a a a a 1 1 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a 1 a a a a 1 1 1 1 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a 1 1 1 1 a 1 a e e e e e e f e e e e e f e e e e e
    e e e e e e e e e e e e e e a a 1 1 1 1 1 1 1 a a a 1 1 1 a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a 1 1 1 1 1 a a a 1 1 1 a a a a 1 1 1 a a a a a a a a 1 1 1 1 a a a 1 1 1 a a 1 1 1 1 1 1 1 1 1 1 a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a 1 e e e e e e f e e e e e f e e e e e
    e e e e e e e e e e e e e e a a a a a a a a a 1 1 1 1 a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a 1 1 1 1 a a a 1 1 1 1 1 1 1 1 a a a a 1 1 1 1 a a 1 1 a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 a a a a a a a e e f f f f f f f e e e f e e e e e
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a e e e e e e f e e f f f f f f f f f
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a e e e e e e f e e e e e f e e e e e
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a e e e e e e f e e e e f e e e e e e
    e e e e e e e e e e e e e e a a 1 1 1 1 1 1 1 a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a e e f f f f f f f f f f f e e e e e
    e e e e e e e e e e e e e e 1 1 a a a a a a 1 a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a e e e e e e e f e e e e f f f f f f
    e e e e e e e e e e e e e e a a a a a a a a 1 a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a a e e e e e e e f e e e e f e e e e e
    e e e e e e e e e e e e e e a a a a a a a a a 1 a a a a a a a 1 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a a e e e e e f f f f f f f f e e e e e
    e e e e e e e e e e e e e e a a a a a a a a a a 1 1 a a a 1 1 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a 1 1 a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a 1 1 1 1 1 a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a e e f f f f e e f e e e e e f f f f e
    e e e e e e e e e e e e e e a a a a a a a a a a a a 1 1 1 a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a 1 1 a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a 1 a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a e e e e e e e f f f f f f f f f e e e
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a 1 a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a e e e e f f f e f e e e e e f f f e e
    e e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a e e f f e e e e f f e e e e e f e e e
    e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a e e e e e e e e f f e e e e f f e e e
    e e e e e e e e e e e e e a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 a a a a a a a a a a a a a a a a a a a a a 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 a a a a a a a a a a e e e e e e e e f e e e e e e e e e e
"""))

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
mario.set_kind(SpriteKind.player)

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
    goombas.set_kind(SpriteKind.enemy)
    
game.on_update_interval(750, on_update_interval)

def on_button_event_a_pressed():
    fire = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . 5 5 5 5 5 5 . . . . .
        . . . . 5 2 2 2 2 2 2 5 . . . .
        . . . 5 2 2 4 4 4 4 2 5 . . . .
        . . 5 2 2 4 5 5 5 4 2 5 . . . .
        . . . 5 2 2 4 4 4 4 2 5 . . . .
        . . . . 5 2 2 2 2 2 2 5 . . . .
        . . . . . 5 5 5 5 5 5 . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), mario, 50, 0)
controller.player1.on_button_event(ControllerButton.A, ControllerButtonEvent.PRESSED, on_button_event_a_pressed)

def on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

def on_goombas_hit(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    info.change_score_by(1)
    
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_goombas_hit)

