#include <gtest/gtest.h>

class MyThirdEnvironment : public ::testing::Environment {
public:
	~MyThirdEnvironment() override {}

	// Override this to define how to set up the environment.
	void SetUp() override {}

	// Override this to define how to tear down the environment.
	void TearDown() override {}
};

::testing::Environment* const MyThird_env = ::testing::AddGlobalTestEnvironment(new MyThirdEnvironment);

