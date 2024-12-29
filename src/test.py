import logging
import os
import sys

from pxr import Ar, Sdf, UsdUtils

resolver = Ar.GetResolver()
dump_root: str = f"{os.getcwd()}/dump/"

if len(sys.argv) < 2:
    raise IndexError("usdFile not specified")

# convert below to parse args
usdFile: str = sys.argv[1]

core_layer = Sdf.Layer.FindOrOpen(usdFile)

# usdutils method
# compute_deps = UsdUtils.ComputeAllDependencies(usdFile)
"""
the above method seems promising, the only thing that we need to 
do is resolve what is a dependency of what as at the moment it is returning a list of all nested dependencies
"""


# TODO
# - figure out a way to sort dependencies so we can find out
# what is dependent on what
# - test speed
# - run unit tests on compute dependencies function


def test_layer_exists(layer: str):
    if not os.path.isfile(layer):
        assert FileNotFoundError(f"File {layer} not found")
    else:
        print("FILE FOUND")


def _usd_utils_dependencies():
    # remember to warn for unresolved references
    for sublayer in core_layer.subLayerPaths:
        dependencies = UsdUtils.ComputeAllDependencies(assetPath=sublayer)
        # dependencies[0] are layer dependencies
        # dependencies[1] is all non-layer dependendcies
        # dependencies[2] is unresolved dependencies
        layered_dependencies = dependencies[0]

        for layer in layered_dependencies:
            test_layer_exists(layer=layer.realPath)

        # print(sublayer)
        # print(len(dependencies[1]))
        # print(dependencies[1])
        # print("\n")


_usd_utils_dependencies()


# asset resolver methods
def test_if_sublayer_resolves(path: str):
    """given an unresolved path, tests if a path will resolve"""
    resolved_path = resolver.Resolve(path)
    if not resolved_path:
        raise AssertionError("WARNING: not resolved")


# test if path exists on dependencies


def _sublayer_resolution():
    """this is good for resolving single layer dependencies"""
    for sublayer in core_layer.subLayerPaths:
        resolved_sublayer = resolver.Resolve(sublayer)
        new_layer = Sdf.Layer.FindOrOpen(resolved_sublayer)
        for _sub in new_layer.subLayerPaths:
            # atm this doesnt work, need to find an
            # alternative way to solve nested dependencies
            rs = Ar.GetResolver()
            resolved = rs.Resolve(_sub)
            print(resolved)
