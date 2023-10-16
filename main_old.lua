function love.load()
    bump = require("libraries/bump")
    world = bump.newWorld()

    camera = require("libraries/camera")
    cam = camera()

    anim8 = require("libraries/anim8")
    love.graphics.setDefaultFilter("nearest", "nearest")

    sti = require("libraries/sti")
    gameMap = sti("assets/maps/testMap.lua", { "bump" })
    gameMap:bump_init(world)

    player = {}
    player.x = 400
    player.y = 350
    player.speed = 3
    player.spriteSheet = love.graphics.newImage("assets/sprites/player-sheet.png")
    player.grid = anim8.newGrid(12, 18, player.spriteSheet:getWidth(), player.spriteSheet:getHeight())

    world:add(player, player.x, player.y, 12, 18)

    player.animations = {}
    player.animations.down = anim8.newAnimation(player.grid("1-4", 1), 0.2)
    player.animations.left = anim8.newAnimation(player.grid("1-4", 2), 0.2)
    player.animations.right = anim8.newAnimation(player.grid("1-4", 3), 0.2)
    player.animations.up = anim8.newAnimation(player.grid("1-4", 4), 0.2)

    player.anim = player.animations.down
end

function love.update(dt)
    local isMoving = false

    local goalX, goalY = player.x, player.y

    if love.keyboard.isDown("s") then
        goalY = player.y + player.speed
        player.anim = player.animations.down
        isMoving = true
    end
    if love.keyboard.isDown("a") then
        goalX = player.x - player.speed
        player.anim = player.animations.left
        isMoving = true
    end
    if love.keyboard.isDown("d") then
        goalX = player.x + player.speed
        player.anim = player.animations.right
        isMoving = true
    end
    if love.keyboard.isDown("w") then
        goalY = player.y - player.speed
        player.anim = player.animations.up
        isMoving = true
    end

    local actualX, actualY = world:move(player, goalX, goalY, slide)
    player.x, player.y = actualX, actualY

    if isMoving == false then
        player.anim:gotoFrame(2)
    end

    player.anim:update(dt)

    cam:lookAt(player.x, player.y)

    local w = love.graphics.getWidth()
    local h = love.graphics.getHeight()

    if cam.x < w / 2 then
        cam.x = w / 2
    end

    if cam.y < h / 2 then
        cam.y = h / 2
    end

    local mapW = gameMap.width * gameMap.tilewidth
    local mapH = gameMap.height * gameMap.tileheight

    if cam.x > (mapW - w / 2) then
        cam.x = (mapW - w / 2)
    end
    if cam.y > (mapH - h / 2) then
        cam.y = (mapH - h / 2)
    end

end

function love.draw()
    cam:attach()
    gameMap:drawLayer(gameMap.layers["Ground"])
    gameMap:drawLayer(gameMap.layers["Trees"])
    player.anim:draw(player.spriteSheet, player.x, player.y, nil, 4, nil, 6, 9)
    cam:detach()
end