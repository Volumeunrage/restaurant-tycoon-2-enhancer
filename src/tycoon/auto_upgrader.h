#pragma once
#include <thread>
#include <atomic>

class AutoUpgrader {
public:
    AutoUpgrader();
    ~AutoUpgrader();

    void start(double interval_seconds);
    void stop();

private:
    void upgrade_loop();
    std::atomic<bool> running_;
    std::thread worker_;
    double interval_;
};