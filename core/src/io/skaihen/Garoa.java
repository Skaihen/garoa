package io.skaihen;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input.Keys;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.utils.ScreenUtils;

import java.awt.*;

public class Garoa extends ApplicationAdapter {
    private int widthScreen, heightScreen;
    private OrthographicCamera camera;
    private Texture plepImg;
    private SpriteBatch batch;
    private Rectangle plep;

    @Override
    public void create() {
        widthScreen = Gdx.graphics.getWidth();
        heightScreen = Gdx.graphics.getHeight();
        camera = new OrthographicCamera(widthScreen, heightScreen);
        camera.setToOrtho(false, widthScreen, heightScreen);

        plepImg = new Texture("plep.jpg");
        batch = new SpriteBatch();

        plep = new Rectangle();
        plep.x = widthScreen / 2 - 64 / 2;
        plep.y = 20;
        plep.width = 64;
        plep.height = 64;
    }

    @Override
    public void render() {
        ScreenUtils.clear(1, 1, 1, 1);

        camera.update();

        batch.setProjectionMatrix(camera.combined);
        batch.begin();
        batch.draw(plepImg, plep.x, plep.y);
        batch.end();

        if (Gdx.input.isTouched()) {
            Vector3 touchPos = new Vector3();
            touchPos.set(Gdx.input.getX(), Gdx.input.getY(), 0);
            camera.unproject(touchPos);
            plep.x = (int) touchPos.x - 64 / 2;
        }
        if (Gdx.input.isKeyPressed(Keys.A)) plep.x -= (int) (200 * Gdx.graphics.getDeltaTime());
        if (Gdx.input.isKeyPressed(Keys.D)) plep.x += (int) (200 * Gdx.graphics.getDeltaTime());

        if (plep.x < 0) plep.x = 0;
        if (plep.x > widthScreen - 64) plep.x = widthScreen - 64;
    }

    @Override
    public void dispose() {
        batch.dispose();
        plepImg.dispose();
    }
}
