package io.github.xvold.hungercontrol.command;

import com.mojang.brigadier.CommandDispatcher;
import net.minecraft.commands.CommandSourceStack;
import net.minecraft.commands.Commands;
import net.minecraft.network.chat.Component;
import io.github.xvold.hungercontrol.Config;

public class HungerControlCommand {
    public static void register(CommandDispatcher<CommandSourceStack> dispatcher) {
        dispatcher.register(Commands.literal("hungercontrol")
            .requires(source -> source.hasPermission(2))
            .then(Commands.literal("info")
                .executes(ctx -> {
                    ctx.getSource().sendSuccess(() -> Component.literal(
                        String.format("Hunger Control: enabled=%s, exhaustionMultiplier=%.2f", Config.enable, Config.exhaustionMultiplier)
                    ), false);
                    return 1;
                })
            )
            .then(Commands.literal("reload")
                .executes(ctx -> {
                    Config.reloadFromFile();
                    ctx.getSource().sendSuccess(() -> Component.literal(
                        String.format("Hunger Control config reloaded. Current multiplier: %.2f", Config.exhaustionMultiplier)
                    ), true);
                    return 1;
                })
            )
        );
    }
}
