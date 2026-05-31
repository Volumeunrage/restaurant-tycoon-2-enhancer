cmake_minimum_required(VERSION 3.10)
project(restaurant-tycoon-2-enhancer)

set(CMAKE_CXX_STANDARD 17)

add_executable(restaurant_enhancer
    src/main.cpp
    src/tycoon/auto_collector.cpp
    src/tycoon/auto_upgrader.cpp
)

target_include_directories(restaurant_enhancer PRIVATE src)
target_link_libraries(restaurant_enhancer PRIVATE roblox_api)