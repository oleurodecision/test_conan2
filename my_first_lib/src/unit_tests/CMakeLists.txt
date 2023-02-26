# ============================================================================
# External requirements
# ============================================================================

find_package (GTest REQUIRED)

# ============================================================================
# Targets
# ============================================================================

# ----------------------------------------------------------------------------
# unit_tests
# ----------------------------------------------------------------------------
add_executable (unit_tests)

target_sources (unit_tests
	PRIVATE
	src/localtest.test.cc
	src/MyFirstLibEnvironment.cc)

target_link_libraries (unit_tests
	PRIVATE
	GTest::gtest_main)
 
# ----------------------------------------------------------------------------
# run_unit_tests
# ----------------------------------------------------------------------------

set (TESTS_REPORTS_DIR "${CMAKE_BINARY_DIR}/tests-reports")
set (TESTS_REPORTS_FILE "${TESTS_REPORTS_FILE}/unit_tests-results.xml")

add_custom_target (run_unit_tests
	DEPENDS ${TESTS_REPORTS_DIR} ${TESTS_REPORTS_FILE})

add_custom_command(OUTPUT ${TESTS_REPORTS_DIR}
	COMMAND ${CMAKE_COMMAND} -E make_directory ${TESTS_REPORTS_DIR}
	COMMENT "Creates the unit tests working directory")

add_custom_command(OUTPUT ${TESTS_REPORTS_FILE}
	COMMAND $<TARGET_FILE:unit_tests>
	DEPENDS unit_tests
	WORKING_DIRECTORY ${TESTS_REPORTS_DIR}
	COMMENT "Runs the unit tests")
