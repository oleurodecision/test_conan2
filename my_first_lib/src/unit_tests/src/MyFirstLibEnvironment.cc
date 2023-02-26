#include <gtest/gtest.h>

class MyFirstLibEnvironment : public ::testing::Environment {
public:
	~MyFirstLibEnvironment() override {}

	// Override this to define how to set up the environment.
	void SetUp() override {}

	// Override this to define how to tear down the environment.
	void TearDown() override {}
};

::testing::Environment* const MyFirstLib_env = ::testing::AddGlobalTestEnvironment(new MyFirstLibEnvironment);

