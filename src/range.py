import sys

from pxr import Sdf

DUMMY: str = (
    "/Applications/Houdini/Houdini20.5.445/Frameworks/Houdini.framework/Versions/20.5/Resources/houdini/usd/assets/crag/crag.usd"
)

if len(sys.argv) > 1:
    DUMMY = sys.argv[1]

root_layer = Sdf.Layer.FindOrOpen(DUMMY)
x = root_layer.GetCompositionAssetDependencies()
for lyr in x:
    print(lyr)
    print(root_layer.ComputeAbsolutePath(lyr))


def recursive_layer_search(layer, layer_list):
    """
    recursively searches the references in a usd file

    :args:
        layer : Sdf.Layer
        - the layer to search dependencies from

        layer_list : List[Sdf.Layer]
        - an initial empty list that is used to store all dependencies externally
    """
    layer_list.append(layer)
    dependencies = layer.GetCompositionAssetDependencies()

    if not dependencies or not dependencies[0]:
        return

    for i in dependencies:
        resolved_path = layer.ComputeAbsolutePath(i)
        new_layer = Sdf.Layer.FindOrOpen(resolved_path)
        recursive_layer_search(new_layer, layer_list)


layers = []
recursive_layer_search(layer=root_layer, layer_list=layers)
