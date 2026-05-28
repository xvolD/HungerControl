package io.github.xvold.hungercontrol;

import com.mojang.logging.LogUtils;
import io.github.xvold.hungercontrol.command.HungerControlCommand;
import net.neoforged.neoforge.common.NeoForge;
import net.neoforged.neoforge.event.RegisterCommandsEvent;
import net.neoforged.neoforge.event.server.ServerStartingEvent;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.FMLJavaModLoadingContext;
import net.neoforged.fml.ModLoadingContext;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.config.ModConfig;
import net.neoforged.fml.event.lifecycle.FMLCommonSetupEvent;
import net.neoforged.fml.ModContainer;
import org.slf4j.Logger;

@Mod(HungerControlMod.MODID)
public class HungerControlMod {
    public static final String MODID = "hungercontrol";
    private static final Logger LOGGER = LogUtils.getLogger();

    public HungerControlMod() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();
        ModContainer modContainer = ModLoadingContext.get().getActiveContainer();
        modEventBus.addListener(this::commonSetup);
        modContainer.registerConfig(ModConfig.Type.COMMON, Config.SPEC);
        NeoForge.EVENT_BUS.register(this);
        NeoForge.EVENT_BUS.addListener(this::onRegisterCommands);
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        LOGGER.info("Hunger Control initialized. Multiplier: {}", Config.exhaustionMultiplier);
    }

    private void onRegisterCommands(final RegisterCommandsEvent event) {
        HungerControlCommand.register(event.getDispatcher());
    }

    @SubscribeEvent
    public void onServerStarting(ServerStartingEvent event) {
        LOGGER.info("Hunger Control active on server.");
    }
}
