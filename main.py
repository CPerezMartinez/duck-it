@namespace
class SpriteKind:
    otro = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite, effects.spray, 100)
    sprites.destroy(bala)
    info.change_score_by(-3)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2, effects.spray, 100)
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.otro, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    sprites.destroy(otherSprite3, effects.spray, 100)
    sprites.destroy(bala)
    info.change_score_by(2)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.otro, on_on_overlap3)

def on_a_pressed():
    global bala
    bala = sprites.create_projectile_from_sprite(assets.image("""
        ajo
        """), Avion, 200, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
info.on_countdown_end(on_countdown_end)

def on_on_overlap4(sprite4, otherSprite4):
    sprites.destroy(otherSprite4, effects.spray, 100)
    sprites.destroy(bala)
    info.change_score_by(5)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    sprites.destroy(otherSprite5, effects.spray, 100)
    sprites.destroy(bala)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap5)

def on_on_overlap6(sprite6, otherSprite6):
    sprites.destroy(otherSprite6, effects.spray, 100)
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap6)

Comida: Sprite = None
Enemigo: Sprite = None
bala: Sprite = None
Avion: Sprite = None
scene.set_background_image(assets.image("""
    fondo
    """))
Avion = sprites.create(assets.image("""
    pato
    """), SpriteKind.player)
Avion.set_position(25, 56)
controller.player1.move_sprite(Avion)
game.splash("Pulsa per començar")
info.start_countdown(40)

def on_update_interval():
    global Enemigo
    Enemigo = sprites.create(assets.image("""
        cuervo
        """), SpriteKind.enemy)
    Enemigo.set_position(scene.screen_width(), randint(0, 100))
    Enemigo.vx = -75
game.on_update_interval(500, on_update_interval)

def on_update_interval2():
    global Enemigo
    Enemigo = sprites.create(assets.image("""
            el otro de 2 puntos
            """),
        SpriteKind.otro)
    Enemigo.set_position(scene.screen_width(), randint(0, 100))
    Enemigo.vx = -75
game.on_update_interval(500, on_update_interval2)

def on_update_interval3():
    global Comida
    Comida = sprites.create(assets.image("""
        comida
        """), SpriteKind.food)
    Comida.set_position(scene.screen_width(), randint(0, 100))
    Comida.vx = -75
game.on_update_interval(500, on_update_interval3)
