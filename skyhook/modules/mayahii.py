import traceback
try:
    import pymel.core as pm
    import maya.cmds as cmds
except:
    print(str(traceback.format_exc()))
    pass


def maya_version():
    return cmds.about(q=True, v=True)
