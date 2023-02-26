# ============================================================================
# CMake configuration
# ============================================================================

cmake_minimum_required (VERSION 3.23.0)

# ============================================================================
# External requirements
# ============================================================================

# ============================================================================
# Targets configuration
# ============================================================================

# ----------------------------------------------------------------------------
# library
# ----------------------------------------------------------------------------

add_library (my_first_lib)

set_target_properties (my_first_lib
	PROPERTIES
		OUTPUT_NAME my_first_lib)

target_sources (my_first_lib
	PRIVATE
	src/my_first_lib/first.cc
	#[[ sources ]])

target_sources (my_first_lib
	PUBLIC
	FILE_SET HEADERS
	BASE_DIRS src
	FILES
	src/my_first_lib/first.hh
	#[[ sources ]])

target_include_directories (my_first_lib
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
	)

target_link_libraries (my_first_lib
	PUBLIC
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

install (TARGETS my_first_lib EXPORT ${PROJECT_NAME}-export
	FILE_SET HEADERS
	INCLUDES DESTINATION include
)

# ----------------------------------------------------------------------------
# Export configuration
# ----------------------------------------------------------------------------

add_library (${PROJECT_NAME}::my_first_lib ALIAS my_first_lib)

