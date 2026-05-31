#include "auto_upgrader.h"
#include <iostream>
#include <chrono>

AutoUpgrader::AutoUpgrader() : running_(false), interval_(0) {}

AutoUpgrader::~AutoUpgrader() {
    stop();
}

void AutoUpgrader::start(double interval_seconds) {
    if (running_) return;
    interval_ = interval_seconds;
    running_ = true;
    worker_ = std::thread(&AutoUpgrader::upgrade_loop, this);
}

void AutoUpgrader::stop() {
    if (!running_) return;
    running_ = false;
    if (worker_.joinable()) {
        worker_.join();
    }
}

void AutoUpgrader::upgrade_loop() {
    while (running_) {
        std::cout << "[AutoUpgrader] Checking for affordable upgrades..." << std::endl;
        // Simulate Roblox API call
        std::this_thread::sleep_for(std::chrono::duration<double>(interval_));
    }
}