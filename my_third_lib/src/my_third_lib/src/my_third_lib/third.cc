#include "my_third_lib/third.hh"

#include "my_second_lib/second.hh"

namespace third
{
std::string print()
{
	return second::print();
}
}
