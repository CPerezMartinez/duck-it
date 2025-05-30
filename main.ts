namespace SpriteKind {
    export const otro = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.spray, 100)
    sprites.destroy(bala)
    info.changeScoreBy(-3)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite4, otherSprite4) {
    sprites.destroy(otherSprite4, effects.spray, 100)
    sprites.destroy(bala)
    info.changeScoreBy(5)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite5, otherSprite5) {
    sprites.destroy(otherSprite5, effects.spray, 100)
    sprites.destroy(bala)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite6, otherSprite6) {
    sprites.destroy(otherSprite6, effects.spray, 100)
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.otro, function (sprite2, otherSprite2) {
    sprites.destroy(otherSprite2, effects.spray, 100)
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.otro, function (sprite3, otherSprite3) {
    sprites.destroy(otherSprite3, effects.spray, 100)
    sprites.destroy(bala)
    info.changeScoreBy(2)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    bala = sprites.createProjectileFromSprite(assets.image`ajo`, Avion, 200, 0)
})
info.onCountdownEnd(function () {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.confetti)
})
let Comida: Sprite = null
let Enemigo: Sprite = null
let bala: Sprite = null
let Avion: Sprite = null
scene.setBackgroundImage(assets.image`fondo`)
Avion = sprites.create(assets.image`pato`, SpriteKind.Player)
Avion.setPosition(25, 56)
controller.player1.moveSprite(Avion)
game.splash("Pulsa per començar")
info.startCountdown(15)
game.onUpdateInterval(500, function () {
    Enemigo = sprites.create(assets.image`cuervo`, SpriteKind.Enemy)
    Enemigo.setPosition(scene.screenWidth(), randint(0, 100))
    Enemigo.vx = -75
})
game.onUpdateInterval(500, function () {
    Enemigo = sprites.create(assets.image`el otro de 2 puntos`, SpriteKind.otro)
    Enemigo.setPosition(scene.screenWidth(), randint(0, 100))
    Enemigo.vx = -75
})
game.onUpdateInterval(500, function () {
    Comida = sprites.create(assets.image`comida`, SpriteKind.Food)
    Comida.setPosition(scene.screenWidth(), randint(0, 100))
    Comida.vx = -75
})
