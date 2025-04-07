bl_info = {
    "name": "Trainz PBR Generator",
    "author": "Jing Bo Zhang",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "View3D > Sidebar > Tool Tab",
    "description": "Generates Trainz-compatible PBR materials from a base image",
    "category": "Material",
}

import bpy
from . import operator

def register():
    operator.register()

def unregister():
    operator.unregister()