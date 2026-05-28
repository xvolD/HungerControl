import os, shutil, json

BASE = os.path.dirname(os.path.abspath(__file__))

versions = [
    {
        "name": "1.20.2-forge",
        "mc": "1.20.2",
        "forge": "48.1.0",
        "loader_range": "[48,)",
        "forge_range": "[48,)",
        "mc_range": "[1.20.2,1.21)",
        "java": 17,
        "pack_format": 18,
        "loader": "forge",
        "fg_plugin_range": "[6.0,6.2)",
    },
    {
        "name": "1.20.3-forge",
        "mc": "1.20.3",
        "forge": "49.0.2",
        "loader_range": "[49,)",
        "forge_range": "[49,)",
        "mc_range": "[1.20.3,1.21)",
        "java": 17,
        "pack_format": 22,
        "loader": "forge",
        "fg_plugin_range": "[6.0,6.2)",
    },
    {
        "name": "1.20.4-forge",
        "mc": "1.20.4",
        "forge": "49.2.7",
        "loader_range": "[49,)",
        "forge_range": "[49,)",
        "mc_range": "[1.20.4,1.21)",
        "java": 17,
        "pack_format": 22,
        "loader": "forge",
        "fg_plugin_range": "[6.0,6.2)",
    },
    {
        "name": "1.20.6-forge",
        "mc": "1.20.6",
        "forge": "50.2.8",
        "loader_range": "[50,)",
        "forge_range": "[50,)",
        "mc_range": "[1.20.6,1.21)",
        "java": 17,
        "pack_format": 32,
        "loader": "forge",
        "fg_plugin_range": "[6.0,6.2)",
    },
    {
        "name": "1.21-forge",
        "mc": "1.21",
        "forge": "51.0.33",
        "loader_range": "[51,)",
        "forge_range": "[51,)",
        "mc_range": "[1.21,1.22)",
        "java": 21,
        "pack_format": 34,
        "loader": "forge",
        "fg_plugin_range": "[6.0,6.3)",
    },
    {
        "name": "1.21-neoforge",
        "mc": "1.21",
        "neo": "21.0.167",
        "loader_range": "[1,)",
        "mc_range": "[1.21,1.22)",
        "java": 21,
        "pack_format": 34,
        "loader": "neoforge",
    },
    {
        "name": "1.21.1-forge",
        "mc": "1.21.1",
        "forge": "52.1.14",
        "loader_range": "[52,)",
        "forge_range": "[52,)",
        "mc_range": "[1.21.1,1.22)",
        "java": 21,
        "pack_format": 34,
        "loader": "forge",
        "fg_plugin_range": "[6.0,6.3)",
    },
    {
        "name": "1.21.1-neoforge",
        "mc": "1.21.1",
        "neo": "21.1.232",
        "loader_range": "[1,)",
        "mc_range": "[1.21.1,1.22)",
        "java": 21,
        "pack_format": 34,
        "loader": "neoforge",
    },
]

MOD_ID = "hungercontrol"
MOD_NAME = "Hunger Control"
MOD_LICENSE = "MIT"
MOD_VERSION = "1.0.0"
MOD_GROUP = "io.github.xvold.hungercontrol"
MOD_AUTHORS = "xvolD"
MOD_DESC = "A configurable hunger exhaustion multiplier for modpack developers.\\nAllows fine-tuning of food drain speed via a simple config file."

def mkdirs(path):
    os.makedirs(path, exist_ok=True)

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Forge build.gradle template
FORGE_BUILD_GRADLE = '''plugins {
    id 'eclipse'
    id 'idea'
    id 'maven-publish'
    id 'net.minecraftforge.gradle' version '%(fg_range)s'
    id 'org.spongepowered.mixin' version '0.7.38'
}

version = mod_version
group = mod_group_id

base {
    archivesName = mod_id
}

java.toolchain.languageVersion = JavaLanguageVersion.of(%(java)d)

minecraft {
    mappings channel: mapping_channel, version: mapping_version
    copyIdeResources = true
    runs {
        configureEach {
            workingDirectory project.file('run')
            property 'forge.logging.markers', 'REGISTRIES'
            property 'forge.logging.console.level', 'debug'
            mods {
                "${mod_id}" {
                    source sourceSets.main
                }
            }
        }
        client { property 'forge.enabledGameTestNamespaces', mod_id }
        server { property 'forge.enabledGameTestNamespaces', mod_id; args '--nogui' }
        gameTestServer { property 'forge.enabledGameTestNamespaces', mod_id }
        data {
            workingDirectory project.file('run-data')
            args '--mod', mod_id, '--all', '--output', file('src/generated/resources/'), '--existing', file('src/main/resources/')
        }
    }
}

mixin {
    add sourceSets.main, 'hungercontrol.refmap.json'
    config 'hungercontrol.mixins.json'
}

sourceSets.main.resources { srcDir 'src/generated/resources' }

repositories {
    maven { url 'https://repo.spongepowered.org/repository/maven-public/' }
}

dependencies {
    minecraft "net.minecraftforge:forge:${minecraft_version}-${forge_version}"
    annotationProcessor 'org.spongepowered:mixin:0.8.5:processor'
}

tasks.named('processResources', ProcessResources).configure {
    var replaceProperties = [
            minecraft_version: minecraft_version, minecraft_version_range: minecraft_version_range,
            forge_version: forge_version, forge_version_range: forge_version_range,
            loader_version_range: loader_version_range,
            mod_id: mod_id, mod_name: mod_name, mod_license: mod_license, mod_version: mod_version,
            mod_authors: mod_authors, mod_description: mod_description,
    ]
    inputs.properties replaceProperties
    filesMatching(['META-INF/mods.toml', 'pack.mcmeta']) {
        expand replaceProperties + [project: project]
    }
}

tasks.named('jar', Jar).configure {
    manifest {
        attributes([
                'Specification-Title'     : mod_id,
                'Specification-Vendor'    : mod_authors,
                'Specification-Version'   : '1',
                'Implementation-Title'    : project.name,
                'Implementation-Version'  : project.jar.archiveVersion,
                'Implementation-Vendor'   : mod_authors,
                'Implementation-Timestamp': new Date().format("yyyy-MM-dd'T'HH:mm:ssZ")
        ])
    }
    finalizedBy 'reobfJar'
}

publishing {
    publications { register('mavenJava', MavenPublication) { artifact jar } }
    repositories { maven { url "file://${project.projectDir}/mcmodsrepo" } }
}

tasks.withType(JavaCompile).configureEach {
    options.encoding = 'UTF-8'
}
'''

# NeoForge build.gradle template
NEOFORGE_BUILD_GRADLE = '''plugins {
    id 'java-library'
    id 'eclipse'
    id 'idea'
    id 'maven-publish'
    id 'net.neoforged.gradle.userdev' version '7.1.36'
    id 'org.spongepowered.mixin' version '0.7.38'
}

version = mod_version
group = mod_group_id

base {
    archivesName = mod_id
}

java.toolchain.languageVersion = JavaLanguageVersion.of(%(java)d)

minecraft {
    version = "${minecraft_version}-${neo_version}"
    mappings channel: mapping_channel, version: mapping_version
    copyIdeResources = true
    runs {
        configureEach {
            workingDirectory project.file('run')
            systemProperty 'neoforge.enabledGameTestNamespaces', mod_id
            modSource project.sourceSets.main
        }
        client { }
        server { programArgument '--nogui' }
        gameTestServer { }
        data {
            workingDirectory project.file('run-data')
            programArguments.addAll '--mod', mod_id, '--all', '--output', file('src/generated/resources/').absolutePath, '--existing', file('src/main/resources/').absolutePath
        }
    }
}

mixin {
    add sourceSets.main, 'hungercontrol.refmap.json'
    config 'hungercontrol.mixins.json'
}

sourceSets.main.resources { srcDir 'src/generated/resources' }

repositories {
    maven { url 'https://repo.spongepowered.org/repository/maven-public/' }
}

dependencies {
    implementation "net.neoforged:neoforge:${neo_version}"
    annotationProcessor 'org.spongepowered:mixin:0.8.5:processor'
}

tasks.named('processResources', ProcessResources).configure {
    var replaceProperties = [
            minecraft_version: minecraft_version, minecraft_version_range: minecraft_version_range,
            neo_version: neo_version,
            loader_version_range: loader_version_range,
            mod_id: mod_id, mod_name: mod_name, mod_license: mod_license, mod_version: mod_version,
            mod_authors: mod_authors, mod_description: mod_description,
    ]
    inputs.properties replaceProperties
    filesMatching(['META-INF/neoforge.mods.toml', 'pack.mcmeta']) {
        expand replaceProperties + [project: project]
    }
}

tasks.named('jar', Jar).configure {
    manifest {
        attributes([
                'Specification-Title'     : mod_id,
                'Specification-Vendor'    : mod_authors,
                'Specification-Version'   : '1',
                'Implementation-Title'    : project.name,
                'Implementation-Version'  : project.jar.archiveVersion,
                'Implementation-Vendor'   : mod_authors,
                'Implementation-Timestamp': new Date().format("yyyy-MM-dd'T'HH:mm:ssZ")
        ])
    }
    finalizedBy 'reobfJar'
}

publishing {
    publications { register('mavenJava', MavenPublication) { artifact jar } }
    repositories { maven { url "file://${project.projectDir}/mcmodsrepo" } }
}

tasks.withType(JavaCompile).configureEach {
    options.encoding = 'UTF-8'
}
'''

# settings.gradle for Forge
FORGE_SETTINGS = '''pluginManagement {
    repositories {
        gradlePluginPortal()
        maven { name = 'MinecraftForge'; url = 'https://maven.minecraftforge.net/' }
        maven { name = 'SpongePowered'; url = 'https://repo.spongepowered.org/repository/maven-public/' }
    }
}
plugins {
    id 'org.gradle.toolchains.foojay-resolver-convention' version '0.5.0'
}
'''

# settings.gradle for NeoForge
NEOFORGE_SETTINGS = '''pluginManagement {
    repositories {
        gradlePluginPortal()
        maven { name = 'NeoForged'; url = 'https://maven.neoforged.net/releases/' }
        maven { name = 'SpongePowered'; url = 'https://repo.spongepowered.org/repository/maven-public/' }
    }
}
plugins {
    id 'org.gradle.toolchains.foojay-resolver-convention' version '0.5.0'
}
'''

# Java source: Forge (identical to root)
FORGE_HUNGER_MOD = open(os.path.join(BASE, "src/main/java/io/github/xvold/hungercontrol/HungerControlMod.java")).read()
FORGE_CONFIG = open(os.path.join(BASE, "src/main/java/io/github/xvold/hungercontrol/Config.java")).read()
FORGE_COMMAND = open(os.path.join(BASE, "src/main/java/io/github/xvold/hungercontrol/command/HungerControlCommand.java")).read()
FORGE_MIXIN = open(os.path.join(BASE, "src/main/java/io/github/xvold/hungercontrol/mixin/PlayerMixin.java")).read()

# NeoForge adapted sources
NEOFORGE_HUNGER_MOD = FORGE_HUNGER_MOD.replace(
    'import net.minecraftforge.common.MinecraftForge;',
    'import net.neoforged.neoforge.common.NeoForge;'
).replace(
    'import net.minecraftforge.event.RegisterCommandsEvent;',
    'import net.neoforged.neoforge.event.RegisterCommandsEvent;'
).replace(
    'import net.minecraftforge.event.server.ServerStartingEvent;',
    'import net.neoforged.neoforge.event.server.ServerStartingEvent;'
).replace(
    'import net.minecraftforge.eventbus.api.IEventBus;',
    'import net.neoforged.bus.api.IEventBus;'
).replace(
    'import net.minecraftforge.eventbus.api.SubscribeEvent;',
    'import net.neoforged.bus.api.SubscribeEvent;'
).replace(
    'import net.minecraftforge.fml.ModLoadingContext;',
    'import net.neoforged.fml.ModLoadingContext;'
).replace(
    'import net.minecraftforge.fml.common.Mod;',
    'import net.neoforged.fml.common.Mod;'
).replace(
    'import net.minecraftforge.fml.config.ModConfig;',
    'import net.neoforged.fml.config.ModConfig;'
).replace(
    'import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;',
    'import net.neoforged.fml.event.lifecycle.FMLCommonSetupEvent;'
).replace(
    'import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;',
    'import net.neoforged.fml.FMLJavaModLoadingContext;\nimport net.neoforged.fml.ModContainer;'
).replace(
    'IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();',
    'IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();\n        ModContainer modContainer = ModLoadingContext.get().getActiveContainer();'
).replace(
    'ModLoadingContext.get().registerConfig(ModConfig.Type.COMMON, Config.SPEC);',
    'modContainer.registerConfig(ModConfig.Type.COMMON, Config.SPEC);'
).replace(
    'MinecraftForge.EVENT_BUS.register(this);',
    'NeoForge.EVENT_BUS.register(this);'
).replace(
    'MinecraftForge.EVENT_BUS.addListener(this::onRegisterCommands);',
    'NeoForge.EVENT_BUS.addListener(this::onRegisterCommands);'
)

NEOFORGE_CONFIG = FORGE_CONFIG.replace(
    'import net.minecraftforge.common.ForgeConfigSpec;',
    'import net.neoforged.neoforge.common.ModConfigSpec;'
).replace(
    'private static final ForgeConfigSpec.Builder BUILDER = new ForgeConfigSpec.Builder();',
    'private static final ModConfigSpec.Builder BUILDER = new ModConfigSpec.Builder();'
).replace(
    'public static final ForgeConfigSpec.BooleanValue ENABLE = BUILDER',
    'public static final ModConfigSpec.BooleanValue ENABLE = BUILDER'
).replace(
    'public static final ForgeConfigSpec.DoubleValue EXHAUSTION_MULTIPLIER = BUILDER',
    'public static final ModConfigSpec.DoubleValue EXHAUSTION_MULTIPLIER = BUILDER'
).replace(
    'public static final ForgeConfigSpec.BooleanValue AFFECT_PLAYERS_ONLY = BUILDER',
    'public static final ModConfigSpec.BooleanValue AFFECT_PLAYERS_ONLY = BUILDER'
).replace(
    'public static final ForgeConfigSpec.BooleanValue DEBUG_LOG = BUILDER',
    'public static final ModConfigSpec.BooleanValue DEBUG_LOG = BUILDER'
).replace(
    'public static final ForgeConfigSpec SPEC = BUILDER.build();',
    'public static final ModConfigSpec SPEC = BUILDER.build();'
).replace(
    'import net.minecraftforge.eventbus.api.SubscribeEvent;',
    'import net.neoforged.bus.api.SubscribeEvent;'
).replace(
    'import net.minecraftforge.fml.common.Mod;',
    'import net.neoforged.fml.common.Mod;'
).replace(
    'import net.minecraftforge.fml.event.config.ModConfigEvent;',
    'import net.neoforged.fml.event.config.ModConfigEvent;'
).replace(
    'import net.minecraftforge.fml.loading.FMLPaths;',
    'import net.neoforged.fml.loading.FMLPaths;'
)

# Command and mixin are loader-agnostic (only touch Mojang/Brigadier classes)
NEOFORGE_COMMAND = FORGE_COMMAND
NEOFORGE_MIXIN = FORGE_MIXIN

for v in versions:
    root = os.path.join(BASE, "versions", v["name"])
    mkdirs(root)
    java_dir = os.path.join(root, "src/main/java/io/github/xvold/hungercontrol")
    mixin_dir = os.path.join(java_dir, "mixin")
    cmd_dir = os.path.join(java_dir, "command")
    res_dir = os.path.join(root, "src/main/resources")
    meta_dir = os.path.join(res_dir, "META-INF")
    mkdirs(java_dir)
    mkdirs(mixin_dir)
    mkdirs(cmd_dir)
    mkdirs(meta_dir)

    # gradle.properties
    gp_lines = [
        "org.gradle.jvmargs=-Xmx3G",
        "org.gradle.daemon=false",
        "",
        "minecraft_version=%s" % v["mc"],
        "minecraft_version_range=%s" % v["mc_range"],
        "loader_version_range=%s" % v["loader_range"],
        "mapping_channel=official",
        "mapping_version=%s" % v["mc"],
        "",
        "mod_id=%s" % MOD_ID,
        "mod_name=%s" % MOD_NAME,
        "mod_license=%s" % MOD_LICENSE,
        "mod_version=%s" % MOD_VERSION,
        "mod_group_id=%s" % MOD_GROUP,
        "mod_authors=%s" % MOD_AUTHORS,
        "mod_description=%s" % MOD_DESC,
    ]
    if v["loader"] == "forge":
        gp_lines.insert(5, "forge_version=%s" % v["forge"])
        gp_lines.insert(6, "forge_version_range=%s" % v["forge_range"])
    else:
        gp_lines.insert(5, "neo_version=%s" % v["neo"])
    write(os.path.join(root, "gradle.properties"), "\n".join(gp_lines) + "\n")

    # settings.gradle
    if v["loader"] == "forge":
        write(os.path.join(root, "settings.gradle"), FORGE_SETTINGS)
    else:
        write(os.path.join(root, "settings.gradle"), NEOFORGE_SETTINGS)

    # build.gradle
    if v["loader"] == "forge":
        write(os.path.join(root, "build.gradle"), FORGE_BUILD_GRADLE % {"fg_range": v.get("fg_plugin_range", "[6.0,6.2)"), "java": v["java"]})
    else:
        write(os.path.join(root, "build.gradle"), NEOFORGE_BUILD_GRADLE % {"java": v["java"]})

    # Java sources
    if v["loader"] == "forge":
        write(os.path.join(java_dir, "HungerControlMod.java"), FORGE_HUNGER_MOD)
        write(os.path.join(java_dir, "Config.java"), FORGE_CONFIG)
        write(os.path.join(cmd_dir, "HungerControlCommand.java"), FORGE_COMMAND)
        write(os.path.join(mixin_dir, "PlayerMixin.java"), FORGE_MIXIN)
    else:
        write(os.path.join(java_dir, "HungerControlMod.java"), NEOFORGE_HUNGER_MOD)
        write(os.path.join(java_dir, "Config.java"), NEOFORGE_CONFIG)
        write(os.path.join(cmd_dir, "HungerControlCommand.java"), NEOFORGE_COMMAND)
        write(os.path.join(mixin_dir, "PlayerMixin.java"), NEOFORGE_MIXIN)

    # pack.mcmeta
    write(os.path.join(res_dir, "pack.mcmeta"), json.dumps({"pack": {"description": {"text": "%s resources" % MOD_ID}, "pack_format": v["pack_format"]}}, indent=2) + "\n")

    # hungercontrol.mixins.json
    mixins = {
        "required": True,
        "minVersion": "0.8",
        "package": "io.github.xvold.hungercontrol.mixin",
        "compatibilityLevel": "JAVA_%d" % v["java"],
        "refmap": "hungercontrol.refmap.json",
        "mixins": ["PlayerMixin"],
        "client": [],
        "injectors": {"defaultRequire": 1}
    }
    write(os.path.join(res_dir, "hungercontrol.mixins.json"), json.dumps(mixins, indent=2) + "\n")

    # mods.toml / neoforge.mods.toml
    if v["loader"] == "forge":
        tmpl = open(os.path.join(BASE, "src/main/resources/META-INF/mods.toml")).read()
        write(os.path.join(meta_dir, "mods.toml"), tmpl)
    else:
        neo_toml = '''modLoader="javafml"
loaderVersion="${loader_version_range}"
license="${mod_license}"

[[mods]]
modId="${mod_id}"
version="${mod_version}"
displayName="${mod_name}"
logoFile="hungercontrol.png"
authors="${mod_authors}"
description="""${mod_description}"""

[[dependencies.${mod_id}]]
    modId="neoforge"
    mandatory=true
    versionRange="${loader_version_range}"
    ordering="NONE"
    side="BOTH"

[[dependencies.${mod_id}]]
    modId="minecraft"
    mandatory=true
    versionRange="${minecraft_version_range}"
    ordering="NONE"
    side="BOTH"
'''
        write(os.path.join(meta_dir, "neoforge.mods.toml"), neo_toml)

    # copy icon
    shutil.copy(os.path.join(BASE, "src/main/resources/hungercontrol.png"), res_dir)

    # copy gradle wrapper files
    for f in ["gradlew", "gradlew.bat"]:
        src = os.path.join(BASE, f)
        dst = os.path.join(root, f)
        shutil.copy(src, dst)
    wrapper_src = os.path.join(BASE, "gradle/wrapper")
    wrapper_dst = os.path.join(root, "gradle/wrapper")
    mkdirs(wrapper_dst)
    for f in os.listdir(wrapper_src):
        shutil.copy(os.path.join(wrapper_src, f), wrapper_dst)

print("Done generating", len(versions), "version subprojects.")
