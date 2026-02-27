#include <iostream>
#include <thread>
#include <atomic>
#include <cstdint>

class mysem {
  public:
    mysem(uint32_t init_value){};
    void acquire(){};
    void release(){};
  private:
    std::atomic<uint32_t> counter;
};

void random_work() { };

int main(int argc, char**argv)
{
  mysem s(2);
  std::thread t1([&]() {
    s.acquire();
    std::cout << 1; random_work(); std::cout << 1;
    s.release();
  });

  std::thread t2([&]() {
    s.acquire();
    std::cout << 2; random_work(); std::cout << 2;
    s.release();
  });

  t1.join(); t2.join();
  std::cout << std::endl;
}
