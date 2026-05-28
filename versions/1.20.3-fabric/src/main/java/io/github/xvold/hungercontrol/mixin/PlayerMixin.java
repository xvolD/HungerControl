package io.github.xvold.hungercontrol.mixin;

import io.github.xvold.hungercontrol.Config;
import net.minecraft.world.entity.player.Player;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.ModifyVariable;

@Mixin(Player.class)
public class PlayerMixin {
    @ModifyVariable(method = "causeFoodExhaustion", at = @At("HEAD"), argsOnly = true)
    private float hungercontrol$multiplyExhaustion(float amount) {
        if (!Config.enable) {
            return amount;
        }
        return amount * (float) Config.exhaustionMultiplier;
    }
}
