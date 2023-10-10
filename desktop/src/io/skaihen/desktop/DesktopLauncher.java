package io.skaihen.desktop;

import org.mini2Dx.desktop.DesktopMini2DxConfig;

import com.badlogic.gdx.backends.lwjgl.DesktopMini2DxGame;

import io.skaihen.Garoa;

public class DesktopLauncher {
	public static void main (String[] arg) {
		DesktopMini2DxConfig config = new DesktopMini2DxConfig(Garoa.GAME_IDENTIFIER);
		config.vSyncEnabled = true;
		new DesktopMini2DxGame(new Garoa(), config);
	}
}
