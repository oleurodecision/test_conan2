# ============================================================================
# CMake configuration
# ============================================================================

cmake_minimum_required (VERSION 3.23.0)

# ============================================================================
# External requirements
# ============================================================================

find_package (my_second_lib REQUIRED)

# ============================================================================
# Targets configuration
# ============================================================================

# ----------------------------------------------------------------------------
# library
# ----------------------------------------------------------------------------

add_library (my_third_lib STATIC)

set_target_properties (my_third_lib
	PROPERTIES
		OUTPUT_NAME my_third_lib
		POSITION_INDEPENDENT_CODE ON)

target_sources (my_third_lib
	PRIVATE
	src/my_third_lib/third.cc
	#[[ sources ]])

target_include_directories (my_third_lib
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
	)

target_link_libraries (my_third_lib
	PUBLIC
		my_second_lib::my_second_lib
	)

# ----------------------------------------------------------------------------
# unit_tests
# ----------------------------------------------------------------------------

add_subdirectory (unit_tests)

# ----------------------------------------------------------------------------
# func_tests
# ----------------------------------------------------------------------------

add_subdirectory (func_tests)

# ============================================================================
# Install configuration
# ============================================================================

# ----------------------------------------------------------------------------
# Export configuration
# ----------------------------------------------------------------------------

add_library (${PROJECT_NAME}::my_third_lib ALIAS my_third_lib)

