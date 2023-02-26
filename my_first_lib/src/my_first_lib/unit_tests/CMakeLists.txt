if (NOT TARGET unit_tests)
	return ()
endif ()

target_sources (unit_tests
	PRIVATE
		#[[ sample
		src/libproject.test.cc
		]]
)

target_link_libraries (unit_tests
	PRIVATE
	${PROJECT_NAME}::my_first_lib)

