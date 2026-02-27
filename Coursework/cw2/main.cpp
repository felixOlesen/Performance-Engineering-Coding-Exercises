#include <iostream>
#include <thread>
#include <atomic>
#include <cstdint>
#include <random>

class mysem {
  public:
    mysem(uint32_t init_value){ 
      counter.store(init_value, std::memory_order_seq_cst); 
    };
    
    void acquire(){
      int current = counter.load(std::memory_order_seq_cst);
    
      while (current == 0) {
        counter.wait(current); 
        current = counter.load(std::memory_order_seq_cst);
      }

      counter.fetch_sub(1, std::memory_order_seq_cst);
    };
    
    void release(){ 
      counter.fetch_add(1, std::memory_order_seq_cst);
      counter.notify_one();
    };
  
  private:
    std::atomic<uint32_t> counter;
};

void random_work() {
  int random_amount = rand() % 1001;
  int count = 0;
  for (int i = 0; i < random_amount; ++i) {
    count++;
  }
};

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
