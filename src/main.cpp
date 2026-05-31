#include <iostream>
#include "tycoon/auto_collector.h"
#include "tycoon/auto_upgrader.h"

int main() {
    std::cout << "Restaurant Tycoon 2 Enhancer - Initializing..." << std::endl;

    AutoCollector collector;
    AutoUpgrader upgrader;

    collector.start(5.0);  // Collect every 5 seconds
    upgrader.start(10.0);  // Upgrade every 10 seconds

    std::cout << "Enhancer running. Press Enter to stop..." << std::endl;
    std::cin.get();

    collector.stop();
    upgrader.stop();

    return 0;
}