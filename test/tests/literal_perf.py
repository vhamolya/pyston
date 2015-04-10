# run_args: -n
# statcheck: noninit_count("slowpath_runtimecall") <= 5
# expected: statfail
# - TODO

# A test to make sure that we fast-path literal creation.

# 100 elements:
{
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
    1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1, 1:1,
}

# 100 elements:
[
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
]

# 100 elements:
{
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
}

# 100 elements:
(
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
)
