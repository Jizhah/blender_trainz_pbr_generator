
# Blender Trainz PBR Material Generator

This script helps you convert a base image into Trainz-compatible PBR material format (`.m.pbrmetal`) in Blender 4.1. It integrates into the Blender UI for easy access, allowing you to generate the necessary textures and set up the material nodes automatically.

### Features:
- **Automatic Texture Generation**:
  - `_albedo`: Base color texture.
  - `_normal`: Placeholder normal map (with a flat normal).
  - `_parameters`: Placeholder map for emissive, metallic, roughness, and ambient occlusion (AO).
  
- **Automatic Node Setup**:
  - Connects the textures to the appropriate shader nodes for a Trainz-compatible PBR material.

- **Material Renaming**: 
  - Automatically renames the material to `.m.pbrmetal`.

---

### Setup Instructions:

#### Requirements:
- **Blender 4.1** or higher.
- **Python** (installed by default with Blender).
- **Pillow** library for image creation. Install it using the following steps.

#### How to Install Pillow (Windows CMD):

1. **Open Command Prompt**:
   - Press **Win + R** to open the "Run" dialog, then type `cmd` and hit **Enter**.
  
2. **Navigate to Blender's Python folder**:
   - In the Command Prompt, navigate to Blender's Python directory. For Blender 4.1, the default path might look like:
     ```bash
     cd "C:\Program Files\Blender Foundation\Blender 4.1\4.1\python\bin"
     ```
   - If Blender is installed in a different location, adjust the path accordingly.

3. **Install Pillow using pip**:
   - In the same Command Prompt window, type the following command and press **Enter**:
     ```bash
     .\python.exe -m pip install pillow
     ```
   - This will install the **Pillow** library, which is required for image creation.

#### How to Install the Extension in Blender:
1. **Load Your Model and Texture**:
   - Select your 3D model in Blender.
   - Open the **Material Properties** panel.
   - Ensure your material has an **Image Texture node** with an image loaded (e.g., `metal.jpg`).

2. **Install the Extension in Blender**:
   - Go to **Edit > Preferences > Add-ons > Install...**.
   - Select the downloaded `trainz_pbr_generator.py` file.
   - Enable the **Trainz PBR Generator** add-on by checking the box.

3. **Use the Extension from the UI**:
   - After running the script, switch to the **3D View**.
   - In the **Tool Shelf** (press **T** if it's not visible), you will find a new **Trainz PBR Generator** panel.
   - **Select the object** you want to apply the material to.
   - **Click the "Generate Trainz PBR Material" button** to automatically create and connect the textures and nodes.

---

### Generated Files:
The script will create the following textures in the same directory as the base image:

- `yourimage_albedo.png`
- `yourimage_normal.png`
- `yourimage_parameters.png`

These textures will be connected to the material nodes in Blender.

---

### Node Setup:
- **_albedo**: Linked to **Base Color** of the Principled BSDF.
- **_normal**: Linked to the **Normal Map** node, which is then linked to the **Normal** input of the Principled BSDF.
- **_parameters**: Separated into RGB channels to control **Metallic**, **Roughness**, and **AO**:
  - R → **Emission**
  - G → **Roughness**
  - B → **Ambient Occlusion**
  - A → **Metallic**

---

### Important Notes:
- **Placeholder Textures**: The script generates placeholder textures. For real-world use, you’ll need to bake the actual normal and roughness maps.
- The base image must be a **local file**, not a temporary image loaded in Blender.
- Ensure the material has **Use Nodes** enabled.
- The script clears any existing nodes and creates the new setup automatically.

---

## Blender Trainz PBR 材料生成器

这个脚本帮助您将基础图像转换为与Trainz兼容的PBR材质格式（`.m.pbrmetal`）在Blender 4.1中使用。它集成到Blender的UI中，便于操作，自动生成必要的纹理并设置材质节点。

### 功能：
- **自动纹理生成**：
  - `_albedo`：基础颜色纹理。
  - `_normal`：占位符法线贴图（平面法线）。
  - `_parameters`：占位符贴图，用于发光、金属度、粗糙度和环境光遮蔽（AO）。

- **自动节点设置**：
  - 将纹理连接到适当的着色器节点，生成与Trainz兼容的PBR材质。

- **材质重命名**：
  - 自动将材质命名为`.m.pbrmetal`。

---

### 安装说明：

#### 要求：
- **Blender 4.1** 或更高版本。
- **Python**（Blender自带）。
- **Pillow**库用于图像创建。使用以下步骤进行安装。

#### 如何在Windows中安装Pillow：

1. **打开命令提示符**：
   - 按下**Win + R**键打开"运行"对话框，然后输入`cmd`并按下**Enter**。

2. **进入Blender的Python文件夹**：
   - 在命令提示符中，进入Blender的Python目录。对于Blender 4.1，默认路径可能类似于：
     ```bash
     cd "C:\Program Files\Blender Foundation\Blender 4.1\4.1\python\bin"
     ```
   - 如果Blender安装在其他位置，请相应地调整路径。

3. **使用pip安装Pillow**：
   - 在同一命令提示符窗口中，输入以下命令并按下**Enter**：
     ```bash
     .\python.exe -m pip install pillow
     ```
   - 这将安装**Pillow**库，这是图像创建所必需的。

#### 如何在Blender中安装插件：
1. **加载您的模型和纹理**：
   - 在Blender中选择您的3D模型。
   - 打开**材质属性**面板。
   - 确保您的材质具有**图像纹理节点**，并加载了图像（例如`metal.jpg`）。

2. **在Blender中安装插件**：
   - 进入**编辑 > 首选项 > 插件 > 安装...**。
   - 选择下载的`trainz_pbr_generator.py`文件。
   - 通过勾选框启用**Trainz PBR Generator**插件。

3. **通过UI使用插件**：
   - 运行脚本后，切换到**3D视图**。
   - 在**工具架**中（如果不可见，请按**T**），您将找到一个新的**Trainz PBR Generator**面板。
   - **选择**您要应用材质的对象。
   - **点击“生成Trainz PBR材质”按钮**，以自动创建和连接纹理和节点。

---

### 生成的文件：
脚本将在与基础图像相同的目录中创建以下纹理：

- `yourimage_albedo.png`
- `yourimage_normal.png`
- `yourimage_parameters.png`

这些纹理将自动连接到Blender中的材质节点。

---

### 节点设置：
- **_albedo**：连接到Principled BSDF的**Base Color**。
- **_normal**：连接到**法线贴图**节点，然后连接到Principled BSDF的**Normal**输入。
- **_parameters**：将RGB通道分配给控制**金属度**、**粗糙度**和**环境光遮蔽（AO）**：
  - R → **发光**
  - G → **粗糙度**
  - B → **环境光遮蔽**
  - A → **金属度**

---

### 重要注意事项：
- **占位符纹理**：脚本生成占位符纹理。对于实际使用，您需要烘焙实际的法线和粗糙度贴图。
- 基础图像必须是**本地文件**，而不是Blender中加载的临时图像。
- 确保材质启用了**使用节点**（Use Nodes）。
- 脚本会清除现有节点并自动创建新的节点设置。
