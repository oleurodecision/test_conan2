#include <gtest/gtest.h>

class MyExeEnvironment : public ::testing::Environment {
public:
	~MyExeEnvironment() override {}

	// Override this to define how to set up the environment.
	void SetUp() override {}

	// Override this to define how to tear down the environment.
	void TearDown() override {}
};

::testing::Environment* const MyExe_env = ::testing::AddGlobalTestEnvironment(new MyExeEnvironment);

