package io.github.xvold.hungercontrol;

import io.github.xvold.hungercontrol.command.HungerControlCommand;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class HungerControlMod implements ModInitializer {
    public static final String MODID = "hungercontrol";
    public static final Logger LOGGER = LoggerFactory.getLogger(MODID);

    @Override
    public void onInitialize() {
        Config.load();
        LOGGER.info("Hunger Control initialized. Multiplier: {}", Config.exhaustionMultiplier);
        CommandRegistrationCallback.EVENT.register((dispatcher, registryAccess, environment) -> {
            HungerControlCommand.register(dispatcher);
        });
    }
}
