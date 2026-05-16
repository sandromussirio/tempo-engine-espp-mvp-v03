import bpy
import bmesh
import unicodedata
from math import radians
from mathutils import Vector, Matrix


# ============================================================
# REGRA OPERACIONAL
# Nunca apagar a cena global.
# Limpar apenas objetos do proprio prefixo.
# ============================================================

def clean_prefix(prefix):
    for obj in list(bpy.context.scene.objects):
        if obj.name.startswith(prefix):
            bpy.data.objects.remove(obj, do_unlink=True)


# ============================================================
# LAYERS / INSTRUCOES
# ============================================================

def normalize_layer(text):
    text = unicodedata.normalize("NFD", str(text))
    return "".join(c for c in text if c.isalnum()).upper()


def resolve_instruction(layer, instrucoes):
    key = normalize_layer(layer)
    return instrucoes.get(key), key


# ============================================================
# MATERIAIS
# ============================================================

def material_rgb(rgb):
    name = "MAT_%s_%s_%s" % (rgb[0], rgb[1], rgb[2])
    mat = bpy.data.materials.get(name)

    if mat is None:
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True

        bsdf = None
        for node in mat.node_tree.nodes:
            if node.type == "BSDF_PRINCIPLED":
                bsdf = node
                break

        if bsdf:
            r = rgb[0] / 255.0
            g = rgb[1] / 255.0
            b = rgb[2] / 255.0
            bsdf.inputs["Base Color"].default_value = (r, g, b, 1.0)

    mat.diffuse_color = (
        rgb[0] / 255.0,
        rgb[1] / 255.0,
        rgb[2] / 255.0,
        1.0
    )

    return mat


def material_transparente(rgb, alpha=0.28):
    name = "MAT_GLASS_%s_%s_%s_%s" % (
        rgb[0],
        rgb[1],
        rgb[2],
        int(alpha * 100)
    )

    mat = bpy.data.materials.get(name)

    if mat is None:
        mat = bpy.data.materials.new(name)

    mat.use_nodes = True

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    output = nodes.new("ShaderNodeOutputMaterial")
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    r = rgb[0] / 255.0
    g = rgb[1] / 255.0
    b = rgb[2] / 255.0

    bsdf.inputs["Base Color"].default_value = (r, g, b, alpha)
    bsdf.inputs["Alpha"].default_value = alpha

    mat.diffuse_color = (r, g, b, alpha)
    mat.blend_method = "BLEND"

    if hasattr(mat, "show_transparent_back"):
        mat.show_transparent_back = True

    return mat


# ============================================================
# GEOMETRIA
# ============================================================

def sanitize_points(points):
    if len(points) > 2 and points[0] == points[-1]:
        return points[:-1]
    return points


def create_polyline_solid(name, points, base_z, extrude, rgb=None, material=None):
    points = sanitize_points(points)

    mesh = bpy.data.meshes.new(name + "_MESH")
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)

    bm = bmesh.new()

    verts = []
    for p in points:
        x = p[0]
        y = p[1]
        verts.append(bm.verts.new((x, y, base_z)))

    face = bm.faces.new(verts)
    bmesh.ops.recalc_face_normals(bm, faces=[face])

    bm.to_mesh(mesh)
    bm.free()

    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.extrude_region_move(
        TRANSFORM_OT_translate={"value": (0, 0, extrude)}
    )
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode="OBJECT")

    obj.select_set(False)

    if material is None and rgb is not None:
        material = material_rgb(rgb)

    if material is not None:
        obj.data.materials.append(material)
        obj.active_material = material
        obj.color = material.diffuse_color

    return obj


def create_circle_solid(name, center, radius, base_z, extrude, rgb=None, material=None, vertices=64):
    x = center[0]
    y = center[1]

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius,
        depth=extrude,
        location=(x, y, base_z + extrude / 2.0)
    )

    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_MESH"

    if material is None and rgb is not None:
        material = material_rgb(rgb)

    if material is not None:
        obj.data.materials.append(material)
        obj.active_material = material
        obj.color = material.diffuse_color

    return obj


def create_ellipse_solid(name, center, semi_x, semi_y, base_z, extrude, rgb=None, material=None, vertices=64):
    x = center[0]
    y = center[1]

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=1.0,
        depth=extrude,
        location=(x, y, base_z + extrude / 2.0)
    )

    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_MESH"
    obj.scale.x = semi_x
    obj.scale.y = semi_y

    if material is None and rgb is not None:
        material = material_rgb(rgb)

    if material is not None:
        obj.data.materials.append(material)
        obj.active_material = material
        obj.color = material.diffuse_color

    return obj


# ============================================================
# BOOLEAN
# ============================================================

def apply_boolean_difference(base, cut):
    bpy.context.view_layer.update()

    cut.hide_set(True)
    cut.hide_render = True

    cut.location.z -= 0.001
    bpy.context.view_layer.update()

    bpy.ops.object.select_all(action="DESELECT")

    mod = base.modifiers.new(name="SUB_" + cut.name, type="BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.object = cut

    if hasattr(mod, "solver"):
        mod.solver = "EXACT"

    bpy.context.view_layer.objects.active = base
    base.select_set(True)

    bpy.ops.object.modifier_apply(modifier=mod.name)

    bpy.data.objects.remove(cut, do_unlink=True)


# ============================================================
# ROTACAO
# ============================================================

def rotate_around_line(obj, p1, p2, angle_deg):
    v1 = Vector(p1)
    v2 = Vector(p2)

    axis = (v2 - v1).normalized()
    R = Matrix.Rotation(radians(angle_deg), 4, axis)

    obj.matrix_world = (
        Matrix.Translation(v1) @
        R @
        Matrix.Translation(-v1) @
        obj.matrix_world
    )


# ============================================================
# MEDICAO
# ============================================================

def get_min_max_z(obj):
    zs = []

    for corner in obj.bound_box:
        world_corner = obj.matrix_world @ Vector(corner)
        zs.append(world_corner.z)

    return min(zs), max(zs)