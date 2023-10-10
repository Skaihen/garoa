package io.skaihen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.backends.lwjgl3.Lwjgl3Application;
import com.badlogic.gdx.backends.lwjgl3.Lwjgl3ApplicationConfiguration;
import com.badlogic.gdx.backends.lwjgl3.Lwjgl3WindowAdapter;

// Please note that on macOS your application needs to be started with the -XstartOnFirstThread JVM argument
public class DesktopLauncher {
	public static void main(String[] arg) {
		Lwjgl3ApplicationConfiguration config = new Lwjgl3ApplicationConfiguration();

		config.setTitle("Garoa");

		config.setWindowedMode(800, 480);

		config.setWindowListener(new Lwjgl3WindowAdapter() {
			@Override
			public void focusLost() {
				Gdx.graphics.setForegroundFPS(10);
			}

			@Override
			public void focusGained() {
				Gdx.graphics.setForegroundFPS(60);
			}
		});
		config.useVsync(true);

		new Lwjgl3Application(new Garoa(), config);
	}
}
