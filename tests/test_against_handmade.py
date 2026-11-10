"""Correctness tests against hand-solved graphs (N <= 8).

The real tests are added in step 7, once the solvers and handmade graphs exist.
For now this only checks that the project imports correctly.
"""


def test_project_imports():
    import src  # noqa: F401
    import networkx  # noqa: F401
