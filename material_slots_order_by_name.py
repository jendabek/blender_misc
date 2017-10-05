# mesh_relax.py Copyright (C) 2010, Fabian Fricke
#
# Relaxes selected vertices while retaining the shape as much as possible
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "Order Slots by Name",
    "author": "Jan Kadeřábek",
    "version": (1, 0),
    "blender": (2, 7, 0),
    "location": "Material Tab > Specials Menu (Down Arrow)",
    "description": "Reorders material slots by their name",
    "category": "Material",
}

import bpy

slotsNames = []

def draw(self, context):
   self.layout.operator(
        OrderMaterialSlots.bl_idname,
        icon="SYNTAX_ON")

def updateSlotsNames():
    global slotsNames
    slotsNames = []
    slots = bpy.context.active_object.material_slots
    for slot in slots:
        slotsNames.append(slot.name)

class OrderMaterialSlots(bpy.types.Operator):
    """Order Slots by Name"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "material.order_material_slots"        # unique identifier for buttons and menu items to reference.
    bl_label = "Order Slots by Name"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):

        obj = bpy.context.active_object

        updateSlotsNames()
        slotsNamesSorted = sorted(slotsNames)
        selectedSlotName = slotsNames[obj.active_material_index]

        for slotNameInSorted in slotsNamesSorted:
            for slotName in slotsNames:
                
                if(slotNameInSorted == slotName):
                    obj.active_material_index = slotsNames.index(slotNameInSorted)
                    offset = slotsNamesSorted.index(slotName) - slotsNames.index(slotName)
                    offsetAbs = abs(offset)

                    if(offset < 0):
                        for j in range(offsetAbs):
                            bpy.ops.object.material_slot_move(direction='UP')
                    elif(offset < 0):
                        for k in range(aoffsetAbs):
                            obpy.ops.object.material_slot_move(direction='DOWN')
                    updateSlotsNames()
                    break

        obj.active_material_index = slotsNames.index(selectedSlotName)
        return {"FINISHED"}


def register():
    bpy.utils.register_class(OrderMaterialSlots)
    bpy.types.MATERIAL_MT_specials.append(draw)


def unregister():
    bpy.utils.unregister_class(OrderMaterialSlots)
    bpy.types.MATERIAL_MT_specials.remove(draw)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()