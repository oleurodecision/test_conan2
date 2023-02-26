#include "my_second_lib/second.hh"

#include "my_first_lib/first.hh"

namespace second
{
std::string print()
{
	return first::print().append("Enter the neXt.\n");
}
}
