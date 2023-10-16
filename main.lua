function love.load()
    anim8 = require("libraries/anim8.lua")

    player = {}
    player.x = 400
    player.y = 200
    player.speed = 3
    player.spriteSheet = love.graphics.newImage("assets/sprites/player-sheet.png")
    player.grid = anim8.newGrid(12, 18, player.spriteSheet:getWidth(), player.spriteSheet:getHeight())

    player.animations = {}
    player.animations.down = anim8.newAnimation(player.grid("1-4", 1), 0.2)

    background = love.graphics.newImage("assets/world/test.png")
end

function love.update(dt)
    if love.keyboard.isDown("right") then
        player.x = player.x + player.speed
    end
    if love.keyboard.isDown("left") then
        player.x = player.x - player.speed
    end
    if love.keyboard.isDown("up") then
        player.y = player.y - player.speed
    end
    if love.keyboard.isDown("down") then
        player.y = player.y + player.speed
    end

    player.animations.down:update(dt)
end

function love.draw()
    love.graphics.draw(background, 0, 0)
    player.animations.down:draw(player.spriteSheet, player.x, player.y, nil, 10)
end