import bpy


def set_keyframes(target, shape_key, frame, step_size):
    key_block = target.data.shape_keys.key_blocks[shape_key]
    key_block.value = 1
    key_block.keyframe_insert('value')
    key_block.value = 0
    key_block.keyframe_insert('value', frame=frame + step_size)
    key_block.keyframe_insert('value', frame=frame - step_size)


def show_popup(title, message):
    def draw(self, ctx):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon='ERROR')


def duplicate_object(src_obj):
    new_data = src_obj.data.copy()
    new_object = bpy.data.objects.new(src_obj.name + "_shapekeys", new_data)
    bpy.context.collection.objects.link(new_object)
    return new_object


def generate_shape_key(target, mesh, frame):
    shape_key_name = f"NewShape_{frame}"
    new_shape_key = target.shape_key_add(name=shape_key_name, from_mix=False)
    for v, vertex in enumerate(new_shape_key.data):
        vertex.co = mesh.vertices[v].co
    return shape_key_name


def main():
    # Initial checks and setup
    active_object = bpy.context.object
    if active_object is None:
        show_popup("Warning", "No Active Object. Exiting Script.")
        return
    
    current_frame = bpy.context.scene.frame_current
    target = duplicate_object(active_object)

    if not target.data.shape_keys:
        target.shape_key_add(name="Basis")

    # Step Size
    step_size = 3

    # Evaluation setup
    DG = bpy.context.evaluated_depsgraph_get()
    evaluated_object = active_object.evaluated_get(DG)

    for frame in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end, step_size):
        bpy.context.scene.frame_set(frame)

        # Transfer mesh state to shapekey
        new_mesh = bpy.data.meshes.new_from_object(evaluated_object, depsgraph=DG)
        shape_key_name = generate_shape_key(target, new_mesh, frame)
        
        set_keyframes(target, shape_key_name, frame, step_size)
        
    target.data.update()
    bpy.context.scene.frame_current = current_frame
    
if __name__ == '__main__':
    main()
