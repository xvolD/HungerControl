package io.github.xvold.hungercontrol.mixin;

import io.github.xvold.hungercontrol.Config;
import net.minecraft.world.food.FoodData;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(FoodData.class)
public class FoodDataMixin {
    @Shadow
    private float exhaustionLevel;

    @Inject(method = "addExhaustion", at = @At("HEAD"), cancellable = true)
    private void hungercontrol$onAddExhaustion(float amount, CallbackInfo ci) {
        if (Config.enable) {
            amount = amount * (float) Config.exhaustionMultiplier;
        }
        this.exhaustionLevel = Math.min(this.exhaustionLevel + amount, 40.0f);
        ci.cancel();
    }
}
