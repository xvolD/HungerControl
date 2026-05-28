#!/bin/bash
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"

build_version() {
    local dir="$1"
    local java_ver
    if [[ "$dir" == *"1.20.1"* ]] || [[ "$dir" == *"1.20.2"* ]] || [[ "$dir" == *"1.20.3"* ]] || [[ "$dir" == *"1.20.4"* ]]; then
        java_ver="17"
    else
        java_ver="21"
    fi

    echo "========================================"
    echo "Building $dir (Java $java_ver)"
    echo "========================================"

    if [ "$java_ver" == "17" ]; then
        export JAVA_HOME="/c/Program Files/Eclipse Adoptium/jdk-17.0.17.10-hotspot"
    else
        export JAVA_HOME="/c/Program Files/Android/openjdk/jdk-21.0.8"
    fi
    export PATH="$JAVA_HOME/bin:$PATH"

    cd "$ROOT/$dir"
    ./gradlew build --no-daemon
}

for d in versions/*/; do
    build_version "$d"
done

echo ""
echo "All versions built successfully!"
