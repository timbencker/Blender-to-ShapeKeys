# Blender-to-ShapeKeys - Blender Animation Export Script

Convert Blender animations to shape keys for use on other 3D platforms.
Export your animated modifiers, GeoNodes, rigs, and more.

## Overview

This Python script is a utility for 3D artists, web and game developers who need to transfer animations from Blender to various platforms.  
It transfers Blender-specific animations — like GeoNodes, armatures, bones — to more often supported animated shape keys.

## Supported Platforms

Useful for platforms and formats that support shape keys, like:

- `.fbx`: **Unity**, **Unreal Engine**, **Godot**
- `.gltf`, `.glb`: **WebGL**, **Three.js**, **Babylon.js**

## Key Features

- **Mesh State to Shape Key Transformation**: Convert various Blender-native mesh modifications such as GeoNodes, Modifiers, Armatures into animated shape keys.
- **Set Stepsize**: Define the number of shape keys to generate, proportionate to the resulting mesh data size.
- **Automated Keyframing**: Effortless insertion of keyframes.
- **Non-Destructive Workflow**: The script operates on a duplicated object, leaving your original artwork untouched.

## Limitations

- Consistent Vertex Count Required: Animations must maintain a consistent vertex count for every frame.
- Potential File Size Increase: Exports to GLTF or FBX may result in substantial file sizes.
- Consider Efficient Engine Solutions: Explore more efficient engine-specific solutions or formats where applicable.

## Installation & Usage

1. Choose your 3D object.
2. Open the script in Blender Text Editor.
3. Hit run.

## Contribute & License

Contributions and pull requests are welcome. This script is licensed under the MIT License.

**Author:** Tim Bencker (2023)
