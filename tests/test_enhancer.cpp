#include <gtest/gtest.h>
#include "../src/tycoon/auto_collector.h"
#include "../src/tycoon/auto_upgrader.h"

TEST(AutoCollectorTest, StartStop) {
    AutoCollector collector;
    collector.start(0.1);
    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    collector.stop();
    SUCCEED();
}

TEST(AutoUpgraderTest, StartStop) {
    AutoUpgrader upgrader;
    upgrader.start(0.1);
    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    upgrader.stop();
    SUCCEED();
}