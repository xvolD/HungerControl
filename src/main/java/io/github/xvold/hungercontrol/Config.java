package io.github.xvold.hungercontrol;

import com.electronwill.nightconfig.core.file.CommentedFileConfig;
import net.minecraftforge.common.ForgeConfigSpec;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.config.ModConfigEvent;
import net.minecraftforge.fml.loading.FMLPaths;

@Mod.EventBusSubscriber(modid = HungerControlMod.MODID, bus = Mod.EventBusSubscriber.Bus.MOD)
public class Config {
    private static final ForgeConfigSpec.Builder BUILDER = new ForgeConfigSpec.Builder();

    public static final ForgeConfigSpec.BooleanValue ENABLE = BUILDER
            .comment("Whether the hunger exhaustion multiplier is applied.")
            .define("enable", true);

    public static final ForgeConfigSpec.DoubleValue EXHAUSTION_MULTIPLIER = BUILDER
            .comment("Global multiplier for all hunger exhaustion gain.",
                     "1.0 = vanilla speed. 0.5 = half speed. 0.2 = 5x slower.")
            .defineInRange("exhaustionMultiplier", 1.0, 0.0, 100.0);

    public static final ForgeConfigSpec.BooleanValue AFFECT_PLAYERS_ONLY = BUILDER
            .comment("If true, only player exhaustion is affected.",
                     "Currently always player-only; reserved for future mob support.")
            .define("affectPlayersOnly", true);

    public static final ForgeConfigSpec.BooleanValue DEBUG_LOG = BUILDER
            .comment("Log exhaustion changes to the console for debugging.")
            .define("debugLog", false);

    public static final ForgeConfigSpec SPEC = BUILDER.build();

    public static boolean enable;
    public static double exhaustionMultiplier;
    public static boolean affectPlayersOnly;
    public static boolean debugLog;

    @SubscribeEvent
    static void onLoad(final ModConfigEvent event) {
        enable = ENABLE.get();
        exhaustionMultiplier = EXHAUSTION_MULTIPLIER.get();
        affectPlayersOnly = AFFECT_PLAYERS_ONLY.get();
        debugLog = DEBUG_LOG.get();
    }

    public static void reloadFromFile() {
        java.nio.file.Path configPath = FMLPaths.CONFIGDIR.get().resolve("hungercontrol-common.toml");
        CommentedFileConfig cfg = CommentedFileConfig.of(configPath);
        cfg.load();
        SPEC.acceptConfig(cfg);
        enable = ENABLE.get();
        exhaustionMultiplier = EXHAUSTION_MULTIPLIER.get();
        affectPlayersOnly = AFFECT_PLAYERS_ONLY.get();
        debugLog = DEBUG_LOG.get();
    }
}
