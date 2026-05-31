#pragma once
#include <thread>
#include <atomic>

class AutoCollector {
public:
    AutoCollector();
    ~AutoCollector();

    void start(double interval_seconds);
    void stop();

private:
    void collect_loop();
    std::atomic<bool> running_;
    std::thread worker_;
    double interval_;
};