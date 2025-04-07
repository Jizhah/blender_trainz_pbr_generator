
# Blender Trainz PBR Material Generator

This script helps you convert a base image into Trainz-compatible PBR material format (`.m.pbrmetal`) in Blender 4.1. It integrates into the Blender UI for easy access, allowing you to generate the necessary textures and set up the material nodes automatically.

## Features

- **Automatic Texture Generation**:
  - `_albedo`: Base color texture.
  - `_normal`: Placeholder normal map (with a flat normal).
  - `_parameters`: Placeholder map for metallic, roughness, and ambient occlusion (AO).
  
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
   - Select the downloaded `trainz_pbr_generator_blender41.zip` file.
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
  - R → **Metallic**
  - G → **Roughness**
  - B → **Ambient Occlusion**

## Important Notes

- **Placeholder Textures**: The script generates placeholder textures. For real-world use, you’ll need to bake the actual normal and roughness maps.
- The base image must be a local file, not a temporary image loaded in Blender.
- Ensure the material has **Use Nodes** enabled.
- The script clears any existing nodes and creates the new setup automatically.

## Testing and Export

1. You can test the material in **Trainz** using the **Trainz Mesh Exporter** or **FBX**.
2. Ensure the textures are in the correct folder location when exporting.
3. Verify in **Trainz Content Manager** that the materials and textures are applied correctly.

---

# Blender Trainz PBR 材质生成器

此脚本帮助您将基础图像转换为 Trainz 兼容的 PBR 材质格式（`.m.pbrmetal`），并集成到 Blender 4.1 的 UI 中，方便用户直接通过界面生成所需的贴图和设置材质节点。

## 功能

- **自动生成贴图**：
  - `_albedo`: 基础颜色贴图。
  - `_normal`: 占位符法线贴图（平面法线）。
  - `_parameters`: 金属度、粗糙度和环境光遮蔽（AO）占位符贴图。
  
- **自动设置节点**：
  - 将贴图连接到相应的材质节点，生成 Trainz 兼容的 PBR 材质。

- **自动重命名材质**：
  - 将材质重命名为 `.m.pbrmetal` 格式。

## 环境准备

### 要求

- **Blender 4.1** 或更高版本。
- **Python**（Blender 默认安装）。
- **Pillow** 图像处理库。可以通过以下命令安装：

  ```bash
  blender --background --python-expr "import pip; pip.main(['install', 'pillow'])"
  ```

  或通过 pip 安装：

  ```bash
  pip install pillow
  ```

### 如何在 Blender 中设置脚本

1. **加载模型和贴图**：
   - 在 Blender 中选择您的 **3D 模型**。
   - 打开 **材质属性** 面板。
   - 确保材质中有一个 **图像纹理节点**，并加载一张本地图片（如 `metal.jpg`）。

2. **将脚本添加到 Blender UI**：
   - 打开 **Scripting** 标签页。
   - 点击 **新建** 创建一个新的脚本。
   - 将以下脚本粘贴到编辑器中，并点击 **运行脚本** 来注册 UI 面板。

3. **通过 UI 使用插件**：
   - 运行脚本后，切换到 **3D 视图**。
   - 在 **工具架（T）** 中，您将看到一个新的 **Trainz PBR 生成器** 面板。
   - **选择对象**，确保它有图像纹理节点。
   - 点击面板中的 **“生成 Trainz PBR 材质”** 按钮，脚本将自动创建并连接贴图和节点。

## 生成的文件

脚本将在原始贴图所在的同一文件夹中生成以下贴图：

- `yourimage_albedo.png`
- `yourimage_normal.png`
- `yourimage_parameters.png`

这些贴图将被自动连接到材质的节点上。

## 节点设置

- **_albedo**: 连接到 **Base Color**（基础颜色）输入。
- **_normal**: 连接到 **Normal Map** 节点，并将其连接到 **Normal** 输入。
- **_parameters**: 分离 RGB 通道，控制 **金属度**、**粗糙度** 和 **环境光遮蔽**（AO）：
  - R → **金属度**
  - G → **粗糙度**
  - B → **环境光遮蔽**

## 注意事项

- **占位符贴图**：脚本生成的法线和粗糙度贴图为占位符。在实际使用中，您可能需要根据需求制作真实的法线和粗糙度贴图。
- 原始贴图必须是本地文件，不能是 Blender 临时加载的图像。
- 确保材质启用了 **“使用节点（Use Nodes）”**。
- 脚本会清除已有节点并重新创建节点结构。

## 测试与导出

1. 使用 **Trainz Mesh Exporter** 或 **FBX** 导出带有 `.m.pbrmetal` 材质的模型。
2. 在 **Trainz 内容管理器（Content Manager）** 中验证贴图是否正确应用。
3. 导出后，确保贴图文件位于正确的文件夹路径下。
