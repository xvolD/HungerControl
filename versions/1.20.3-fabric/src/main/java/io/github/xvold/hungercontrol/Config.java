package io.github.xvold.hungercontrol;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import net.fabricmc.loader.api.FabricLoader;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.nio.file.Files;
import java.nio.file.Path;

public class Config {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final Path CONFIG_PATH = FabricLoader.getInstance().getConfigDir().resolve("hungercontrol.json");

    public static boolean enable = true;
    public static double exhaustionMultiplier = 1.0;
    public static boolean affectPlayersOnly = true;
    public static boolean debugLog = false;

    public static void load() {
        if (!Files.exists(CONFIG_PATH)) {
            save();
            return;
        }
        try (Reader reader = Files.newBufferedReader(CONFIG_PATH)) {
            ConfigData data = GSON.fromJson(reader, ConfigData.class);
            if (data != null) {
                enable = data.enable;
                exhaustionMultiplier = data.exhaustionMultiplier;
                affectPlayersOnly = data.affectPlayersOnly;
                debugLog = data.debugLog;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void save() {
        ConfigData data = new ConfigData();
        data.enable = enable;
        data.exhaustionMultiplier = exhaustionMultiplier;
        data.affectPlayersOnly = affectPlayersOnly;
        data.debugLog = debugLog;
        try (Writer writer = Files.newBufferedWriter(CONFIG_PATH)) {
            GSON.toJson(data, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void reloadFromFile() {
        load();
    }

    private static class ConfigData {
        boolean enable = true;
        double exhaustionMultiplier = 1.0;
        boolean affectPlayersOnly = true;
        boolean debugLog = false;
    }
}
