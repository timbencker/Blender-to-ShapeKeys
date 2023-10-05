# Blender-to-ShapeKeys - Blender Animation Export Script

This Python script is a utility for 3D artists, web and game developers enabling export from Blender to other 3D packages.  
Convert Blender-specific animations — like GeoNodes, Modifiers, Armatures — to more often supported animated shape keys.

## Supported Platforms

Useful for platforms and formats that support shape keys, like:

- `.fbx`: **Unity**, **Unreal Engine**, **Godot**
- `.gltf`, `.glb`: **WebGL**, **Three.js**, **Babylon.js**

## Key Features

- **Mesh State to Shape Keys**: Transfer Blender-native mesh modifications such as GeoNodes, Modifiers, Armatures.
- **Set Stepsize**: Choose number of generated shape keys, proportionate to the resulting mesh data size.
- **Automated Keyframing**: Effortless keyframe generation.
- **Non-Destructive Workflow**: Generates a duplicated object, leaving your original artwork untouched.

## Limitations

- Consistent Vertex Count Required: Animations must maintain a consistent vertex count for every frame.
- File Size Increase: Exports to GLTF or FBX may result in substantial file sizes.
- Consider Efficient Engine Solutions: Explore more efficient engine-specific solutions or formats where applicable.

## Installation & Usage

1. Choose your 3D object.
2. Open the script in Blender Text Editor.
3. Hit run.

## Contribute & License

Contributions and pull requests are welcome. Licensed under MIT.

**Author:** Tim Bencker (2023)
