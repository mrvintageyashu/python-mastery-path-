def very_slow_func():
    print("mera yashu mera yashu yashu")
    print("mera yashu mera yashu yashu")
    print("mera yashu mera yashu yashu")
    print("mera yashu mera yashu yashu")
    print("mera yashu mera yashu yashu")
    return 70

if((a:=very_slow_func())>10):
    print(a)

else:
    print("its not greater than 10")