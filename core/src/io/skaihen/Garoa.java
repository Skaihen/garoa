package io.skaihen;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.utils.ScreenUtils;

public class Garoa extends ApplicationAdapter {
	private SpriteBatch batch;
	private Texture img;
	private int widthScreen, heightScreen;
	private OrthographicCamera orthographicCamera;
	
	@Override
	public void create () {
		widthScreen = Gdx.graphics.getWidth();
		heightScreen = Gdx.graphics.getHeight();
		orthographicCamera = new OrthographicCamera(widthScreen, heightScreen);
		orthographicCamera.setToOrtho(false, widthScreen, heightScreen);

		batch = new SpriteBatch();
		img = new Texture("plep.jpg");
	}

	@Override
	public void render () {
		ScreenUtils.clear(0, 0, 0, 1);

		orthographicCamera.update();

		batch.setProjectionMatrix(orthographicCamera.combined);
		batch.begin();
		batch.draw(img, 0, 0);
		batch.end();
	}
	
	@Override
	public void dispose () {
		batch.dispose();
		img.dispose();
	}
}
