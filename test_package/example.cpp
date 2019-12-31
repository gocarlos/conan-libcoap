#include <coap2/coap.h>
#include <iostream>

int main() {

  std::cout << "hello world\n";

  coap_context_t *ctx = nullptr;

  coap_startup();

  /* create CoAP context and a client session */
  ctx = coap_new_context(nullptr);
  coap_cleanup();

  std::cout << "successfully executed\n";

  return 0;
}
