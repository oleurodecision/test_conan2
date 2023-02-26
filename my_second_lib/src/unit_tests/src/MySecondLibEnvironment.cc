#include <gtest/gtest.h>

class MySecondLibEnvironment : public ::testing::Environment {
public:
	~MySecondLibEnvironment() override {}

	// Override this to define how to set up the environment.
	void SetUp() override {}

	// Override this to define how to tear down the environment.
	void TearDown() override {}
};

::testing::Environment* const MySecondLib_env = ::testing::AddGlobalTestEnvironment(new MySecondLibEnvironment);

