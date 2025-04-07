
# Blender Trainz PBR Material Generator

This script helps you convert a base image into Trainz-compatible PBR material format (`.m.pbrmetal`) in Blender 4.1. It integrates into the Blender UI for easy access, allowing you to generate the necessary textures and set up the material nodes automatically.

## Features

- **Automatic Texture Generation**:
  - `_albedo`: Base color texture.
  - `_normal`: Placeholder normal map (with a flat normal).
  - `_parameters`: Placeholder map for emissive, metallic, roughness, and ambient occlusion (AO).
  
- **Automatic Node Setup**:
  - Connects the textures to the appropriate shader nodes for a Trainz-compatible PBR material.

- **Material Renaming**: 
  - Automatically renames the material to `.m.pbrmetal`.

## Setup Instructions

### Requirements

- **Blender 4.1** or higher.
- **Python** (installed by default with Blender).
- **Pillow** library for image creation. Install it using the following command:

  ```bash
  blender --background --python-expr "import pip; pip.main(['install', 'pillow'])"
  ```

  Or install via pip:

  ```bash
  pip install pillow
  ```

### How to Install the Extension in Blender

1. **Load Your Model and Texture**:
   - Select your 3D model in Blender.
   - Open the **Material Properties** panel.
   - Ensure your material has an **Image Texture node** with an image loaded (e.g., `metal.jpg`).

2. **Install the Extension in Blender**:
   - Go to **Edit > Preferences > Add-ons > Install...**.
   - Select the downloaded `trainz_pbr_generator.zip` file.
   - Enable the **Trainz PBR Generator** add-on by checking the box.

3. **Use the Extension from the UI**:
   - After running the script, switch to the **3D View**.
   - In the **Tool Shelf** (press **T** if it's not visible), you will find a new **Trainz PBR Generator** panel.
   - **Select the object** you want to apply the material to.
   - **Click the "Generate Trainz PBR Material" button** to automatically create and connect the textures and nodes.

## Generated Files

The script will create the following textures in the same directory as the base image:

- `yourimage_albedo.png`
- `yourimage_normal.png`
- `yourimage_parameters.png`

These textures will be connected to the material nodes in Blender.

## Node Setup

- **_albedo**: Linked to **Base Color** of the Principled BSDF.
- **_normal**: Linked to the **Normal Map** node, which is then linked to the **Normal** input of the Principled BSDF.
- **_parameters**: Separated into RGB channels to control **Metallic**, **Roughness**, and **AO**:
  - R → **Emissive**
  - G → **Roughness**
  - B → **Ambient Occlusion**
  - A → **Metallic**

## Important Notes

- **Placeholder Textures**: The script generates placeholder textures. For real-world use, you’ll need to bake the actual normal and roughness maps.
- The base image must be a local file, not a temporary image loaded in Blender.
- Ensure the material has **Use Nodes** enabled.
- The script clears any existing nodes and creates the new setup automatically.

---