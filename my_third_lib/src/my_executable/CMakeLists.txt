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

add_executable (my_executable)

set_target_properties (my_executable
	PROPERTIES
		OUTPUT_NAME my_executable
	)

target_sources (my_executable
	PRIVATE
		src/main.cc
	)

target_include_directories (my_executable
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
	)

target_link_libraries (my_executable
	PUBLIC
		${PROJECT_NAME}::my_third_lib
	)

# ============================================================================
# Install configuration
# ============================================================================

install (TARGETS my_executable EXPORT ${PROJECT_NAME}-export)

# ----------------------------------------------------------------------------
# Export configuration
# ----------------------------------------------------------------------------

add_executable (${PROJECT_NAME}::my_executable ALIAS my_executable)

