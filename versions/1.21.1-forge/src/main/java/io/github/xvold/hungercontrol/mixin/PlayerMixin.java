package io.github.xvold.hungercontrol.mixin;

import io.github.xvold.hungercontrol.Config;
import net.minecraft.world.entity.player.Player;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.ModifyArg;

@Mixin(Player.class)
public class PlayerMixin {
    @ModifyArg(
        method = "causeFoodExhaustion",
        at = @At(
            value = "INVOKE",
            target = "Lnet/minecraft/world/food/FoodData;addExhaustion(F)V"
        ),
        index = 0
    )
    private float hungercontrol$multiplyExhaustion(float amount) {
        if (!Config.enable) {
            return amount;
        }
        return amount * (float) Config.exhaustionMultiplier;
    }
}
