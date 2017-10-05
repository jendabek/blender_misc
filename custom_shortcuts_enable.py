import bpy

bl_info = {
	"name": "Custom Shortcuts Enable",
	"author": "Jan Kadeřábek",
	"version": (1, 0),
	"blender": (2, 7, 0),
	"location": "",
	"description": "",
	"category": "User",
}

class show_only_render(bpy.types.Operator):
	bl_idname = "view3d.show_only_render"
	bl_label = "Show Only Render"

	def execute(self, context):
		space = bpy.context.space_data

		if space.show_only_render:
			space.show_only_render = False
		else:
			space.show_only_render = True
		return {"FINISHED"}

class show_edges(bpy.types.Operator):
	bl_idname = "mesh.show_edges"
	bl_label = "Show Edges"

	def execute(self, context):
		obj = bpy.context.active_object

		if obj.data.show_edges :
			obj.data.show_edges = False
		else:
			obj.data.show_edges = True
		return {"FINISHED"}
class trigger_shadeless(bpy.types.Operator):
	bl_idname = "screen.trigger_shadeless"
	bl_label = "Trigger Shadeless"

	def execute(self, context):
		obj = bpy.context.active_object
		material = obj.data.materials[obj.active_material_index]

		if material.use_shadeless :
			material.use_shadeless = False
		else:
			material.use_shadeless = True
		return {"FINISHED"}

def register():
	bpy.utils.register_class(show_only_render)
	bpy.utils.register_class(trigger_shadeless)
	bpy.utils.register_class(show_edges)


def unregister():
	bpy.utils.unregister_class(show_only_render)
	bpy.utils.unregister_class(trigger_shadeless)
	bpy.utils.unregister_class(show_edges)
