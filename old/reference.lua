local function drawPlayer()
    drawBox(player, 0, 1, 0)
end

-- Block functions

local blocks = {}

local function addBlock(x, y, w, h)
    local block = { x = x, y = y, w = w, h = h }
    blocks[#blocks + 1] = block
    world:add(block, x, y, w, h)
end

local function drawBlocks()
    for _, block in ipairs(blocks) do
        drawBox(block, 1, 0, 0)
    end
end




-- Main LÖVE functions

function love.load()
    world:add(player, player.x, player.y, player.w, player.h)

    addBlock(0, 0, 800, 32)
    addBlock(0, 32, 32, 600 - 32 * 2)
    addBlock(800 - 32, 32, 32, 600 - 32 * 2)
    addBlock(0, 600 - 32, 800, 32)

    for i = 1, 30 do
        addBlock(math.random(100, 600),
                math.random(100, 400),
                math.random(10, 100),
                math.random(10, 100)
        )
    end
end

function love.update(dt)
    cols_len = 0
    updatePlayer(dt)
end

function love.draw()
    gameMap:drawLayer(gameMap.layers["Ground"])
    gameMap:drawLayer(gameMap.layers["Trees"])
    drawBlocks()
    drawPlayer()
    if shouldDrawDebug then
        drawDebug()
        drawConsole()
    end
    drawMessage()
end

-- Non-player keypresses
function love.keypressed(k)
    if k == "escape" then
        love.event.quit()
    end
    if k == "tab" then
        shouldDrawDebug = not shouldDrawDebug
    end
    if k == "delete" then
        collectgarbage("collect")
    end
end