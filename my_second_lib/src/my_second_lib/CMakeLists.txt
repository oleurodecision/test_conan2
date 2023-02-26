# ============================================================================
# CMake configuration
# ============================================================================

cmake_minimum_required (VERSION 3.23.0)

# ============================================================================
# External requirements
# ============================================================================

find_package (my_first_lib REQUIRED)

# ============================================================================
# Targets configuration
# ============================================================================

# ----------------------------------------------------------------------------
# library
# ----------------------------------------------------------------------------

add_library (my_second_lib)

set_target_properties (my_second_lib
	PROPERTIES
		OUTPUT_NAME my_second_lib)

target_sources (my_second_lib
	PRIVATE
	src/my_second_lib/second.cc
	#[[ sources ]])

target_sources (my_second_lib
	PUBLIC
	FILE_SET HEADERS
	BASE_DIRS src
	FILES
	src/my_second_lib/second.hh
	#[[ sources ]])

target_include_directories (my_second_lib
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
	)

target_link_libraries (my_second_lib
	PUBLIC
		my_first_lib::my_first_lib)

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

install (TARGETS my_second_lib EXPORT ${PROJECT_NAME}-export
	FILE_SET HEADERS
	INCLUDES DESTINATION include
)

# ----------------------------------------------------------------------------
# Export configuration
# ----------------------------------------------------------------------------

add_library (${PROJECT_NAME}::my_second_lib ALIAS my_second_lib)

