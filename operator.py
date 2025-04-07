import bpy
import os
from PIL import Image

def create_placeholder_textures(base_image_path):
    directory, filename = os.path.split(base_image_path)
    name, ext = os.path.splitext(filename)
    albedo_path = os.path.join(directory, f"{name}_albedo{ext}")
    normal_path = os.path.join(directory, f"{name}_normal{ext}")
    parameters_path = os.path.join(directory, f"{name}_parameters{ext}")

    if not os.path.exists(albedo_path):
        Image.open(base_image_path).save(albedo_path)
    if not os.path.exists(normal_path):
        base = Image.open(base_image_path)
        w, h = base.size
        Image.new("RGB", (w, h), (128, 128, 255)).save(normal_path)
    if not os.path.exists(parameters_path):
        base = Image.open(base_image_path)
        w, h = base.size
        Image.new("RGB", (w, h), (0, 128, 255)).save(parameters_path)

    return albedo_path, normal_path, parameters_path

def setup_trainz_material(material):
    if not material.use_nodes:
        material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()

    tex_albedo = nodes.new("ShaderNodeTexImage")
    tex_normal = nodes.new("ShaderNodeTexImage")
    tex_params = nodes.new("ShaderNodeTexImage")
    normal_map = nodes.new("ShaderNodeNormalMap")
    separate_rgb = nodes.new("ShaderNodeSeparateRGB")
    principled = nodes.new("ShaderNodeBsdfPrincipled")
    output = nodes.new("ShaderNodeOutputMaterial")

    tex_albedo.location = (-800, 300)
    tex_params.location = (-800, 0)
    tex_normal.location = (-800, -300)
    normal_map.location = (-600, -300)
    separate_rgb.location = (-600, 0)
    principled.location = (-200, 0)
    output.location = (200, 0)

    base_img_node = None
    for node in nodes:
        if isinstance(node, bpy.types.ShaderNodeTexImage) and node.image:
            base_img_node = node
            break
    if not base_img_node:
        print("No image texture node found.")
        return
    base_img_path = bpy.path.abspath(base_img_node.image.filepath_raw)
    albedo_path, normal_path, params_path = create_placeholder_textures(base_img_path)

    tex_albedo.image = bpy.data.images.load(albedo_path)
    tex_normal.image = bpy.data.images.load(normal_path)
    tex_params.image = bpy.data.images.load(params_path)

    tex_albedo.color_space = 'sRGB'
    tex_normal.color_space = 'NONE'
    tex_params.color_space = 'NONE'

    links.new(tex_albedo.outputs["Color"], principled.inputs["Base Color"])
    links.new(tex_normal.outputs["Color"], normal_map.inputs["Color"])
    links.new(normal_map.outputs["Normal"], principled.inputs["Normal"])
    links.new(tex_params.outputs["Color"], separate_rgb.inputs["Image"])
    links.new(separate_rgb.outputs["R"], principled.inputs["Metallic"])
    links.new(separate_rgb.outputs["G"], principled.inputs["Roughness"])
    links.new(principled.outputs["BSDF"], output.inputs["Surface"])

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
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "No active material found.")
            return {'CANCELLED'}

def register():
    bpy.utils.register_class(TrainzPBRPanel)
    bpy.utils.register_class(GenerateTrainzPBROperator)

def unregister():
    bpy.utils.unregister_class(TrainzPBRPanel)
    bpy.utils.unregister_class(GenerateTrainzPBROperator)