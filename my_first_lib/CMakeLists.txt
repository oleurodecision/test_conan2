# ============================================================================
# CMake configuration
# ============================================================================

cmake_minimum_required (VERSION 3.23.0)

# ============================================================================
# Project configuration
# ============================================================================

project (my_first_lib
	VERSION 0.0
	LANGUAGES CXX)

# ============================================================================
# External requirements
# ============================================================================

# ----------------------------------------------------------------------------
# External requirements setup
# ----------------------------------------------------------------------------
# additional cmake modules
list (PREPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

# library behaviour
set (CMAKE_FIND_PACKAGE_SORT_ORDER NATURAL)
set (CMAKE_FIND_PACKAGE_SORT_DIRECTION DEC)
set (CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)

# ----------------------------------------------------------------------------
# Dependency version number
# ----------------------------------------------------------------------------
#[[ sample
set (${PROJECT_NAME}_BOOST_VERSION 1.65.1)
#]]

#[[sample
# ----------------------------------------------------------------------------
# Boost
# ----------------------------------------------------------------------------
find_package (Boost ${${PROJECT_NAME}_BOOST_VERSION} REQUIRED COMPONENTS program_options)
#]]

# ============================================================================
# Compiler configurations
# ============================================================================

# ----------------------------------------------------------------------------
# Compilation settings
# ----------------------------------------------------------------------------
set (CMAKE_CXX_STANDARD 14)
set (CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_CXX_EXTENSION OFF)

# ----------------------------------------------------------------------------
# Default compilation flags
# ----------------------------------------------------------------------------

# ============================================================================
# Installation
# ============================================================================

if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
	set (CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install/${PROJECT_NAME}-${PROJECT_VERSION}"
		CACHE PATH "${PROJECT_NAME} default install path" FORCE)
endif ()

include (GNUInstallDirs)

# ----------------------------------------------------------------------------
# Configuration files
# ----------------------------------------------------------------------------
set (ConfigPackageLocation "lib/cmake/${PROJECT_NAME}-${PROJECT_VERSION}")

include (CMakePackageConfigHelpers)

write_basic_package_version_file ("${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config-version.cmake"
	VERSION ${PROJECT_VERSION}
	COMPATIBILITY SameMinorVersion
	)

configure_package_config_file (cmake/${PROJECT_NAME}-config.cmake.in
	"${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config.cmake"
	INSTALL_DESTINATION "${ConfigPackageLocation}"
	NO_SET_AND_CHECK_MACRO
	NO_CHECK_REQUIRED_COMPONENTS_MACRO
	)

# ----------------------------------------------------------------------------
# Install
# ----------------------------------------------------------------------------
install (FILES
	"${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config.cmake"
	"${CMAKE_CURRENT_BINARY_DIR}/cmake/${PROJECT_NAME}-config-version.cmake"
	DESTINATION "${ConfigPackageLocation}"
	)

install (EXPORT ${PROJECT_NAME}-export
	FILE ${PROJECT_NAME}-targets.cmake
	NAMESPACE ${PROJECT_NAME}::
	DESTINATION "${ConfigPackageLocation}"
	)

# ============================================================================
# Documentation
# ============================================================================

add_subdirectory (doc)

# ============================================================================
# Targets configurations
# ============================================================================

#add_subdirectory (src/unit_tests)
add_subdirectory (src/func_tests)
add_subdirectory (src)

