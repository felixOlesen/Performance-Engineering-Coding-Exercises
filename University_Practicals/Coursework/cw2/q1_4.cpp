#include <iostream>
#include <thread>
#include <atomic>
#include <cstdint>
#include <random>
#include <linux/futex.h>
#include <sys/syscall.h>
#include <unistd.h>

class mysem {
  public:
    mysem(uint32_t init_value){ 
      counter.store(init_value, std::memory_order_seq_cst); 
    };
    
    void acquire(){
      uint32_t* counter_ptr = reinterpret_cast<uint32_t*>(&counter);
    
      while (true) {
        for(int i=0; i < 100; i++) {

          uint32_t current = counter.load(std::memory_order_seq_cst);
          
          if(current > 0) {
            counter.fetch_sub(1, std::memory_order_seq_cst);
            return;
          }
        }


        syscall(SYS_futex, counter_ptr, FUTEX_WAIT, 0, nullptr, nullptr, 0);
      }
    };
    
    void release(){
      uint32_t* counter_ptr = reinterpret_cast<uint32_t*>(&counter);

      counter.fetch_add(1, std::memory_order_seq_cst);

      // Futex wake up one thread
      syscall(SYS_futex, counter_ptr, FUTEX_WAKE, 1, nullptr, nullptr, 0);

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
