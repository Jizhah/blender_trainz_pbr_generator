bl_info = {
    "name": "Trainz PBR Material Generator",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "View3D > Tool Shelf > Trainz PBR Generator",
    "description": "Generates placeholder Trainz PBR textures and node setup.",
    "category": "Material",
}

import bpy
import os
from PIL import Image

def create_placeholder_textures(base_image_path):
    import os
    from PIL import Image

    if not os.path.exists(base_image_path):
        print(f"File does not exist: {base_image_path}")
        return None, None, None

    directory, filename = os.path.split(base_image_path)
    name, ext = os.path.splitext(filename)

    albedo_path = os.path.join(directory, f"{name}_albedo.png")
    normal_path = os.path.join(directory, f"{name}_normal.png")
    parameters_path = os.path.join(directory, f"{name}_parameters.png")

    print(f"Creating textures in: {directory}")

    if not os.path.exists(albedo_path):
        print("Creating albedo...")
        Image.open(base_image_path).save(albedo_path)

    if not os.path.exists(normal_path):
        print("Creating normal...")
        base = Image.open(base_image_path)
        w, h = base.size
        Image.new("RGB", (w, h), (128, 128, 255)).save(normal_path)

    if not os.path.exists(parameters_path):
        print("Creating parameters...")
        base = Image.open(base_image_path)
        w, h = base.size
        # RGBA: R = Emissive (0), G = Roughness (128), B = AO (255), A = Metallic (0)
        Image.new("RGBA", (w, h), (0, 128, 255, 0)).save(parameters_path)

    return albedo_path, normal_path, parameters_path

def setup_trainz_material(material):
    if not material.use_nodes:
        material.use_nodes = True

    node_tree = material.node_tree
    nodes = node_tree.nodes
    links = node_tree.links

    # STEP 1: Find the base image BEFORE clearing nodes
    base_image = None
    for node in nodes:
        if isinstance(node, bpy.types.ShaderNodeTexImage) and node.image:
            base_image = node.image
            break

    if not base_image:
        print("No image texture node with an image found in material.")
        return

    base_img_path = bpy.path.abspath(base_image.filepath_raw)

    # STEP 2: Generate placeholder images if not already done
    albedo_path, normal_path, params_path = create_placeholder_textures(base_img_path)

    # Check if the generated paths are valid
    if not albedo_path or not normal_path or not params_path:
        print("Error: Generated texture paths are empty or invalid.")
        return

    # Debugging: Print the generated paths
    print(f"Albedo Path: {albedo_path}")
    print(f"Normal Path: {normal_path}")
    print(f"Params Path: {params_path}")

    # STEP 3: Now clear nodes and create a fresh setup
    nodes.clear()

    tex_albedo = nodes.new("ShaderNodeTexImage")
    tex_normal = nodes.new("ShaderNodeTexImage")
    tex_params = nodes.new("ShaderNodeTexImage")
    normal_map = nodes.new("ShaderNodeNormalMap")
    principled = nodes.new("ShaderNodeBsdfPrincipled")
    output = nodes.new("ShaderNodeOutputMaterial")

    # STEP 4: Try to load images, ensure paths are valid
    try:
        tex_albedo.image = bpy.data.images.load(albedo_path)
        tex_normal.image = bpy.data.images.load(normal_path)
        tex_params.image = bpy.data.images.load(params_path)
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    # STEP 5: Arrange node positions
    tex_albedo.location = (-800, 300)
    tex_params.location = (-800, 0)
    tex_normal.location = (-800, -300)
    normal_map.location = (-600, -300)
    principled.location = (-200, 0)
    output.location = (200, 0)

    # STEP 6: Make node connections
    links.new(tex_albedo.outputs["Color"], principled.inputs["Base Color"])
    links.new(tex_normal.outputs["Color"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], principled.inputs["Normal"])
    
    # Directly link parameters to Roughness and Metallic
    links.new(tex_params.outputs["Color"], principled.inputs["Roughness"])
    links.new(tex_params.outputs["Alpha"], principled.inputs["Metallic"])

    links.new(principled.outputs["BSDF"], output.inputs["Surface"])

    # STEP 7: Rename material
    if not material.name.endswith(".m.pbrmetal"):
        material.name += ".m.pbrmetal"


class TrainzPBRPanel(bpy.types.Panel):
    bl_label = "Trainz PBR Generator"
    bl_idname = "VIEW3D_PT_trainz_pbr"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.generate_trainz_pbr", text="Generate Trainz PBR Material")

class GenerateTrainzPBROperator(bpy.types.Operator):
    bl_idname = "object.generate_trainz_pbr"
    bl_label = "Generate Trainz PBR Material"

    def execute(self, context):
        obj = context.active_object
        if obj and obj.active_material:
            setup_trainz_material(obj.active_material)
            self.report({'INFO'}, "Trainz PBR material generated.")
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "No active material found.")
            return {'CANCELLED'}

classes = [TrainzPBRPanel, GenerateTrainzPBROperator]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except Exception:
            pass

if __name__ == "__main__":
    register()
