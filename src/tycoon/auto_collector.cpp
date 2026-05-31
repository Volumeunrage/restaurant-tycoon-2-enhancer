#include "auto_collector.h"
#include <iostream>
#include <chrono>

AutoCollector::AutoCollector() : running_(false), interval_(0) {}

AutoCollector::~AutoCollector() {
    stop();
}

void AutoCollector::start(double interval_seconds) {
    if (running_) return;
    interval_ = interval_seconds;
    running_ = true;
    worker_ = std::thread(&AutoCollector::collect_loop, this);
}

void AutoCollector::stop() {
    if (!running_) return;
    running_ = false;
    if (worker_.joinable()) {
        worker_.join();
    }
}

void AutoCollector::collect_loop() {
    while (running_) {
        std::cout << "[AutoCollector] Collecting money from all sources..." << std::endl;
        // Simulate Roblox API call
        std::this_thread::sleep_for(std::chrono::duration<double>(interval_));
    }
}