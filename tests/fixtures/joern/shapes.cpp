class A { public: int f(int x) { return x + 1; } };
template <typename T> T id(T v) { return v; }
int main() { A a; return id(a.f(2)); }
